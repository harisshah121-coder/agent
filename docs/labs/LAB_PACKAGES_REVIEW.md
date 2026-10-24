# Review: Lab Build Packages and Lab 1 structural package (2026-10-24)

Source documents (owner's uploads, not committed; marked confidential by the author):
- *Roll-to-Garment Prototype: Lab Build Packages*, A. Sherazee, 2026-10-21 (30 pages).
- *RTG-L1 Lab 1 Structural Package Rev B.2 PRELIMINARY*, 2026-10-23 (A3 drawings, BOQ, open issues), with the CAD zip (STEP, DXF, generator source, check report).

Decision D-019: his four-lab plan is the project's build baseline. The earlier concept model (`cad/concept/`) stays as a reference only.

## 1. What his plan is
- **Stage 1 ($250k, months 1–9):** four bench rigs that prove the transitions no bought machine performs, on a frozen 240–300 gsm jersey lot:
  - Rig A: single-ply pickup.
  - Rig B: collar on a collapsing form.
  - Rig C: fold and side seam.
  - Rig D: release and turn.
- **Stage 2 (months 9–15, seed-funded):** the integrated 6 x 4 m cell with two cobots on pedestals.
- **Construction route:** everything is sewn flat; the side-and-underarm seam is the only closing seam, and the shirt is turned at the end. Hems are open-flat, not tubular (OI-7 sign-off).
- **Four labs:**
  - Lab 1: structure, external shop.
  - Lab 2: sewing fixtures, external shop.
  - Lab 3: grippers, in-house first.
  - Lab 4: collar form and supports, in-house first.
  - The integrator keeps the master CAD, the interface control document, the controls, the policy and the garment record.

## 2. How it maps to our framework
| His item | Our identifiers | Note |
|---|---|---|
| Registration table RT-100 (vacuum, 4 zones) | ST03 buffer / staging, M11 vision | Replaces our gantry staging table |
| Rig A needle / hybrid head (Lab 3) | ST03 extraction, P-ST03-001 class (Schmalz SNG) | Same gripper family; on a cobot, not a gantry |
| Rig B collar station: RB-500 + rotary stage + collapsing form (Lab 4) + cylinder-bed overlocker (Lab 2) | ST06 collar module | Different mechanism from our roller module; matches real cylinder-bed practice |
| Folding table FT-200 (Rig C) | ST05 side seam | New: a hinge and vacuum do the alignment |
| Release, turning tube, chute OC-600 (Rig D) | ST07 output | New: shirt turned right side out at the end |
| Flat-bed overlock and coverstitch on SP-400 plinths | ST05 heads | Same head classes (Jack E4/C4, W4) |
| Two cobots (UR5e class) on CP-300 pedestals | ST04 manipulation | Replaces our UR10e on a 3.6 m track plus the Festo gantry |
| Control stack: garment record, station controller, skills plus policy, vision, motion and I/O, independent safety | M02, M06–M11, M10, M14 | Same layering and the same safety rule |
| Bought cutter ~1.8 x 1.6 m (Stage 2) | ST02 | Smaller than our conveyor cutter |

## 3. What is different from our concept model
- **No overhead gantry, no robot track:** two fixed-pedestal cobots, with tables and forms that define where the fabric is.
- **Construction order:**
  - Ours closed the sides and then hemmed a tube.
  - His hems everything flat, closes last, and turns the shirt.
- **Collar:** a collapsing form on a turntable with a metered rib, not rollers.
- **Footprint:** 6 x 4 m against our 10 x 5 m.
- **Programme:** proves the four transitions on benches before any cell exists.
- **Budget:** Stage 1 is $250k, including people; our development cell carried about USD 0.25M of parts alone.

## 4. Findings from modelling his Lab 1
The model and checks are in `cad/labs/lab1/` and `sim/labs/`; results are in `sim/results/lab1_cobots.json`.
1. **Cobot reach (OI-6).**
   - A UR5e on his 700 mm pedestal with the tool pointing down reaches 0.86 m horizontally at table height (MuJoCo, Menagerie UR5e geometry; tool stack 0.12 m, an estimate).
   - In the provisional layout, 8 of 10 rig tasks are reachable and collision-free against every Lab 1 part.
   - The two failures are both Rig C at the folding table: laying the butterfly on the hinge and pinching the side-seam edge need 1.0–2.3 m.
   - A 1.2 x 1.6 m table cannot be served end to end by one 0.86 m arm on a fixed pedestal. The options are a longer-reach arm, a pedestal at the hinge end plus a second arm, or a carrier.
2. **RT-104 camera uprights:** they sit at X = 750 on both long edges of the registration table, where a pedestal cobot works across the table. Cobot A had to move 300 mm sideways to clear one.
3. **Two cobots on Rig B:** Rig B uses both cobots (drape, then rib loop). With two arms, Rigs A, C and D cannot run at the same time as Rig B, yet his Stage 1 timeline overlaps them (Rig B Apr–Aug, Rig C May–Jul).
4. **STEP labels:** FT-200 labels the moving leaf's perforated sheet "FT-206_fixed_sheet" and repeats several names (FT-210, FT-211, FT-209). His check.py uses the right names, so only the STEP export is affected.
5. **Roll width:** Lab 1 item 6 takes rolls up to 1,850 mm wide, while the buy-list cutter bed is about 1.8 x 1.6 m. Real conveyor cutters take at most 1.8 m material width (Zünd G3 technical data: https://www.zund.com/media/391/download/tda_technical%20data%20G3_13_EN-us.pdf?v=3). Confirm the roll width against the chosen cutter.
6. **His fold geometry checks out in our model:** the moving-leaf group rotates 180 degrees about his hinge axis (1.5 mm above datum B) and lies over the fixed leaf.

## 5. What to ask him
- The master floor layout or a drilling template. The model's floor positions are provisional until then.
- Who serves the folding table (Rig C load and edge pinch, Rig D hem pull), and with which arm.
- Whether RT-104 can move to the short edges.
- The Lab 2 package when ready. The model gains the fixtures as geometry, replacing the envelopes.

## 6. Market check (2026-10-23, sourced)
- No one sells a verified roll-to-tee cell with conventional stitching:
  - Silana claims one but has no delivery found (https://patents.justia.com/assignee/silana-gmbh).
  - SoftWear starts from cut panels, and its Gen-3 line is late (https://www.bbc.com/news/articles/c0q2gkj97eko).
  - CreateMe bonds seams instead of stitching them (https://www.textileworld.com/textile-world/knitting-apparel/2026/02/createme-untuckit-supima-unite-to-launch-first-digitally-bonded-garments).
  - Jack/Aitu automate single operations with humanoids (https://english.news.cn/20260724/b9c5a91b473c445bbd9a0c2de28a5493/c.html).
- Semi-automatic collar attachment on cylinder-bed overlocks exists (Pegasus FRA, April 2026: https://www.pegasus.co.jp/en/news/wp-content/uploads/2026/04/20260409_FRA_E.pdf). This supports Rig B's head choice, and it is also the benchmark Rig B must beat.
