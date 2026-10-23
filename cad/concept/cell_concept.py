"""Concept 3D model of the Roll-to-Garment development cell (assemblies A00-A10).

Level of detail: LOD0/LOD1 concept geometry sized from datasheet dimensions in
docs/BUILD_GUIDE_MACHINE.md; every part in docs/spine/parts.csv with qty > 0 is
placed and labelled with its part ID (checked by audit_model.py).
World frame: mm, origin at the front-left floor corner of the guarded envelope,
+X along material flow, +Y toward the back, +Z up.

Layout (revised after the 2026-10-23 model audit):
  front row  y 150-750  : overlock | collar module | coverstitch | inspection (x 5050-5950)
  track      y 800-1080 : 7th-axis track, UR10e base at y = 940
  back zone  y 1250-2900: cutter (cutting zone x 1200-3700, pick-off x 3700-4300),
                          staging x 4370-5290, flat hemmer x 5310-5910, tool stand
  gantry     columns at x 3760 / 5890, y 1140 / 2945, X beams at z 2300
Run:  /home/user/.venvs/cad/bin/python cad/concept/cell_concept.py
"""
from __future__ import annotations
import math
from pathlib import Path
from build123d import Box, Cylinder, Pos, Rot, Color, Compound, Polyline, make_face, extrude, export_gltf, export_step

OUT = Path(__file__).resolve().parents[1] / "out"
OUT.mkdir(exist_ok=True)

# Layout constants (mm) shared with sim/ and the viewer
TRACK_Y, TRACK_X0, TRACK_X1 = 940, 1700, 5300
UR_HOME_X, UR_BASE_Z = 3300, 820
GANTRY_X0, GANTRY_X1, GANTRY_Y0, GANTRY_Y1, GANTRY_H = 3760, 5890, 1140, 2945, 2300

C = {
    "alu": (0.78, 0.80, 0.82, 1), "steel": (0.35, 0.37, 0.40, 1), "dark": (0.15, 0.16, 0.18, 1),
    "guard": (0.85, 0.90, 0.95, 0.18), "yellow": (0.98, 0.78, 0.10, 1), "festo": (0.10, 0.45, 0.75, 1),
    "ur": (0.55, 0.75, 0.90, 1), "urgrey": (0.72, 0.74, 0.76, 1), "fabric": (0.95, 0.95, 0.92, 1),
    "rib": (0.85, 0.85, 0.80, 1), "felt": (0.25, 0.27, 0.30, 1), "juki": (0.92, 0.92, 0.90, 1),
    "table": (0.60, 0.48, 0.34, 1), "cab": (0.80, 0.82, 0.84, 1), "red": (0.85, 0.12, 0.10, 1),
    "green": (0.15, 0.70, 0.30, 1), "cam": (0.10, 0.10, 0.12, 1), "light": (0.95, 0.98, 1.0, 1),
    "belt": (0.10, 0.12, 0.14, 1), "orange": (0.95, 0.50, 0.10, 1), "floor": (0.22, 0.24, 0.25, 1),
}

def box(l, w, h, x, y, z, col, label):
    """Box with its min corner at (x, y, z)."""
    s = Pos(x + l / 2, y + w / 2, z + h / 2) * Box(l, w, h)
    s.color = Color(*C[col]); s.label = label
    return s

def cyl(r, h, x, y, z, col, label, axis="z"):
    s = Cylinder(r, h)
    if axis == "x": s = Rot(0, 90, 0) * s
    if axis == "y": s = Rot(90, 0, 0) * s
    s = Pos(x, y, z) * s
    s.color = Color(*C[col]); s.label = label
    return s

def plate(points, z, t, col, label):
    s = Pos(0, 0, z) * extrude(make_face(Polyline(*points, close=True)), t)
    s.color = Color(*C[col]); s.label = label
    return s

def asm(label, parts):
    return Compound(label=label, children=parts)

TEE = [(0, 0), (500, 0), (500, 480), (430, 560), (330, 600), (290, 520), (210, 520), (170, 600), (70, 560), (0, 480)]
SLEEVE = [(0, 0), (380, 0), (340, 220), (190, 260), (40, 220)]

# ---------------- A00 frame, guarding, utilities ----------------
def a00():
    p, L, W, H = [], 6000, 3000, 2000
    posts = [(x, y) for x in range(0, L + 1, 1500) for y in (0, W)] + [(0, 1500), (L, 1500)]
    for i, (x, y) in enumerate(posts):
        p.append(box(60, 60, H, x - 30, y - 30, 0, "yellow", f"A00 guard post {i} (P-ST00-001)" if i == 0 else f"A00 guard post {i}"))
    p.append(box(L - 60, 8, H - 200, 30, W - 4, 100, "guard", "A00 back guard panel"))
    p.append(box(8, W - 60, H - 200, -4, 30, 100, "guard", "A00 left guard panel"))
    p.append(box(8, W - 880, H - 200, L - 4, 850, 100, "guard", "A00 right guard panel (output opening y 0-850)"))
    p.append(box(1410, 8, H - 200, 1530, -4, 100, "guard", "A00 front guard panel 1"))
    p.append(box(1410, 8, H - 200, 3030, -4, 100, "guard", "A00 front guard panel 2"))
    p.append(box(1410, 8, H - 200, 4530, -4, 100, "guard", "A00 front interlocked door"))
    p.append(box(10000, 5000, 5, -1500, -1300, -5, "floor", "A00 floor"))
    p.append(box(700, 600, 800, -1300, 1500, 0, "festo", "A00 compressor + dryer + FRL (P-ST00-004)"))
    return asm("A00 Frame and guarding", p)

# ---------------- A01 roll handling ----------------
def a01():
    p = []
    for y in (1050, 2920):
        p.append(box(500, 60, 60, 150, y - 30, 0, "steel", "A01 stand foot"))
        p.append(box(60, 60, 900, 370, y - 30, 0, "steel", "A01 stand upright"))
    p.append(cyl(230, 1900, 400, 1985, 900, "fabric", "A01 fabric roll 1.8 m", axis="y"))
    p.append(cyl(40, 2000, 400, 1985, 900, "steel", "A01 roll shaft", axis="y"))
    p.append(box(120, 120, 140, 340, 2850, 1000, "orange", "A01 let-off servo + dancer (P-ST01-001)"))
    p.append(cyl(35, 1900, 760, 1985, 760, "alu", "A01 dancer roller", axis="y"))
    p.append(box(160, 200, 160, 860, 1000, 780, "festo", "A01 edge guide E+L (P-ST01-002)"))
    p.append(box(40, 1900, 40, 820, 1035, 980, "dark", "A01 static bar (P-ST01-003)"))
    p.append(box(700, 600, 300, 150, 150, 0, "orange", "A01 roll lifter (P-ST01-004)"))
    p.append(box(560, 1800, 2, 630, 1085, 900, "fabric", "A01 fabric web"))
    return asm("A01 Roll handling", p)

# ---------------- A02 cutter ----------------
CUT_X0, CUT_X1, CUT_Y0, CUT_Y1 = 1200, 3700, 1250, 2900
def a02():
    p = [box(CUT_X1 - CUT_X0, CUT_Y1 - CUT_Y0, 820, CUT_X0, CUT_Y0, 0, "steel", "A02 cutter base, cutting zone (P-ST02-001)"),
         box(CUT_X1 - CUT_X0, CUT_Y1 - CUT_Y0, 60, CUT_X0, CUT_Y0, 820, "felt", "A02 vacuum conveyor felt belt"),
         box(600, CUT_Y1 - CUT_Y0, 820, CUT_X1, CUT_Y0, 0, "steel", "A02 pick-off conveyor extension frame"),
         box(600, CUT_Y1 - CUT_Y0, 60, CUT_X1, CUT_Y0, 820, "felt", "A02 pick-off conveyor belt")]
    for x in (CUT_X0, CUT_X1 + 600):
        p.append(cyl(60, CUT_Y1 - CUT_Y0, x, (CUT_Y0 + CUT_Y1) / 2, 850, "dark", "A02 conveyor drum", axis="y"))
    gx = 2450
    for y in (CUT_Y0 - 60, CUT_Y1):
        p.append(box(160, 60, 300, gx - 80, y, 820, "dark", "A02 gantry side"))
    p.append(box(200, CUT_Y1 - CUT_Y0 + 120, 160, gx - 100, CUT_Y0 - 60, 1120, "light", "A02 cutting gantry beam"))
    p.append(box(220, 220, 320, gx - 110, 1900, 900, "dark", "A02 cutting head (DRT + EOT)"))
    p.append(box(900, 500, 900, 2000, 3060, 0, "steel", "A02 vacuum blower 5.5 kW, outside guard, ducted"))
    for y in (CUT_Y0 - 80, CUT_Y1 + 10):
        p.append(box(60, 60, 1300, 3500, y, 880, "alu", "A10 camera bridge post"))
    p.append(box(60, CUT_Y1 - CUT_Y0 + 150, 60, 3500, CUT_Y0 - 80, 2180, "alu", "A10 camera bridge"))
    p.append(box(90, 90, 140, 3485, 2030, 2040, "cam", "A10 24 MP bed camera (P-ST10-002)"))
    return asm("A02 Cutter", p)

# ---------------- A03 extraction and buffer (staging + kit) ----------------
def a03():
    p = [box(920, 1300, 820, 4370, 1400, 0, "steel", "A03 staging table frame"),
         box(920, 1300, 30, 4370, 1400, 820, "light", "A03 staging table top (backlit)")]
    z = 851
    p.append(plate([(4370 + x, 1430 + y) for x, y in TEE], z, 2, "fabric", "A03 kit front panel"))
    p.append(plate([(4370 + x, 2060 + y) for x, y in TEE], z, 2, "fabric", "A03 kit back panel"))
    p.append(box(500, 40, 2, 4370, 2670, z, "rib", "A03 kit neck rib strip"))
    for i, x0 in enumerate((1450, 2050, 2650)):
        p.append(plate([(x0 + x, 1350 + y) for x, y in TEE], 881, 2, "fabric", f"A02 cut front {i}"))
        p.append(plate([(x0 + x, 2000 + y) for x, y in TEE], 881, 2, "fabric", f"A02 cut back {i}"))
    p.append(plate([(3760 + x, 1400 + y) for x, y in SLEEVE], 881, 2, "fabric", "A02 cut sleeve L"))
    p.append(plate([(3760 + x, 1800 + y) for x, y in SLEEVE], 881, 2, "fabric", "A02 cut sleeve R"))
    p.append(box(70, 70, 40, 4390, 1310, 1900, "cam", "A03 staging camera (P-ST10-004)"))
    p.append(box(60, 60, 600, 4320, 1290, 1340, "alu", "A03 staging camera post"))
    return asm("A03 Extraction and buffer", p)

# ---------------- A04 manipulation ----------------
def ur10e_simplified(x, y, z):
    """Static simplified UR10e for the STEP export; the viewer shows the real MuJoCo Menagerie meshes."""
    p = [box(260, 260, z - 280, x - 130, y - 130, 280, "steel", "A04 UR10e pedestal"),
         cyl(95, 120, x, y, z + 60, "urgrey", "A04 UR10e base (P-ST04-002)"),
         cyl(75, 180, x, y, z + 181, "ur", "A04 UR10e shoulder"),
         box(613, 120, 120, x - 613, y - 60, z + 181 - 60, "urgrey", "A04 UR10e upper arm"),
         box(110, 100, 572, x - 668, y - 50, z + 181 - 572, "urgrey", "A04 UR10e forearm")]
    tx, tz = x - 613, z + 181 - 572
    p += [box(90, 90, 120, tx - 45, y - 45, tz - 120, "urgrey", "A04 UR10e wrist"),
          box(120, 80, 140, tx - 60, y - 40, tz - 260, "dark", "A04 Robotiq 2F-85 gripper (P-ST04-004)"),
          box(30, 20, 30, tx - 15, y + 40, tz - 290, "orange", "A04 GelSight Mini fingertip (P-ST04-005)"),
          box(42, 42, 23, tx + 50, y - 21, tz - 150, "cam", "A04 RealSense D405 wrist camera (P-ST04-006)")]
    return p

def a04():
    p = []
    for x in (GANTRY_X0, GANTRY_X1):
        for y in (GANTRY_Y0, GANTRY_Y1):
            p.append(box(80, 80, GANTRY_H, x - 40, y - 40, 0, "alu", "A04 gantry column"))
    for y in (GANTRY_Y0, GANTRY_Y1):
        p.append(box(GANTRY_X1 - GANTRY_X0 + 120, 120, 150, GANTRY_X0 - 60, y - 60, GANTRY_H, "festo", "A04 Festo EGC-120 X axis (P-ST04-001)"))
    gx = 4800
    p.append(box(110, GANTRY_Y1 - GANTRY_Y0 + 120, 120, gx - 55, GANTRY_Y0 - 60, GANTRY_H + 150, "festo", "A04 Festo EGC-80 Y axis 1500 stroke"))
    p.append(box(160, 160, 160, gx - 80, 2000, GANTRY_H + 50, "dark", "A04 Y carriage + valve terminal (P-ST09-014)"))
    p.append(box(80, 80, 900, gx - 40, 2040, GANTRY_H - 700, "festo", "A04 Z axis"))
    p.append(box(60, 30, 30, gx + 40, 2065, GANTRY_H - 650, "cam", "A03 double-ply sensor UDC-18GS (P-ST03-003)"))
    p.append(box(160, 160, 60, gx - 80, 2000, GANTRY_H - 760, "dark", "A04 ATI QC-11 tool changer (P-ST04-003)"))
    p.append(box(600, 90, 70, gx - 300, 2035, GANTRY_H - 830, "alu", "A03 T1 needle bar"))
    p.append(box(600, 30, 40, gx - 300, 2005, GANTRY_H - 820, "festo", "A03 EXAIR air knife nose (P-ST03-002)"))
    for i in range(6):
        p.append(cyl(18, 60, gx - 250 + i * 100, 2080, GANTRY_H - 860, "dark", "A03 Schmalz SNG-M needle head (P-ST03-001)"))
    # tool stand with parked T4 vacuum pad
    p.append(box(500, 300, 800, 5350, 2560, 0, "steel", "A04 tool stand"))
    p.append(cyl(75, 60, 5480, 2710, 830, "dark", "A03 T4 Piab KCS 150 vacuum pad, parked (P-ST03-004)"))
    p.append(box(60, 40, 50, 5455, 2690, 860, "festo", "A03 Festo OVEM ejector (P-ST03-005)"))
    # 7th-axis track and UR10e
    p.append(box(TRACK_X1 - TRACK_X0, 280, 180, TRACK_X0, TRACK_Y - 140, 0, "steel", "A04 7th-axis track base (P-ST04-007)"))
    p.append(box(TRACK_X1 - TRACK_X0, 40, 40, TRACK_X0, TRACK_Y - 110, 180, "alu", "A04 7th-axis rail 1"))
    p.append(box(TRACK_X1 - TRACK_X0, 40, 40, TRACK_X0, TRACK_Y + 70, 180, "alu", "A04 7th-axis rail 2"))
    p.append(box(420, 260, 60, UR_HOME_X - 210, TRACK_Y - 130, 220, "festo", "A04 7th-axis carriage"))
    p += ur10e_simplified(UR_HOME_X, TRACK_Y, UR_BASE_Z)
    return asm("A04 Manipulation", p)

# ---------------- A05 sewing heads, A06 collar ----------------
def station(x, y, label, pid, cyl_arm=False, rot=False):
    """Sewing table 1100 x 600 (rot=True: 600 x 1100 along Y) with head, box, camera, thread stand and sensor."""
    L, W = (600, 1100) if rot else (1100, 600)
    p = [box(L, W, 30, x, y, 760, "table", f"{label} table")]
    for dx in (40, L - 80):
        for dy in (40, W - 80):
            p.append(box(40, 40, 760, x + dx, y + dy, 0, "steel", f"{label} table leg"))
    hx, hy = (x + 180, y + 380) if rot else (x + 380, y + 180)
    hl, hw = (240, 380) if rot else (380, 240)
    if cyl_arm:
        p.append(box(hl if not rot else 160, hw if rot else 160, 260, hx, hy + (0 if rot else 40), 790, "juki", f"{label} cylinder arm ({pid})"))
        p.append(box(160, 220, 420, hx + (0 if rot else 300), hy + (300 if rot else 10), 790, "juki", f"{label} head body"))
    else:
        p.append(box(hl, hw, 300, hx, hy, 790, "juki", f"{label} head ({pid})"))
        p.append(box(140 if not rot else hl, hw if not rot else 140, 120, hx + (240 if not rot else 0), hy + (0 if not rot else 240), 1090, "juki", f"{label} head top"))
    bx, by = (x + 200, y + 800) if rot else (x + 800, y + 260)
    p.append(box(200 if not rot else 300, 300 if not rot else 200, 180, bx, by, 520, "dark", f"{label} control box (P-ST05-002)"))
    p.append(box(60, 60, 60, hx + 120, hy - 90 if not rot else hy + 120, 1250, "cam", f"{label} needle camera (P-ST10-003)"))
    p.append(cyl(25, 300, x + 100, y + W - 100, 790, "steel", f"{label} thread stand"))
    p.append(box(50, 30, 40, x + 75, y + W - 160, 1090, "orange", f"{label} Eltex thread sensor (P-ST05-004)"))
    return p

def a05():
    p = station(1500, 150, "A05 overlock JUKI MO-6814S", "P-ST05-001")
    p += station(3900, 150, "A05 coverstitch JUKI MF-7923", "P-ST05-003", cyl_arm=True)
    p += station(5310, 1400, "A05 flat hemmer Jack W4-UT", "P-ST05-006", rot=True)
    return asm("A05 Sewing heads", p)

def a06():
    p = station(2700, 150, "A06 collar overlock", "P-ST06-001", cyl_arm=True)
    p.append(cyl(45, 260, 3200, 470, 1150, "orange", "A06 expansion roller 1 (P-ST06-002)", axis="y"))
    p.append(cyl(45, 260, 3200, 470, 1380, "orange", "A06 expansion roller 2"))
    p.append(box(260, 200, 300, 2750, 480, 790, "festo", "A06 rib meter/cut unit"))
    p.append(box(70, 70, 40, 3300, 700, 1700, "cam", "A06 collar camera (P-ST10-004)"))
    p.append(box(40, 40, 900, 3315, 710, 800, "alu", "A06 collar camera post"))
    return asm("A06 Collar module", p)

# ---------------- A07 finishing and output ----------------
def a07():
    p = [box(900, 700, 800, 5050, 100, 0, "steel", "A07 inspection table frame"),
         box(900, 700, 40, 5050, 100, 800, "light", "A07 backlight tiles (P-ST07-002)"),
         plate([(5250 + x, 150 + y) for x, y in TEE], 841, 3, "fabric", "A07 finished tee on inspection")]
    for y in (55, 805):
        p.append(box(40, 40, 1200, 5480, y, 840, "alu", "A07 camera post"))
    p.append(box(40, 790, 40, 5480, 55, 2040, "alu", "A07 camera beam"))
    p.append(box(100, 100, 150, 5450, 400, 1890, "cam", "A07 16 MP camera (P-ST07-001)"))
    p.append(box(2000, 500, 80, 5960, 200, 760, "belt", "A07 discharge belt mk GUF-P (P-ST07-003)"))
    p.append(box(2000, 500, 760, 5960, 200, 0, "steel", "A07 belt stand"))
    p.append(box(300, 60, 300, 6600, 140, 840, "red", "A07 reject flipper gate"))
    return asm("A07 Finishing and output", p)

# ---------------- A09 control and safety ----------------
def a09():
    p = [box(800, 500, 2000, -1300, 200, 0, "cab", "A09 control enclosure Rittal AX (P-ST09-007) housing C6030 (P-ST09-001), EtherCAT I/O (P-ST09-002), TwinSAFE (P-ST09-003), 24 V + UPS (P-ST09-005), switchgear (P-ST09-006)"),
         box(800, 500, 2000, -1300, 800, 0, "cab", "A09 drive enclosure Rittal AX housing economy servo drives (P-ST09-004)"),
         box(60, 60, 1500, 4400, -300, 0, "steel", "A09 HMI post"),
         box(340, 60, 260, 4260, -330, 1300, "dark", "A09 HMI CP2912 (P-ST09-008)"),
         box(80, 60, 200, 4500, -400, 900, "yellow", "A09 enabling switch PITenable on hook (P-ST09-013)"),
         cyl(35, 300, 5990, -60, 2150, "green", "A09 tower light (P-ST09-009)")]
    for x in (100, 1600, 3200, 5300):
        p.append(box(80, 80, 120, x, -100, 1100, "red", "A09 e-stop (P-ST09-010)"))
    for x in (4545, 5925):
        p.append(box(40, 50, 120, x, -60, 1000, "yellow", "A09 guard-locking interlock AZM300 (P-ST09-011)"))
    for x in (30, 1410):
        p.append(box(50, 50, 1500, x, -110, 100, "yellow", "A09 light curtain roll-load (P-ST09-012)"))
    for y in (120, 760):
        p.append(box(50, 50, 1500, 6040, y, 100, "yellow", "A09 light curtain output (P-ST09-012)"))
    return asm("A09 Control and safety", p)

# ---------------- A10 vision and compute ----------------
def a10():
    return asm("A10 Vision and compute", [
        box(450, 300, 150, -1250, 300, 2000, "dark", "A10 vision IPC Neousys + RTX 4000 SFF (P-ST10-001)"),
        box(250, 250, 90, -1250, 900, 2000, "dark", "A10 Jetson AGX Thor dev kit (P-ST10-005)")])

def build():
    return Compound(label="Roll-to-Garment development cell (concept)",
                    children=[a00(), a01(), a02(), a03(), a04(), a05(), a06(), a07(), a09(), a10()])

if __name__ == "__main__":
    cell = build()
    export_gltf(cell, str(OUT / "cell_concept.glb"), binary=True, linear_deflection=1.0, angular_deflection=0.3)
    export_step(cell, str(OUT / "cell_concept.step"))
    bb = cell.bounding_box()
    print("bbox mm", round(bb.size.X), round(bb.size.Y), round(bb.size.Z))
