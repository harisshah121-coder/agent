# Roll-to-Garment: read this first

This repository is the working home of an AI-directed roll-to-garment manufacturing venture: a modular, guarded industrial cell that turns a roll of knit fabric into finished garments (first product: a premium short-sleeve T-shirt), driven by an AI software stack that goes from conversational design to pattern, nesting, cutting, manipulation, sewing and finishing. The owner's 53-page white paper is the source of truth for intent; the research reports and build guides in `docs/` are the source of truth for how it gets built.

## Read order for a new session
1. This file.
2. `docs/STATE.md`: where the project is and the next actions.
3. `docs/00_PROJECT_MASTER.md`: everything the project is about and everything we need to do.
4. `docs/logs/SESSION_LOG.md` (latest entry) and `docs/logs/DECISIONS.md`.
5. The guide relevant to the task: `docs/BUILD_GUIDE_MACHINE.md`, `docs/BUILD_GUIDE_SOFTWARE.md`, `docs/BUILD_GUIDE_3D_MODEL.md`, `docs/BUILD_GUIDE_SIMULATION.md`, all keyed by `docs/ARCHITECTURE_SPINE.md`.

## Where things are
- `docs/source/`: the white paper (PDF and extracted text, grep it rather than reading it whole).
- `docs/research/`: sourced research reports R01–R17 and the briefs that produced them.
- Gap register and seed summary: sections 10–11 of `docs/00_PROJECT_MASTER.md` (decision D-012).
- `docs/spine/`: machine-readable registries (parts, interfaces, takt) that the guides reference by ID.
- `docs/logs/`: session log, decisions, research log, tooling status, audits.
- `docs/superpowers/`: design specs and implementation plans.
- `cad/labs/lab1/`: the build-baseline model (D-019) from Ali's Lab 1 STEP files; his raw package goes in `input/` (git-ignored, confidential). Review: `docs/labs/LAB_PACKAGES_REVIEW.md`.
- `cad/concept/`, `cad/out/`: earlier concept 3D model (reference only since D-019), STEP/GLB exports, viewer page generator.
- `sim/`: MuJoCo reach/cycle and SimPy throughput simulations with results.
- `scripts/check_docs.py`: consistency checks; run it after editing any guide.

## Rules for working here
- Identifiers: stations ST00–ST10, software modules M01–M14, 3D assemblies A00–A10, parts `P-<station>-<seq>`. Defined once in `docs/ARCHITECTURE_SPINE.md`; never invent new ones elsewhere.
- Every factual claim carries a source URL or is labelled estimate / unverified. Never invent part numbers, prices or results.
- No `TBD` or `TODO` without `owner:` and `next:` on the same line.
- Before ending a session: append to `docs/logs/SESSION_LOG.md`, update `docs/STATE.md`, record any decision in `docs/logs/DECISIONS.md`, commit.
- Use the superpowers process: brainstorm → plan → execute with subagents → verify before claiming completion.
- Keep model identifiers out of committed files.
- Git: branch `claude/vigilant-goldberg-ize71v`; push with `-u`; open a draft PR when a phase is complete.

## Tooling
See `docs/logs/TOOLING.md` for which plugins, connectors, skills and container installs exist, what they are for, and what still needs the owner.
