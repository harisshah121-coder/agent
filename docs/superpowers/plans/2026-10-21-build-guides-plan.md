# Roll-to-Garment Build Guides Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce three executable master build guides (machine, software, 3D model), the project master document, the seed thesis, and a context-preservation system, all grounded in sourced research.

**Architecture:** Research fans out to 17 isolated agents that write sourced reports. A shared spine fixes identifiers and interfaces. Three writer agents produce the guides from the spine and the reports. An independent auditor checks the set. A script checks mechanical consistency after every step.

**Tech Stack:** Markdown in git; Python 3.13 for the checker; research via web search, Parallel search, alphaXiv, Context7, FactoryFox.

**Spec:** `docs/superpowers/specs/2026-10-21-build-guides-design.md`

## Global Constraints
- Every factual claim in a guide or report carries a source URL or is labelled "estimate" or "unverified".
- Station IDs ST00–ST10, module IDs M01–M14, assembly IDs A00–A10 and part IDs `P-<station>-<seq>` are the only identifiers used; `ARCHITECTURE_SPINE.md` is their single definition.
- Prices in USD unless stated, with date and list/quote/estimate label.
- No model identifiers in any committed file.
- Commit after each task with the required trailers; logs updated before each commit.

## Review Focus
1. A part selected in Guide 1 that Guide 3 cannot obtain geometry for: the checker must flag any `P-` ID without a CAD source entry.
2. A station interface whose electrical or data side is declared in Guide 1 but not consumed by any module in Guide 2: the checker lists interfaces by ID and reports orphans.
3. A takt-time budget that does not sum to the 100-shirts-per-12-hour target: Guide 1 section 1 shows the arithmetic and the checker recomputes it from a machine-readable table.
4. A white-paper figure that research contradicts but a guide still repeats: the dossier's conflicts table is cross-referenced by the auditor against every number in the guides.
5. A "TBD" that survives into a final guide: the checker fails on `TBD`/`TODO` tokens without an `owner:` and `next:` annotation on the same line.

---

### Task 1: Context scaffolding
**Files:** Create `CLAUDE.md`, `docs/STATE.md`, `docs/00_PROJECT_MASTER.md` (v0), `docs/logs/*.md`, `docs/research/_BRIEF_COMMON.md`, `docs/research/_BRIEFS.md`.
**Produces:** the briefs every research agent reads; the log files every later task appends to.
- [x] Write the files (this session, 2026-10-21).
- [ ] Commit: `docs: add spec, plan, context files and research briefs`.

### Task 2: Research fan-out
**Files:** Create `docs/research/R01_*.md` … `R17_*.md`; `.mcp.json` (by R17).
**Interfaces:** Consumes `_BRIEF_COMMON.md` + the agent's section of `_BRIEFS.md`. Produces one report per domain with the six required sections.
- [ ] Dispatch 17 agents in one response (general-purpose), one per brief section.
- [ ] On each return: record path, summary, unknowns and conflicts in `docs/logs/RESEARCH_LOG.md`.
- [ ] Verify each report has the six required sections and a non-empty Sources list: `python3 scripts/check_docs.py --reports`.
- [ ] Commit: `research: add R01–R17 sourced reports`.

### Task 3: Synthesis documents
**Files:** Create `docs/01_RESEARCH_DOSSIER.md`, `docs/02_GAP_ANALYSIS.md`, `docs/03_SEED_THESIS.md`.
**Interfaces:** Consumes all reports. Produces the conflicts table (dossier §Conflicts) and the gap register (gap analysis table with columns `ID | Hole | Evidence | Fix | Where fixed | Status`), which Guide writers must honour.
- [ ] Write the dossier: one section per report with the decision-relevant findings, then cross-cutting themes, then the conflicts-with-white-paper table.
- [ ] Write the gap analysis: every hole from the reports plus my own reading of the white paper, each with a fix and where in the guides it lands.
- [ ] Write the seed thesis; run the `founderos:skeptical-investor` agent on it; fix what it finds.
- [ ] Commit: `docs: add research dossier, gap analysis, seed thesis`.

### Task 4: Spine and checker
**Files:** Create `docs/ARCHITECTURE_SPINE.md`, `scripts/check_docs.py`, `docs/spine/parts.csv`, `docs/spine/interfaces.csv`, `docs/spine/takt.csv`.
**Interfaces:** Produces the ID registry (stations, modules, assemblies), the parts registry CSV (`part_id,station,vendor,vendor_pn,description,qty,unit_price_usd,price_basis,price_date,cad_source,source_url`), the interfaces CSV (`iface_id,from,to,kind,spec,consumer_module`), the takt CSV (`station,seconds_per_garment,parallel_units,source`). The guides reference these by ID.
- [ ] Write the spine from the dossier's selections.
- [ ] Write the checker: `--reports` (six sections + sources), `--guides` (IDs defined, parts have CAD source, interfaces consumed, takt sums, TBD rule). Run on current files; expected: reports pass, guides not yet present.
- [ ] Commit: `docs: add architecture spine, registries and checker`.

### Task 5–7: The three guides (parallel writer agents)
**Files:** Create `docs/BUILD_GUIDE_MACHINE.md`, `docs/BUILD_GUIDE_SOFTWARE.md`, `docs/BUILD_GUIDE_3D_MODEL.md`.
**Interfaces:** Each consumes the spine, the registries, the dossier, the gap analysis and the relevant reports. Each must follow the section structure in the spec §5 exactly. Guide 1 populates `parts.csv`; Guide 3 populates `cad_source` for every part; Guide 2 lists the interface IDs each module consumes.
- [ ] Dispatch three writer agents in one response with the spec section, the spine, and the file list to read.
- [ ] Run `python3 scripts/check_docs.py --guides`; fix failures with targeted edits.
- [ ] Commit: `docs: add the three master build guides`.

### Task 8: Independent audit
**Files:** Modify the guides and synthesis docs as needed; create `docs/logs/AUDIT_2026-10-21.md`.
- [ ] Dispatch one auditor agent (fresh context) with the spec §7 quality bar and the Review Focus list; it writes findings with severity and exact locations.
- [ ] Fix every blocking finding; record the rest with owner and next action.
- [ ] Re-run the checker; expected: pass.
- [ ] Commit: `docs: audit fixes`.

### Task 9: Finalize and publish
**Files:** Modify `docs/00_PROJECT_MASTER.md` (v1), `README.md`, `docs/STATE.md`, logs.
- [ ] Rewrite the master document from the final guides; update STATE and logs; record decisions.
- [ ] Push to `claude/vigilant-goldberg-ize71v`; open a draft PR; subscribe to its activity.
- [ ] Report to the owner with the file map and the open decisions that need them.
