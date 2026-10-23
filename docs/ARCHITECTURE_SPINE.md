# Architecture spine (v1, 2026-10-23)

The single definition of every identifier the three build guides share. Part selections, interface specifications and the takt budget are filled in from the research dossier (Task 4) and live in the machine-readable registries under `docs/spine/`. v0 fixes the structure so the guides can be written against it.

## 1. Identifier schemes
| Kind | Pattern | Example | Defined in |
|---|---|---|---|
| Station | `STnn` (00–10) | ST04 | section 2 |
| Software module | `Mnn` (01–14) | M08 | section 3 |
| 3D assembly | `Ann` (00–10), mirrors station | A04 | section 4 |
| Part | `P-STnn-nnn`, sequential within a station | P-ST04-012 | `spine/parts.csv` |
| Interface | `IF-<from>-<to>-<kind>-nn`, kind ∈ {MECH, ELEC, PNEU, DATA} | IF-ST04-ST05-DATA-01 | `spine/interfaces.csv` |
| Skill (software) | `SK-<verb>-<object>` | SK-pick-ply | Guide 2 §4 M08 |
| Operation (garment) | `OP-nn-<name>` | OP-03-attach-neck-rib | Guide 1 §1, Guide 2 §3 |
| Requirement | `REQ-<station or module>-nn` | REQ-ST02-03 | each guide's station or module section |
| Test | `TST-<station or module>-nn` | TST-ST05-01 | each guide's acceptance tests |
| Gap | `GAP-nn` | GAP-07 | `02_GAP_ANALYSIS.md` |
| Decision | `D-nnn` | D-004 | `logs/DECISIONS.md` |

## 2. Stations
| ID | Station | Boundary (what is inside) |
|---|---|---|
| ST00 | Frame, guarding, infrastructure | Extrusion frame, guarding panels and doors, cabinet enclosure, cable ways, utilities entry, levelling, lighting |
| ST01 | Roll handling | Roll holder/unwinder, edge guide, tension/dancer, static control, relaxation feed to the cutter conveyor |
| ST02 | Cutting | Vacuum conveyor bed, cutting gantry and tool heads, vacuum blower and zoning, registration camera, piece marking, scrap removal |
| ST03 | Extraction and buffer | Pick-off from the bed end, ply verification, buffer/staging surfaces, order tracking |
| ST04 | Manipulation | Gantry, arm(s), tool changer, gripper toolbox, wrist sensing, placement and alignment at ST05/ST06/ST07 |
| ST05 | Sewing heads | Overlock, coverstitch, lockstitch heads with servo, trimmer, presser control, pullers, guides, needle-area cameras |
| ST06 | Collar/neckband module | Rib handling, split support, differential feed, rib attach and cover |
| ST07 | Finishing, inspection, output | Thread trim, lint removal, inspection station, turning/folding/stacking, labelling, bagging, output conveyor |
| ST08 | Optional decoration | Embroidery head and hooping, DTG/DTF printer, pretreat and cure, heat press |
| ST09 | Control and safety | PLC/IPC, safety PLC, servo drives, I/O, valve terminals, HMI, e-stops, light curtains, scanners, interlocks, cabinet internals |
| ST10 | Vision and compute | Cameras, 3D sensors, lighting, edge inference PC, switches, calibration targets |

## 3. Software modules
| ID | Module | One-line contract |
|---|---|---|
| M01 | Design workspace | Conversational and visual interface that reads and writes M02 records and submits jobs |
| M02 | Canonical garment record | Versioned schema describing a garment: pieces, seams, operations, materials, sizes, decoration |
| M03 | Pattern engine | Record + size + material profile → pattern pieces (SVG/DXF) with seam allowances and notches |
| M04 | Nesting | Pieces + fabric width + rules → marker (cut file) with piece IDs and orientation constraints |
| M05 | Material profiles | Measured fabric parameters that tune cutting, handling, sewing and inspection |
| M06 | Assembly compiler | Record + profiles → ordered operations → skill calls with parameters and quality gates |
| M07 | Cell scheduler | Jobs × stations × takt → schedule, buffers, intervention budget |
| M08 | Skill runtime | Behaviour-tree execution of skills with perception feedback and recovery branches |
| M09 | Motion control and HAL | Deterministic motion on PLC/drives; identical API over simulation and physical backends |
| M10 | Independent safety layer | Safety PLC logic and certified devices; never written to by M01–M09, M11–M14 |
| M11 | Perception | Edge, ply, seam and defect perception services at defined rates and latencies |
| M12 | MCP server | Tools in three tiers (read, design-write, operate); no approval or safety tools |
| M13 | Digital twin and simulation | Kinematic/physics simulation backend for M09 and visual demonstration |
| M14 | Data, logging, observability | Event log, metrics, traces, run records, autonomy and quality statistics |

## 4. 3D assemblies
`A00`–`A10` mirror `ST00`–`ST10` one-to-one: A00 frame and guarding, A01 roll handling, A02 cutter, A03 extraction and buffer, A04 manipulation, A05 sewing heads, A06 collar module, A07 finishing and output, A08 decoration, A09 control and safety, A10 vision and compute. Each assembly is a build123d module exporting STEP and glTF, with a joints file for URDF/MJCF generation. Sub-assemblies use `Ann.m` (for example `A04.2` gripper toolbox). Vendor geometry is referenced by `part_id` and stored under `cad/vendor/<part_id>/`.

## 5. Interface kinds and what each row must specify
| Kind | Required fields in `spec` |
|---|---|
| MECH | Mounting pattern, envelope (mm), mass (kg), datum, allowable loads |
| ELEC | Voltage, current, connector, cable type, fieldbus, signal list |
| PNEU | Pressure (bar), flow (l/min), port size, vacuum level (kPa) if any |
| DATA | Message or signal name, schema, rate (Hz), latency budget (ms), transport |

## 6. Registries (machine-readable)
- `spine/parts.csv`: `part_id,station,vendor,vendor_pn,description,qty,unit_price_usd,price_basis,price_date,cad_source,source_url`. `price_basis` ∈ {list, reseller, quote, estimate}. `cad_source` ∈ {vendor STEP <url>, code-CAD, scan, none: <reason>}.
- `spine/interfaces.csv`: `iface_id,from,to,kind,spec,consumer_module`.
- `spine/takt.csv`: `station,seconds_per_garment,parallel_units,source`. Throughput = 43,200 s ÷ max(seconds_per_garment ÷ parallel_units); target ≥ 100 garments per 12-hour shift.
`scripts/check_docs.py --guides` enforces all of the above.

## 7. Data contracts shared by the guides
- Job package: `{job_id, garment_record_ref, size, quantity, material_profile_ref, marker_ref, operations[], decoration[], quality_gates[], created_by, approvals[]}`; identical for simulation (M13) and cell (M09).
- Run record: `{run_id, job_id, station_events[], interventions[], inspections[], outcome}` written by M14.
- Skill call: `{skill_id, params, preconditions[], postconditions[], timeout_ms, recovery[]}` issued by M06, executed by M08 through M09 and M11.
