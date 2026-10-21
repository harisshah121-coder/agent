# Decision log (ADR style)

| ID | Date | Decision | Status | Rationale / consequences |
|---|---|---|---|---|
| D-001 | 2026-10-21 | First product is the premium short-sleeve knit T-shirt | Accepted | White paper target; simplest construction (shoulders, neck rib, sleeves, side seams, hems); everything else follows |
| D-002 | 2026-10-21 | Three master guides (machine, software, 3D) keyed by one architecture spine with shared IDs | Accepted | Owner's request; prevents drift between guides |
| D-003 | 2026-10-21 | Research-first with sourced reports; no invented parts or numbers | Accepted | Credibility for a seed raise and for ordering parts |
| D-004 | 2026-10-21 | Code-CAD (build123d on OpenCASCADE) as the master 3D model format; vendor STEP imported; exports to STEP/glTF/URDF/MJCF/USD; Blender for visuals; R3 for the web walkthrough | Proposed | Reproducible, diff-able, scriptable by Claude; to be confirmed by R15 |
| D-005 | 2026-10-21 | Deterministic motion and safety on PLC/safety PLC; AI/ROS 2 plans and perceives but never commands safety | Accepted | White paper principle; standards (ISO 13849) require deterministic safety functions |
| D-006 | 2026-10-21 | Context preservation: CLAUDE.md read-first, STATE.md, logs/ updated every session, everything committed | Accepted | Owner's request |
| D-007 | 2026-10-21 | Project-scoped `.mcp.json` for GitHub-only MCP servers (Nexar/Octopart, KiCad, build123d-mcp); secrets via environment variables, never in the repo | Proposed | No catalog button exists for them; R17 verifies |
