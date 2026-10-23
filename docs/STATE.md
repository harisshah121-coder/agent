# Project state

Updated: 2026-10-23 (session 1 end)

## Phase
Phase 1 (research and master build guides): **done**. Phase 2 (3D model): next.

## Status
| Item | Status |
|---|---|
| Research R01–R16 | Done. R03, R04, R08, R12, R13, R15 complete; R01, R02, R05, R06, R07, R09, R10, R11, R14, R16 closed out with findings only (sources inline) after repeated usage-limit stops |
| R17 tooling | Installs done (see logs/TOOLING.md); report not written; `.mcp.json` written by hand |
| Machine guide | Done: docs/BUILD_GUIDE_MACHINE.md (BOM generated from docs/spine/parts.csv) |
| Software guide | Done: docs/BUILD_GUIDE_SOFTWARE.md |
| 3D model guide | Done: docs/BUILD_GUIDE_3D_MODEL.md |
| Project master v1 with gaps and seed case | Done |
| Independent audit | Skipped at owner's request (token cost); `scripts/check_docs.py` passes |
| 3D concept model + viewer | Done: cad/concept/cell_concept.py, cad/out/cell_concept.step/.glb, viewer published as a private artifact |
| Simulation guide + L1/L2 sims | Done: docs/BUILD_GUIDE_SIMULATION.md, sim/; audited layout, collision-checked: arm 312.8 s of 328 s, 79 % of shifts reach 100 |
| Model audit | PASS: docs/logs/MODEL_AUDIT.md (all parts placed, dimensions, zero collisions) |
| Draft PR | Blocked: the GitHub repo has no default branch |

## Next actions
0. Close the gap (4.7 % arm margin, 79 % of shifts): MTTR target, shorter regrasp, bench seam timing; add the gantry timeline to L1 (Simulation guide §8.5).
1. 3D guide checkpoint C1: vendor geometry register (`cad/vendor/REGISTER.csv`).
2. 3D guide checkpoint C2: LOD0 envelopes for A00–A10 in build123d on the floor plan.
3. C3 reach study and C4 cycle-time study in MuJoCo.

## Open decisions for the owner
- Create a `main` branch on GitHub so a pull request can be opened.
- Company/product name (placeholder: Roll-to-Garment, R2G).
- First deployment region (CE vs UL/NFPA route).
- Gantry + UR10e (selected) vs. lower-cost presentation for the first cell.
