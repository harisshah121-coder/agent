# Design spec: Roll-to-Garment master build guides (phase 1)

Date: 2026-10-21 · Status: approved by owner directive (the owner asked for the three guides, the master document and the logs in plain words; the interactive review gate was collapsed because the owner is not available mid-task). Corrections are welcome at any time and will be folded in.

## 1. Intent (what the owner asked for, in their words, condensed)
- Build everything: the software, the 3D model and (later) the machine. First research every element, then write master build guides the build can be executed from.
- Three final guides: the machine (every component, real parts, every brand, "every nail and wire", especially the robotics), the software, and the 3D model (every single model).
- A master document that covers everything the project is about and everything we need to do.
- Context and memory preserved across sessions: logs for everything.
- Make it a genuine $10M seed-raise idea: find all holes and fix them.
- Verify, audit and sanity-check everything. Research what is happening right now in physical AI, manufacturing robotics, motion control and machine vision so the guides are true to life.
- Use the superpowers process to plan and execute; use the best MCP servers and skills for every workflow.

## 2. Assumptions (mine; say so if any is wrong)
1. First product is the white paper's premium short-sleeve knit T-shirt. Everything is designed so other garments follow without redesign, but the T-shirt is what the guides must get built.
2. The white paper (`docs/source/white_paper.txt`, extracted from the PDF beside it) is the source of truth for intent. Where research contradicts it, the guides say so and the gap analysis records the resolution.
3. The guides are written for execution by Claude with the owner approving purchases and doing physical work, so every step is explicit, numbered and testable.
4. Prices are USD unless stated, dated, and labelled list / quote / estimate. No part is invented: every part cited has a vendor page or datasheet link, or is marked "candidate, unverified".
5. Software is built open-source-first; commercial tools are allowed where they are the industry standard and the guide says why.

## 3. Deliverables (all under `docs/`)
| File | Purpose |
|---|---|
| `../CLAUDE.md` | Read-first context for any session: what the project is, where things are, rules |
| `STATE.md` | Live status and next actions |
| `00_PROJECT_MASTER.md` | Everything the project is about and everything we need to do |
| `01_RESEARCH_DOSSIER.md` | Index and synthesis of all research reports, with conflicts resolved |
| `02_GAP_ANALYSIS.md` | Every hole found in the white paper and plan, with the fix |
| `03_SEED_THESIS.md` | The $10M seed case: why now, why this, milestones the money buys |
| `ARCHITECTURE_SPINE.md` | Shared identifiers, interfaces and parts registry all three guides use |
| `BUILD_GUIDE_MACHINE.md` | Guide 1: the physical cell, every component, real parts, assembly, commissioning |
| `BUILD_GUIDE_SOFTWARE.md` | Guide 2: the whole software stack, module by module, with tests |
| `BUILD_GUIDE_3D_MODEL.md` | Guide 3: every 3D model, the toolchain, vendor geometry import, simulation, walkthrough |
| `research/*.md` | One sourced report per research domain (R01–R17), plus the briefs that produced them |
| `logs/SESSION_LOG.md`, `logs/DECISIONS.md`, `logs/RESEARCH_LOG.md`, `logs/TOOLING.md` | Memory across sessions |
| `superpowers/specs/*`, `superpowers/plans/*` | This spec and the implementation plan |
| `scripts/check_docs.py` (repo root `scripts/`) | Mechanical consistency checks across the guides |

## 4. Shared spine (summary; the full version lives in `ARCHITECTURE_SPINE.md`)
Stations: ST00 frame/guarding/infrastructure · ST01 roll handling · ST02 cutting · ST03 extraction and buffer · ST04 manipulation (gantry + arm + gripper toolbox) · ST05 sewing heads · ST06 collar/neckband module · ST07 finishing, inspection, output · ST08 optional decoration · ST09 control and safety · ST10 vision and compute.
Software modules: M01 design workspace · M02 canonical garment record · M03 pattern engine · M04 nesting · M05 material profiles · M06 assembly compiler · M07 cell scheduler · M08 skill runtime · M09 motion control and hardware abstraction · M10 independent safety layer · M11 perception · M12 MCP server · M13 digital twin and simulation · M14 data, logging, observability.
3D assemblies mirror stations: A00–A10. Part IDs: `P-<station>-<seq>` with a vendor part number beside every ID.
Interfaces: every station declares mechanical (mounting, envelope, mass), electrical (voltage, I/O, fieldbus), pneumatic (pressure, flow, ports) and data (messages, rates) interfaces in the same table format.

## 5. Required structure of each guide
### Guide 1: machine
1. Scope and product specification (the T-shirt: fabric, construction, tolerances, takt time budget per station).
2. Cell architecture and layout: footprint, flow, dimensions, utilities (power, air, network), floor plan.
3. Per station (ST00–ST10): function; requirements; candidate parts table; selected part and alternates with reasons; integration (mechanical, electrical, pneumatic, data); build steps; acceptance tests.
4. Electrical and control architecture: cabinet layout, drives, I/O list, network, safety circuit.
5. Pneumatics and vacuum: schematic-level description, sizing.
6. Safety and compliance plan: standards, risk assessment method, PL targets, guarding, certification route.
7. Complete bill of materials: every part, fastener class, cable, consumable, with cost at three tiers ($52k / $83k / $140k white-paper scenarios mapped to real parts), and the sourcing plan with lead times.
8. Assembly sequence and commissioning plan, with the order in which subsystems are brought up and tested.
9. Test and validation protocol: factory acceptance, site acceptance, the 100-shirt shift test.
10. Risks, unknowns and the experiments that retire them.
### Guide 2: software
1. Scope and principles (deterministic control, AI never commands safety, simulation parity).
2. Architecture: modules, data flow, deployment topology (cell PC, PLC, cloud/workstation).
3. Data model: canonical garment record, job package, material profile, cell configuration, event log.
4. Per module (M01–M14): purpose; interfaces (API, message types, schemas); dependencies; implementation plan; tests; acceptance criteria.
5. MCP server specification: tools per permission tier; what is never exposed.
6. Safety boundary and how software proves it stays on its side.
7. Simulation and digital twin integration: same job package drives sim and cell.
8. Development environment, repository layout, CI, coding standards, versions pinned.
9. Milestones and build order (sprint-level), with what is demonstrable at each.
10. Verification plan: unit, integration, hardware-in-the-loop, shift tests.
### Guide 3: 3D model
1. Purpose and outputs (STEP, glTF, URDF/MJCF, USD, Blender, R3 walkthrough) and what each is for.
2. Toolchain and environment with pinned versions and verified install commands.
3. Modelling conventions: units, origins, naming, levels of detail, assembly structure, metadata for BOM.
4. Vendor geometry import workflow, per vendor source, with the fallback when no CAD exists.
5. Per assembly (A00–A10): parts list → source of each model (vendor STEP or code-CAD) → joints and kinematics → animation and simulation hooks.
6. Simulation setup (MuJoCo first, Isaac Sim optional) and the cycle-time study method.
7. Blender animation and the R3 interactive walkthrough.
8. BOM generation from the model and reconciliation with Guide 1.
9. Verification checklist: interference, reach, envelope, cycle time, mass, centre of gravity.

## 6. Process
1. Research first: 17 parallel agents, one per domain, each writing a sourced report to `docs/research/`.
2. Synthesis: dossier, gap analysis, seed thesis.
3. Spine, then the three guides written in parallel from the spine and the research, then an independent audit agent that checks consistency and unsupported claims, then fixes.
4. `scripts/check_docs.py` runs after every writing step. Logs updated at each phase. Commit at each phase. Push and draft PR at the end of the phase.

## 7. Quality bar and success criteria
- A competent integrator can order parts and start building from Guide 1; a developer can start sprint 1 from Guide 2; a CAD operator (or Claude) can produce every model from Guide 3.
- Every number is sourced or labelled as an estimate. No "TBD" without an owner and a next action.
- Cross-guide consistency: same IDs, same selected parts, same interfaces, same takt-time budget.
- The gap analysis closes or explicitly schedules every hole found; the seed thesis is defensible against the skeptical-investor review.

## 8. Out of scope for this phase
Writing production code, producing CAD files, buying parts, the pitch deck itself. These are the next phases and the guides are their input.
