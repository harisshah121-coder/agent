"""Export static obstacle boxes (metres, axis-aligned) from the concept model for MuJoCo collision checks."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import cell_concept as cc
ROOT = Path(__file__).resolve().parents[2]
MOVING = re.compile(r"UR10e|Robotiq|GelSight|RealSense|7th-axis carriage|cutting gantry|cutting head|gantry side|EGC-80|Y carriage|Z axis|tool changer|needle bar|air knife|needle head|double-ply|floor|fabric|kit |cut |finished tee|rib strip|web")
boxes = []
for a in cc.build().children:
    for s in a.children:
        if MOVING.search(s.label): continue
        b = s.bounding_box()
        boxes.append({"name": s.label, "c": [(b.min.X + b.max.X) / 2000, (b.min.Y + b.max.Y) / 2000, (b.min.Z + b.max.Z) / 2000],
                      "h": [max(b.size.X, 2) / 2000, max(b.size.Y, 2) / 2000, max(b.size.Z, 2) / 2000]})
(ROOT / "sim/results/cell_boxes.json").write_text(json.dumps(boxes, indent=0))
print(len(boxes), "static boxes")
