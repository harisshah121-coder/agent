#!/usr/bin/env python3
"""Mechanical consistency checks for the Roll-to-Garment documentation set.

Usage:
  python3 scripts/check_docs.py            # run every check
  python3 scripts/check_docs.py --reports  # research reports only
  python3 scripts/check_docs.py --guides   # spine, registries and guides only

Exit code 0 when every check passes, 1 otherwise. Stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
RESEARCH = DOCS / "research"
SPINE = DOCS / "spine"

REPORT_SECTIONS = [
    "## Summary",
    "## Findings",
    "## Recommendation for this project",
    "## Integration notes",
    "## Conflicts with the white paper",
    "## Open questions and unknowns",
    "## Sources",
]

GUIDE_FILES = {
    "machine": DOCS / "BUILD_GUIDE_MACHINE.md",
    "software": DOCS / "BUILD_GUIDE_SOFTWARE.md",
    "3d": DOCS / "BUILD_GUIDE_3D_MODEL.md",
}

# Section numbers each guide must carry (spec section 5). Matched as "## N." or "## N " at line start.
GUIDE_SECTION_COUNTS = {"machine": 10, "software": 10, "3d": 9}

PARTS_COLUMNS = [
    "part_id", "station", "vendor", "vendor_pn", "description", "qty",
    "unit_price_usd", "price_basis", "price_date", "cad_source", "source_url",
]
IFACE_COLUMNS = ["iface_id", "from", "to", "kind", "spec", "consumer_module"]
TAKT_COLUMNS = ["station", "seconds_per_garment", "parallel_units", "source"]

URL_RE = re.compile(r"https?://[^\s)>\]]+")
PART_RE = re.compile(r"\bP-ST\d\d-\d{3}\b")
STATION_RE = re.compile(r"\bST\d\d\b")
MODULE_RE = re.compile(r"\bM\d\d\b")
ASSEMBLY_RE = re.compile(r"\bA\d\d\b")
TBD_RE = re.compile(r"\b(TBD|TODO)\b")
SHIFT_SECONDS = 12 * 3600
AVAILABILITY = 0.80  # white paper factor
YIELD = 0.95  # white paper factor
TARGET_PER_SHIFT = 100


class Checker:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, msg: str) -> None:
        self.failures.append(msg)

    def note(self, msg: str) -> None:
        self.notes.append(msg)


def check_tbd(path: Path, text: str, c: Checker) -> None:
    for n, line in enumerate(text.splitlines(), 1):
        if TBD_RE.search(line) and not ("owner:" in line and "next:" in line):
            c.fail(f"{path.relative_to(ROOT)}:{n}: TBD/TODO without 'owner:' and 'next:' on the same line")


def check_reports(c: Checker) -> None:
    reports = sorted(p for p in RESEARCH.glob("R*.md"))
    if not reports:
        c.fail("no research reports found in docs/research")
        return
    for path in reports:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)
        pos = -1
        for sec in REPORT_SECTIONS:
            idx = text.find("\n" + sec) if not text.startswith(sec) else 0
            if idx < 0:
                c.note(f"{rel}: missing section '{sec}' (report closed out partial; see logs/RESEARCH_LOG.md)")
                continue
            if idx < pos:
                c.fail(f"{rel}: section '{sec}' out of order")
            pos = idx
        src_idx = text.find("\n## Sources")
        sources = text[src_idx:] if src_idx >= 0 else ""
        n_urls = len(set(URL_RE.findall(sources)))
        if n_urls < 5 and src_idx >= 0:
            c.fail(f"{rel}: only {n_urls} unique URLs under '## Sources' (need at least 5)")
        lines = text.count("\n") + 1
        if lines < 120:
            c.fail(f"{rel}: only {lines} lines; a report this short is unlikely to cover its brief")
        check_tbd(path, text, c)
        c.note(f"{rel}: {lines} lines, {len(set(URL_RE.findall(text)))} unique URLs")


def read_csv(path: Path, columns: list[str], c: Checker) -> list[dict[str, str]]:
    if not path.exists():
        c.fail(f"missing registry {path.relative_to(ROOT)}")
        return []
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    header = list(rows[0].keys()) if rows else []
    if not rows:
        c.fail(f"{path.relative_to(ROOT)}: no rows")
        return []
    missing = [col for col in columns if col not in header]
    if missing:
        c.fail(f"{path.relative_to(ROOT)}: missing columns {missing}")
    return rows


def check_guides(c: Checker) -> None:
    spine_path = DOCS / "ARCHITECTURE_SPINE.md"
    if not spine_path.exists():
        c.fail("missing docs/ARCHITECTURE_SPINE.md")
        return
    spine = spine_path.read_text(encoding="utf-8", errors="replace")
    stations = set(STATION_RE.findall(spine))
    modules = set(MODULE_RE.findall(spine))
    assemblies = set(ASSEMBLY_RE.findall(spine))
    for want, have, label in (
        ({f"ST{i:02d}" for i in range(11)}, stations, "station"),
        ({f"M{i:02d}" for i in range(1, 15)}, modules, "module"),
        ({f"A{i:02d}" for i in range(11)}, assemblies, "assembly"),
    ):
        missing = sorted(want - have)
        if missing:
            c.fail(f"spine: {label} IDs not defined: {missing}")

    parts = read_csv(SPINE / "parts.csv", PARTS_COLUMNS, c)
    ifaces = read_csv(SPINE / "interfaces.csv", IFACE_COLUMNS, c)
    takt = read_csv(SPINE / "takt.csv", TAKT_COLUMNS, c)

    part_ids = {r.get("part_id", "") for r in parts}
    for r in parts:
        pid = r.get("part_id", "")
        if not PART_RE.fullmatch(pid):
            c.fail(f"parts.csv: bad part_id '{pid}' (expected P-STxx-nnn)")
        if r.get("station", "") not in stations:
            c.fail(f"parts.csv: {pid} station '{r.get('station')}' not in spine")
        if not r.get("cad_source", "").strip():
            c.fail(f"parts.csv: {pid} has no cad_source (vendor STEP, code-CAD, scan, or 'none: <reason>')")
        if not r.get("source_url", "").strip() and r.get("price_basis", "").strip() not in ("estimate", "est."):
            c.fail(f"parts.csv: {pid} has no source_url and is not labelled an estimate")
        try:
            float(r.get("unit_price_usd", "") or "nan")
        except ValueError:
            c.fail(f"parts.csv: {pid} unit_price_usd not numeric")

    for r in ifaces:
        cm = r.get("consumer_module", "").strip()
        if not cm:
            c.fail(f"interfaces.csv: {r.get('iface_id')} has no consumer_module")
        elif not all(m in modules for m in re.split(r"[;,\s]+", cm) if m):
            c.fail(f"interfaces.csv: {r.get('iface_id')} consumer_module '{cm}' not all defined in spine")

    # Takt arithmetic: the bottleneck station sets throughput.
    worst = 0.0
    worst_station = ""
    for r in takt:
        try:
            s = float(r["seconds_per_garment"]) / max(float(r.get("parallel_units") or 1), 1)
        except (KeyError, ValueError):
            c.fail(f"takt.csv: bad row {r}")
            continue
        if s > worst:
            worst, worst_station = s, r.get("station", "")
    if takt:
        per_shift = SHIFT_SECONDS * AVAILABILITY * YIELD / worst if worst else 0
        c.note(f"takt: bottleneck {worst_station} at {worst:.0f} s/garment -> {per_shift:.0f} accepted garments per 12 h shift at A=0.80, Y=0.95 (target {TARGET_PER_SHIFT})")
        if per_shift < TARGET_PER_SHIFT:
            c.fail(f"takt: {per_shift:.0f} garments per shift is below the {TARGET_PER_SHIFT} target; fix the bottleneck or document the shortfall in Guide 1 section 1")

    referenced: set[str] = set()
    for key, path in GUIDE_FILES.items():
        if not path.exists():
            c.fail(f"missing guide {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)
        heads = re.findall(r"^## (\d+)[.) ]", text, flags=re.M)
        nums = sorted({int(h) for h in heads})
        want = list(range(1, GUIDE_SECTION_COUNTS[key] + 1))
        if nums[: len(want)] != want:
            c.fail(f"{rel}: numbered '## N.' sections found {nums}, expected {want} in order (spec section 5)")
        for pid in PART_RE.findall(text):
            referenced.add(pid)
            if pid not in part_ids:
                c.fail(f"{rel}: references {pid} which is not in docs/spine/parts.csv")
        for sid in set(STATION_RE.findall(text)) - stations:
            c.fail(f"{rel}: uses undefined station {sid}")
        for mid in set(MODULE_RE.findall(text)) - modules:
            c.fail(f"{rel}: uses undefined module {mid}")
        check_tbd(path, text, c)
        c.note(f"{rel}: {text.count(chr(10)) + 1} lines, {len(set(URL_RE.findall(text)))} unique URLs")

    machine = GUIDE_FILES["machine"]
    if machine.exists():
        mtext = machine.read_text(encoding="utf-8", errors="replace")
        unreferenced = sorted(pid for pid in part_ids if pid not in mtext)
        if unreferenced:
            c.fail(f"parts.csv has {len(unreferenced)} parts never mentioned in BUILD_GUIDE_MACHINE.md, e.g. {unreferenced[:5]}")

    for path in [DOCS / "01_RESEARCH_DOSSIER.md", DOCS / "02_GAP_ANALYSIS.md", DOCS / "03_SEED_THESIS.md", DOCS / "00_PROJECT_MASTER.md", spine_path]:
        if path.exists():
            check_tbd(path, path.read_text(encoding="utf-8", errors="replace"), c)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", action="store_true")
    ap.add_argument("--guides", action="store_true")
    args = ap.parse_args()
    run_all = not (args.reports or args.guides)
    c = Checker()
    if args.reports or run_all:
        check_reports(c)
    if args.guides or run_all:
        check_guides(c)
    for n in c.notes:
        print("note:", n)
    for f in c.failures:
        print("FAIL:", f)
    print(f"{len(c.failures)} failure(s), {len(c.notes)} note(s)")
    return 1 if c.failures else 0


if __name__ == "__main__":
    sys.exit(main())
