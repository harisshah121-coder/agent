# Roll-to-Garment: project master document (v0, 2026-10-21)

This is the one document that says what the project is and everything we need to do. v0 is written from the owner's white paper (research snapshot dated 19 October 2026) and the session-1 decisions. v1 will be rewritten from the finished research and the three build guides.

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
| 1 (now) | Research every element; write the three master build guides, the dossier, the gap analysis, the seed thesis | `docs/` set, draft PR |
| 2 | 3D model: toolchain, vendor geometry import, every assembly, kinematics, cycle-time simulation, Blender animation, R3 walkthrough | model repo, demos |
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
