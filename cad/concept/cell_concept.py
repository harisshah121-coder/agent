"""Concept 3D model of the Roll-to-Garment development cell (assemblies A00-A10).

Level of detail: LOD0/LOD1 concept geometry sized from datasheet dimensions in
docs/BUILD_GUIDE_MACHINE.md. World frame: mm, origin at front-left floor corner of
the guarded envelope, +X along material flow, +Y toward the back, +Z up.
Run:  /home/user/.venvs/cad/bin/python cad/concept/cell_concept.py
"""
from __future__ import annotations
import json, math
from pathlib import Path
from build123d import (Box, Cylinder, Pos, Rot, Color, Compound, Polyline, make_face,
                       extrude, export_gltf, export_step, Location)

OUT = Path(__file__).resolve().parents[1] / "out"
OUT.mkdir(exist_ok=True)

C = {  # colours (r, g, b, a)
    "alu": (0.78, 0.80, 0.82, 1), "steel": (0.35, 0.37, 0.40, 1), "dark": (0.15, 0.16, 0.18, 1),
    "guard": (0.85, 0.90, 0.95, 0.18), "yellow": (0.98, 0.78, 0.10, 1), "festo": (0.10, 0.45, 0.75, 1),
    "ur": (0.55, 0.75, 0.90, 1), "urgrey": (0.72, 0.74, 0.76, 1), "fabric": (0.95, 0.95, 0.92, 1),
    "rib": (0.85, 0.85, 0.80, 1), "felt": (0.25, 0.27, 0.30, 1), "juki": (0.92, 0.92, 0.90, 1),
    "table": (0.60, 0.48, 0.34, 1), "cab": (0.80, 0.82, 0.84, 1), "red": (0.85, 0.12, 0.10, 1),
    "green": (0.15, 0.70, 0.30, 1), "cam": (0.10, 0.10, 0.12, 1), "light": (0.95, 0.98, 1.0, 1),
    "belt": (0.10, 0.12, 0.14, 1), "orange": (0.95, 0.50, 0.10, 1),
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
    f = make_face(Polyline(*points, close=True))
    s = Pos(0, 0, z) * extrude(f, t)
    s.color = Color(*C[col]); s.label = label
    return s

def asm(label, parts):
    return Compound(label=label, children=parts)

# ---------------- A00 frame and guarding (6 m x 3 m) ----------------
def a00():
    p = []
    L, W, H = 6000, 3000, 2000
    posts = [(x, y) for x in range(0, L + 1, 1500) for y in (0, W)] + [(0, 1500), (L, 1500)]
    for i, (x, y) in enumerate(posts):
        p.append(box(60, 60, H, x - 30, y - 30, 0, "yellow", f"A00 guard post {i}"))
    # panels: back, sides, front (front has operator openings)
    p.append(box(L, 8, H - 200, 0, W - 4, 100, "guard", "A00 back guard panel"))
    p.append(box(8, W, H - 200, -4, 0, 100, "guard", "A00 left guard panel"))
    p.append(box(8, W - 700, H - 200, L - 4, 700, 100, "guard", "A00 right guard panel (output opening below)"))
    p.append(box(1400, 8, H - 200, 1500, -4, 100, "guard", "A00 front guard panel 1"))
    p.append(box(1500, 8, H - 200, 3000, -4, 100, "guard", "A00 front guard panel 2"))
    p.append(box(500, 8, H - 200, 4500, -4, 100, "guard", "A00 front interlocked door"))
    p.append(box(L + 1000, W + 1600, 5, -500, -1200, -5, "dark", "A00 floor"))
    return asm("A00 Frame and guarding", p)

# ---------------- A01 roll handling ----------------
def a01():
    p = []
    for y in (1050, 2950):
        p.append(plate([(150, y, ), (650, y), (450, y), (400, y)], 0, 1, "steel", "x") if False else
                 box(500, 60, 60, 150, y - 30, 0, "steel", "A01 stand foot"))
        p.append(box(60, 60, 900, 370, y - 30, 0, "steel", "A01 stand upright"))
    p.append(cyl(230, 1900, 400, 2000, 900, "fabric", "A01 fabric roll 1.8 m (P-ST01-001)", axis="y"))
    p.append(cyl(40, 2100, 400, 2000, 900, "steel", "A01 roll shaft", axis="y"))
    p.append(box(120, 120, 140, 410, 2960, 840, "orange", "A01 let-off servo"))
    p.append(cyl(35, 1900, 700, 2000, 760, "alu", "A01 dancer roller", axis="y"))
    p.append(box(160, 200, 160, 820, 1000, 780, "festo", "A01 edge guide E+L (P-ST01-002)"))
    p.append(box(40, 1900, 40, 760, 1050, 920, "dark", "A01 static bar (P-ST01-003)"))
    p.append(box(700, 600, 300, 150, 150, 0, "orange", "A01 roll lifter (P-ST01-004)"))
    # web from roll to cutter infeed
    p.append(box(560, 1800, 2, 620, 1100, 900, "fabric", "A01 fabric web"))
    return asm("A01 Roll handling", p)

# ---------------- A02 cutter (iECHO TK4S-2516 class) ----------------
def a02():
    p = []
    x0, y0 = 1200, 1250  # base footprint 2800 x 1700
    p.append(box(2800, 1700, 820, x0, y0, 0, "steel", "A02 cutter base (P-ST02-001)"))
    p.append(box(2800, 1700, 60, x0, y0, 820, "felt", "A02 vacuum conveyor felt belt"))
    for x in (x0, x0 + 2800):
        p.append(cyl(60, 1700, x, y0 + 850, 850, "dark", "A02 conveyor drum", axis="y"))
    gx = x0 + 1400
    for y in (y0 - 60, y0 + 1700):
        p.append(box(160, 60, 300, gx - 80, y, 820, "dark", "A02 gantry side"))
    p.append(box(200, 1820, 160, gx - 100, y0 - 60, 1120, "light", "A02 cutting gantry beam"))
    p.append(box(220, 220, 320, gx - 110, y0 + 600, 900, "dark", "A02 cutting head (DRT + EOT)"))
    p.append(box(900, 500, 900, x0 + 1900, y0 - 560, 0, "steel", "A02 vacuum blower 5.5 kW"))
    # over-bed camera bridge (ST10)
    for y in (y0 - 80, y0 + 1720):
        p.append(box(60, 60, 1300, x0 + 2300, y, 880, "alu", "A10 camera bridge post"))
    p.append(box(60, 1860, 60, x0 + 2300, y0 - 80, 2180, "alu", "A10 camera bridge"))
    p.append(box(90, 90, 140, x0 + 2285, y0 + 805, 2040, "cam", "A10 24 MP bed camera (P-ST10-002)"))
    return asm("A02 Cutter", p)

TEE_FRONT = [(0, 0), (500, 0), (500, 480), (430, 560), (330, 600), (290, 520), (210, 520), (170, 600), (70, 560), (0, 480)]
SLEEVE = [(0, 0), (380, 0), (340, 220), (190, 260), (40, 220)]

def pieces_on_bed(x, y, z, label):
    out = []
    out.append(plate([(x + px, y + py) for px, py in TEE_FRONT], z, 2, "fabric", f"{label} front panel"))
    out.append(plate([(x + 560 + px, y + py) for px, py in TEE_FRONT], z, 2, "fabric", f"{label} back panel"))
    out.append(plate([(x + 1120 + px, y + py) for px, py in SLEEVE], z, 2, "fabric", f"{label} sleeve L"))
    out.append(plate([(x + 1120 + px, y + 320 + py) for px, py in SLEEVE], z, 2, "fabric", f"{label} sleeve R"))
    out.append(box(500, 40, 2, x, y + 650, z, "rib", f"{label} neck rib strip"))
    return out

# ---------------- A03 extraction and buffer ----------------
def a03():
    p = []
    p.append(box(1700, 1300, 820, 4150, 1450, 0, "steel", "A03 staging table frame"))
    p.append(box(1700, 1300, 30, 4150, 1450, 820, "light", "A03 staging table top (backlit)"))
    p += pieces_on_bed(4200, 1650, 851, "A03 kit")
    p += pieces_on_bed(1500, 1450, 881, "A02 cut")
    return asm("A03 Extraction and buffer", p)

# ---------------- A04 manipulation: Festo gantry + UR10e ----------------
UR = dict(d1=181, a2=613, a3=572, d4=174, d5=120, d6=117)

def ur10e(x, y, z, q=(0, -60, 100, -130, -90, 0)):
    """Simplified UR10e chain (forward kinematics for link placement)."""
    p = [box(260, 260, 600, x - 130, y - 130, z - 600, "steel", "A04 UR10e pedestal"),
         cyl(95, 120, x, y, z + 60, "urgrey", "A04 UR10e base (P-ST04-002)")]
    t1, t2, t3, t4 = [math.radians(a) for a in q[:4]]
    sh = (x, y, z + UR["d1"])
    p.append(cyl(75, 180, sh[0], sh[1], sh[2], "ur", "A04 UR10e shoulder"))
    def pt(base, length, ang):
        return (base[0] + length * math.cos(ang) * math.cos(t1), base[1] + length * math.cos(ang) * math.sin(t1), base[2] + length * math.sin(ang))
    el = pt(sh, UR["a2"], -t2 if False else math.radians(-q[1]))
    wr = pt(el, UR["a3"], math.radians(-q[1] - q[2]))
    for a, b, r, lab in ((sh, el, 60, "upper arm"), (el, wr, 48, "forearm")):
        dx, dy, dz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
        L = math.sqrt(dx * dx + dy * dy + dz * dz)
        s = Cylinder(r, L)
        pitch = math.degrees(math.acos(dz / L))
        yaw = math.degrees(math.atan2(dy, dx))
        s = Pos((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (a[2] + b[2]) / 2) * Rot(0, 0, yaw) * Rot(0, pitch, 0) * s
        s.color = Color(*C["urgrey"]); s.label = f"A04 UR10e {lab}"
        p.append(s)
        p.append(cyl(r + 12, 140, b[0], b[1], b[2], "ur", f"A04 UR10e joint after {lab}"))
    p.append(box(90, 90, 230, wr[0] - 45, wr[1] - 45, wr[2] - 230, "urgrey", "A04 UR10e wrist"))
    p.append(box(120, 80, 140, wr[0] - 60, wr[1] - 40, wr[2] - 370, "dark", "A04 Robotiq 2F-85 gripper (P-ST04-004)"))
    return p

def a04():
    p = []
    x0, x1, y0, y1, h = 2900, 5900, 1350, 2950, 2300
    for x in (x0, x1):
        for y in (y0, y1):
            p.append(box(120, 120, h, x - 60, y - 60, 0, "alu", "A04 gantry column"))
    for y in (y0, y1):
        p.append(box(x1 - x0 + 120, 120, 150, x0 - 60, y - 60, h, "festo", "A04 Festo EGC-120 X axis 3000 (P-ST04-001)"))
    gx = 4600
    p.append(box(110, y1 - y0 + 120, 120, gx - 55, y0 - 60, h + 150, "festo", "A04 Festo EGC-80 Y axis"))
    p.append(box(160, 160, 160, gx - 80, 2250, h + 50, "dark", "A04 Y carriage + valve terminal (P-ST09-014)"))
    p.append(box(80, 80, 900, gx - 40, 2290, h - 700, "festo", "A04 Z axis"))
    p.append(box(160, 160, 60, gx - 80, 2250, h - 760, "dark", "A04 ATI QC-11 tool changer (P-ST04-003)"))
    p.append(box(600, 90, 70, gx - 300, 2285, h - 830, "alu", "A03 T1 needle bar (P-ST03-001)"))
    for i in range(6):
        p.append(cyl(18, 60, gx - 250 + i * 100, 2330, h - 880, "dark", "A03 Schmalz SNG-M needle head"))
    p.append(box(300, 300, 900, 5950 - 2000, 1450 + 1350, 0, "steel", "A04 tool stand"))
    p += ur10e(3300, 900, 820)
    return asm("A04 Manipulation", p)

# ---------------- A05 sewing heads, A06 collar ----------------
def sewing_station(x, y, label, head_col="juki", cyl_arm=False):
    p = [box(1100, 600, 30, x, y, 760, "table", f"{label} table")]
    for dx in (40, 1020):
        for dy in (40, 520):
            p.append(box(40, 40, 760, x + dx, y + dy, 0, "steel", f"{label} table leg"))
    hx = x + 380
    if cyl_arm:
        p.append(box(420, 160, 260, hx, y + 220, 790, head_col, f"{label} cylinder arm"))
        p.append(box(160, 220, 420, hx + 300, y + 190, 790, head_col, f"{label} head body"))
    else:
        p.append(box(380, 240, 300, hx, y + 180, 790, head_col, f"{label} head"))
        p.append(box(140, 240, 120, hx + 240, y + 180, 1090, head_col, f"{label} head top"))
    p.append(box(200, 300, 180, x + 800, y + 260, 520, "dark", f"{label} control box (P-ST05-002)"))
    p.append(box(60, 60, 60, hx + 120, y + 90, 1250, "cam", f"{label} needle camera (P-ST10-003)"))
    p.append(cyl(25, 300, x + 100, y + 500, 790, "steel", f"{label} thread stand"))
    return p

def a05():
    p = sewing_station(1500, 250, "A05 overlock JUKI MO-6814S (P-ST05-001)")
    p += sewing_station(3800, 250, "A05 coverstitch JUKI MF-7923 (P-ST05-003)", cyl_arm=True)
    return asm("A05 Sewing heads", p)

def a06():
    p = sewing_station(2650, 250, "A06 collar overlock (P-ST06-001)", cyl_arm=True)
    p.append(cyl(45, 260, 3150, 520, 1150, "orange", "A06 expansion roller 1 (P-ST06-002)", axis="y"))
    p.append(cyl(45, 260, 3150, 520, 1380, "orange", "A06 expansion roller 2"))
    p.append(box(260, 200, 300, 2700, 600, 790, "festo", "A06 rib meter/cut unit"))
    return asm("A06 Collar module", p)

# ---------------- A07 finishing and output ----------------
def a07():
    p = [box(1000, 900, 800, 4950, 150, 0, "steel", "A07 inspection table frame"),
         box(1000, 900, 40, 4950, 150, 800, "light", "A07 backlight tiles (P-ST07-002)")]
    p += [plate([(5150 + px, 300 + py) for px, py in TEE_FRONT], 841, 3, "fabric", "A07 finished tee on inspection")]
    for y in (130, 1030):
        p.append(box(40, 40, 1200, 5430, y, 840, "alu", "A07 camera post"))
    p.append(box(40, 940, 40, 5430, 130, 2040, "alu", "A07 camera beam"))
    p.append(box(100, 100, 150, 5400, 550, 1890, "cam", "A07 16 MP camera (P-ST07-001)"))
    p.append(box(2000, 500, 80, 5950, 250, 760, "belt", "A07 discharge belt mk GUF-P (P-ST07-003)"))
    p.append(box(2000, 500, 760, 5950, 250, 0, "steel", "A07 belt stand"))
    return asm("A07 Finishing and output", p)

# ---------------- A09 control and safety, A10 vision/compute ----------------
def a09():
    p = [box(800, 500, 2000, -1300, 200, 0, "cab", "A09 control enclosure Rittal AX (P-ST09-007)"),
         box(800, 500, 2000, -1300, 800, 0, "cab", "A09 drive enclosure Rittal AX (P-ST09-007)"),
         box(60, 60, 1500, 4400, -300, 0, "steel", "A09 HMI post"),
         box(340, 60, 260, 4260, -330, 1300, "dark", "A09 HMI CP2912 (P-ST09-008)"),
         cyl(35, 300, 5990, 0, 2150, "green", "A09 tower light (P-ST09-009)")]
    for x, y in ((100, 0), (1600, 0), (3200, 0), (5300, 0)):
        p.append(box(80, 80, 120, x, y - 90, 1100, "red", "A09 e-stop (P-ST09-010)"))
    for y in (650, 0):
        pass
    # light curtains: roll-load opening (left front) and output opening (right)
    for x in (0, 1450):
        p.append(box(50, 50, 1500, x, -60, 100, "yellow", "A09 light curtain roll-load (P-ST09-012)"))
    for y in (180, 720):
        p.append(box(50, 50, 1500, 5980, y, 100, "yellow", "A09 light curtain output (P-ST09-012)"))
    return asm("A09 Control and safety", p)

def a10():
    return asm("A10 Vision and compute", [box(450, 300, 150, -1250, 300, 2000, "dark", "A10 vision IPC Neousys (P-ST10-001)")])

def build():
    return Compound(label="Roll-to-Garment development cell (concept)",
                    children=[a00(), a01(), a02(), a03(), a04(), a05(), a06(), a07(), a09(), a10()])

if __name__ == "__main__":
    cell = build()
    export_gltf(cell, str(OUT / "cell_concept.glb"), binary=True, linear_deflection=1.0, angular_deflection=0.3)
    export_step(cell, str(OUT / "cell_concept.step"))
    bb = cell.bounding_box()
    print("bbox mm", round(bb.size.X), round(bb.size.Y), round(bb.size.Z))
