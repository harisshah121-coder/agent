# Build Guide 2: The Software (v1, 2026-10-22)

The software stack that takes a garment from conversational design to a running cell: modules M01–M14, their contracts, the stack with pinned versions, the MCP server, the safety boundary, the simulation parity rule, and the build order. Module and station IDs come from `ARCHITECTURE_SPINE.md`; interfaces from `spine/interfaces.csv`. Versions were verified by research report R09 (2026-10-21) unless marked otherwise.

---

## 1. Scope and principles
1. **Deterministic control, learned perception.** Motion runs on the PLC; AI plans, perceives and chooses among bounded skills. Every production textile result in 2025–2026 is a structured cell with learned models inside skills, never as the cell controller (R10 D1).
2. **AI never commands safety.** Safety state is read-only to every software module (M10, §6).
3. **One job package, two backends.** The same job package drives the digital twin (M13) and the cell (M09); differences live only behind the hardware abstraction layer.
4. **Everything is recorded.** Every attempt, intervention and inspection is logged with outcome labels; the log is the training set and the investor evidence (M14).
5. **Open source first**, commercial where it is the industry standard (TwinCAT, vendor cutter software).

## 2. Architecture
```
            ┌──────────── Workstation / cloud ────────────┐
 Operator → │ M01 Design workspace (Next.js + Three.js)   │ ← Claude via M12 MCP server
            │ M02 record · M03 pattern · M04 nesting       │
            │ M05 profiles · M06 compiler · M07 scheduler  │
            │ M14 data (Postgres/Timescale, object store)  │
            └───────────────┬─────────────────────────────┘
                            │ job package (REST/NATS)
            ┌───────────────▼──────── Cell PC (Ubuntu 24.04, ROS 2 Jazzy) ┐
            │ M08 skill runtime (BehaviorTree.CPP 4) · M11 perception     │
            │ M09 HAL: sim backend (M13 MuJoCo) | physical backend         │
            └───────┬─────────────────────┬──────────────────────┬────────┘
                    │ ADS / OPC UA         │ RTDE 500 Hz           │ GigE Vision
            ┌───────▼───────┐       ┌──────▼──────┐        ┌──────▼──────┐
            │ ST09 TwinCAT  │       │ UR10e ctrl  │        │ ST10 cameras │
            │ M10 TwinSAFE  │       └─────────────┘        └─────────────┘
            └───────────────┘
```
Deployment: workstation/cloud services in Docker; cell PC and vision IPC on the isolated cell LAN; one firewall uplink (R14 F16).

## 3. Data model
### 3.1 Canonical garment record (M02)
Versioned JSON validated by Pydantic v2 models, stored in Postgres (JSONB) with immutable revisions. Top-level fields:
`record_id, revision, product{type, fit, size_range}, pieces[{piece_id, role, grain, pattern_ref, notches[], allowances}], seams[{seam_id, pieces[2], stitch_iso4915, seam_iso4916, length_mm, ease, sequence}], materials[{role, material_profile_ref}], trims[], labels[], decoration[], quality{tolerances, aql}, approvals[]`.
The white paper's appendix B example is the starting schema; extend, never fork.

### 3.2 Material profile (M05)
`{profile_id, fabric{fiber, structure, gsm, width_mm}, relaxation{method, hours, shrink_l_pct, shrink_w_pct}, curl_index, cutting{tool, speed, vacuum_zone_kpa}, handling{needle_stroke_mm, vacuum_ok, static}, sewing{spm_max, diff_ratio, stitch_len_mm, needle, thread}, sim{stretch, bend, friction}, sources[]}`. Populated from cheap measurements (Cusick drape, tag data) and from logged runs (R12).

### 3.3 Job package (spine §7)
`{job_id, garment_record_ref, size, quantity, material_profile_ref, marker_ref, operations[], decoration[], quality_gates[], created_by, approvals[]}`. Signed and immutable once approved.

### 3.4 Event log and run record (M14)
`run_record{run_id, job_id, station_events[], interventions[{time, station, cause, operator_action, duration_s}], inspections[], outcome}` plus time-series signals (axis states, vacuum levels, stitch counts) in TimescaleDB, and images/episodes in object storage in LeRobotDataset format (R10 D6).

## 4. Modules
Each module: purpose, interfaces, stack, implementation steps, tests, acceptance.

### M01 Design workspace
- **Purpose**: conversational and visual design of the garment and its production; job submission and live cell view.
- **Stack**: Next.js 16 + React 19, Three.js / React Three Fiber for 3D garment and cell views, Tailwind; talks to services over REST; embeds the M13 twin view (glTF from Guide 3).
- **Implementation**: (1) record editor with schema-driven forms; (2) pattern preview from M03 (SVG); (3) 3D preview (draped mesh from GarmentCode/simulator, visual only); (4) job submit with approval step; (5) live cell dashboard (M14 streams).
- **Tests**: Playwright end-to-end: create record → preview → submit; **Accept**: a non-engineer can produce an approved T-shirt job in < 10 minutes.

### M02 Canonical garment record
- **Stack**: Python 3.13, Pydantic v2, FastAPI, SQLAlchemy 2, PostgreSQL 18.
- **Implementation**: schema package `r2g_schema` with JSON Schema export; revision table; diff and validation endpoints.
- **Tests**: hypothesis property tests (every valid record round-trips; every seam references existing pieces); **Accept**: white paper appendix B example validates.

### M03 Pattern engine
- **Stack**: GarmentCode / `pygarment` 2.0.2 (MIT, ETH Zürich) installed and importable in this container; the only programmatic, MIT, parametric option (R09 F1). Export DXF-AAMA (ASTM D6673) with our own writer.
- **Implementation**: T-shirt program (front, back, sleeve, rib) parametrised by size chart and material shrink; seam allowances and notches; grading across sizes.
- **Tests**: pattern piece areas within 1 % of reference; seam pairs equal length (minus ease) for each size; **Accept**: S–XXL patterns export and cut correctly on ST02.

### M04 Nesting
- **Stack**: start with `sparrow`/`jagua-rs` (open-source, strong on strip packing) or deepnest-next; OR-Tools for rule post-processing; commercial fallback (Lectra Diamino, Gerber AccuNest) if efficiency gap > 3 % (R09 F2).
- **Implementation**: strip width = usable fabric width; grain constraints (0°/180° only); kit grouping so one garment's pieces sit together for extraction order.
- **Tests**: marker efficiency on the 5-piece tee vs. a manual reference; **Accept**: ≥ 80 % utilisation (est. target) and piece IDs carried to the cut file (IF-M04-ST02-DATA-01).

### M05 Material profiles
- **Implementation**: profile CRUD; measurement import; online update from M14 run statistics (e.g., effective shrink, vacuum level achieved, seam offset).
- **Accept**: each downstream module reads its parameters from the profile, none hard-coded.

### M06 Assembly compiler
- **Purpose**: record + profiles → ordered operations (OP-01…OP-11, Guide 1 §1.2) → skill calls with parameters, preconditions, postconditions and quality gates.
- **Stack**: Python; rules as data; validated against the station capability table.
- **Tests**: compile the tee for every size; every operation maps to an available skill; **Accept**: compiled plan runs unchanged in simulation and on the cell.

### M07 Cell scheduler
- **Stack**: OR-Tools CP-SAT 9.15 (installed in this container).
- **Model**: jobs × operations × resources (ST02, gantry carriage, UR10e, each head, collar module, inspection) with occupancy times from `spine/takt.csv` and measured data; objective = throughput with WIP cap 3–4 shirts (Guide 1 §1.3); intervention budget as a soft constraint.
- **Tests**: reproduces the 5.47 min interval with the takt table; **Accept**: replans within 1 s on a station fault.

### M08 Skill runtime
- **Stack**: ROS 2 Jazzy (LTS) on Ubuntu 24.04; BehaviorTree.CPP ≥ 4.9 with Groot2 for monitoring; skills as ROS 2 action servers. ROS 2 Lyrical (May 2026) is the migration target once Isaac ROS and drivers are confirmed on it (R09 F3).
- **Skills (initial set)**: `SK-pick-ply`, `SK-place-ply`, `SK-align-edge`, `SK-present-seam`, `SK-feed-seam`, `SK-stretch-rib`, `SK-handoff`, `SK-inspect-garment`, `SK-recover-misplace`.
- **Design rules**: each skill has explicit preconditions (state funnels), postconditions verified by perception or force/tactile sensing, a timeout and recovery branches; learned policies (LeRobot ACT/Diffusion, later π0.5/GR00T fine-tunes) are allowed only inside a skill node with the same contract (R10 D2; R12 techniques table).
- **Accept**: each skill reaches its success target in simulation, then on the bench, with every failure classified.

### M09 Motion control and hardware abstraction
- **Contract**: `HAL` interface with two backends: `SimBackend` (MuJoCo 3.16 via M13) and `CellBackend` (TwinCAT over ADS/pyads or OPC UA/asyncua; UR10e via `ur_robot_driver` RTDE; cutter vendor API; sewing box I/O through the PLC).
- **Deterministic side**: TwinCAT PLC programs (IEC 61131-3 Structured Text) own axis motion (NC PTP), sequencing interlocks between machines and all I/O; software sends goals, the PLC validates and executes.
- **Tests**: identical integration test suite runs against both backends; **Accept**: a full tee job runs in sim and on the cell with the same job package and skill plan.

### M10 Independent safety layer
- **Hardware/logic**: Beckhoff TwinSAFE (EL6910) program, validated to the PL targets in Guide 1 §6.
- **Software side**: read-only safety state topic (IF-ST09-M10-DATA-01); no write path exists in any software module; code review rule and an automated test that fails the build if any module links a write call to safety variables.
- **Accept**: SISTEMA report and validation record for every safety function.

### M11 Perception
- **Services**: cut verification and piece pose (ST02, 24 MP, 0.28 mm/px), ply state and grasp points (ST03/ST04, depth-derived surface normals generalise across colour better than RGB, R10 D4), seam edge tracking at the needle (≥ 200 fps ROI, ≤ 10 ms), collar loop checks, garment measurement and defect detection (ST07).
- **Stack**: OpenCV, Harvesters/Aravis (GenICam), SAM-family segmentation and RF-DETR (Apache) where learned detection is needed; TensorRT on the RTX/Jetson; buy inspection (Cognex/Keyence anomaly tools) if build time exceeds benefit (R10 D4).
- **Accept**: each service meets its accuracy and latency budget in `spine/interfaces.csv`.

### M12 MCP server
See §5.

### M13 Digital twin and simulation
- **Stack**: MuJoCo 3.16 (installed) for kinematics, reach, cycle time and policy evaluation; Genesis 1.4.4 (installed) and Isaac Sim 6.x optional for deformables and synthetic images; models exported from Guide 3 (URDF → MJCF).
- **Rule**: simulation qualifies geometry, reach and timing, never cloth behaviour (R10 D5; R15).
- **Accept**: twin cycle time within ±10 % of the measured cell after calibration.

### M14 Data, logging, observability
- **Stack**: PostgreSQL 18 + TimescaleDB, NATS for internal events, OpenTelemetry traces, Grafana/Loki dashboards, object storage for images and LeRobotDataset episodes.
- **Metrics**: accepted shirts per shift, availability, yield, interventions per 100 garments (with cause), per-station occupancy vs. budget.
- **Accept**: the shift test report (Guide 1 §9) is generated automatically from the log.

## 5. MCP server specification (M12)
Built with the official MCP Python SDK (2.x installed in this container; `MCPServer` class, formerly FastMCP). Three tiers; each tool carries its tier and every call is logged to M14.

| Tier | Tools | Who |
|---|---|---|
| read | `get_record`, `list_jobs`, `get_job_status`, `get_cell_state`, `get_metrics`, `get_run_report`, `search_logs`, `get_material_profile` | Any authorised agent |
| design-write | `create_record`, `revise_record`, `generate_pattern`, `nest_marker`, `compile_job`, `simulate_job`, `propose_material_profile` | Designers and agents; outputs are drafts |
| operate | `submit_job_for_approval`, `pause_job`, `resume_job`, `request_operator_intervention` | Operators; every call needs a human approval in M01 before it takes effect |

**Never exposed**: approvals themselves, safety state writes, drive or I/O commands, PLC program changes, skill parameter overrides outside profile limits.

## 6. Safety boundary
- Physical separation: safety logic on TwinSAFE; deterministic control on TwinCAT; ROS 2 and AI on separate PCs.
- Data direction: safety → software read-only; software → PLC goals only, validated by PLC state machines (mode, interlocks, envelopes).
- Proof: architecture review against ISO 13849-1 and ISO/IEC TR 5469; automated build check (M10); penetration test of the cell network before customer delivery (R14 F16).

## 7. Simulation and digital-twin integration
1. Guide 3 exports each assembly to STEP/glTF and a joints file; the URDF emitter builds the cell URDF; MuJoCo compiles MJCF.
2. `SimBackend` implements the HAL on MuJoCo with vendor velocity/acceleration limits.
3. M06 compiles a job; M07 schedules it; M08 executes skills against `SimBackend`; M14 logs it as if it were real.
4. Same steps against `CellBackend` on the real cell. Divergence reports compare per-skill timing and outcomes.

## 8. Development environment and repository layout
- Python 3.13 managed with `uv`; pinned in `pyproject.toml` + lock; Node 22 LTS for M01; ROS 2 Jazzy in a Docker dev container; TwinCAT 3 XAE on a Windows engineering PC.
- Repository:
```
software/
  schema/        M02 Pydantic models, JSON Schema
  pattern/       M03 GarmentCode programs, DXF writer
  nesting/       M04
  profiles/      M05
  compiler/      M06
  scheduler/     M07 (OR-Tools)
  ros2_ws/       M08 skills, behaviour trees; M09 HAL; M11 perception nodes
  plc/           TwinCAT project (ST, safety project separate)
  mcp_server/    M12
  sim/           M13 MuJoCo models (generated from cad/)
  data/          M14 services, dashboards
  web/           M01 Next.js app
```
- CI: lint (ruff, eslint), types (mypy/pyright, tsc), unit tests (pytest, hypothesis), sim integration tests on every merge; Semgrep scan once signed in.

## 9. Milestones and build order
| # | Milestone | Demonstrable result | Depends on |
|---|---|---|---|
| S1 | Schema + pattern + nesting | Approved tee record → graded patterns → marker DXF | — |
| S2 | Twin v1 | Cell model in MuJoCo with UR10e and gantry; reach and timing | Guide 3 C3 |
| S3 | Compiler + scheduler | Tee job compiled and scheduled at 5.47 min interval in sim | S1, S2 |
| S4 | Skill runtime in sim | Full kinematic job run in sim with logging | S3 |
| S5 | Bench HAL | Overlock bench rig driven through HAL; needle camera seam tracking | Guide 1 §10 exp. 1 |
| S6 | Cell HAL | Cutter, gantry, UR10e, heads through one HAL | Guide 1 §8 steps 4–7 |
| S7 | First shirt | One accepted shirt from roll | S6 |
| S8 | Shift test | 12-hour run, report auto-generated | S7 |
| S9 | MCP + workspace | Claude designs a tee variant and submits it for approval | S1, S3 |

## 10. Verification plan
| Level | What | Gate |
|---|---|---|
| Unit | Every module | Coverage on schema, compiler, scheduler ≥ 80 % (target) |
| Integration (sim) | Full job against SimBackend | Runs on every merge |
| Hardware-in-the-loop | TwinCAT in simulation mode / bench rigs | Before each cell deployment |
| Cell acceptance | Guide 1 §9 tests | Before seed milestone demo |
| Safety | M10 checks, SISTEMA, network test | Before any customer unit |
