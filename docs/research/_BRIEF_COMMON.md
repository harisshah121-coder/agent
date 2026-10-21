# Common brief for research agents (read fully before starting)

## Project in one paragraph
We are building an AI-directed roll-to-garment manufacturing cell: a modular, guarded industrial machine that takes a roll of knit fabric and produces finished garments (first product: a premium short-sleeve T-shirt), with an AI-driven software stack doing design → pattern → nesting → cutting → manipulation → sewing → finishing. The owner's white paper is the source of truth for intent: `/home/user/agent/docs/source/white_paper.txt` (extracted text, 3,009 lines; PDF beside it). Targets from the white paper: at least 100 acceptable premium T-shirts per 12-hour shift; factory build-and-test cost scenarios $52,000 / $83,000 / $140,000; reference selling price $100,000; one operator supervising; deterministic control; AI never commands safety. This is physical AI applied to apparel; the guides we write from your report must be true to what exists in October 2026.

## Cell stations (use these IDs)
ST00 Frame, guarding, cell infrastructure · ST01 Roll handling (loading, unwind, edge guiding, tension, relaxation, feed) · ST02 Cutting (single-ply knife cutting on a vacuum conveyor bed; nesting; piece ID) · ST03 Extraction and buffer (pick cut pieces off the bed, remove scrap, stage pieces) · ST04 Manipulation (gantry + arm + gripper toolbox; place and align plies at sewing stations) · ST05 Sewing heads (overlock 504/514, coverstitch 406/602, lockstitch 301; automatic presser foot, trimmer, feed control) · ST06 Collar/neckband module (rib attach with split support and differential feed) · ST07 Finishing, inspection, output (thread trim, inspection camera, fold/stack/bag, label) · ST08 Optional decoration (embroidery, DTG/DTF print, heat press) · ST09 Control and safety (PLC, safety PLC, drives, I/O, HMI, e-stops, light curtains, interlocks) · ST10 Vision and compute (cameras, 3D sensors, lighting, edge inference PC, networking).

## Software modules (for software-related reports)
M01 Design workspace · M02 Canonical garment record · M03 Pattern engine (GarmentCode) · M04 Nesting · M05 Material profiles · M06 Assembly compiler (garment → operations → skills) · M07 Cell scheduler · M08 Skill runtime (behaviour trees) · M09 Motion control and hardware abstraction (simulation and physical backends) · M10 Independent safety layer · M11 Perception · M12 MCP server (read / design-write / operate tiers; approval and safety never exposed) · M13 Digital twin and simulation · M14 Data, logging, observability.

## What your report must contain
Write Markdown to the exact path in your task. Structure, in this order:
1. `## Summary`: 8–15 bullets with the decisions this research supports.
2. `## Findings`: organized by sub-topic. Hardware tables use the columns `Vendor | Model / part number | Key specs | Price (currency, date, list/quote/est.) | Lead time | CAD available? (format, where) | Source URL`. Software and research tables use `Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL`.
3. `## Recommendation for this project`: a selected option plus one or two alternates per decision, with reasoning and risk.
4. `## Integration notes`: mechanical, electrical, pneumatic and data interfaces; everything else the selection needs to work (cables, connectors, mounts, drivers, software).
5. `## Conflicts with the white paper`: where what you found contradicts an assumption in the white paper (grep it), stated plainly. Write "None found" if none.
6. `## Open questions and unknowns`: what you could not confirm and the cheapest way to confirm it (quote request, sample, test).
7. `## Sources`: every URL you relied on, numbered, with a few words on what it supported.

## Rigor rules (non-negotiable)
- Every factual claim (spec, price, availability, date, paper result) carries a source URL. No source: mark "unverified" explicitly.
- Never invent part numbers, prices or benchmark results. If a price is not published, write "price not published; request quote" and, if possible, an order-of-magnitude estimate clearly labelled "est." with the basis.
- Prefer primary sources: vendor product pages, datasheets, manuals, standards bodies, papers, official docs, GitHub repositories. Reseller pages are fine for prices; say which reseller.
- Prices carry currency and the date you saw them, and the basis (list, reseller, quote, estimate).
- Record whether CAD (STEP/IGES/native/URDF) is downloadable and where (vendor configurator, TraceParts, 3DContentCentral, PARTcommunity, McMaster-Carr, GrabCAD, ROS descriptions). We will build the 3D model from vendor geometry, so this column matters as much as the price.
- Today is 2026-10-21. Prefer 2025–2026 information; flag anything older than 2023 as possibly stale.

## Tools
- Web: `WebSearch` (mode "standard" first; "extended" for niche or very recent topics) and `WebFetch`. Load the Parallel search tools with `ToolSearch` query `select:mcp__plugin_parallel_parallel-search__web_search,mcp__plugin_parallel_parallel-search__web_fetch`; they accept several queries per call and return excerpts, good for broad sweeps and for fetching several URLs with one objective.
- Papers: load `mcp__alphaXiv__discover_papers`, `mcp__alphaXiv__get_paper_content` via ToolSearch.
- Library docs: `mcp__Context7__resolve-library-id` and `mcp__Context7__query-docs` via ToolSearch.
- Suppliers: `mcp__plugin_factoryfox_factoryfox__search_suppliers` via ToolSearch.
- The white paper: `grep -n -i "<term>" /home/user/agent/docs/source/white_paper.txt`, then `sed -n 'A,Bp'` for the passage. Do not read the whole file into context at once.
- Write your report with Bash heredocs (`cat > file <<'EOF'`), early and incrementally (append sections with `cat >> file <<'EOF'`), so nothing is lost if you run out of budget. Write the Summary last by prepending it or by editing.
- Do not ask the user questions. Do not run git commands. Do not modify any file other than your report (R17 is the exception named in its task). Do not install software unless your task says so.

## Budget and finish
- Aim for 30–80 searches or fetches. Cover every item in your task list; if an item has no good source after three attempts, record it as unknown and move on. Do not loop.
- When done, reply with: the report path; a summary of at most 250 words of the most decision-relevant findings; the three biggest unknowns; any conflicts with the white paper. The file is the deliverable; the reply is the handoff.
