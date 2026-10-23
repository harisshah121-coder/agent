"""Build cad/out/cell_viewer.html: an interactive three.js viewer with the GLB embedded."""
import base64, csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from hotspots import HOTSPOTS
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
rig = base64.b64encode((root / "cad/out/ur10e_rig.glb").read_bytes()).decode()
rigmeta = (root / "cad/out/ur10e_rig.json").read_text()
rc = json.loads((root / "sim/results/reach_cycle.json").read_text())
td = json.loads((root / "sim/results/throughput_des.json").read_text())
sim = {"arm_s": rc["layout_B_seventh_axis"]["cycle"]["arm_occupancy_s"], "required_s": rc["assumptions"]["required_interval_s"],
       "fixed_fail": [k for k, v in rc["layout_A_fixed_pedestal"]["reach"].items() if not v["reachable"]],
       "a080": [c for c in td["cases_availability_080"] if c["p_intervention"] == 0.01]}
html = (root / "cad/concept/viewer_template.html").read_text(encoding="utf-8")
html = html.replace("__HOTSPOTS__", json.dumps(HOTSPOTS)).replace("__RIG__", rig).replace("__RIGMETA__", rigmeta).replace("__SIM__", json.dumps(sim))
html = html.replace("__STATIONS__", json.dumps(stations)).replace("__TOTAL__", f"{total:,}").replace("__GLB__", glb)
(root / "cad/out/cell_viewer.html").write_text(html, encoding="utf-8")
print("viewer bytes", len(html))
