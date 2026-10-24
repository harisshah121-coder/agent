"""Embed the Lab 1 model, the UR5e rig and the reach-checked keyframes into one artifact page.
Run after build_model.py and sim/labs/lab1_cobots.py:
  python3 cad/labs/lab1/make_artifact.py
"""
import base64, json, pathlib
HERE = pathlib.Path(__file__).parent; OUT = HERE / "out"; ROOT = HERE.parents[2]
b = lambda p: base64.b64encode(p.read_bytes()).decode()
cob = json.loads((ROOT / "sim/results/lab1_cobots.json").read_text())
lay = json.loads((OUT / "lab1_layout.json").read_text())
cob["base"] = {k: v["base"] for k, v in lay["cobots"].items()}
html = (HERE / "artifact_template.html").read_text(encoding="utf-8")
html = html.replace("__CELL__", b(OUT / "lab1_cell.glb")).replace("__RIG__", b(OUT / "ur5e_rig.glb"))
html = html.replace("__RIGMETA__", (OUT / "ur5e_rig.json").read_text()).replace("__COBOTS__", json.dumps(cob)).replace("__LAYOUT__", json.dumps(lay))
(OUT / "lab1_bench.html").write_text(html, encoding="utf-8")
print("artifact bytes", len(html))
