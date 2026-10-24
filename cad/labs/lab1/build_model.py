"""Build the Lab 1 / Stage 2 cell model from his STEP files and layout.py.

Outputs (cad/labs/lab1/out/): lab1_cell.glb (named nodes), lab1_boxes.json (static AABBs in metres for MuJoCo),
lab1_layout.json (pedestal tops, hinge axis, work points for the viewer and the sim).
Run: /home/user/.venvs/cad/bin/python cad/labs/lab1/build_model.py
"""
import json, math, pathlib, sys
from build123d import import_step, Box, Cylinder, Cone, Pos, Rot, Color

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import layout as L

IN, OUT = HERE / "input", HERE / "out"
OUT.mkdir(exist_ok=True)
MAT = {"steel": (0.42, 0.44, 0.47, 1), "alu": (0.78, 0.8, 0.82, 1), "skin": (0.9, 0.9, 0.88, 1), "bought": (0.25, 0.27, 0.3, 1)}

def colour_for(name):
    if any(k in name for k in ("plate", "sheet")): return MAT["skin"] if "sheet" in name else MAT["alu"]
    if any(k in name for k in ("plenum", "chute", "upright", "crossbar")): return MAT["alu"]
    if "(ref)" in name or "_ref_" in name or "candidate" in name or "pillow" in name: return MAT["bought"]
    return MAT["steel"]

cache, parts, boxes, seen = {}, [], [], {}
for fname, label, (x, y, z), rz in L.PARTS:
    if fname not in cache: cache[fname] = import_step(str(IN / fname))
    for k in cache[fname].children:
        nm = k.label or "part"
        if fname.startswith("FT-200"):
            b = k.bounding_box()
            moving = nm.startswith(L.FT_MOVING) or (nm.startswith("FT-206") and b.max.Y <= L.FT_MOVING_SHEET_Y_BELOW + 1e-6)
            if nm.startswith("FT-206") and moving: nm = "FT-206_moving_sheet"   # his STEP labels this sheet 'fixed'
            nm = ("FTMOVE " if moving else "") + nm
        key = f"{label} | {nm}"; seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key += f" #{seen[key]}"                            # his STEP repeats some labels
        s = k.moved(Pos(x, y, z) * Rot(0, 0, rz)); s.label = key
        s.color = Color(*colour_for(nm)); parts.append(s)
        if not key.split("| ")[1].startswith("FTMOVE"):
            bb = s.bounding_box()
            boxes.append(dict(name=key, min=[bb.min.X / 1e3, bb.min.Y / 1e3, bb.min.Z / 1e3], max=[bb.max.X / 1e3, bb.max.Y / 1e3, bb.max.Z / 1e3]))

def env(label, kind, c, size, rgba):
    if kind == "box":
        s = Pos(c[0], c[1], c[2] + size[2] / 2) * Box(*size)
    elif kind == "cyl":
        s = Pos(c[0], c[1], c[2] + size[1] / 2) * Cylinder(size[0] / 2, size[1])
    elif kind == "cone":
        s = Pos(c[0], c[1], c[2] + size[2] / 2) * Cone(size[0] / 2, size[1] / 2, size[2])
    elif kind == "cylx":
        s = Pos(*c) * Rot(0, 90, 0) * Cylinder(size[0] / 2, size[1])
    else:  # cyly
        s = Pos(*c) * Rot(90, 0, 0) * Cylinder(size[0] / 2, size[1])
    s.label = label; s.color = Color(*rgba); return s

for e in L.ENVELOPES:
    s = env(*e); parts.append(s)
    if not e[0].startswith("FABRIC"):
        bb = s.bounding_box()
        boxes.append(dict(name=e[0], min=[bb.min.X / 1e3, bb.min.Y / 1e3, bb.min.Z / 1e3], max=[bb.max.X / 1e3, bb.max.Y / 1e3, bb.max.Z / 1e3]))

# fence (Lab 1 item 7): 40 mm posts every ~1 m and mesh panels; openings and door left out of the panels
Lc, Wc, H = L.CELL["L"], L.CELL["W"], L.CELL["fence_h"]
def panel(x0, y0, x1, y1, tag):
    lx, ly = max(abs(x1 - x0), 20), max(abs(y1 - y0), 20)
    s = Pos((x0 + x1) / 2, (y0 + y1) / 2, 100 + (H - 100) / 2) * Box(lx, ly, H - 100)
    s.label = f"L1 fence panel {tag}"; s.color = Color(0.95, 0.75, 0.1, 0.25); return s
o = L.FENCE
spans = [(0, 0, 0, Wc, "left"), (0, Wc, o["door_back"][0], Wc, "back 1"), (o["door_back"][1], Wc, Lc, Wc, "back 2")]
for x0, y0, x1, y1, tag in spans: parts.append(panel(x0, y0, x1, y1, tag))
door = Pos(sum(o["door_back"]) / 2, Wc, 100 + (H - 100) / 2) * Box(o["door_back"][1] - o["door_back"][0], 20, H - 100)
door.label = "L1 fence interlocked service door"; door.color = Color(0.95, 0.55, 0.1, 0.35); parts.append(door)
floor = Pos(Lc / 2, Wc / 2, -5) * Box(Lc + 1000, Wc + 1000, 10); floor.label = "floor"; floor.color = Color(0.2, 0.21, 0.22, 1); parts.append(floor)

# GLB via trimesh: per-part tessellation. The hole-grid base plates sit under the perforated skin and the
# plinth grid plates are seen from above, so they get a coarser tolerance (geometry unchanged, fewer triangles).
import numpy as np, trimesh
COARSE = ("base_plate", "fixed_plate", "moving_plate", "SP-401", "CP-301", "RB-501")
scene = trimesh.Scene()
for s in parts:
    coarse = any(k in s.label for k in COARSE)
    v, t = s.tessellate(4.0 if coarse else 0.8, 1.2 if coarse else 0.4)
    if not t: continue
    m = trimesh.Trimesh(np.array([(p.X, p.Y, p.Z) for p in v]) / 1000.0, np.array(t), process=False)
    rgba = (np.array(tuple(s.color)) * 255).astype(np.uint8)
    m.visual = trimesh.visual.ColorVisuals(m, face_colors=np.tile(rgba, (len(t), 1)))
    scene.add_geometry(m, node_name=s.label, geom_name=s.label)
scene.export(str(OUT / "lab1_cell.glb"))

# layout facts the sim and viewer need (metres)
def place(origin, rz, lx, ly, lz=0.0):
    c, sn = math.cos(math.radians(rz)), math.sin(math.radians(rz))
    return [(origin[0] + c * lx - sn * ly) / 1e3, (origin[1] + sn * lx + c * ly) / 1e3, (origin[2] + lz) / 1e3]
ped = {lab: (o, rz) for f, lab, o, rz in L.PARTS if f.startswith("CP-300")}
fo, frz = next((o, rz) for f, lab, o, rz in L.PARTS if f.startswith("FT-200"))
ro, rrz = next((o, rz) for f, lab, o, rz in L.PARTS if f.startswith("RT-100"))
info = dict(
    stage=L.CELL["stage"],
    cobots={k: dict(base=place(ped[v["pedestal"]][0], 0, 250, 250, 700)) for k, v in L.COBOTS.items()},
    hinge=dict(p0=place(fo, frz, 0, L.FT_HINGE_LOCAL["y"], L.FT_HINGE_LOCAL["z"]), p1=place(fo, frz, 1200, L.FT_HINGE_LOCAL["y"], L.FT_HINGE_LOCAL["z"])),
    folding_table=dict(fixed=[place(fo, frz, x, y, 850) for x, y in ((0, 3), (1200, 3), (1200, 803), (0, 803))],
                       moving=[place(fo, frz, x, y, 850) for x, y in ((0, -3), (1200, -3), (1200, -803), (0, -803))]),
    registration_table=[place(ro, rrz, x, y, 850) for x, y in ((0, 0), (1500, 0), (1500, 1000), (0, 1000))],
    collar_form=[L.FORM_XY[0] / 1e3, L.FORM_XY[1] / 1e3, (L.RB_TOP + 380) / 1e3],
    cell=L.CELL,
)
(OUT / "lab1_layout.json").write_text(json.dumps(info, indent=1))
(OUT / "lab1_boxes.json").write_text(json.dumps(boxes, indent=0))
print("parts", len(parts), "static boxes", len(boxes), "glb", (OUT / "lab1_cell.glb").stat().st_size)
