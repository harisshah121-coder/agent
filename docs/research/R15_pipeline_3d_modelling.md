# R15 · 3D modelling and simulation pipeline for the roll-to-garment cell

Research agent R15 · written 2026-10-21 · scope: CAD/mesh/URDF/MJCF/USD toolchain, vendor geometry sources, electrical and pneumatic drawing tools, fabrication vendors, and the honest limits of what the 3D model proves.

<!-- SUMMARY_PLACEHOLDER -->

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
