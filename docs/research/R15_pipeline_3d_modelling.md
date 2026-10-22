# R15 · 3D modelling and simulation pipeline for the roll-to-garment cell

Research agent R15 · written 2026-10-21 · scope: CAD/mesh/URDF/MJCF/USD toolchain, vendor geometry sources, electrical and pneumatic drawing tools, fabrication vendors, and the honest limits of what the 3D model proves.

## Summary

- Keep decision D-004: build123d 0.13.0 (Apache-2.0, released 2026-09-21) on cadquery-ocp 8.0.1 and Python 3.13 is the master model for assemblies A00–A10; it installed and exported STEP, glTF and STL in this container on 2026-10-21, and its `import_step` keeps vendor assembly structure, labels and colours [1], [4], [7].
- Pinned toolchain (all versions verified on PyPI/GitHub/vendor pages 2026-10-21): build123d 0.13.0, ocp-vscode 4.2.0, trimesh 5.1.1, yourdfpy 0.0.60, robot_descriptions 3.3.0, MuJoCo 3.15.0, mujoco-menagerie 2026.9.4, obj2mjcf 0.0.25, bpy/Blender 5.2.2 LTS (Python 3.13), Draftwright (AGPL, separate env), KiCad 10.0.6, QElectroTech 0.100, FreeCAD 1.1.4 (not the 26.3 RC), Isaac Sim 6.2 (optional, RTX 4080+), onshape-to-robot 1.8.3 (only with a paid Onshape plan).
- No build123d-to-URDF library exists: write a small emitter from each assembly's joints file, let MuJoCo convert URDF→MJCF (`MjSpec.from_file` + `encode`) and Isaac Sim convert URDF→USD; onshape-to-robot is the only turnkey CAD→URDF/MJCF tool and needs Onshape Standard at $1,500/user/yr [13], [17], [33].
- Use MuJoCo Menagerie for purchased arms and grippers: UR5e, UR10e (BSD-3-Clause) and Robotiq 2F-85 (BSD-2-Clause) exist; FANUC, ABB, KUKA iisy and Doosan do not, and must be converted from ROS descriptions with the documented Menagerie recipe [31], [32], [86], [87].
- Blender route is GLB (build123d `export_gltf`) → built-in glTF importer; STEP Importer 1.2.1 / STEPper Reborn 2.3.0 exist for raw vendor STEP but have reported performance regressions on large files; mechanism motion by constraints/drivers; headless Cycles/EEVEE renders; `.blend` → R3 imports meshes and Empties only, so walkthrough motion is scripted in R3 [42], [43], [45], [51].
- Vendor geometry is obtainable for most families (UR, KUKA, ABB, Festo, igus, Rexroth, HIWIN, THK/Rollon/Güdel via TraceParts, Schmalz, SCHUNK, Zimmer, OnRobot, ATI, Robotiq, Beckhoff, Siemens, SICK, Rittal, Phoenix, Basler, FLIR, Zivid, Photoneo, RealSense, Orbbec, Jetson, Misumi, McMaster, Vention), mostly behind free logins; not obtainable publicly for Zünd cutters and all industrial sewing heads (envelope models from manuals, then measure the bought head) [82]–[121].
- Licences decide where files may live: McMaster-Carr CAD may not be redistributed or fabricated from; CADENAS-portal files are for CAD/BIM design only (AI training banned, EUR 20,000 penalty); GrabCAD is non-commercial; UR meshes may be published only with UR's T&Cs attached; Menagerie/ROS models are BSD/Apache. Keep `cad/vendor/` private and use bd_warehouse for fasteners [108], [109], [111], [83].
- Fabrication norms: quick-turn CNC 1–4 days (Protolabs, Fictiv), standard 3–7 business days (Xometry), JLCCNC 3 days + shipping from $5, PCBWay from 2 days; SendCutSend laser/bend ships in 1–4 days with instant DXF pricing; EOAT prints on Bambu H2D ($1,849) / H2S ($1,399) or Prusa CORE One+ (~$1,299, currency to verify) [71]–[81].
- Drawings: ISO 128-1:2020 (CHF 44) with ISO 2768-m as the default tolerance class most online shops apply; ASME Y14.5-2018 ($380) only for US partners; Draftwright generates ISO-style multi-view PDF/SVG/DXF straight from build123d parts [67]–[70], [122].
- Electrical and pneumatic: QElectroTech 0.100 (GPL) for cabinet schematics with EPLAN only on an integrator's demand (price on request); SMC PneuDraw free online or Festo FluidDraw 365 (ISO 1219-1, valve-terminal circuit generation; price after login) for pneumatics [61], [62], [63], [65].
- Simulation scope is honest and matches the white paper: the model proves geometry, reach, kinematic limits, nominal takt and interfaces; it does not prove fabric handling, seam quality or safety compliance; RoboDK ($3,995 + $1,500/yr) is an optional OEM-timing cross-check, Visual Components is unnecessary at one-cell scale [52], [54].
- Isaac Sim 6.2 is optional and hardware-gated (RTX 4080 / 16 GB VRAM / 32 GB RAM minimum); its CAD Converter accepts STEP/IGES/JT/Parasolid/SolidWorks/Inventor/glTF and its Onshape importer handles assemblies with API keys [24], [27], [28].
- Conflicts with the white paper: none; open items are mostly licence texts and OEM CAD requests (Zünd, sewing heads, FANUC) plus two 10-minute environment tests (bpy + mujoco + build123d in one venv; Open3D on Python 3.13).

## Findings

Conventions in this report: versions and prices were read on 2026-10-21; "login" means the vendor requires a free account; source numbers refer to the list in `## Sources`. Software tables use `Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL`; hardware tables use `Vendor | Model / part number | Key specs | Price (currency, date, list/quote/est.) | Lead time | CAD available? (format, where) | Source URL`.

### F1. Code-CAD core: build123d, OCP, CadQuery, viewers

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| build123d | 0.13.0 (PyPI, 2026-09-21); 0.12.0 2026-09-18, 0.11.1 2026-07-02 | Apache-2.0 | 3.2 M total PyPI downloads, ~718 k/month; 3 maintainers | Master model for assemblies A00–A10 (already decided D-004; installed and smoke-tested in this container on Python 3.13 with cadquery-ocp 8.0.1: STEP, glTF, STL export worked) | [1], [2], [3], [125] |
| cadquery-ocp (OCP, OCCT bindings) | 8.0.1.1.0 (2026-10-05); 7.9.3.x Jan–May 2026 | Apache-2.0 | wheels for CPython 3.11–3.14, Linux/macOS/Windows; `Requires-Python >=3.11,<3.15` | Pulled automatically by build123d; since build123d 0.11.0 the dependency is `cadquery-ocp-novtk` (no VTK), which breaks some Jupyter viewers but is lighter | [4], [2] |
| ocp-vscode (OCP CAD Viewer) | 4.2.0 (2026-10-13) | Apache-2.0 | Python >=3.10; VS Code extension + standalone viewer; "Library Manager" can install build123d/cadquery | Interactive viewer during modelling; `from ocp_vscode import show` | [5] |
| CadQuery | 2.8.0 (2026-06-21); 2.7.0 2026-02-13 | Apache-2.0 | 3 maintainers; conda-forge primary channel (`mamba install cadquery`) | Alternate code-CAD; `cq.Assembly` constraints solver, STEP/XBF/glTF assembly export, `Assembly.importStep`. Not needed if build123d is the master; useful for reading XBF/XCAF files | [6], [8] |
| build123d docs: joints and assemblies | docs at v0.13.0 | CC/Apache | `RigidJoint`, `RevoluteJoint`, `LinearJoint`, `CylindricalJoint`, `BallJoint` with `connect_to`; assemblies are `Compound` trees via `parent`/`children` | Joints are a modelling aid (one-time reposition), not a kinematic solver; they still give us named joint frames and ranges to emit URDF/MJCF from | [7] |
| build123d I/O | v0.13.0 | Apache-2.0 | `export_step` (colour + label, per-product naming), `export_gltf` (PBR materials), `export_stl`, `Mesher` (3MF/STL with metadata), `import_step` (read-only STEP assembly tree with labels, colours, per-instance locations), `import_svg` | Covers STEP in/out and GLB out, the two formats the spine requires | [7], [1] |
| Draftwright | 0.1.x on PyPI (repo created 2026-06-14, 1,932 commits) | AGPL-3.0 | active; `pip install draftwright`; needs Python >=3.10 and build123d >=0.9 | Automated multi-view fabrication drawings (orthographic views, section, ISO hatching, title block) to PDF/SVG/DXF from a build123d solid or STEP file. AGPL: keep it in a separate drawing environment (the project's own advice) | [122] |
| build123d-drafting-helpers | 0.8.0 | not captured (PyPI) | third-party, pure Python | Dimensions, leaders, GD&T symbols, title block, lint; `make-drawing part.step --tolerance "ISO 2768-f"` | [123] |
| build123d-mcp | 0.3.x (0.3.81 per libraries.io) | Apache-2.0 | active; soft-pins build123d >=0.10,<0.12 in 0.3.59 (check against 0.13) | AI-assisted modelling, measurement, render_view, drawing lint; R17 verifies the install | [124] |
| bd_warehouse | catalogued via build123d-mcp | Apache-2.0 (per Context7 listing) | parametric fasteners, bearings, gears, threads | Replaces McMaster-Carr fastener CAD, whose terms forbid redistribution (see F7) | [124] |

Python 3.13 support: cadquery-ocp 8.0.1.1.0 ships cp311–cp314 wheels [4]; build123d 0.13.0 is a pure-Python wheel [1]; the container install on Python 3.13 succeeded (TOOLING.md, 2026-10-21). ocp-vscode needs >=3.10 [5].

Large-STEP handling (what the docs say): build123d's own assembly example deep-copies an imported screw 600 times and writes a 52 MB STEP in about 5 s [7]; `import_step` walks the XDE tree read-only and keeps instance locations, so a vendor assembly keeps its structure [7]. Nothing in the docs promises fast tessellation of very large vendor files; the practical rule (recommendation, not a sourced claim) is to import each vendor STEP once, strip internals, cache a simplified BREP/GLB per `part_id`, and never re-tessellate robots on every build.

### F2. GUI CAD: FreeCAD, Onshape, Fusion, SolidWorks

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| FreeCAD | 1.1 released 2026-03-24; 1.1.4 (bug-fix) 2026-09-28; next is 26.3 (CalVer, three releases/year), RC1 2026-10-08, final not released as of 2026-10-21 | LGPL-2.1+ | very active (weekly dev builds) | Viewer and sanity-check GUI for STEP we export; Assembly Workbench (Ondsel solver) has joints, exploded views, BOM, and (1.1) a Simulation tool to animate joints; TechDraw for drawings if Draftwright is not enough. Pin 1.1.4, not the 26.3 RC | [9], [10], [11], [12] |
| Onshape | SaaS, updates every 3 weeks; FeatureScript MCP Server in App Store (Onshape Labs, blog 2026-09-03) | proprietary | Free plan $0 (non-commercial, every document public); Standard $1,500/user/year; Professional $2,500/user/year (USD, onshape.com, 2026-10-21, list) | Only if the owner wants a cloud GUI; a commercial project cannot use the Free plan. Onshape + onshape-to-robot is the cleanest GUI route to URDF/MJCF, and Isaac Sim has a native Onshape importer | [13], [14], [15], [27] |
| onshape-to-robot | 1.8.3 (2026-08-26) | MIT | 1 maintainer (Rhoban); regular releases through 2026 | Exports an Onshape assembly to URDF, SDF or MuJoCo MJCF: `pip install onshape-to-robot`; env `ONSHAPE_API`, `ONSHAPE_ACCESS_KEY`, `ONSHAPE_SECRET_KEY`; `config.json` with `url` and `output_format`; run `onshape-to-robot my-robot`; test with `onshape-to-robot-mujoco my-robot` | [16], [17] |
| Autodesk Fusion | subscription $680/user/year ($85/month); Fusion for Startups ~$150 for 3 years (qualified); personal-use edition free | proprietary | — | Personal use is limited to non-commercial, home-based projects by individuals earning < $1,000/year, 10 active editable documents, limited import/export types: not usable for this venture. The startup programme is the cheap commercial route if a Fusion-based partner needs it | [18], [19], [20] |
| SolidWorks | 3DEXPERIENCE SOLIDWORKS Design Standard $2,820/year (US, reseller Ohmycad price list, Oct 2026); SolidWorks for Makers $48/year | proprietary | — | Makers licence is personal use only (< $2,000/year revenue). Only relevant if a contract designer insists; our STEP exports open in it | [21], [22] |

### F3. Mesh tools, URDF and MJCF generation, robot models

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| trimesh | 5.1.1 (2026-10-02); pure Python 3.10+ | MIT | ~4 k stars, 666 forks, 1,042 dependents, PyPI attestations | Mesh load/convert (STL/OBJ/GLB), watertight checks, convex hulls, mass properties for URDF inertials | [37] |
| Open3D | PyPI 0.19.0 (2025-01-08), wheels for Python 3.8–3.12 only; open3d.org lists 0.20.0 downloads with Python 3.10–3.14 options | MIT | large; slow PyPI cadence | Point clouds and `simplify_quadric_decimation`; in a Python 3.13 env use the 0.20.0 wheels from open3d.org or skip it (trimesh + Blender Decimate cover our needs) | [38] |
| Blender Decimate / bpy | bpy 5.2.2 (2026-09-15), `Requires-Python ==3.13.*`; bpy 4.5.14 needs Python 3.11 | GPL-3.0 | Blender Foundation | Headless decimation and GLB re-export in the same Python 3.13 version as the CAD env | [41] |
| yourdfpy | 0.0.60 (2026-01-23) | MIT | 1 maintainer | URDF parse/validate/visualise/forward kinematics; loads 12/12 test URDFs vs 4/12 for urdfpy | [36] |
| robot_descriptions | 3.3.0 (2026-10-12) | Apache-2.0 | active | One-line loaders for open robot descriptions into MuJoCo, Pinocchio, PyBullet, yourdfpy (`pip install robot_descriptions`) | [35] |
| MuJoCo | 3.15.0 (GitHub release 2026-10-05) | Apache-2.0 | Google DeepMind; frequent releases | Kinematics, reach and cycle-time studies; loads URDF directly (with `<mujoco><compiler meshdir=... discardvisual="false"/></mujoco>` inside `<robot>`), `MjSpec.from_file`, `spec.encode('model.xml')` to save MJCF, `.mjz` to bundle assets. URDF is not schema-checked: mistyped attributes are silently ignored | [29], [33] |
| mujoco-menagerie (pip) | 2026.9.4 (2026-09-28); Python >=3.10.12 | Apache-2.0 package; each model ships its own LICENSE | 3 maintainers; GitHub release archive | `pip install mujoco-menagerie`; `mm.get('universal_robots_ur5e').spec('ur5e')`, `spec.attach(...)` to mount grippers, `r.files('scene')` to vendor files with the model's oid | [30] |
| Menagerie models relevant here | repo main | UR5e BSD-3-Clause; UR10e BSD-3-Clause; KUKA iiwa 14 BSD-3; Franka FR3 Apache-2.0; Flexiv Rizon4S Apache-2.0; Kinova Gen3 BSD-3; Robotiq 2F-85 and 2F-85 v4 BSD-2-Clause; Panda gripper Apache-2.0 | curated by DeepMind | No FANUC, ABB, Doosan or Techman model in Menagerie (checked the model table): those arms need URDF→MJCF conversion from the ROS descriptions in F7 | [31] |
| obj2mjcf | 0.0.25 (PyPI) | MIT | 378 stars; used to build Menagerie | Splits multi-material OBJ, writes MJCF asset/geom stubs, optional CoACD convex decomposition for collision meshes | [34] |
| Menagerie derivation recipe (UR5e) | README | — | — | The documented URDF→MJCF route we should copy: DAE→OBJ in Blender, obj2mjcf, add `<mujoco><compiler discardvisual="false"/></mujoco>` to the URDF, load in MuJoCo, save MJCF, add actuators, keyframe and hand-made collision geometry | [32] |
| Robotiq official ROS 2 packages | robotiq/ros v1.1.0 (2026-08-14) | BSD-3-Clause | ros2_control driver + descriptions for 2F-85, 2F-140, Hand-E (Humble/Jazzy/Lyrical); continues PickNik's ros2_robotiq_gripper; `robotiq/isaacsim_assets` also exists | Gripper URDFs and meshes for the toolbox A04.2 | [88] |

There is no published "build123d-to-URDF" library (searched; none found): the project must write its own exporter from the joints file in each `Ann` module (link = labelled `Compound`, joint = build123d `Joint` label + axis + range + parent/child), emit meshes per link (GLB for visuals, decimated STL/OBJ for collisions via trimesh or obj2mjcf/CoACD) and let MuJoCo convert URDF→MJCF. onshape-to-robot is the only turnkey CAD→URDF/MJCF exporter found, and it needs Onshape.

### F4. Simulators: Isaac Sim, RoboDK, Visual Components, Vention

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| NVIDIA Isaac Sim | 6.2.0 (release notes updated 2026-10-14); 5.1.0 unsupported | proprietary, free | open-source on GitHub; URDF/MJCF importers now in the `isaacsim-asset` wheel; MJCF importer bundles MuJoCo 3.12.0 | Optional: perception/synthetic data for M11 and ROS 2 SIL. Imports URDF (GUI or `./python.sh standalone_examples/api/isaacsim.asset.importer.urdf/urdf_import.py --urdf ... --merge-mesh --collision-from-visuals`), MJCF, Onshape assemblies (API key, tessellation chord/angle tolerances) and CAD via the Omniverse CAD Converter (STEP/IGES, JT, Parasolid, SolidWorks, Inventor, Creo, NX, CATIA, STL, OBJ, FBX, glTF/GLB, 3MF, DWG/DXF) | [23], [25], [26], [27], [28] |
| Isaac Sim requirements | 2026 | — | — | Ubuntu 22.04/24.04 or Windows 11; minimum RTX 4080 with 16 GB VRAM, 32 GB RAM, driver 595.x; GPUs without RT cores not supported; Ubuntu 22.04 support deprecated | [24] |
| RoboDK | current (docs v5.9 API) | proprietary | — | Professional licence $3,995 permanent incl. 1 year maintenance, then $1,500/year optional (USD, robodk.com, 2026-10-21, list); 30-day trial limited to 50 program instructions; Educational $145/year. Python API (`pip install robodk`) includes an "Estimated cycle time" example, robot library with OEM models (UR, FANUC), post-processors and online drivers | [52], [53] |
| Visual Components | 5.0 (2026-03-12): MQTT connector in Professional/Premium | proprietary | Essentials / Professional / Premium editions; Python API | Price not published; request quote. Discrete-event line simulation; stronger than we need for a one-cell takt study (MuJoCo + a Python scheduler model is enough) | [54] |
| Vention MachineBuilder | cloud CAD, free to design | proprietary | 3,000+ plug-and-play parts, 300+ designs, real-time BOM and price, MachineMotion AI controller (EtherCAT, Jetson) | Designs export as STEP from MachineBuilder or the design summary page; imported user CAD lives in "My Models" and is not quoted. Useful as a priced frame/gantry configurator whose STEP we re-import into build123d | [56], [57], [58] |

### F5. Blender pipeline (visuals, mechanism animation, cloth look, R3 hand-off)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| Blender 5.2 LTS | released 2026-07-14; 5.2.2 on 2026-09-15; supported to July 2028; 4.5 LTS (4.5.14) supported to July 2027 | GPL-3.0 | Blender Foundation | Pin 5.2 LTS: same Python 3.13 as the CAD env (bpy 5.2.2), EEVEE improvements, VFX Platform 2025 libraries | [39], [40], [41] |
| glTF 2.0 importer/exporter | built in, enabled by default | GPL-3.0 | Khronos glTF-Blender-IO | The main CAD→Blender route: build123d `export_gltf(..., "assembly.glb")` then `File ▸ Import ▸ glTF 2.0`; keeps hierarchy, PBR materials, custom properties (extras) | [45] |
| STEP Importer (Clonephaze) | 1.2.1 (2026-07-21), Blender 5.1 and newer | GPL-3.0-or-later | 28,977 downloads; uses Cascadio to convert STEP→glTF then Blender's glTF importer | Direct STEP drag-and-drop (vendor STEP without going through build123d); assembly hierarchy to collections; tessellation presets; no STEP export | [42] |
| STEPper Reborn | 2.3.0 (2026-07-10), Blender 5.1 and newer | GPL-3.0-or-later | 7,683 downloads; 29 stars; based on cadquery-ocp | Alternative importer; known limits: per-face materials broken, wrong scale for FreeCAD STEP in non-mm units; one user reports a 500 MB STEP that took 20 min in 5.0 hanging in 5.2 | [43] |
| STEPper NEXT (Peak Design fork) | 2.1.x for Blender 5.1; pythonocc-core 7.9.3 / Python 3.13 | GPL | native C++ mesh extraction, ShapeFix healing, material database | Third option for heavy STEP files | [44] |
| Cloth simulation | Blender 5.2 manual | — | — | Settings: Quality Steps, Speed Multiplier, Vertex Mass, Air Viscosity, Bending Model (linear/angular), Tension/Compression/Shear/Bending stiffness and damping, internal springs, pressure, collisions. These are visual, uncalibrated parameters: no documented mapping from KES/FAST fabric measurements to Blender stiffness | [46], [47] |
| Mechanism animation | Blender 5.2 manual | — | — | Object constraints (Copy Location/Rotation/Transforms, Limit Location/Rotation, Transformation, Child Of) and Drivers (scripted expressions; rotations in radians) animate gantry axes, arm joints and gripper strokes from a few driver variables; keyframe from MuJoCo joint trajectories via bpy | [48], [49] |
| Headless rendering | Blender 5.2 manual | — | — | `blender -b file.blend -E CYCLES -s 10 -e 500 -t 2 -a`; `-f N` for one frame; EEVEE for fast turntables, Cycles for final stills | [50] |
| R3 import of `.blend` | R3 MCP docs (BLENDER_ASSETS.md, HOWTO_BLENDER_LINK.md) | R3 platform | connector active in this project | R3 imports meshes and Empties only (one R3 Mesh per Blender object, origins, parenting, first UV map, packed images, Principled Base Color/Metallic/Roughness/Alpha/Emission/Normal strength; modifiers applied on upload). Not imported: lights, cameras, curves, armatures, animation, particles, mapping nodes, procedural textures, second UV map. Rules: one object per moving part with the origin on its axis, do not apply transforms, pack images, parent to objects not bones. Upload via `r3_blender_upload`, then `r3_blender_import`, frame the camera, `r3_preview_create` (7-day links) | [51] |

Consequence for the walkthrough: motion in R3 is driven by R3 Code components writing `mesh.rotation`/`position`, not by Blender animation, so the Blender file is a static, well-parented asset and the motion script is written against R3's entityRefs.

### F6. Electrical and pneumatic drawing tools, drawing standards

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| KiCad | 10.0.0 (2026-03-20 announcement); 10.0.6 bug-fix 2026-08-29 | GPL-3.0 | 7,609 commits in the 10 cycle; STEP now shipped only for official 3D libraries | Custom PCBs (sensor breakouts, EOAT boards) and their STEP for the 3D model. Not an IEC cabinet-schematic tool | [59], [60] |
| QElectroTech | 0.100 (January 2026) | GPL | >8,000 symbols; Windows/macOS/Linux | Cabinet and I/O schematics for ST09 (electrical, also pneumatic/hydraulic symbol sets); free alternative to EPLAN | [61] |
| EPLAN Electric P8 | yearly platform versions | proprietary, subscription 12–36 months, single or concurrent | industry reference; most PLC/safety/pneumatic vendors publish EPLAN macros (Siemens CAx, Pilz, Schmalz, SMC, SCHUNK) | Price not published; request quote (third-party sites quote on request only). Use only if an integrator or the owner's electrical contractor requires EPLAN deliverables | [62], [101], [104], [91], [66], [93] |
| Festo FluidDraw | P7 (update 7.1.1, 2026-07-13); FluidDraw 365 annual network subscription (auto-renewing, cancellable) | proprietary | Festo/Art Systems | Pneumatic/hydraulic/electrical schematics with ISO 1219-1 and DIN EN 60617 symbol libraries, DIN EN 81346-2 equipment tags, GRAFCET, Festo catalogue, valve-terminal circuit generation, BOMs. Price shown only after login to Festo App World: request | [63], [64] |
| SMC PneuDraw (online) | current | free | SMC | Draws pneumatic circuits with symbols linked to SMC parts, auto parts list; export DXF/SVG/PDF, list to CSV/XLS; SMC also offers DXF symbol library, EPLAN library and STEP AP214 3D libraries | [65], [66] |
| ISO 128 series | 128-1:2020 (confirmed 2026), 128-2:2022, 128-3:2022, 128-100:2020; ISO 129-1:2018 (+Amd 1:2020) for dimensioning | ISO | — | ISO 128-1 is CHF 44 (iso.org, 2026-10-21, list). General tolerances: ISO 2768-1:1989 (m class is the default most online shops apply) | [67], [68], [70] |
| ASME Y14.5-2018 (R2024) | reaffirmed 2024 | ASME | — | $380 PDF or print (asme.org, 2026-10-21, list); use when US shops or US partners read the drawings; otherwise ISO 1101/ISO 128 | [69] |

### F7. Vendor geometry sources (per vendor family named in R01–R08)

Legend for "Licence/terms": V = vendor's own terms; P = portal terms (CADENAS/TraceParts/GrabCAD); U = not stated on the page (unverified).

| Vendor family (brief) | Vendor | Where to get geometry | Format | Login? | Licence / reuse terms | Source URL |
|---|---|---|---|---|---|---|
| Cutters (R01) | Zünd G3/S3 | No CAD download found; dimensional sheets only (e.g. G3 L-3200 working area 3200×1800 mm, overall 4480×3610 mm incl. workstation, 1290 kg; G3 sizes M/L/XL/2XL/3XL; S3 M/L/XL) | PDF dims | — | request STEP from Zünd at quotation (U) | [120] |
| Cutters (R01) | Lectra Virga, Gerber Z1, Eastman, Bullmer, iECHO | No public CAD found (3 searches) | — | — | request from vendor or model an envelope from datasheets (U) | [120] |
| Cobots (R02) | Universal Robots UR5e/UR7e, UR10e/UR12e, UR20 | support site "Robot Step file" pages (updated 2025-10-28); drilling-template STEP for base flanges | STEP (zip) | yes | V: UR Graphical Documentation T&Cs: may be made public only inside a downloadable software package that includes the T&Cs (the ROS description does this); ROS 2 description code is BSD-3-Clause | [82], [83] |
| Cobots (R02) | FANUC CRX | ROS-Industrial `fanuc_crx10ia_support` (community, Apache-2.0/BSD-3); official FANUC CAD portal not confirmed | URDF+meshes | GitHub | ROS-I licences; OEM STEP unverified (U) | [86] |
| Cobots (R02) | ABB GoFa CRB 15000 | ABB Robotics One product family page "View Variants & CAD Files"; ABB Library datasheets | CAD per variant | ABB account likely | V (ABB terms on download page, not extracted) | [84] |
| Cobots (R02) | KUKA LBR iisy | my.kuka.com product pages: STEP, Parasolid, NX, 2D DXF per variant plus energy-supply CAD, DELMIA/Process Simulate data | STEP etc. | yes | V (KUKA download terms, not extracted) | [85] |
| Cobots (R02) | Doosan | `doosan-robot2` ROS 2 (Humble) with descriptions | URDF+meshes | GitHub | BSD-3-Clause per GitHub (README badge says Apache-2.0: check LICENSE before redistribution) | [87] |
| Cobots (R02) | Franka FR3, Kinova Gen3, Flexiv Rizon4S, KUKA iiwa14 | MuJoCo Menagerie | MJCF+OBJ | no | per-model (Apache-2.0 / BSD-3) | [31] |
| Gantries, linear motion (R02/R07) | Festo (EXCM, ELGA, EGC, ...) | festo.partcommunity.com (CADENAS) and Festo product configurator | STEP and 100+ formats | portal account | P: CADENAS terms (use limited to CAD/BIM design; AI training forbidden; redistribution not granted) | [95], [109] |
| | igus drylin, e-chains | igus.partcommunity.com, igus-cad.com; e-chain 3D models free without registration | STEP | no (e-chain) | P/V | [96] |
| | Bosch Rexroth linear motion and profiles | Linear Motion configurator with CAD download; CAD-files search by material number; FRAMEpro plug-in (Inventor/SolidWorks) for profiles; 3Dfindit | STEP | some files need login | P/V | [97], [99] |
| | HIWIN | CAD configurator for axes, guideways, ballscrews, servo motors | STEP | — | V | [98] |
| | THK, Rollon (17,243 models), Güdel (136), PBC Linear (250), item (168), HepcoMotion | TraceParts | STEP, native | TraceParts account | P: TraceParts general terms of use (consumer terms not extracted: read before redistribution, U) | [99], [110] |
| | 80/20 | 3Dfindit (CADENAS) profiles catalog; 80/20 site | STEP | — | P | [106] |
| | Misumi | product configurator → part number → CAD download (STEP/IGES/DXF) | STEP | yes | V (Misumi terms not extracted, U) | [107] |
| | Vention | MachineBuilder design export | STEP | free account | V | [56] |
| Tool changers, F/T (R02) | ATI | "3D CAD Models" section on ati-ia.com | STEP (per model) | — | V (U) | [90] |
| | Stäubli | Robotics download centre (register/login) | CAD | yes | V | [94] |
| | Robotiq (2F-85, Hand-E, EPick, FT 300-S) | robotiq.com/support knowledge base (CAD, manuals); official ROS 2 descriptions; Isaac Sim assets repo | STEP; URDF | support site | V; ROS packages BSD-3-Clause | [88] |
| | OnRobot VGC10 | product page "Step File" download | STEP | — | V (U) | [89] |
| Grippers (R03) | Schmalz SNG-V/-AP/-M, SNGi-AE | per-part "Live CAD-Model" with download in various formats; EPLAN macro for electric variants | STEP etc. | yes ("Login for CAD Download") | V | [91] |
| | Zimmer Group | product page "Download CAD data" | CAD | — | V (U) | [92] |
| | SCHUNK | schunk.com CAD/ECAD downloads (free, request or direct), EPLAN data portal; 3Dfindit catalogue | STEP | — | V/P | [93] |
| | Piab, FIPA, Coval, Sommer | not verified this round (one search; no primary page captured) | — | — | U | — |
| Sewing heads (R04) | Juki, Pegasus, Yamato, Brother, Jack, Siruba, Dürkopp Adler | No OEM STEP found; Juki publishes catalogues, instruction manuals and parts lists with dimensional drawings (e.g. DDL-8700L head 28 kg); GrabCAD has no verified model for Juki DDL (search returned product pages only) | PDF dims | — | Model the head as a measured envelope: buy the head first, then measure or 3D-scan; GrabCAD community models are non-commercial-use only under GrabCAD terms | [121], [111] |
| PLC, safety, cabinet (R05) | Beckhoff | TraceParts Beckhoff catalogue (CP29xx, CP69xx ...) and Beckhoff product pages | STEP, native | TraceParts account | P | [100] |
| | Siemens | CAx Download Manager via SiePortal (3D models, 2D drawings, EPLAN macros, connection diagrams); IPC data only in the image database | STEP, EPLAN | free account | V | [101] |
| | SICK | each datasheet points to www.sick.com/<part> for "CAD dimensional models" | STEP | — | V | [103] |
| | Rittal | product pages, PARTcommunity, iOS/Android app | multiCAD | — | P/V | [102] |
| | Pilz | product pages carry EPLAN P8 macros and software; 3D CAD not confirmed on the pages fetched | EPLAN | — | U for 3D | [104] |
| | Phoenix Contact | CAD files and 3D models downloadable after free registration | STEP | yes | V | [105] |
| | WAGO, Euchner, Schmersal, Keyence, Banner | not verified this round | — | — | U | — |
| Cameras, 3D, compute (R06) | Basler ace 2 | per-model page on docs.baslerweb.com: "Download the CAD/technical drawing" | STEP/drawing | — | V | [112] |
| | Teledyne FLIR Blackfly S | softwareservices.flir.com dimensions page: "BFS-PGE Standard/Large CAD Models"; Teledyne Vision Solutions downloads (login for software) | CAD | some | V | [113] |
| | IDS uEye | IDS download centre (CAD presence not confirmed) | — | — | U | [114] |
| | Zivid 2+ (M60/MR60/L110/LR110/M130/MR130), Zivid 3, mounts, calibration boards | zivid.com/downloads: `.step` and `.stl`, plus CAD FOV models | STEP, STL | no | U (no licence text on page) | [115] |
| | Photoneo PhoXi / MotionCam-3D | device-resources page, CAD per size (form before download); 2026 housings slightly wider than previous | CAD | form | U | [116] |
| | Intel RealSense (now RealSense Inc.) | dev.realsenseai.com/docs/cad-files | CAD | no | U | [117] |
| | Orbbec Gemini 335/335L/335Lg | orbbec.com docs "Download CAD Files (Gemini 330 Series)" | CAD | no | U | [118] |
| | NVIDIA Jetson | Jetson Download Center: STEP for Orin Nano dev kit, AGX Orin dev kit, Thor module | STEP | NVIDIA account | V | [119] |
| Extrusion and fasteners (R07) | McMaster-Carr | CAD for 700,000+ parts (STEP, SLDPRT, Parasolid), SolidWorks add-in, API | STEP | — | V: CAD models are provided only to decide whether to buy; no reproduction, redistribution or fabrication from them: cannot live in a public repo | [108] |
| | item | item Engineeringtool and TraceParts catalogue | STEP | — | P/V | [99] |
| Decoration, finishing (R08) | Tajima, Brother, Kornit, Epson, Veit, folding/bagging makers | not researched for CAD this round (out of scope for the first cell model) | — | — | U | — |

Portal terms that matter:
- CADENAS PARTcommunity/3Dfindit (Festo, igus, Rittal, SCHUNK, 80/20 catalogs): data may be used only for CAD and BIM designs; use for machine learning / generative AI training is expressly prohibited with a EUR 20,000 contractual penalty plus EUR 500 per file [109].
- McMaster-Carr: CAD models only for purchase decisions; no retention, redistribution or fabrication from them [108].
- GrabCAD community: content is owned by uploaders; the site licence is for non-commercial, internal use; older guidance says contributed content is non-commercial unless stated otherwise [111].
- Universal Robots: graphical documentation (STEP, DAE, STL, GLB, JT, EPLAN) may be published only inside a software package that includes UR's T&Cs [83].
- MuJoCo Menagerie: per-model LICENSE files; the UR5e/UR10e models are BSD-3-Clause, Robotiq 2F-85 BSD-2-Clause, so they can be redistributed with attribution [30], [31].
- TraceParts and 3DContentCentral consumer terms were not extracted (the fetched TraceParts page covered distributor contracts): unverified until read.

### F8. Fabrication vendors and EOAT printing (price and lead-time norms)

| Vendor | Model / part number | Key specs | Price (currency, date, list/quote/est.) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Xometry | CNC machining service | milled parts up to 2,032×1,219×610 mm; instant quotes from STEP/Parasolid/ACIS/mesh; standard inspection included | instant quote only | standard 3–7 business days; quick-turn 3–4 days; expedite available | accepts STEP | [71] |
| Protolabs | CNC machining (factory and Network) | factory max 559×356×95 mm; ±0.127 mm without drawing, ISO 2768-f with drawing; Network ISO 2768-f (metals) | quote (DFM feedback) | as fast as 1 day (factory); automated milling "as fast as 4 days" | accepts STEP | [72] |
| Fictiv | CNC machining | no minimum order; ISO 2768-m without drawing; ±0.0025 mm with drawing on metals; aluminium mill lead "as fast as 3 days", steel/stainless 7 days | quote | as fast as 1 day | accepts STEP | [73] |
| JLCCNC | CNC milling/turning; sheet metal | ±0.05 mm CNC, ±0.2 mm sheet; 3-/4-/5-axis | CNC "from $5", sheet metal "from $0.40" (USD, jlccnc.com, 2026-10-21, list); quotes >20 pcs go to manual review; +1 day factory transfer; price adjustment notice 2026-05-08 | CNC build time 3 days; sheet metal 2 days (plus shipping from China) | accepts STEP | [74], [75] |
| PCBWay | CNC milling | 3- and 5-axis | instant quote | "as fast as 2 days"; typical from 5 days | accepts STEP | [76] |
| SendCutSend | laser cut, bend, CNC route, tapping, hardware, powder coat | 175+ materials; bending up to 30"×44" (762×1,118 mm), bend-to-edge ±0.015"; examples: 5052 Al 0.187" 3.6×2.5" $9.41 ea (qty 1), $3.20 (qty 100); 0.063" Al laser+anodize+bend+tap 4×4.8" $38.49 (qty 1) | USD, sendcutsend.com, 2026-10-21, list examples | ships in as little as 24 h; bending adds 1–2 days; 100+ parts +2–4 days | accepts DXF/STEP; templates | [77], [78] |
| Bambu Lab | H2D (dual nozzle) | 350×320×320 mm (single material 325×320×325 nominal), heated chamber, AMS 2 Pro, optional 10/40 W laser | $1,849 (typical $2,099) USD, Bambu US store, 2026-10-21, list; EU from €1,549 | in stock (store) | none needed | [79] |
| Bambu Lab | H2S | 340×320×340 mm build; PMSM servo extruder; up to 1,000 mm/s | $1,399 (typical $1,499) USD, Bambu US store, 2026-10-21, list | in stock | — | [80] |
| Prusa | CORE One+ (Gen 2); MK4S | enclosed CoreXY (CORE One); MK4S bedslinger | CORE One+ "from $1,299", MK4S "from $999" (prusa3d.com listing fetched via AU locale; currency ambiguous: verify on the US store) | — | — | [81] |

Norms to plan with (from the rows above): quick-turn CNC in 1–4 days costs a premium; standard CNC 3–7 business days (US) or 3 days + shipping (JLCCNC); laser/bent sheet 1–4 days (SendCutSend); 3D-printed EOAT bodies in hours on a CF-capable printer (H2D/H2S heated chamber for ASA/CF-nylon).

## Recommendation for this project

### R-1. Pinned toolchain (one Python 3.13 environment for CAD + sim + Blender scripting; separate env for AGPL drawing tools)

Selected (versions verified 2026-10-21; install commands from the official docs [1], [3], [5], [17], [30], [35], [41], [122]):

```bash
python3.13 -m venv ~/.venvs/cad && source ~/.venvs/cad/bin/activate
python -m pip install --upgrade pip
pip install build123d==0.13.0 ocp-vscode==4.2.0            # pulls cadquery-ocp-novtk 8.0.1.x automatically [1][2][4]
pip install trimesh==5.1.1 yourdfpy==0.0.60 robot_descriptions==3.3.0
pip install mujoco mujoco-menagerie==2026.9.4 obj2mjcf==0.0.25   # mujoco: GitHub release 3.15.0 (2026-10-05); pin after `pip show mujoco` [29]
pip install bpy==5.2.2                                      # Blender as a module; requires Python 3.13 exactly; ~370 MB wheel [41]
# separate environment for drawings (AGPL-3.0), exchange STEP files between the two [122]
python3.13 -m venv ~/.venvs/draw && ~/.venvs/draw/bin/pip install draftwright build123d-drafting-helpers
# only if Onshape is adopted (Standard plan, commercial use) [13][17]
pip install onshape-to-robot==1.8.3
```

Desktop applications: Blender 5.2 LTS (5.2.2) with the "STEP Importer" extension 1.2.1 for ad-hoc vendor STEP [39], [42]; FreeCAD 1.1.4 as the free GUI viewer/TechDraw fallback (do not adopt the 26.3 RC) [10]; KiCad 10.0.6 for PCBs [59]; QElectroTech 0.100 for cabinet schematics [61]; SMC PneuDraw (free, online) for pneumatic circuits, upgrading to Festo FluidDraw 365 if the valve-terminal circuit generation and Festo BOM integration are wanted [65], [63]; Isaac Sim 6.2 only on a machine with an RTX 4080-class or better GPU [24]; RoboDK Professional ($3,995 + $1,500/yr) only when OEM-accurate cycle times with FANUC/UR controller models are needed for the sales case [52].

Alternates: CadQuery 2.8.0 if a constraint solver for assemblies becomes necessary (build123d joints are positional, not solved) [6], [8]; Onshape Standard ($1,500/user/yr) + onshape-to-robot for anyone who wants a GUI and a turnkey URDF/MJCF exporter [13], [16]; STEPper Reborn/NEXT as alternative Blender STEP importers [43], [44].

Risk: build123d is 0.x and releases monthly-ish (0.10 → 0.13 between Nov 2025 and Sep 2026 [1]); pin exact versions in `pyproject.toml`, keep a lock file, and upgrade deliberately. bpy and cadquery-ocp both pin NumPy-era binaries; test them in one env (open question Q-1) and fall back to two envs if they conflict.

### R-2. Master-model and export policy (confirms decision D-004)

- Each assembly `A00`–`A10` is a build123d module whose top-level `Compound` carries labels, colours and `Joint` objects; `export_step` writes the STEP (labels become product names) and `export_gltf` writes the GLB for Blender/web [7]. This is exactly what the spine already requires [125].
- The joints file per assembly (joint label, type, axis, limits, parent/child link labels, mass properties from `Shape.volume`/`center`) is the single source for a small in-house URDF emitter (no library exists; see F3). MuJoCo converts URDF→MJCF (`MjSpec.from_file` on the URDF with the `<mujoco><compiler meshdir discardvisual="false"/></mujoco>` extension, then `spec.encode("Ann.xml")`) [33]; Isaac Sim imports the same URDF when needed [25].
- Purchased arms and grippers are not re-modelled: UR5e/UR10e and Robotiq 2F-85 come from Menagerie (BSD licences) and are attached to the station MJCF with `MjSpec.attach` at a named site [30], [31]; FANUC/Doosan/ABB/KUKA arms, if chosen by R02, are converted from their ROS descriptions with the Menagerie recipe [32], [86], [87].
- Vendor STEP lives in `cad/vendor/<part_id>/` in a private store (not the public repo) with a `LICENSE.txt` per part and a register of source, date and terms, because McMaster-Carr and CADENAS-hosted files cannot be redistributed and UR files only inside a package that carries UR's T&Cs [108], [109], [83]. Standard fasteners come from bd_warehouse instead of McMaster CAD [124].

### R-3. Format conversion matrix (selected routes; all tools verified in Findings)

| From → To | Tool and call | Notes |
|---|---|---|
| build123d → STEP (AP214, colours, labels) | `export_step(assembly, "A04.step")` | per-product names from labels [7] |
| build123d → GLB | `export_gltf(assembly, "A04.glb")` | PBR materials carried [7] |
| build123d → STL / 3MF | `export_stl`, `Mesher().write("x.3mf")` | 3MF keeps part numbers and metadata [7] |
| build123d → DXF/SVG/PDF drawings | Draftwright `make_drawing(part, out=..., title=..., number=...)`; helpers `make-drawing part.step --tolerance "ISO 2768-f"` | AGPL env; lint checks ISO coverage [122], [123] |
| Vendor STEP → build123d | `import_step("ur5e.step")` | read-only XDE tree with labels, colours, instance locations [7] |
| Vendor STEP → Blender | STEP Importer 1.2.1 (Cascadio → glTF → Blender) or STEPper Reborn 2.3.0 | or go via build123d → GLB → built-in glTF importer [42], [43], [45] |
| GLB → Blender | File ▸ Import ▸ glTF 2.0 (built in) | hierarchy, materials, extras preserved [45] |
| Blender → R3 | save `.blend` with packed images → `r3_blender_upload` → `r3_blender_import` | meshes and Empties only; motion scripted in R3 [51] |
| Blender → images/video | `blender -b scene.blend -E CYCLES -s 1 -e 240 -a` (or `-E BLENDER_EEVEE_NEXT`) | headless on the build server [50] |
| Onshape assembly → URDF/SDF/MJCF | `onshape-to-robot my-robot` with `config.json {"url":..., "output_format":"urdf"}` | needs API keys and a commercial Onshape plan [17], [13] |
| URDF → MJCF | `mujoco.MjSpec.from_file("robot.urdf")` + `spec.encode("robot.xml")`; `.mjz` bundles meshes | OBJ meshes via obj2mjcf; URDF attributes not schema-checked [33], [34] |
| URDF / MJCF / Onshape / STEP → USD | Isaac Sim URDF importer (`urdf_import.py --urdf ... --merge-mesh`), MJCF importer, Onshape importer, CAD Converter (STEP/IGES/JT/Parasolid/SLDPRT/IPT/PRT/CATPart/STL/OBJ/FBX/GLB/3MF/DWG) | RTX GPU required [25], [26], [27], [28] |
| USD → URDF | Isaac Sim USD-to-URDF exporter (validates joint limits since 6.2) | round-trip check only [23] |
| Mesh simplification / collision hulls | trimesh (`convex_hull`, mass properties), obj2mjcf `--decompose` (CoACD), Blender Decimate via bpy | visuals from GLB, collisions from decimated/convex meshes [37], [34], [41] |
| Open robot descriptions → sim | `robot_descriptions.loaders.mujoco.load_robot_description("ur5e_mj_description")` | quick reach studies before our own assemblies exist [35] |

### R-4. End-to-end workflow with checkpoints

| Checkpoint | Deliverable | Pass criterion |
|---|---|---|
| C0 Toolchain pinned | `pyproject.toml` + lock; smoke test exporting STEP/GLB/STL from a box | done 2026-10-21 for build123d 0.13.0 on Python 3.13 (TOOLING.md); extend to bpy/mujoco |
| C1 Vendor geometry register | `cad/vendor/<part_id>/` (private) with LICENSE and source register for every bought part in R01–R08 | every part_id has STEP or an "envelope model + reason" entry; no McMaster/GrabCAD files in the public repo |
| C2 Station envelopes | A00 frame + A01–A10 envelopes from datasheet dimensions (Zünd G3 footprint, head masses, cabinet) | floor plan with clearances; interference check by OCCT boolean on the whole cell < 1 s per pair |
| C3 Kinematic assemblies | joints file per `Ann`; URDF emitted; MJCF compiled; UR/Robotiq attached from Menagerie | `mj_forward` runs; reach map of A04 covers the 3 m × 1.5 m envelope at the required poses (R02 architecture) |
| C4 Cycle-time model | MuJoCo joint-space trajectories with vendor velocity/acceleration limits; scheduler replay against the takt registry | nominal takt ≤ 7.2 min/garment (100 per 12 h) with stated margins; RoboDK cross-check if the sales case needs OEM controller timing |
| C5 Visual twin | GLB → Blender 5.2 scene with constraints/drivers; EEVEE turntables; Cycles stills; `.blend` → R3 preview link | R3 import log clean (no `textured=0`, no origin collapse); walkthrough scripted in R3 |
| C6 Fabrication package | Draftwright drawings (ISO 128, ISO 2768-m default), DXF for SendCutSend, STEP for CNC quotes (Xometry/Protolabs/Fictiv/JLCCNC/PCBWay), EOAT prints | at least two instant quotes per custom part with lead time recorded |
| C7 Electrical and pneumatic | QElectroTech schematics for ST09 (IEC 60617 symbols); PneuDraw/FluidDraw pneumatic sheets (ISO 1219-1); EPLAN export only if an integrator demands it | every I/O point in the spine interface registry appears on a sheet |
| C8 Optional perception twin | Isaac Sim 6.2 import of the USD cell for camera placement and synthetic data | only after hardware with RTX 4080+ is available |

### R-5. Honest limits: what the model proves and does not

Proves (with the tools above): geometric fit and clearances; reach and joint-limit feasibility of arms and gantry; nominal cycle time from kinematic limits; sensor fields of view; interface locations for cables, air and mounting; drawing-level manufacturability of custom parts.

Does not prove: knit behaviour on the vacuum bed, ply pick-up and double-pick rates, edge curl, seam quality, thread faults, vacuum leakage, static, or operator ergonomics. Blender cloth is an uncalibrated visual model [46]; MuJoCo/MJWarp advertise cloth and soft bodies [128] but no validated knit parameters exist here; Isaac Sim adds rendering realism, not textile truth. Safety compliance (PL d) is proven by the safety design and validation, not by the model. This matches the white paper: simulation "can help explore reach, scheduling and candidate policies, but real textile response and seam quality require physical testing" (white paper lines 788–789) and "It cannot certify real-cloth behavior solely from geometric simulation" (line 1172).

## Integration notes

- Repository layout (consistent with the spine [125]): `model/Ann.py` per assembly; `model/joints/Ann.json`; `cad/vendor/<part_id>/` private; `exports/{step,glb,urdf,mjcf,usd}/` generated, never hand-edited; `drawings/` from the AGPL env; `blender/` scenes; `r3/` scripts. CI job: build all `Ann` modules, export, run `yourdfpy` validation and `mujoco` compile, fail on interference.
- Units and frames: build123d works in mm (`Unit.MM` default in `export_step` [7]); URDF/MJCF/USD/Blender/R3 expect metres: scale 0.001 at mesh export and keep Z-up (glTF is +Y up; Blender's exporter handles the convention [45]). Record the cell origin at ST00's reference corner and reuse it in every export.
- Mechanical: vendor STEP files for UR arms include the base flange drilling template STEP [82]; Zünd and sewing heads are envelope models until STEP or measurements exist (F7). Decimate vendor meshes to visual (≤ 50 k triangles per arm) and convex collision sets (obj2mjcf/CoACD [34]).
- Electrical/data interfaces into the model: every I/O point in the spine interface registry gets a named `Location` in build123d (connector positions) so cable lengths and energy-chain routes (igus CAD [96]) can be measured from the model; electrical sheets in QElectroTech reference the same IDs.
- Pneumatic: FluidDraw/PneuDraw sheets list SMC/Festo part numbers whose STEP files come from SMC's STEP AP214 libraries and Festo PARTcommunity [66], [95]; valve-terminal circuits can be auto-generated in FluidDraw [63].
- Software: the joints file is also the hand-off to M09 (motion control/hardware abstraction) and M13 (digital twin); the MJCF is the simulation backend for M08 skill tests; Isaac Sim USD feeds M11 synthetic data when an RTX workstation exists.
- Licences in distributed demos: ship only Menagerie/ROS-licensed robot meshes and our own geometry in public artefacts (R3 previews, GLB downloads); keep McMaster, CADENAS-portal and GrabCAD content out [108], [109], [111].
- Drivers and plug-ins: VS Code + OCP CAD Viewer (ocp-vscode 4.2.0) for modelling [5]; Blender extensions installed from extensions.blender.org (STEP Importer, glTF built-in) [42], [45]; R3 connector already active in this project (TOOLING.md) for `r3_blender_upload`/`r3_blender_import` [51].

## Conflicts with the white paper

None found. The white paper states that its schematics "are not dimensioned fabrication drawings, collision-checked layouts, licensed supplier designs or images of working hardware" (lines 258–261), that simulation supports geometric checks, policy exploration and scheduling "with a measured gap to real materials" (lines 1251–1252), and that the final engineering record must include mechanical CAD, wiring and a supplier-backed parts list (lines 2389–2391). The pipeline above produces exactly those artefacts and claims no more than the white paper allows. One nuance rather than a conflict: the white paper does not name any CAD system, so the code-CAD choice (D-004) is a project decision, not a white-paper requirement.

## Open questions and unknowns

| # | Unknown | Cheapest way to confirm |
|---|---|---|
| Q-1 | Whether bpy 5.2.2, mujoco 3.15 and build123d 0.13 coexist in one Python 3.13 venv (NumPy/ABI conflicts) | `pip install` all three in a fresh venv and import each (10 min); fall back to two envs |
| Q-2 | Open3D wheels for Python 3.13 on PyPI (0.19.0 stops at 3.12; open3d.org lists 0.20.0 for 3.13/3.14) | `pip install open3d` in the 3.13 env; else download the 0.20.0 wheel from open3d.org, or drop Open3D |
| Q-3 | Zünd G3/S3 STEP availability and NDA terms; Lectra/Eastman/Bullmer/iECHO CAD | ask at quotation (R01 owner); meanwhile model envelopes from the technical-data PDFs |
| Q-4 | OEM STEP for sewing heads (Juki, Pegasus, Yamato, Brother, Jack, Dürkopp Adler) | email two distributors; if none, buy the chosen head first and measure/scan it; model table cut-outs from the instruction manuals |
| Q-5 | FANUC CRX official CAD portal and terms; ABB, KUKA, Doosan download terms text | create vendor accounts and read the download terms (30 min); ROS descriptions cover simulation meanwhile |
| Q-6 | TraceParts, 3DContentCentral and Misumi consumer terms on redistribution of downloaded CAD | read the terms pages (20 min) before any vendor file enters a shared artefact |
| Q-7 | Pilz, WAGO, Euchner, Schmersal, Keyence, Banner, Piab, FIPA, Coval, Sommer, IDS 3D CAD availability | one product page each (1 h total) when R05/R03/R06 selections are fixed |
| Q-8 | STEP Importer / STEPper performance on 100 MB+ robot STEP in Blender 5.2 (user reports of regressions) | import one UR STEP (5 min); if slow, go via build123d → GLB |
| Q-9 | RoboDK cycle-time fidelity versus real UR/FANUC controllers | compare RoboDK time with URSim (free) for one pick-place cycle before buying the $3,995 licence |
| Q-10 | FluidDraw 365 price, Visual Components and EPLAN prices | FluidDraw: login to Festo App World; others: request quotes (both optional) |
| Q-11 | MuJoCo/MJWarp cloth or flex suitability for cotton jersey | not a modelling question; schedule a physical ply-handling test per the white paper; treat any cloth sim as visual only |
| Q-12 | Prusa CORE One+ price currency on the fetched page | open prusa3d.com with the US locale (2 min) |
| Q-13 | Isaac Sim hardware: does the owner's workstation meet RTX 4080 / 16 GB VRAM / 32 GB RAM | run the Isaac Sim Compatibility Checker [24] |

## Sources

1. https://pypi.org/project/build123d — build123d 0.13.0 (2026-09-21), Apache-2.0, `pip install build123d`, release history.
2. https://github.com/gumyr/build123d/releases — switch to `cadquery-ocp-novtk` 7.9 at 0.11.0.
3. https://build123d.readthedocs.io/en/v0.13.0/_sources/installation.rst.txt — official install commands (pip, git, poetry, OCP stubs).
4. https://pypi.org/project/cadquery-ocp/ — cadquery-ocp 8.0.1.1.0 (2026-10-05), Python >=3.11,<3.15, cp311–cp314 wheels.
5. https://pypi.org/project/ocp-vscode/4.2.0/ — OCP CAD Viewer 4.2.0 (2026-10-13), Python >=3.10, Library Manager.
6. https://pypi.org/project/cadquery/ — CadQuery 2.8.0 (2026-06-21), conda install.
7. https://github.com/gumyr/build123d/blob/dev/docs/joints.rst , https://github.com/gumyr/build123d/blob/dev/docs/assemblies.rst , https://github.com/gumyr/build123d/blob/dev/docs/import_export.rst , https://github.com/gumyr/build123d/blob/dev/docs/tutorial_materials.rst , https://github.com/gumyr/build123d/blob/dev/src/build123d/exporters3d.py , https://github.com/gumyr/build123d/blob/dev/src/build123d/importers.py (read through Context7 `/gumyr/build123d`) — joints, assemblies, `export_step` signature, `export_gltf`, Mesher, `import_step` assembly recursion, 52 MB STEP example.
8. https://cadquery.readthedocs.io/en/latest/importexport.html and https://github.com/CadQuery/cadquery/blob/master/doc/importexport.rst — CadQuery import/export formats (STEP, XBF, XCAF, glTF), `Assembly.importStep`.
9. https://wiki.freecad.org/Release_notes_1.1 — FreeCAD 1.1 released 2026-03-24; Assembly Simulation and BOM features.
10. https://blog.freecad.org/ — FreeCAD 1.1.4 (2026-09-28) and 26.3 RC1 (2026-10-08) announcements.
11. https://github.com/freecad/freecad/releases — 26.3 RC1, CalVer, three releases per year.
12. https://wiki.freecad.org/Assembly_Workbench — Assembly workbench tools (Ondsel solver, joints, exploded view, BOM, simulation).
13. https://onshape.com/en/pricing — Free $0 (non-commercial, public documents), Standard $1,500/user/yr, Professional $2,500/user/yr.
14. https://www.onshape.com/en/legal/terms-of-use — Free Plan documents are public; licence granted on public documents.
15. https://www.onshape.com/en/blog/get-started-featurescript-mcp-server — FeatureScript MCP Server (Onshape Labs, App Store), 2026-09-03.
16. https://pypi.org/project/onshape-to-robot/1.0.0/ — onshape-to-robot release history (1.8.3 on 2026-08-26), MIT.
17. https://onshape-to-robot.readthedocs.io/en/latest/getting_started.html — install, API keys, `config.json`, export and test commands.
18. https://www.autodesk.com/products/fusion-360/personal — Fusion for personal use terms; $680/yr commercial.
19. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Fusion-360-Free-License-Changes.html — 10 active editable documents limit.
20. https://www.autodesk.com/products/fusion-360/blog/fusion-subscription-types/ — Fusion plans; Fusion for Startups ~$150 for 3 years.
21. https://www.solidworks.com/solution/solidworks-makers — SolidWorks for Makers $48/yr, < $2,000 revenue.
22. https://ohmycad.com/en/official-3dexperience-solidworks-price-list/ — 3DEXPERIENCE SOLIDWORKS 2026 price list (US Standard $2,820/yr), reseller, Oct 2026.
23. https://docs.isaacsim.omniverse.nvidia.com/latest/overview/release_notes.html — Isaac Sim 6.2.0 release notes (importers in `isaacsim-asset` wheel, MuJoCo 3.12.0, URDF exporter).
24. https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html — system requirements (RTX 4080 minimum, 32 GB RAM, driver 595).
25. https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/import_urdf.html — URDF import tutorial and CLI arguments.
26. https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/importers_exporters.html — importer list (URDF, MJCF, Onshape, CAD Converter).
27. https://docs.omniverse.nvidia.com/extensions/latest/ext_onshape.html — Onshape importer (assemblies only, tessellation tolerances, API key authentication).
28. https://docs.omniverse.nvidia.com/extensions/latest/ext_cad-converter/manual.html — CAD Converter supported formats.
29. https://github.com/google-deepmind/mujoco/releases — MuJoCo 3.15.0 (2026-10-05).
30. https://pypi.org/project/mujoco-menagerie — mujoco-menagerie 2026.9.4 (2026-09-28), API, per-model licences.
31. https://github.com/google-deepmind/mujoco_menagerie — model table with licences (UR5e, UR10e, iiwa14, FR3, Rizon4S, Gen3, Robotiq 2F-85).
32. https://github.com/google-deepmind/mujoco_menagerie/blob/main/universal_robots_ur5e/README.md — URDF→MJCF derivation steps, BSD-3-Clause.
33. https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst and https://github.com/google-deepmind/mujoco/blob/main/doc/python.rst (via Context7 `/google-deepmind/mujoco`) — URDF extensions, meshdir, no schema check, `MjSpec` load/encode.
34. https://pypi.org/project/obj2mjcf/ and https://github.com/kevinzakka/obj2mjcf — obj2mjcf 0.0.25, MIT, CoACD decomposition.
35. https://pypi.org/project/robot_descriptions/ — robot_descriptions 3.3.0 (2026-10-12), Apache-2.0, loaders.
36. https://pypi.org/project/yourdfpy/ — yourdfpy 0.0.60 (2026-01-23), MIT.
37. https://pypi.org/project/trimesh and https://deps.dev/pypi/trimesh — trimesh 5.1.1 (2026-10-02), MIT, ~4 k stars.
38. https://pypi.org/project/open3d/ and https://www.open3d.org/ — open3d 0.19.0 on PyPI (2025-01-08, Python 3.8–3.12); 0.20.0 downloads with Python 3.10–3.14.
39. https://www.blender.org/download/releases/5-2/ — Blender 5.2 LTS released 2026-07-14, supported to July 2028.
40. https://www.blender.org/download/lts/ — current LTS: 5.2.2 and 4.5.14 (2026-09-15).
41. https://pypi.org/project/bpy — bpy 5.2.2 (Python ==3.13.*), bpy 4.5.14 (Python 3.11), GPL-3.0.
42. https://extensions.blender.org/add-ons/step-importer/ — STEP Importer 1.2.1 (Cascadio → glTF), Blender 5.1+, GPL-3.0.
43. https://extensions.blender.org/add-ons/stepper-reborn — STEPper Reborn 2.3.0, limitations, user report on large files.
44. https://github.com/RomainGuimbal/STEPper_nextborn — STEPper NEXT (pythonocc-core 7.9.3 / Python 3.13, Blender 5.1).
45. https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html — glTF 2.0 importer/exporter (built in).
46. https://docs.blender.org/manual/en/latest/physics/cloth/settings/physical_properties.html — cloth physical properties.
47. https://docs.blender.org/manual/en/latest/physics/cloth/settings/index.html — cloth quality steps, speed multiplier.
48. https://docs.blender.org/manual/en/latest/animation/constraints/index.html — object constraints list.
49. https://docs.blender.org/manual/en/latest/animation/drivers/index.html — drivers.
50. https://docs.blender.org/manual/en/latest/advanced/command_line/render.html — headless rendering flags.
51. R3 MCP server documents `BLENDER_ASSETS.md` and `HOWTO_BLENDER_LINK.md` (read with `r3_docs_read`; server https://mcp.r3js.org/mcp) — what the `.blend` importer supports, model-prep checklist, upload/import/preview tools.
52. https://robodk.com/pricing — RoboDK Professional $3,995, maintenance $1,500/yr, trial limits, Educational $145.
53. https://robodk.com/doc/en/PythonAPI/index.html and https://robodk.com/doc/en/PythonAPI/intro.html — Python API modules and "Estimated cycle time" example.
54. https://www.visualcomponents.com/blog/visual-components-5-0-the-fastest-way-from-concept-to-reality — Visual Components 5.0 (2026-03-12).
55. https://www.capterra.com/p/188853/Visual-Components — Visual Components editions; pricing "contact vendor" (third-party listing).
56. https://docs.vention.io/ — "Designs can be exported as STEP files from Vention via the MachineBuilder or the design summary page".
57. https://vention.com/machine-builder — 3,000+ components, CAD import/export, real-time BOM and price.
58. https://docs.vention.io/docs/parts-library-discovery — Parts Library categories (My Models imported CAD not quoted).
59. https://www.kicad.org/blog/2026/03/Version-10.0.0-Released and https://www.kicad.org/blog/2026/08/KiCad-10.0.6-Release — KiCad 10.0.0 and 10.0.6.
60. https://www.elektormagazine.com/news/kicad-10-release — KiCad 10 feature summary; STEP shipped for official 3D libraries (secondary source).
61. https://www.qelectrotech.org/ and https://qelectrotech.org/index.php.fr — QElectroTech 0.100 (January 2026), GPL, 8,000+ symbols.
62. https://www.eplan.com/us-en/products/eplan-electric-p8/ — EPLAN Electric P8 subscription terms (12–36 months), fluid power module.
63. https://www.festo.com/appworld/fluiddraw-p6.html — FluidDraw 365 licensing (network licences, yearly, login for prices), symbol libraries.
64. https://www.art-systems.de/www/site/en/fluiddraw — FluidDraw P7, update 7.1.1 (2026-07-13).
65. https://www.smc.eu/en-ie/products/engineering-tools/pneumatic_circuits_drawing — SMC PneuDraw (online), exports DXF/SVG/PDF, parts list.
66. https://www.smc.eu/en-gb/products/engineering-tools — SMC pneumatic symbols (DXF), EPLAN library, 3D product libraries (STEP AP214).
67. https://www.iso.org/standard/65296.html — ISO 128-1:2020, CHF 44, confirmed 2026.
68. https://www.iso.org/committee/45986/x/catalogue/p/0/u/1/w/0/d/0 — ISO/TC 10 catalogue (ISO 128-2:2022, 128-3:2022, 128-100:2020, 129-1:2018).
69. https://www.asme.org/codes-standards/find-codes-standards/dimensioning-and-tolerancing — ASME Y14.5-2018 (R2024), $380.
70. https://www.iso.org/obp/ui#!iso:std:7748:en — ISO 2768-1:1989 general tolerances.
71. https://www.xometry.com/capabilities/cnc-machining-service/ — Xometry CNC lead times (3–7 business days), max part size.
72. https://www.protolabs.com/services/cnc-machining/ — Protolabs CNC: as fast as 1 day, factory vs network tolerances and sizes.
73. https://www.fictiv.com/capabilities/cnc-machining-services — Fictiv CNC: as fast as 1 day, tolerances, per-material lead times, no MOQ.
74. https://jlccnc.com/ — JLCCNC prices "from $5" CNC / "from $0.40" sheet metal, build times, tolerances.
75. https://jlccnc.com/help/article/cnc-machining-ordering-guidelines — manual review above 20 pcs, lead-time rules.
76. https://www.pcbway.com/rapid-prototyping/CNC-machining/CNC-Milling.html — PCBWay CNC as fast as 2 days.
77. https://sendcutsend.com/ — SendCutSend 24 h shipping claim, example prices.
78. https://sendcutsend.com/services/cnc-bending/ — bending lead time, sizes, tolerances, example prices.
79. https://us.store.bambulab.com/products/h2d and https://eu.store.bambulab.com/products/h2d — Bambu Lab H2D price and specs.
80. https://us.store.bambulab.com/products/h2s — Bambu Lab H2S price and build volume.
81. https://www.prusa3d.com/product/prusa-core-one — Prusa CORE One+ and MK4S listed prices (locale AU; currency to verify).
82. https://www.universal-robots.com/download/mechanical-e-series/ur5eur7e/robot-step-file-ur5eur7e-e-series/ , https://www.universal-robots.com/download/mechanical-e-series/ur10eur12e/robot-step-file-ur10eur12e-e-series , https://www.universal-robots.com/download/mechanical-ur-series/ur20/robot-step-file-ur20 , https://www.universal-robots.com/developer/hardware-and-motion/cad-files-robot-models — UR STEP downloads (login) and drilling templates.
83. https://github.com/UniversalRobots/Universal_Robots_ROS2_Description and https://github.com/UniversalRobots/Universal_Robots_ROS2_Description/blob/22f055da2fa7e2158254426107d1f257fd56aebb/meshes/ur20/LICENSE.txt — BSD-3-Clause code; UR graphical documentation T&Cs for meshes.
84. https://one.robotics.abb.com/en/robots/p/GoFa-CRB-15000 — ABB GoFa family page with "View Variants & CAD Files" and downloads.
85. https://my.kuka.com/s/product/lbr-iisy-15-r930/01t1i0000025vO7AAI?language=en_US — KUKA LBR iisy CAD (STEP, Parasolid, NX, DXF; login).
86. https://github.com/ros-industrial/fanuc — ROS-Industrial FANUC support incl. `fanuc_crx10ia_support`; Apache-2.0 / BSD-3; community support level.
87. https://github.com/DoosanRobotics/doosan-robot2 — Doosan ROS 2 packages, BSD-3-Clause (GitHub) with Apache-2.0 badge.
88. https://github.com/robotiq/ros , https://github.com/robotiq , https://robotiq.com/support — official Robotiq ROS 2 packages (BSD-3-Clause, descriptions), Isaac Sim assets repo, support/CAD site.
89. https://onrobot.com/en/products/vgc10-vacuum-gripper — VGC10 STEP download.
90. https://www.ati-ia.com/products/toolchanger/tool_changer_models.aspx — ATI tool changer models and "3D CAD Models" section.
91. https://www.schmalz.com/en-se/products/automation-743270/other-gripping-technologies-746237/needle-grippers-306131/needle-grippers-sng-v-306144/10.01.29.00176 and https://www.schmalz.com/en/products/automation-743270/other-gripping-technologies-746237/needle-grippers-306131/electric-needle-grippers-sngi-ae-306138/10.01.29.00390 — Schmalz Live CAD model (login for download), EPLAN macro.
92. https://www.zimmer-group.com/en/products/components/handling-technology/2-jaw-parallel-grippers/series-gh6000/products/ghk6160 — Zimmer product page "Download CAD data".
93. https://schunk.com/us/en/services/downloads/cad/ecad-data and https://www.3dfindit.com/en/cad-bim-library/manufacturer/schunk?path=schunk — SCHUNK CAD/ECAD downloads, EPLAN portal, 3Dfindit catalogue.
94. https://www.staubli.com/global/en/robotics/download.html — Stäubli robotics download centre (register/login).
95. https://festo.partcommunity.com/3d-cad-models — Festo CAD models on CADENAS PARTcommunity.
96. https://igus.partcommunity.com/3d-cad-models?countryIso=US&info=igus%2Fdrylin_lineargleitlager%2Fantriebstechnik%2Fsaw_asmtab.prj&languageIso=en and https://www.igus.eu/energy-chain/configurator/3d-cad-models — igus drylin CAD, e-chain CAD free without registration.
97. https://www.boschrexroth.com/en/us/c/linear-motion-technology-selector , https://www.boschrexroth.com/en/us/downloads/cad-files , https://www.boschrexroth.com/en/us/c/framepro-cad-plug-in — Rexroth configurator CAD download, CAD file search, FRAMEpro plug-in.
98. https://www.hiwin.de/en/cad-konfigurator and https://www.hiwin.de/en/tools/produktkonfiguratoren — HIWIN CAD configurators.
99. https://www.traceparts.com/en/search/traceparts-classification-mechanical-components-linear-and-rotary-motion-linear-motion-guides?CatalogPath=TRACEPARTS%3ATP01004003 and https://www.traceparts.com/en/search/thk?CatalogPath=THK%3AF_THK — TraceParts linear-motion suppliers and model counts (Rollon, Güdel, PBC Linear, item, HIWIN, THK).
100. https://www.traceparts.com/en/product/beckhoff-cp693100000000?CatalogPath=BECKHOFF%3ABECKHOFF.030.060.030&Product=10-22082014-076815 — Beckhoff CAD on TraceParts.
101. https://support.industry.siemens.com/cs/us/en/view/89671877 — Siemens CAx Download Manager (3D, 2D, EPLAN; free account).
102. https://www.rittal.com/us-en_US/Software/CAD-data — Rittal CAD data routes (product pages, PARTcommunity, app).
103. https://www.sick.com/media/pdf/9/69/669/dataSheet_RE13-SAC_1059503_en.pdf — SICK datasheet pointing to CAD dimensional models on the product page.
104. https://www.pilz.com/en-CA/eshop/Small-controllers-PNOZmulti/Small-controllers-PNOZmulti-2/PNOZmulti-2-base-units/Accessories-PNOZmulti-2/c/0010100204710680OV — Pilz product downloads (EPLAN P8 macros, software).
105. https://www.phoenixcontact.com/en-us/registration-benefits — Phoenix Contact CAD/3D downloads require registration.
106. https://www.3dfindit.com/en/cad-bim-library/manufacturer/80/20/metric/profiles?path=8020%2Fmetric%2Fprofiles — 80/20 profiles on 3Dfindit (CADENAS).
107. https://us.misumi-ec.com/guide/category/ecatalog/use_cad.html and https://us.misumi-ec.com/maker/misumi/cad/ — Misumi CAD download (login, configurator, STEP/IGES/DXF).
108. https://www.mcmaster.com/cad-models/ and https://www.mcmaster.com/termsandconditions — McMaster-Carr CAD library and CAD-model use restrictions.
109. https://www.cadenas.de/terms-of-use-3d-cad-models — PARTcommunity/3Dfindit terms of use (CAD/BIM use only; AI training prohibited; penalties).
110. https://info.traceparts.com/de/legal/general-terms-and-conditions-for-traceparts-product-catalog-services-applicable-to-parts-distributors and https://www.traceparts.com/en — TraceParts terms (distributor contract; consumer General Terms of Use linked in the footer, not extracted).
111. https://grabcad.com/terms and https://grabcad.com/questions/license-for-free-models — GrabCAD website terms (non-commercial internal use; content owned by uploaders).
112. https://docs.baslerweb.com/a2a5328-4gcbas — Basler ace 2 model page with CAD/technical drawing download.
113. https://softwareservices.flir.com/BFS-PGE-27S5/latest/40-Installation/Dimensions.htm and https://www.teledynevisionsolutions.com/zh-cn/learn/learning-center/machine-vision/mv-getting-started — Blackfly S CAD models and Teledyne camera CAD links.
114. https://en.ids-imaging.com/downloads.html — IDS download centre.
115. https://www.zivid.com/downloads — Zivid STEP/STL for cameras, mounts, calibration boards.
116. https://www.photoneo.com/downloads/device-resources — Photoneo CAD per model, 2026 housing change note.
117. https://dev.realsenseai.com/docs/cad-files — RealSense CAD files page.
118. https://www.orbbec.com/docs/g330-download-cad-files — Orbbec Gemini 330 series CAD files.
119. https://developer.nvidia.com/embedded/downloads and https://forums.developer.nvidia.com/t/jetson-agx-orin-developer-kit-step-file/264253 — Jetson STEP models in the Jetson Download Center.
120. https://www.zund.com/en/cutting-systems/digital-cutting-systems/g3-cutter , https://www.zund.com/en/products/cutters/s3 , https://www.zund.dk/wp-content/uploads/2016/07/D3-Technical-Data_brochure.pdf (2016, possibly stale), https://flexografica.com/wp-content/uploads/2024/05/G3-Technical-Data.pdf — Zünd G3/S3 sizes, overall dimensions and weights; no CAD download offered.
121. https://www.juki.co.jp/industrial_e/products_e/alldocument.php and https://www.juki.co.jp/industrial_e/products_e/lether_e/flatbed_e/detail.php?cd=DDL-8700L_E — Juki catalogues/manuals/parts lists; DDL-8700L head weight 28 kg; no CAD.
122. https://github.com/pzfreo/draftwright and https://pypi.org/project/draftwright — Draftwright (AGPL-3.0), install, requirements, outputs.
123. https://pypi.org/project/build123d-drafting-helpers/0.8.0 — build123d-drafting-helpers 0.8.0 CLI and API.
124. https://pypi.org/project/build123d-mcp and https://pypi.org/project/build123d-mcp/0.3.59 — build123d-mcp (Apache-2.0), tools, bd_warehouse catalogue resource, build123d pin.
125. `/home/user/agent/docs/ARCHITECTURE_SPINE.md` (section 4) and `/home/user/agent/docs/logs/DECISIONS.md` (D-004), `/home/user/agent/docs/logs/TOOLING.md` — project conventions, D-004 code-CAD decision, build123d install smoke test (internal).
126. https://www.autodesk.com/au/products/fusion-360/overview — Fusion regional pricing and personal-use limits (AU page; corroborates [18]).
127. https://github.com/PickNikRobotics/ros2_robotiq_gripper — predecessor of the official Robotiq ROS 2 driver (BSD-3-Clause, 180 stars).
128. https://github.com/google-deepmind/mujoco_warp — MuJoCo Warp (GPU MuJoCo; mentions cloth and soft bodies).
