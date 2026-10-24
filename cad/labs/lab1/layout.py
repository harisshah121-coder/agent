"""Stage 2 cell layout built only from the Lab Build Packages (A. Sherazee, 2026-10-21) and the
Lab 1 structural package Rev B.2 (2026-10-23).

What comes from where:
- Lab 1 parts: his STEP files, unchanged (input/*.step, reference geometry per his README).
- Scope: Lab 1 Stage 1 (items 1-5, 8, 9 and a two-sided bench fence). Station order follows his cell figure
  (page 3): registration table -> collar station -> folding table -> release and turn; two cobots on pedestals.
- Bought items and Lab 2-4 items: envelopes sized from the numbers in his guide where it gives them;
  where it does not, the size is marked EST in the label.
- Floor positions: NOT in his package (the integrator keeps the master layout). The positions below are
  provisional, chosen to follow his route and checked for cobot reach by sim/labs/lab1_cobots.py.
Units: mm, floor frame. X along the route (0 at the left fence), Y depth (0 front, 4000 back), Z up.
"""

CELL = dict(L=6000, W=4000, fence_h=2000, stage="Stage 1 bench area")

# Lab 1 Stage 1 deliverables (his page 12 "Stage split": items 1-5, 8, 9 and a two-sided fence for the bench area).
# file, instance label, origin (x, y, z) in the floor frame, rotation about Z (deg)
PARTS = [
    ("RT-100_registration_table.step", "L1 RT-100 registration table (Rig A)", (950, 1900, 0), 0),
    ("FT-200_folding_table.step",      "L1 FT-200 folding table (Rigs C and D)", (4400, 1000, 0), 90),   # hinge along Y at x = 4400
    ("CP-300_cobot_pedestal.step",     "L1 CP-300 cobot pedestal A",   (1900, 1150, 0), 0),
    ("CP-300_cobot_pedestal.step",     "L1 CP-300 cobot pedestal B",   (3000, 1150, 0), 0),
    ("SP-400_sewing_plinth.step",      "L1 SP-400 plinth, collar overlocker (Rig B)", (2350, 50, 0), 0),
    ("SP-400_sewing_plinth.step",      "L1 SP-400 plinth, flat-bed overlock (side seam head, position open OI-3)", (5300, 1350, 0), 0),
    ("SP-400_sewing_plinth.step",      "L1 SP-400 plinth, flat-bed coverstitch (hems)", (1000, 3150, 0), 0),
    ("RB-500_rotary_base.step",        "L1 RB-500 rotary station base (Rig B)", (2400, 600, 0), 0),
    ("OC-600_output_chute.step",       "L1 OC-600 output chute (Rig D)", (3250, 2700, 0), 0),
]

# Folding table: moving-leaf parts (his check.py motion-sweep group) and the hinge axis in FT-200 local frame.
FT_MOVING = ("FT-202", "FT-205B", "FT-210", "FT-204", "FT-207", "FT-214", "FT-216")
FT_MOVING_SHEET_Y_BELOW = 0            # the second FT-206 sheet (y < 0) is the moving leaf's skin
FT_HINGE_LOCAL = dict(y=0.0, z=851.5)  # FT['top_height'] + FT['hinge_offset'] (params.py)

RB_TOP = 600                            # RB['plate_height']
FORM_XY = (2700, 900)                   # turntable centre = RB-500 plate centre
# Envelopes for items his guide describes but Lab 1 does not draw: (label, kind, centre/base, size, rgba)
ENVELOPES = [
    ("BUY hollow rotary stage, frame 200, on adapter RB-505 (OI-2; height EST)", "box", (FORM_XY[0], FORM_XY[1], RB_TOP), (200, 200, 90), (0.25, 0.3, 0.38, 1.0)),
    ("L4 body cradle cone (size EST)", "cone", (FORM_XY[0], FORM_XY[1], RB_TOP + 90), (400, 180, 230), (0.82, 0.82, 0.8, 1.0)),
    ("L4 collapsing neckline form, 8 segments, 150-180 mm expanded", "cyl", (FORM_XY[0], FORM_XY[1], RB_TOP + 320), (170, 60), (0.15, 0.45, 0.75, 1.0)),
    ("BUY cylinder-bed overlocker on the Lab 2 collar fixture (size EST)", "box", (2700, 330, 700), (520, 260, 430), (0.86, 0.86, 0.83, 1.0)),
    ("BUY flat-bed 4-thread overlock on a Lab 2 flat seam fixture (size EST)", "box", (5650, 1600, 700), (500, 300, 420), (0.86, 0.86, 0.83, 1.0)),
    ("BUY flat-bed coverstitch with hem folder on the Lab 2 hem fixture (size EST)", "box", (1350, 3400, 700), (500, 300, 420), (0.86, 0.86, 0.83, 1.0)),
    ("L2 rib loop fixture with 100 mm peg (location EST)", "box", (3350, 850, 0), (300, 300, 950), (0.55, 0.6, 0.65, 1.0)),
    ("L4 turning tube, 120 mm bore x 700 mm, suction at far end", "cyly", (3250, 2300, 950), (130, 700), (0.75, 0.78, 0.8, 1.0)),
    ("L3 tool park stand (size EST)", "box", (1150, 900, 0), (300, 250, 900), (0.55, 0.6, 0.65, 1.0)),
]

# Stage 1: two-sided fence for the bench area (left and back); Stage 2 adds the full guarding.
FENCE = dict(sides=("left", "back"), door_back=(4300, 5200))

# Cobots (buy list: UR5e class, 5 kg, ~900 mm reach) on the CP-300 pedestals, base on the 700 mm top plate.
COBOTS = {"A": dict(pedestal="L1 CP-300 cobot pedestal A"), "B": dict(pedestal="L1 CP-300 cobot pedestal B")}
