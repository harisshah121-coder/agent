#!/usr/bin/env python3
"""Render docs/spine/parts.csv into the BOM block of BUILD_GUIDE_MACHINE.md."""
import csv
from pathlib import Path
root = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(root / "docs/spine/parts.csv", encoding="utf-8")))
out = ["| Part ID | Station | Vendor | Part number | Description | Qty | Unit USD | Basis | Line USD | CAD source |", "|---|---|---|---|---|---|---|---|---|---|"]
tot, by = 0.0, {}
for r in rows:
    line = float(r["qty"]) * float(r["unit_price_usd"])
    tot += line; by[r["station"]] = by.get(r["station"], 0) + line
    out.append(f"| {r['part_id']} | {r['station']} | {r['vendor']} | {r['vendor_pn']} | {r['description']} | {r['qty']} | {float(r['unit_price_usd']):,.0f} | {r['price_basis']} | {line:,.0f} | {r['cad_source']} |")
out += ["", "| Station | Subtotal USD |", "|---|---|"] + [f"| {k} | {v:,.0f} |" for k, v in sorted(by.items())] + [f"| **Total** | **{tot:,.0f}** |"]
g = root / "docs/BUILD_GUIDE_MACHINE.md"
t = g.read_text(encoding="utf-8")
a, b = t.index("<!-- BOM:START -->") + len("<!-- BOM:START -->"), t.index("<!-- BOM:END -->")
g.write_text(t[:a] + "\n" + "\n".join(out) + "\n" + t[b:], encoding="utf-8")
print(f"{len(rows)} parts, total USD {tot:,.0f}")
