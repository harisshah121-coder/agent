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
