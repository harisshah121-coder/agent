# Build Guide 3: The 3D Model (v1, 2026-10-22)

How every 3D model of the cell gets built: toolchain, conventions, vendor geometry import, each assembly A00–A10, kinematics and simulation, Blender animation, the R3 interactive walkthrough, BOM reconciliation and verification. Sources: research report R15 (toolchain, licences, conversion routes) plus R01–R08 for the parts. Assembly IDs mirror stations (`ARCHITECTURE_SPINE.md` §4).

---

## 1. Purpose and outputs
| Output | Format | Used for |
|---|---|---|
| Master model | build123d Python modules (one per assembly) | Source of truth; diffable; scriptable by Claude |
| Engineering exchange | STEP AP214 with labels and colours | Vendors, machining quotes, integrators |
| Visual | GLB (glTF 2.0) | Blender, web (M01 Three.js), R3 |
| Kinematics | joints file → URDF → MJCF (MuJoCo) / USD (Isaac Sim, optional) | Reach, collisions, cycle time, M13 twin |
| Drawings | ISO 128 PDF/DXF via Draftwright (ISO 2768-m default) | Fabricated parts |
| Animation | Blender 5.2 scene, rendered video | Investor demo, process explanation |
| Walkthrough | R3 project with imported .blend and scripted motion; private preview link | Interactive demo |
| BOM | generated from model metadata, reconciled with `spine/parts.csv` | One parts list across guides |

Honest limit: the model proves geometry, clearances, reach, joint limits, nominal cycle time, sensor fields of view and interface locations. It does not prove knit behaviour, pick reliability, seam quality or safety compliance (R15 R-5).

## 2. Toolchain and environment
Verified in this container on 2026-10-21/22 unless marked.

| Tool | Version | Status here | Purpose |
|---|---|---|---|
| Python | 3.13 | installed | everything |
| build123d | 0.13.0 (cadquery-ocp 8.0.1) | **installed, STEP/GLB/STL export tested** (`/home/user/.venvs/cad`) | master CAD |
| build123d-mcp | 0.3.91 | installed in the same venv | lets Claude drive build123d as an MCP server |
| build123d-drafting-helpers | 0.15.5 | installed | drawings helpers |
| MuJoCo | 3.16.0 | installed (`/home/user/.venvs/sim`) | kinematics, timing |
| Genesis | 1.4.4 | installed (`/home/user/.venvs/sim`) | optional deformables |
| onshape-to-robot, RoboDK API | 1.8.3, 6.0.2 | installed (`/home/user/.venvs/tools`) | optional |
| trimesh, yourdfpy, robot_descriptions, mujoco-menagerie, obj2mjcf | 5.1.1, 0.0.60, 3.3.0, 2026.9.4, 0.0.25 | pin per R15 R-1 | meshes, URDF, Menagerie models |
| bpy (Blender as a module) | 5.2.2 (needs Python 3.13 exactly) | to install | headless scenes and renders |
| Blender desktop | 5.2 LTS + STEP Importer 1.2.1 | owner's PC (optional) | interactive review |
| Isaac Sim | 6.2 | optional, needs RTX 4080/16 GB VRAM | perception twin |
| QElectroTech / SMC PneuDraw | 0.100 / online | — | electrical and pneumatic sheets |

Install (R15 R-1):
```bash
python3.13 -m venv ~/.venvs/cad && . ~/.venvs/cad/bin/activate
pip install build123d==0.13.0 ocp-vscode==4.2.0 trimesh==5.1.1 yourdfpy==0.0.60 robot_descriptions==3.3.0
pip install mujoco mujoco-menagerie==2026.9.4 obj2mjcf==0.0.25 bpy==5.2.2
python3.13 -m venv ~/.venvs/draw && ~/.venvs/draw/bin/pip install draftwright build123d-drafting-helpers   # AGPL, keep separate
```
Risk: build123d is 0.x and moves monthly; pin exact versions and upgrade deliberately. Test bpy, mujoco and build123d in one venv first; split into two if they conflict.

## 3. Modelling conventions
- **Units** mm, kg, s. **World frame**: origin at the cell floor datum, front-left corner of the guarded envelope; +X along material flow (roll → output), +Y toward the back, +Z up.
- **Assembly modules**: `cad/assemblies/a00_frame.py` … `a10_vision.py`; each exposes `build() -> Compound` with labels and colours, `joints() -> list[JointSpec]`, `bom() -> list[BomLine]`.
- **Naming**: product label = `part_id` for bought parts (`P-ST04-002`), `Ann-<name>` for custom parts; sub-assemblies `A04.2-gripper-toolbox`.
- **Levels of detail**: LOD0 envelope box with mounting faces (from datasheet dimensions; first pass for every part), LOD1 vendor STEP or simplified custom geometry, LOD2 full detail only where interference or appearance matters.
- **Metadata** on every product: part_id, vendor, vendor_pn, mass_kg, CAD source and licence note; `bom()` reads these.
- **Collision geometry**: convex hulls / decimated meshes generated per part (trimesh, obj2mjcf `--decompose`); visual meshes from GLB.

## 4. Vendor geometry import workflow
1. For each row in `spine/parts.csv`, read `cad_source`.
2. **Vendor STEP**: download from the vendor configurator or portal (Festo, UR support site, Schmalz, ATI, Robotiq, Beckhoff, Rittal, Phoenix, SICK, Schmersal, Basler, LUCID, Neousys, mk, Dorner, Smart Vision Lights, E+L, Pepperl+Fuchs, Piab, EXAIR, Delta, Patlite, Pilz; TraceParts/CADENAS for others) (R15 vendor table). Store in `cad/vendor/<part_id>/model.step` with `LICENSE.txt` and a line in `cad/vendor/REGISTER.csv` (source URL, date, licence).
3. **Import**: `import_step("model.step")` keeps the vendor assembly tree, labels and colours; place it with a `Location` at its mounting datum; record mass from the datasheet.
4. **No vendor CAD** (cutter, all sewing heads, roll lifter, collar module): build an LOD0 envelope from datasheet dimensions and manual table cut-out drawings; request STEP under NDA (iECHO/Zünd, JUKI, Dürkopp Adler); 3D-scan purchased heads when they arrive (R04, R15).
5. **Arms and grippers for simulation**: use MuJoCo Menagerie UR10e (BSD-3) and Robotiq 2F-85 (BSD-2) directly; attach with `MjSpec.attach` at a named site (R15 R-2).
6. **Fasteners**: bd_warehouse generated models, not McMaster files.
7. **Licences decide where files live**: McMaster-Carr and CADENAS files may not be redistributed (CADENAS bans AI training); GrabCAD is non-commercial; UR meshes only with UR's terms attached. Keep `cad/vendor/` out of the public repository (private storage or git-ignored), and commit only our own code-CAD and generated outputs that contain no restricted geometry (R15).

## 5. Assemblies A00–A10
For each: contents (part IDs), source of geometry, joints, animation and simulation hooks.

| Assembly | Contents | Geometry source | Joints / DOF | Animation and sim hooks |
|---|---|---|---|---|
| A00 Frame and guarding | P-ST00-001 extrusion frame, panels, doors, cable trays, feet | code-CAD from extrusion profiles (vendor STEP sections) | door hinges (revolute) | door-open → safety stop scene; interference check base |
| A01 Roll handling | P-ST01-001 let-off, -002 edge guide, -003 static bar, -004 roll lifter, roll (Ø 400–500 mm, 1.8 m) | code-CAD + vendor STEP (E+L, motor) + envelope (lifter) | roll rotation; dancer arm (revolute); edge-guide shift (prismatic) | web path as a swept surface; roll diameter decreases over a run |
| A02 Cutter | P-ST02-001 bed, gantry, head, conveyor | LOD0 envelope from datasheet until vendor STEP | X, Y gantry (prismatic), Z, knife C axis, conveyor index | cut-path playback from M04 marker DXF; conveyor index |
| A03 Extraction and buffer | T1 needle bar (P-ST03-001/-002), T4 pad (P-ST03-004/-005), staging table | vendor STEP (Schmalz, EXAIR, Piab, Festo) + code-CAD bar | needle stroke (prismatic, visual) | pick-off sequence; pieces as thin flat meshes from M03 patterns |
| A04 Manipulation | P-ST04-001 Festo gantry, -002 UR10e on pedestal, -003 tool changer + stands, -004 gripper, -005/-006 sensors | vendor STEP (Festo, UR, ATI, Robotiq, GelSight, RealSense) + Menagerie for sim | gantry X, Y1, Y2, Z; UR10e 6 revolute; gripper 1 | reach map over 3 m × 1.5 m; tool-change sequence; presentation poses at heads |
| A05 Sewing heads | P-ST05-001 overlock, -003 coverstitch, tables, pullers, needle cameras | LOD0 envelopes from manuals → scans | handwheel (visual), presser foot lift | seam presentation by UR10e; feed direction arrows |
| A06 Collar module | P-ST06-001 cylinder-arm overlock, -002 expansion rollers and rib unit | code-CAD (in-house design) + envelope | roller spread (prismatic), roller rotation | rib loop stretch animation |
| A07 Finishing and output | P-ST07-001 camera, -002 backlights, -003 discharge belt, reject gate | vendor STEP (Basler, SVL, mk/Dorner) + code-CAD table | belt; flipper gate (revolute) | inspection and accept/reject |
| A08 Decoration (optional) | P-ST08-001 embroidery head | envelope | — | hidden in base scenes |
| A09 Control and safety | P-ST09-001…014: cabinets, HMI, tower light, e-stops, interlocks, light curtains | vendor STEP (Rittal, Beckhoff, Patlite, Schneider, Schmersal, SICK, Pilz, Festo) | cabinet doors | light-curtain field volumes; safety zones as transparent volumes |
| A10 Vision and compute | P-ST10-001…006 cameras, lenses, lights, IPC | vendor STEP (Basler, LUCID, Neousys, NVIDIA) | — | camera frustums from R06 FOV math; field-of-view coverage check |

Garment pieces: generated from M03 pattern output (SVG/DXF) as 1 mm-thick flat meshes; Blender cloth only for visual sequences (uncalibrated).

## 6. Simulation setup and cycle-time study
1. Emit URDF from each assembly's `joints()` with a small in-house emitter (no build123d-to-URDF library exists, R15).
2. Convert: `spec = mujoco.MjSpec.from_file("cell.urdf"); spec.encode()` → `cell.xml`; attach Menagerie UR10e and Robotiq 2F-85.
3. Checks: `mj_forward` runs; collision pairs report zero penetration in home and all taught poses.
4. Reach map: sample the 3 m × 1.5 m staging and all presentation poses at the heads; every required pose reachable within joint limits with margin.
5. Cycle time: joint-space trajectories using vendor velocity/acceleration limits for each skill; replay the M07 schedule; target interval ≤ 5.47 min per attempt (Guide 1 §1.3) with stated margins; ST04 occupancy compared with its 4.8 min estimate.
6. Optional cross-checks: RoboDK (USD 3,995 + 1,500/yr) for UR controller timing; Isaac Sim 6.2 for camera placement and synthetic images when an RTX 4080-class GPU is available.

## 7. Blender animation and the R3 walkthrough
- **Route**: build123d `export_gltf` → Blender built-in glTF importer (preserves hierarchy and materials). Raw vendor STEP into Blender only via STEP Importer 1.2.1 when needed (slow on large files) (R15).
- **Mechanisms**: object constraints and drivers on the joint empties; keyframes generated from the MuJoCo trajectories (same timing as the twin).
- **Story sequence** (one continuous shot plus close-ups): roll loads → web feeds → marker cuts → gantry picks pieces → shoulder seam → rib attach → sleeves → sides → hems → inspection → accepted shirt on belt. Fabric shown as flat panels with Blender cloth only in close-ups, labelled "visualisation".
- **Render**: `blender -b scene.blend -E BLENDER_EEVEE_NEXT -a` for drafts; Cycles for stills.
- **R3**: save `.blend` with packed textures → `r3_blender_upload` → `r3_blender_import`; R3 imports meshes and empties only, so station motion is re-scripted in R3 Code components (RENDER_BEFORE for continuous motion, MOUSE_CLICK for "play station" hotspots); `r3_help_write` for controls; share with `r3_preview_create` (free, 7-day private link). Read R3 `CODE_PATTERNS.md` before writing code.

## 8. BOM generation and reconciliation
- Each assembly's `bom()` yields `{part_id, qty, mass_kg, cad_source}`; `scripts/model_bom.py` (to write in phase 2) merges them.
- Reconcile against `spine/parts.csv`: every model part_id exists in the registry; every registry row with qty > 0 appears in the model; quantities match. Differences fail CI.
- Mass and centre of gravity per assembly feed frame and pedestal sizing.

## 9. Verification checklist (checkpoints from R15 R-4)
| Checkpoint | Deliverable | Pass criterion |
|---|---|---|
| C0 Toolchain | pinned env; smoke test | **done** for build123d 0.13.0 (2026-10-21); extend to bpy + MuJoCo in one env |
| C1 Vendor geometry register | `cad/vendor/REGISTER.csv` + files | every part_id has STEP or an envelope + reason; no restricted files in the public repo |
| C2 Station envelopes | A00–A10 at LOD0 placed on the floor plan | clearances ≥ 500 mm walkways; OCCT interference check clean |
| C3 Kinematics | URDF + MJCF; Menagerie arm attached | all poses reachable; zero collisions |
| C4 Cycle time | MuJoCo trajectories + scheduler replay | ≤ 5.47 min interval with margin; ST04 occupancy measured |
| C5 Visual twin | Blender scene; R3 preview link | clean import; walkthrough plays end to end |
| C6 Fabrication package | drawings, DXF, STEP; two quotes per custom part | quotes and lead times recorded |
| C7 Electrical and pneumatic | QElectroTech + PneuDraw sheets | every I/O point in `spine/interfaces.csv` appears on a sheet |
| C8 Perception twin (optional) | Isaac Sim import | camera coverage verified |

**Phase 2 starts here**: C1 (vendor geometry register) and C2 (LOD0 envelopes for A00–A10) are the first build tasks.
