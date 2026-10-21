# Tooling status

Updated 2026-10-21. "Active" means usable in the Claude cloud session for this repo.

## Plugins (claude.ai), by workflow
| Workflow | Plugins | Status |
|---|---|---|
| Method | superpowers, feature-dev, code-review, mcp-server-dev, engineering pack, design pack | Active |
| Research and verification | parallel (search + fetch MCP), firecrawl, exa (server needs auth), research-desk (reference verification MCP), voice-of-customer (HN only), context7 (server needs auth; the Context7 connector is active instead), playwright | Active except where noted |
| Hardware sourcing | factoryfox (supplier search MCP) | Active |
| Seed thesis, IP | founderos, venture-capital-intelligence, pitch-deck-advisor, ip-legal (Descrybe MCP active; CourtListener and Solve Intelligence need auth), product-management | Active |
| 3D, simulation | unity skills, meshy, diagrams; R3 connector | Active |
| Infra | docker-skills, huggingface-skills (server needs auth), semgrep (hook nags until signed in from a desktop; harmless) | Active |

## Connectors (claude.ai)
Active and enabled here: R3, alphaXiv, Wolfram, Linear, Neon, Sentry, Figma, Context7, Mermaid Chart, Excalidraw, Autodesk Product Help, Vercel, Google Drive, Gmail, Google Calendar, Apollo, ZoomInfo.
Not connected and not needed this phase: Roboflow (dataset labelling; alternatives: CVAT, Label Studio, SAM-based auto-labelling), Solve Intelligence (patent drafting; alternatives: Google Patents, Lens.org, ip-legal skills).

## Container installs (self-service, no owner action)
| Harness | Purpose | Status |
|---|---|---|
| build123d 0.13.0 on cadquery-ocp 8.0.1, Python 3.13 (venv /home/user/.venvs/cad) | Code-CAD master model | Installed and smoke-tested (STEP, glTF, STL export) 2026-10-21 |
| build123d-mcp, text-to-cad skills, ros-mcp-server, nexar-mcp, partuno, mcp-server-kicad, mujoco, genesis, GarmentCode, onshape-to-robot | See R17 report | R17 verifies and records |

## Project MCP servers (`.mcp.json`)
Servers that exist only on GitHub/PyPI (no claude.ai catalog entry) are registered in the repo's `.mcp.json` so they load in later sessions. Secrets (Nexar client ID/secret, DigiKey/Mouser keys) are environment variables set in the cloud environment settings, never committed. R17 writes the file and the instructions.

## Final sweep results (2026-10-21)
- KiCad MCP servers: oaslananka-lab/kicad-mcp-pro, mcp-server-kicad (PyPI), mixelpixx/KiCAD-MCP-Server, Seeed-Studio kicad-mcp. Relevant only when electrical schematics are drawn (industrial cabinets are usually drawn in EPLAN; KiCad is the open alternative).
- Parts pricing: LukeL99/nexar-mcp (Octopart/Nexar API; free tier), Partuno (DigiKey + Mouser; own keys). Useful for the electrical BOM.
- CAD: PTC Onshape FeatureScript MCP (official, Aug 2026); Fusion 360 and FreeCAD community MCPs; "3D CAD Converter" plugin (Windows, local file conversion) is optional for the owner's PC.
- Nothing else in the catalogs or on the web changes the plan.
