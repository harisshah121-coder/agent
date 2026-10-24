# Decision log (ADR style)

| ID | Date | Decision | Status | Rationale / consequences |
|---|---|---|---|---|
| D-001 | 2026-10-21 | First product is the premium short-sleeve knit T-shirt | Accepted | White paper target; simplest construction (shoulders, neck rib, sleeves, side seams, hems); everything else follows |
| D-002 | 2026-10-21 | Three master guides (machine, software, 3D) keyed by one architecture spine with shared IDs | Accepted | Owner's request; prevents drift between guides |
| D-003 | 2026-10-21 | Research-first with sourced reports; no invented parts or numbers | Accepted | Credibility for a seed raise and for ordering parts |
| D-004 | 2026-10-21 | Code-CAD (build123d on OpenCASCADE) as the master 3D model format; vendor STEP imported; exports to STEP/glTF/URDF/MJCF/USD; Blender for visuals; R3 for the web walkthrough | Accepted (R15) | Reproducible, diff-able, scriptable by Claude; to be confirmed by R15 |
| D-005 | 2026-10-21 | Deterministic motion and safety on PLC/safety PLC; AI/ROS 2 plans and perceives but never commands safety | Accepted | White paper principle; standards (ISO 13849) require deterministic safety functions |
| D-006 | 2026-10-21 | Context preservation: CLAUDE.md read-first, STATE.md, logs/ updated every session, everything committed | Accepted | Owner's request |
| D-007 | 2026-10-21 | Project-scoped `.mcp.json` for GitHub-only MCP servers (Nexar/Octopart, KiCad, build123d-mcp); secrets via environment variables, never in the repo | Proposed | No catalog button exists for them; R17 verifies |
| D-008 | 2026-10-22 | Cell architecture: belt gantry with pick heads + one UR10e at sewing presentation | Accepted | R02 F10 option a |
| D-009 | 2026-10-22 | Control: Beckhoff C6030/TwinCAT 3 + TwinSAFE; ROS 2 Jazzy on a separate PC via ADS/OPC UA | Accepted | R05 F1 |
| D-010 | 2026-10-22 | Cutter: iECHO TK4S-2516 conveyor (alternate used Zünd G3 L); do not build from components | Accepted | R01 §I |
| D-011 | 2026-10-22 | Heads: JUKI MO-6814S overlock + MF-7923 UT51 coverstitch with documented-I/O boxes; collar module built in-house | Accepted | R04 |
| D-012 | 2026-10-22 | Skip separate dossier/gap/seed files; gap register and seed summary live in the project master | Accepted | Owner asked to finish quickly |
| D-013 | 2026-10-23 | UR10e on a 7th-axis track (P-ST04-007) instead of a fixed pedestal | Accepted | L1 sim: fixed pedestal misses overlock and inspection |
| D-014 | 2026-10-23 | Add Build Guide 4 (simulation) with seven levels and gates | Accepted | Owner request |
| D-015 | 2026-10-23 | Dedicated flat coverstitch head (P-ST05-006) under the gantry for sleeve hems | Accepted | Frees ~35 s of arm time; +22 points of shifts reaching 100 |
| D-016 | 2026-10-23 | Cutter = 2.5 m cutting zone + 0.6 m pick-off conveyor; gantry columns at x 3.76/5.89 m; blower outside guard | Accepted | Model audit collisions |
| D-017 | 2026-10-23 | Recommend a Canadian-controlled Canadian parent (CCPC) through the seed, with a US subsidiary; foreign investors non-controlling | Proposed | Keeps 35% refundable SR&ED + Ontario 8% (R18) |
| D-018 | 2026-10-23 | Layout v3 from collision-checked robot planning: front-left gantry column moved to x 4.35 m, staging camera above the gantry, pick-off conveyor 0.54 m, gantry travel limits, hemmer rotated; simulation figures restated to collision-checked values (312.8 s arm time, 79 % of shifts reach 100) | Accepted | MuJoCo found arm contacts with the column, camera posts and tables; earlier 287 s / 89 % used unchecked moves |
| D-019 | 2026-10-24 | Adopt A. Sherazee's four-lab plan (Lab Build Packages 2026-10-21, Lab 1 Rev B.2) as the build baseline: Stage 1 bench rigs A-D, then the 6 x 4 m two-cobot cell; our concept model kept as reference only | Accepted | Owner: the new model has to be completely his and from his build guide |
