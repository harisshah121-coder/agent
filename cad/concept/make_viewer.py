"""Build cad/out/cell_viewer.html: an interactive three.js viewer with the GLB embedded."""
import base64, csv, json
from pathlib import Path
root = Path(__file__).resolve().parents[2]
glb = base64.b64encode((root / "cad/out/cell_concept.glb").read_bytes()).decode()
rows = list(csv.DictReader(open(root / "docs/spine/parts.csv", encoding="utf-8")))
names = {"ST00": "Frame & guarding", "ST01": "Roll handling", "ST02": "Cutting", "ST03": "Extraction & buffer",
         "ST04": "Manipulation", "ST05": "Sewing heads", "ST06": "Collar module", "ST07": "Inspection & output",
         "ST08": "Decoration (optional)", "ST09": "Control & safety", "ST10": "Vision & compute"}
group = {"ST00": "A00 Frame and guarding", "ST01": "A01 Roll handling", "ST02": "A02 Cutter", "ST03": "A03 Extraction and buffer",
         "ST04": "A04 Manipulation", "ST05": "A05 Sewing heads", "ST06": "A06 Collar module", "ST07": "A07 Finishing and output",
         "ST08": "", "ST09": "A09 Control and safety", "ST10": "A10 Vision and compute"}
stations = []
for sid, nm in names.items():
    parts = [r for r in rows if r["station"] == sid and float(r["qty"]) > 0]
    cost = sum(float(r["qty"]) * float(r["unit_price_usd"]) for r in parts)
    stations.append({"id": sid, "name": nm, "group": group[sid], "cost": round(cost),
                     "parts": [f'{r["vendor"].split(" /")[0]} {r["vendor_pn"].split(" +")[0]}'[:48] for r in parts][:5]})
total = sum(s["cost"] for s in stations)
html = (root / "cad/concept/viewer_template.html").read_text(encoding="utf-8")
html = html.replace("__STATIONS__", json.dumps(stations)).replace("__TOTAL__", f"{total:,}").replace("__GLB__", glb)
(root / "cad/out/cell_viewer.html").write_text(html, encoding="utf-8")
print("viewer bytes", len(html))
