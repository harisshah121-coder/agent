# Roll-to-Garment: project master document (v1, 2026-10-23)

This is the one document that says what the project is and everything we need to do. v1 adds the research results (docs/research, R01–R16), the three master build guides, the gaps found and the seed case.

**The four guides**: `BUILD_GUIDE_SIMULATION.md` (seven simulation levels, first results) · `BUILD_GUIDE_MACHINE.md` (every station, real parts, BOM, assembly, tests) · `BUILD_GUIDE_SOFTWARE.md` (M01–M14, stack, MCP, safety boundary, build order) · `BUILD_GUIDE_3D_MODEL.md` (toolchain, vendor geometry, assemblies A00–A10, simulation, Blender, R3).

## 1. What we are building
An AI-directed roll-to-garment manufacturing cell: a modular, guarded industrial machine that takes a roll of knit fabric at one end and delivers finished, inspected garments at the other, with one operator supervising and an AI software stack doing the design-to-machine work. First product: a premium short-sleeve T-shirt. The same cell and software are designed to extend to other cut-and-sew garments.

The white paper's structure (its sections 01–24 and appendices A–E) is the backbone of this document; its primary-source register is reused where the research confirms it.

## 2. Targets the white paper sets (to be validated by research)
- Output: at least 100 acceptable premium T-shirts per 12-hour shift, measured from a declared starting condition.
- Factory build-and-test cost scenarios: $52,000 / $83,000 / $140,000; reference selling price $100,000 (sensitivity to $125,000 shown in the paper).
- Operator economics (paper's illustrative model): break-even near 50 accepted sales per day at a $12 garment selling price; profit boundaries and sensitivities in sections 20–22.
- Autonomy honesty: with a 1% per-garment intervention probability, the chance of a 100-garment run with no human intervention is about 37%; at 0.1% it is about 90%. The design therefore treats intervention as normal and measured, not as failure.
- Safety: deterministic control and an independent safety layer; AI never commands safety functions.

## 3. The physical cell (stations)
| ID | Station | Function (from the white paper, sections 04–09, 14) |
|---|---|---|
| ST00 | Frame, guarding, infrastructure | Modular frame, guarded enclosure, cabinet, utilities |
| ST01 | Roll handling | Roll loading, low-tension unwind, edge guiding, knit relaxation, dimensional stability |
| ST02 | Cutting | Single-ply knife cutting on a vacuum conveyor bed from a nested marker; scrap handling |
| ST03 | Extraction and buffer | Lifting cut pieces off the bed, staging them in order |
| ST04 | Manipulation | Gantry plus arm with a gripper toolbox; cloth is controlled, not just positioned |
| ST05 | Sewing heads | Overlock, coverstitch and lockstitch heads with automated feed, trim, presser control |
| ST06 | Collar and neckband module | Rib attach with split support and differential feed |
| ST07 | Finishing, inspection, output | Thread trim, inspection, fold/stack/bag, label |
| ST08 | Optional decoration | Embroidery, direct-to-garment or transfer print |
| ST09 | Control and safety | PLC, safety PLC, drives, I/O, HMI, guarding devices |
| ST10 | Vision and compute | Cameras, 3D sensing, lighting, edge inference, networking |

## 4. The software (modules)
| ID | Module | Role (white paper sections 10–13) |
|---|---|---|
| M01 | Design workspace | Conversational and visual design and production control |
| M02 | Canonical garment record | Single machine-readable description of the garment (paper appendix B) |
| M03 | Pattern engine | Parametric patterns (GarmentCode) from the record |
| M04 | Nesting | Marker generation for single-ply cutting |
| M05 | Material profiles | Fabric behaviour parameters that tune every downstream step |
| M06 | Assembly compiler | Garment → operations → skills with parameters |
| M07 | Cell scheduler | Sequencing across stations for throughput and intervention budget |
| M08 | Skill runtime | Behaviour-tree execution of skills with perception in the loop |
| M09 | Motion control and hardware abstraction | Same job package drives the simulator and the real cell |
| M10 | Independent safety layer | Deterministic, certified, never AI-commanded |
| M11 | Perception | Edge detection, ply state, seam tracking, inspection |
| M12 | MCP server | Read / design-write / operate tiers; approval and safety never exposed |
| M13 | Digital twin and simulation | Kinematics, cycle time, visual demonstration |
| M14 | Data, logging, observability | Every run recorded; honest autonomy metrics |

## 5. The 3D model
Code-CAD master model (build123d) with vendor STEP geometry for bought parts; exports to STEP, glTF, URDF/MJCF (MuJoCo), USD (Isaac Sim), Blender (animation, cloth visuals) and R3 (web walkthrough). Assemblies A00–A10 mirror the stations. Honest limit: no simulator proves fabric handling; the model proves geometry, reach, kinematics, cycle time and interfaces.

## 6. Business
Comparables and positioning in white paper sections 17–19; machine cost and margin in section 20; garment cost model in section 21; sensitivities in section 22. The seed thesis (`03_SEED_THESIS.md`) will set out what a $10M seed buys and the milestones that retire the biggest risks (fabric handling reliability, sewing-head automation, throughput, certification, first customers).

## 7. Everything we need to do (phase map)
| Phase | What | Output |
|---|---|---|
| 1 (done) | Research every element; write the three master build guides | `docs/` set |
| 2 (next) | 3D model: toolchain, vendor geometry import, every assembly, kinematics, cycle-time simulation, Blender animation, R3 walkthrough | model repo, demos |
| 3 | Software: M01–M14 in build order with simulation backend first, then hardware-in-the-loop | running stack against the digital twin |
| 4 | Machine: procurement, sub-assembly builds, station bring-up, integration, FAT, 100-shirt shift test | working cell |
| 5 | Seed raise: deck, data room, investor pipeline | term sheet |
| 6 | Certification and first deployment | CE or UL route, first customer |

## 8. Risks the research must retire (initial register)
1. Single-ply knit pick-up and placement reliability (ply separation, curling, static).
2. Robot-fed overlock and coverstitch seams on stretch knit at acceptable quality and speed.
3. Neckband attach with correct stretch ratio.
4. Throughput: takt per station versus the 100-per-shift target.
5. Cost: real parts versus the $52k–$140k scenarios.
6. Safety certification of a cell with AI planning and deterministic control.
7. Market: customers who pay for on-demand, nearshore T-shirts at the modelled price.

## 9. Glossary
See white paper appendix E; the spine adds project-specific terms.

## 10. Gaps found by the research (and where each is handled)
| ID | Gap | Evidence | Fix | Where |
|---|---|---|---|---|
| GAP-01 | Development cell costs about USD 248k in parts, 2–5× the white paper's USD 52k/83k/140k scenarios | parts.csv; R01, R02, R06, R07 | Seed funds the development cell; cost-down plan to a USD 100k sellable cell | Machine guide §7.3 |
| GAP-02 | Robot-fed curved overlock seam on curling jersey is not demonstrated anywhere public | R04, R12 | First bench experiment before buying the full cell | Machine guide §10 #1 |
| GAP-03 | No overlock/coverstitch head has electronic differential feed; rib stretch must come from handling | R04 | In-house expansion-roller collar module | Machine guide §3.6 |
| GAP-04 | No purchasable autonomous collar unit (bought-in operator-loaded est. USD 30–60k) | R04 | Build in-house, modelled on Atlanta 1289/1996 | Machine guide §3.6 |
| GAP-05 | Human SAM 6.5–8.5 min exceeds the 5.47 min required interval | R16 F9 | Pipeline 3–4 shirts; separate extraction carriage; ST04 and ST06 measured first | Machine guide §1.3 |
| GAP-06 | Frame/guarding alone exceeds the white paper's conservative line | R07 | Weldment and simpler guarding in cost-down | Machine guide §3.0, §7.3 |
| GAP-07 | No capex line for folding/bagging/decoration in the white paper | R08 | Optional modules priced separately | Machine guide §3.7–3.8 |
| GAP-08 | Electroadhesion grippers not purchasable; needle marks on jersey unquantified | R03 | Needle + vacuum toolbox; 1,000-cycle wash test | Machine guide §3.3 |
| GAP-09 | No vendor CAD for cutter and any sewing head | R04, R15 | LOD0 envelopes, NDA requests, 3D scans | 3D guide §4 |
| GAP-10 | White paper source register misses the ARM Institute automated T-shirt assembly project (2025) | R12 | Add to the register; contact for results | Research log |
| GAP-12 | A fixed-pedestal UR10e cannot reach the overlock (90 mm short) or inspection table (870 mm short) | sim/results/reach_cycle.json | 7th-axis track added (P-ST04-007) | Simulation guide §8.1 |
| GAP-13 | Arm occupancy 321 s vs 328 s interval: 2 % margin; only 72 % of shifts reach 100 at 80 % availability | sim/results/throughput_des.json | Gantry presents sleeve hems flat (+13 shirts/shift); MTTR ≤ 10 min | Simulation guide §8.2–8.4 |
| GAP-11 | Template sewing is the proven deterministic route for knit seams, while the white paper leans against fixtures | R12 | Keep template/automat routes as fallback for hems | Machine guide §3.5 |

## 11. Seed case (summary; detail in research R13)
- **Open slot**: nobody sells a conventional-stitch roll-to-garment cell near USD 100k (R13).
- **Beachhead**: Berry-Amendment and uniform/teamwear contract sewers (DLA clothing and textiles obligated USD 1.878B in FY2024, USD 624M to cut-and-sew contractors) who need 50–500-piece reorders in days (R13).
- **Why now**: US apparel duties on Asian tees ~25–37 % in 2026 and de minimis ended 2025-08-29; physical-AI tooling (cheap compute, open policies, simulation) matured in 2025–2026 (R13, R10).
- **Proof investors will demand** (SoftWear × Tianyuan is the cautionary precedent): one unattended roll-to-tee run on video with measured takt, yield and interventions; BOM-backed cost; 3–5 LOIs; safety certification started (R13).
- **Raise sizing**: market median seed is USD 4.5M at USD 23.9M post (R13). The owner's USD 10M target is above median and must be justified by the development cell (≈ USD 0.25M parts plus team of 6–8 engineers for 18–24 months) and the first two customer pilot cells; the milestone plan above is the justification.

## 12. Next actions
0. 3D concept model and interactive viewer exist (`cad/concept/`, `cad/out/`); first simulations run (`sim/`).
1. Phase 2 (3D model): checkpoints C1 (vendor geometry register) and C2 (LOD0 envelopes A00–A10) from the 3D guide, then C3 reach study and C4 cycle time.
2. In parallel: the three bench experiments (overlock presentation, needle-pick, rib stretch) from Machine guide §10.
3. Quote requests in Machine guide §7.4.
