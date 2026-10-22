# R02 · Robotics: arms, gantries, linear motion, tool changers (ST04; robotic parts of ST03/ST05/ST06/ST07)

Research agent R02 · written 2026-10-21 · all prices as seen on 2026-10-21 unless stated · currency and basis given per row.
Scope per `_BRIEFS.md` R02: collaborative/industrial arms current in 2026, SCARA and delta robots, Cartesian gantries and linear axes, seventh-axis tracks and pedestals, tool changers, force/torque sensing, arm cable management, what existing sewing-automation products use, and a comparison of three manipulation architectures for a 3 m × 1.5 m envelope at 2–5 kg payload and ±0.5 mm placement.

<!-- SUMMARY_PLACEHOLDER -->

## Findings

Conventions: "RP" = pose repeatability per ISO 9283. "Ext. rate" = fastest documented external servo/streaming rate. Prices: "list" = vendor list, "reseller" = online reseller price, "est." = estimate with basis, "quote" = not published. CAD column records what is downloadable and where. Reseller EUR prices from Unchained Robotics (Germany) exclude VAT.

### F1. Collaborative and light industrial 6-axis arms (ST04 presentation arm, ST03/ST07 handling)

#### F1.1 Universal Robots (Denmark) — e-Series and UR Series, PolyScope 5 / PolyScope X

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Universal Robots | UR3e | 3 kg, 500 mm, RP ±0.03 mm, TCP 3 m/s, built-in F/T (accuracy ±3.5 N), 17 safety functions PL d Cat 3 | quote (UR sells via distributors) | weeks (distributor) | STEP + JT on UR support "Download → Mechanical → Robot 3D CAD" (free account login; UR "Graphical Documentation" terms) | [1][6] |
| Universal Robots | UR7e (re-rated UR5e, same 20.6 kg arm) | 7.5 kg, 850 mm, RP ±0.03 mm, TCP 4 m/s, F/T accuracy ±4.0 N, 570 W max | USD 38,363 (2026-10-21, Vention reseller, PolyScope 5, "ships next day") | next day (Vention) | STEP on UR support (login); Vention part page "3D Model → Download" | [1][7][6] |
| Universal Robots | UR10e | 12.5 kg, 1300 mm, RP ±0.05 mm, TCP 4 m/s (2025 techsheet; older manuals say ~1 m/s typical), F/T accuracy ±5.5 N, 21 safety functions PL d Cat 3, control box 500 Hz, Modbus TCP / EtherNet/IP / PROFINET / PROFIsafe | USD 49,596 (2026-10-21, Vention reseller) | 3 weeks (Vention) | STEP "UR10e/UR12e" (shared mechanical design) on UR support (login) | [2][3][8][9] |
| Universal Robots | UR12e | 12.5 kg, 1300 mm, RP ±0.05 mm, TCP ~4 m/s, 23 configurable safety functions PL d Cat 3, 33.3 kg arm, PolyScope 5 or X | quote (listed by Vention; price not captured) | — | same STEP as UR10e | [4][1] |
| Universal Robots | UR16e | 16 kg, 900 mm, RP ±0.05 mm, TCP 3 m/s | quote | — | STEP on UR support | [1] |
| Universal Robots | UR15 (UR Series, launched Automate May 2025) | 15 kg (17.5 kg with boundary conditions), 1300 mm, RP ±0.05 mm, TCP 5 m/s (fastest UR), wrist joints 300 °/s, arm IP65, F/T accuracy 8.3 N, 21 safety functions PL d Cat 3, 40.7 kg | quote | shipping since June 2025 | STEP "UR15.step.zip" on UR support (login) | [5][10][11] |
| Universal Robots | UR20 | 20 kg (25 kg with boundary conditions), 1750 mm, RP ±0.05 mm | USD 62,990 (2026-10-21, Vention reseller, "ships next day") | next day (Vention) | STEP on UR support | [1][8] |
| Universal Robots | UR30 | 30 kg (35 kg with boundary conditions), 1300 mm | quote | — | STEP "UR30.step.zip" on UR support | [1][12] |
| Universal Robots | UR8 Long, UR18, "g-Series" (UR10g-1750, UR17g-1300, UR18g-950) | Listed on the UR support download filter and in the ROS 2 description mesh licence (UR8LONG, UR18 meshes); specs not captured in this research — **unverified** | quote | — | STEP presumably on UR support | [6][13] |

Controller and interfaces (all current UR arms): RTDE over TCP/IP at up to 500 Hz on current controllers (the RTDE guide notes the historical default of 125 Hz output and that the real-time loop has priority), URScript/primary interface, External Control URCap/URCapX for ROS 2, Modbus TCP, EtherNet/IP, PROFINET, PROFIsafe. PolyScope X is the current-generation software (SW 10.13 latest on the download page; PolyScope 5 SW 5.26 in parallel). [14][15][6]

ROS 2 and simulation: `Universal_Robots_ROS2_Driver` is released for Humble, Jazzy, Kilted, Lyrical and Rolling, supports PolyScope X, PolyScope 5 and CB3 controllers, and the full 3–30 kg line; `Universal_Robots_ROS2_Description` carries URDF + meshes (the UR8LONG/UR15/UR18/UR20/UR30 meshes are under UR's "Graphical Documentation" terms, which are not OSI open source but allow use, modification and sharing with restrictions). MuJoCo Menagerie carries `universal_robots_ur5e`; Isaac Sim ships UR assets; UR maintains a Gazebo simulation package. [16][13][17]

#### F1.2 FANUC CRX series (Japan) — R-30iB Plus / Mini Plus controller, DCS safety

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| FANUC | CRX-5iA | 5 kg, 994 mm, RP ±0.03 mm, 25 kg | EUR 32,000 excl. VAT (2026-10-21, Unchained Robotics reseller) | reseller stock/weeks | FANUC CAD via "Request a quote"/distributor portal; STEP not openly linked on product page (see F1.2 note) | [18][19] |
| FANUC | CRX-10iA | 10 kg, 1249 mm, RP ±0.04 mm, 40 kg, 1000 mm/s collaborative mode, 2000 mm/s high-speed mode, IP67 | EUR 37,000 excl. VAT (2026-10-21, Unchained) | — | as above | [20][18] |
| FANUC | CRX-10iA/L | 10 kg, 1418 mm, RP ±0.04 mm, 40 kg, IP67, J1–J3 120 °/s | EUR 38,500 excl. VAT (2026-10-21, Unchained); also listed USD 47,419 (Unchained US page) | — | as above | [21][22][23] |
| FANUC | CRX-20iA/L | 20 kg, 1418 mm, RP ±0.04 mm, 41 kg, IP67 | EUR 45,000 excl. VAT (2026-10-21, Unchained) | — | as above | [24][22] |
| FANUC | CRX-25iA / CRX-30iA | 25 kg at 1889 mm / 30 kg at 1756 mm, RP ±0.05 mm, 135 kg (CRX-25iA listed by reseller as 30 kg / 1889 mm) | EUR 52,000 excl. VAT (2026-10-21, Unchained, CRX-25iA) | — | as above | [25][18][26] |

Controller/interfaces: R-30iB Plus (CRX uses the Mini Plus cabinet, 410 × 277 × 370 mm), tablet teach pendant, Dual Check Safety (DCS) position/speed monitoring, "8 years zero maintenance". External motion: FANUC's interpolation period (ITP) is 8 ms on most controllers (125 Hz) with 4 ms possible on R-30iB Plus; Stream Motion (J519) and Dynamic Path Modification (R648) are the streaming options; a 2017 ROS-Industrial issue documents that KAREL-based state reporting is quantised to the ITP. [27][28][29]

ROS 2: FANUC released an official ROS 2 driver for the CRX series in 2025 (`FANUC-CORPORATION/fanuc_driver`, a ros2_control "high-bandwidth streaming driver" for real or virtual robots); an independent academic ros2_control hardware interface (`paolofrance/ros2_fanuc_interface`, EtherNet/IP, tested on CRX-10iA/L, CRX-20iA/L, CRX-25iA with R-30iB Mini Plus) is described in arXiv 2506.14487. [30][31][32][33]

CAD note: FANUC product pages offer datasheets and "Request a quote"; the EU datasheet PDFs carry dimensioned drawings. 3D STEP files are distributed through FANUC's customer/partner portals and ROBOGUIDE rather than an open download; Vention lists a "UR10e/UR16e and FANUC CRX-10iA Mounting Plate" (ST-RB-001-0008), confirming the CRX-10iA shares the UR10e base bolt pattern for pedestal design. [20][34]

#### F1.3 ABB GoFa CRB 15000 and SWIFTI CRB 1300 (Sweden/Switzerland) — OmniCore C30

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| ABB | GoFa CRB 15000-5/0.95 | 5 kg, 0.95 m wrist reach (1.05 m flange), RP 0.02 mm, TCP up to 2.2 m/s, torque sensors in all 6 joints, SafeMove Collaborative, OmniCore C30 only | USD 30,000–38,000 (2026-10, Robot Price Index est. from distributor listings; "~$39K" per Standard Bots comparison) — ABB quotes via distributors | — | CAD (STEP etc.) via abb.com Robotics product pages / ABB Library and RobotStudio library | [35][36][37][38][39] |
| ABB | GoFa CRB 15000-10/1.52 | 10 kg, 1.52 m wrist reach (1.63 m flange), RP 0.02 mm, armload 0.5 kg (R25.2), Ultra Accuracy option | ~USD 50,000 (2026, Standard Bots comparison page, est.) | — | as above | [35][38] |
| ABB | GoFa CRB 15000-12/1.27 | 12 kg, 1.27 m wrist reach (1.38 m flange), RP 0.02 mm | ~USD 50,000 (2026, est., same basis) | — | as above | [35][38] |
| ABB | SWIFTI CRB 1300-11/0.9, -10/1.15, -7/1.4 | 11 kg/0.9 m, 10 kg/1.15 m, 7 kg/1.4 m; TCP 6.2 m/s; RP 0.02/0.023/0.03 mm; 1 kg picking cycle 25×300×25 mm 0.41–0.45 s; 75–79 kg; IP40 (IP67 opt.); SafeMove Collaborative + laser scanner, Cat 3 PL d; integrated 4× air lines (6 bar), 1000BASE-T Ethernet on arm | quote | — | as above | [40][41] |

Interfaces: Externally Guided Motion (EGM) position guidance at 4 ms (4.032 ms real controller, i.e. ~250 Hz) with 10–20 ms control lag, UDP + Google protobuf (`egm.proto`); EGM Position Stream up to 250 Hz; RobotWare 7 / OmniCore. [42][43]

ROS 2: `PickNikRobotics/abb_ros2` (ros2_control hardware interface on abb_libegm, RWS client, generic bringup), developed with Optimax; built from source, Humble-era (status on newer distros should be checked before committing). [44][45]

#### F1.4 KUKA LBR iisy (Germany) — KR C5 micro-2, iiQKA.OS2

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| KUKA | LBR iisy 3 R760 / 6 R1300 / 8 R930 | 3 kg / 6 kg / 8 kg, reaches 760 / 1300 / 930 mm | quote ("Log in to view pricing" on my.KUKA) | — | my.KUKA product page: STEP, Parasolid, NX, 2D DXF, Process Simulate and DELMIA data (login) | [46][47] |
| KUKA | LBR iisy 11 R1300 (art. 366982; CR variant 427041) | 11 kg rated (11.72 max), 1300 mm, RP ±0.05 mm, ~46.3 kg, IP54, A1–A3 200 °/s, A6 430 °/s, KR C5 micro-2, cleanroom ISO 3 (CR) | quote | — | STEP/Parasolid/NX/DXF on my.KUKA (login); igus energy-supply kit IGU-TR.920.287 listed as accessory | [47][48] |
| KUKA | LBR iisy 15 R930 (art. 366983) | 15 kg rated (16.41 max), 930 mm, RP ±0.05 mm, IP54, A6 380 °/s | quote | — | as above | [49] |

Interfaces and ROS 2: `kroshu/kuka_drivers` (ROS 2 drivers for all KUKA operating systems: iiQKA/iisy via EAC, Sunrise/iiwa via FRI, KSS via RSI) is released as binaries for Humble and Jazzy (`ros-jazzy-kuka-drivers`, `kuka_robot_descriptions`), last updated 2026-08/09, and requires a real-time kernel client; KUKA RSI runs at 4 ms (IPO fast) or 12 ms (IPO standard), FRI at 1 ms on Sunrise. [50][51][28]

#### F1.5 Doosan Robotics (Korea) — A / M / H / E series

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Doosan | A0509 (A0509s adds 6th-joint F/T) | 5 kg, 900 mm, RP ±0.03 mm, TCP 1 m/s, 21 kg, 2 DI/2 DO on tool | EUR 22,500 excl. VAT (2026-10-21, Unchained) | — | STEP download on Unchained product page and Doosan site | [52][53] |
| Doosan | A0912 | 9 kg, 1200 mm, RP ±0.05 mm, 27 kg | EUR 27,500 excl. VAT (2026-10-21, Unchained) | — | STEP (as above) | [54][53] |
| Doosan | M1013 (flagship, 6 joint torque sensors) | 10 kg, 1300 mm, RP ±0.05 mm, TCP 1 m/s, 33 kg | EUR 33,500 excl. VAT (2026-10-21, Unchained) | — | STEP on Unchained product page | [55][56] |
| Doosan | M0617 / M0609 / M1509 | 6 kg/1700 mm, 6 kg/900 mm, 15 kg/900 mm | M1509 EUR 37,500 excl. VAT (2026-10-21, Unchained) | — | STEP | [56][22] |
| Doosan | H2017 / H2515 | 20 kg/1700 mm, 25 kg/1500 mm, RP ±0.1 mm, 74 kg (H2017) | H2017 EUR 44,000 excl. VAT (2026-10-21, Unchained) | — | STEP | [57][58][56] |

Interfaces: Doosan "Real-time External Control" is a UDP/IP API from an external PC through the controller at up to 1 kHz with `servoj_rt`, `servol_rt`, `speedj_rt`, `speedl_rt`, `torque_rt` commands (DRCF API 1.29/1.31). ROS 2: `doosan-robotics/doosan-robot2` humble branch "controls all models of Doosan robots in ROS 2 (Humble)"; no released binary appears on the ROS index (source build). [59][60][61]

#### F1.6 Techman Robot (Taiwan, Omron network) — TM AI Cobot S series, TMflow 2

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Techman | TM5S | 5 kg, 946 mm, RP ±0.03 mm, 24 kg, arm IP65, max 4 m/s (1.4 m/s at rated payload), J6 450 °/s, built-in eye-in-hand camera, 31 TÜV-certified safety functions PL d Cat 3, RS-232/422/485, Modbus TCP/RTU, PROFINET/EtherNet/IP optional | quote (older TM5-700 listed EUR 30,320 excl. VAT at Unchained, 2026-10-21) | — | 2D/3D files on tm-robot.com download center (members); digital twin on ENCY library | [62][63][64] |
| Techman | TM7S / TM12S / TM14S / TM20S / TM25S / TM30S | S-series line listed by Techman; TM25S & TM30S hardware installation manual v5.04 dated 2026-10; specs not captured here — **unverified in this report** | quote | — | download center | [65][62] |

ROS 2: `TechmanRobotInc/tm2_ros2` supports Foxy, Humble and Jazzy for TMflow 2 / S-series (TMflow ≥ 2.14), includes `tm_description` URDF/meshes for TM5S–TM30S (and camera-less SX variants) and MoveIt 2 configs; the driver sends TMscript over the "Listen Node" (not a hard-real-time servo interface). Older `tmr_ros2` (70 stars) covers the non-S series on Humble. [66][67]

#### F1.7 Yaskawa Motoman HC series (Japan) — YRC1000 / YRC1000micro

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Yaskawa | HC10DTP | 10 kg, 1379 mm absolute (1200 mm effective), RP ±0.05 mm, 58 kg, IP67, 1000 mm/s collaborative / 2000 mm/s hybrid mode, thru-arm air + Ethernet + I/O, ISO tool flange | EUR 38,120 excl. VAT (2026-10-21, Unchained); "from USD 38,000" (All Things Cobots, 2026-10-10, indicative) | "available for immediate shipment" (Motoman US) | 2D/3D downloads listed on yaskawa.eu product page; datasheet on motoman.com | [68][69][70][71] |
| Yaskawa | HC20DTP | 20 kg, 1900 mm absolute (1700 effective), RP ±0.05 mm, 140 kg, IP67 | EUR 52,220 excl. VAT (2026-10-21, Unchained) | — | as above | [72][73] |
| Yaskawa | HC30PL | 30 kg, 1700 mm, RP ±0.05 mm, 140 kg, IP66/67, palletising | "from USD 55,000" (All Things Cobots, indicative) | — | as above | [74][75] |

ROS 2: `Yaskawa-Global/motoros2` v0.2.1 runs on the controller (MotoPlus) as a micro-ROS node for YRC1000, YRC1000micro and DX200 with Humble and Jazzy builds (FastDDS, micro-ROS agent required); no Rolling support. [76]

#### F1.8 Other arms worth tracking in 2026

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| DENSO | COBOTTA PRO 900 / 1300 | 6 kg/900 mm (max reach 1066 mm), RP ±0.03 mm, TCP 2100 mm/s when no person nearby, 29 kg, RC9 controller; PRO 1300: 12 kg/1300 mm, RP ±0.04 mm | "from USD 35,000" (All Things Cobots, 2026-10-10, indicative) | — | DENSO Robotics site (CAD via product pages) | [77][78] |
| DENSO | ROS 2 | `DENSORobot/denso_robot_ros2` (MoveIt 2, Gazebo) official; b-CAP streaming ~8 ms (secondary) | — | — | — | [79][80] |
| Dobot | Nova 5 | 5 kg, 850 mm, RP ±0.05 mm | EUR 4,499–12,169 excl. VAT (2026-10-21, dobot.nu reseller, configuration range) | — | Dobot site | [81] |
| Dobot | CR12A (CR series) | 12 kg, 1200 mm, RP ±0.03 mm, 39.5 kg | EUR 23,100 excl. VAT (2026-10-21, Unchained) | — | — | [82] |
| Elephant Robotics | myCobot Pro 630 | 2 kg, 630 mm, RP ±0.1 mm, 48 V DC, TCP/IP, Modbus, EtherNet/IP, ROS 1/2 | USD 6,999 (2026, vendor list) | — | vendor Gitbook | [83][84] |
| UFACTORY | xArm 6 / xArm 7 / 850 | 5 kg/700 mm/±0.1 mm; 7-DoF 3.5 kg/700 mm; 850: 5 kg/850 mm/±0.02 mm; Python/C++ SDK, ROS 2; servo streaming ~250 Hz (xArm 7 note) | USD 12,650 / 14,950 / 14,100 (2026-07-12, Robotics Center US list) | ships from CA | vendor site | [85][86] |
| Franka Robotics | Franka Research 3 (FR3; arm art. 309969, control 295341) | 7 DoF, 3 kg, 855 mm, RP <±0.1 mm, TCP up to 2 m/s, link-side torque sensors in all 7 joints, 1 kHz Franka Control Interface (libfranka), PL d Cat 3 safety functions (SLP-C, SLS-C, SLS-J, SLD, SEEPO; note FCI cannot run while SLP-C/SLS-C configured on system images < 5.10), Modbus/TCP, OPC UA | USD 39,000 with Franka Hand + academic licence (2026-07, Robotics Center US list); older community estimates USD 13–17k arm-only (2024) | — | URDF/meshes in franka_description; MuJoCo Menagerie `franka_fr3` | [87][88][85][89] |
| Franka | ROS 2 | `frankaemika/franka_ros2` released for Humble (ROS index, updated 2026-09-01); ros2_control + MoveIt | — | — | — | [90] |
| Kinova | Link 6 | IP54, PL d Cat 3 safety functions, integrated F/T sensor; native ROS 2 (ros2_control on Kortex3 API) since Q1 2026, Gazebo/MoveIt 2 launch files (`ros2_link6`) | quote | — | URDF in ros2_link6 | [91] |
| Kinova | Gen3 7-DoF | 4 kg, 902 mm, ROS 2 `ros2_kortex` released Humble/Jazzy/Rolling (updated 2026-09-18) | USD 38,696 (2026, Robotics Center list) | — | kortex_description | [92][93] |
| Flexiv | Rizon 4 / 4s / 10 | Force-controlled arms; `flexiv_ros2` Humble + Jazzy (jazzy-v1 branch for RDK v1.x Rizon line; v2 line for Enlight/MICO); detailed specs/prices **not captured** — quote | quote | — | flexiv_description in flexiv_ros2 | [94] |
| Neuromeka | Indy7 | 7 kg, 1300 mm, RP 0.1 mm (reseller), 28 kg | EUR 23,400 excl. VAT (2026-10-21, Unchained) | — | — | [22] |
| Rainbow Robotics | RB5-850 | 5 kg, 927.7 mm, RP ±0.05 mm, 22 kg, IP54, TCP 1 m/s, M8 tool I/O, GitHub linked from product page | — | — | vendor downloads | [95] |
| Rainbow Robotics | RB10-1300 | 10 kg, 1300 mm, RP ±0.05 mm, 36.5–37.1 kg, IP66, TCP 1 m/s, CB06 control box 16 DI/16 DO | USD 29,500 (Devonics reseller, 2026); EUR 33,000 excl. VAT (Unchained, 2026-10-21) | — | vendor downloads | [96][97][98] |
| Rainbow Robotics | RB3-1200 / RB16-900 / RB20-1900 | 3 kg/1200 mm; 16 kg/900 mm; 20 kg/1900 mm | EUR 23,500 / 35,000 / 44,500 excl. VAT (Unchained, 2026-10-21) | — | — | [98] |
| Standard Bots | Core (RO1) | 18 kg, 1300 mm, RP ±0.025 mm, integrated vision (vendor claims) | USD 37,000 list (vendor page, 2026) | 30-day trial | — | [38] |
| Kassow Robots | KR810 / KR1205 (7-axis) | 10 kg/850 mm RP 0.1 mm; 5 kg/1200 mm | EUR 29,100 / 31,500 excl. VAT (Unchained, 2026-10-21) | — | — | [25][73] |
| AUBO | i5 | 5 kg, 886.5 mm, RP 0.05 mm, 24 kg | EUR 18,600 excl. VAT (Unchained, 2026-10-21) | — | — | [71] |


#### F1.9 Addendum — items confirmed after the main tables

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Universal Robots | **Gen 7 platform, g-Series (launched IMTS, 15 Sept 2026)**: UR10g-1750, UR17g-1300, UR18g-950 (successors to UR8 Long, UR15, UR18, which remain supported) | UR10g-1750: 10 kg (8 kg rated), 1750 mm, RP ±0.08 mm, TCP 5 m/s, 47.3 kg; UR17g-1300: 17.5 kg, 1300 mm, RP ±0.05 mm, 5 m/s, 43.4 kg; UR18g-950: 18 kg, 950 mm, RP ±0.05 mm, 4 m/s, 42 kg; all IP65, 500 Hz control loop, 23 safety functions PL d Cat 3, g-Series tool flange with 1 Gb Ethernet + 24/48 V 3 A at the wrist, Harting base connector, F/T accuracy ±8.3 N; new CB7 Core controller, TP7 pendant, SP7 Smart Panel; e-Series renamed UR3e-540 / UR7e-920 / UR12e-1300 (mechanically unchanged) | quote ("Get pricing") | new (Sept 2026) | STEP for CB7 Core, TP7, SP7 on UR support download page; arm STEP expected under same login | [99][100][101][104][105] |
| Universal Robots | UR8 Long (Sept 2025; now succeeded by UR10g-1750) | 8 kg (10 kg with boundary conditions), 1750 mm, RP ±0.08 mm, TCP 5 m/s, 44.7 kg (30 % lighter than UR20, "ideal for gantries, rails, overhead"), IP65, MotionPlus for external axes | quote | — | STEP on UR support | [102][106] |
| Universal Robots | UR18 (succeeded by UR18g-950) | 18 kg, 950 mm, up to 3 m/s; UR markets it as "light enough for mounting on most standard gantry systems" | quote | — | STEP on UR support | [103][101] |
| Techman | TM12S / TM14S / TM25S | TM12S: 12 kg, 1300 mm, 33.3 kg; TM14S: 14 kg, 1100 mm, 33 kg; TM25S: 25 kg, 1902 mm, 80.6 kg; RP ±0.03 mm (TM12S/14S) / ±0.05 mm (TM25S); J1–J2 100 °/s, J6 225–450 °/s; max TCP 4.5–5.2 m/s; 600 W | quote | — | 2D/3D drawing links on each product page (TM12S, TM12SX) | [107][108][109] |
| Kinova | Link 6 | 6 DoF, 6.0 kg full-range payload (at 200 mm from wrist), 1000 mm reach, max Cartesian speed 1.65 m/s (page truncated), IP54, PL d Cat 3, integrated F/T | quote | — | URDF in ros2_link6 | [110][91] |
| Flexiv | Rizon 4 / Rizon 4s (+F/T) / Rizon 10 | 7 DoF; Rizon 4: 4 kg, 876 mm, 20 kg, force sensing accuracy 0.1 N; Rizon 4s: 4 kg, 919 mm, 21 kg, 0.03 N; Rizon 10: 10 kg, 941–984 mm, 38–39 kg, 0.2 N; all RP ±0.05 mm, IP65, typical TCP 1.0 m/s, max TCP force 150–350 N, ISO 9409-1-50-4-M6 | quote | — | datasheet on flexiv.com; MuJoCo Menagerie has `flexiv_rizon4` and `flexiv_rizon4s`; RoboDK library model | [111][112][113] |

MuJoCo Menagerie (Google DeepMind) arm models relevant to this project as of 2026-10: Universal Robots UR5e and UR10e (BSD-3), Franka FR3 / FR3 v2 / Panda (Apache-2.0), Flexiv Rizon4 / Rizon4S (Apache-2.0), Kinova Gen3 (BSD-3), KUKA LBR iiwa 14 (BSD-3), UFACTORY Lite 6 and xArm7 (BSD-3), Rethink Sawyer, AgileX PiPER, Trossen ViperX/WidowX, SO-ARM100/SO101. No FANUC CRX, ABB GoFa, Doosan, Techman, Yaskawa HC or KUKA iisy models exist in Menagerie; those must come from the vendor URDF packages. [113]

### F2. SCARA and delta robots (fast flat-piece transfer at the cut-bed exit, ST03)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Epson | T6-B602SS (T6-B All-in-One SCARA) | 4-axis, 600 mm, 6 kg max (2 kg rated), RP ±0.040 mm (J1–J2), Z 200 mm, cycle 0.46 s, built-in controller, 22 kg, 100–240 VAC, RC+ 7.0 / RC+ Express, fieldbus slaves optional (EtherNet/IP, PROFINET, EtherCAT) | quote (Epson sells through distributors; T-series positioned as low-cost "slide alternative") | — | **Free download without login**: SolidWorks, STEP and DXF on Epson support page | [118][119][120] |
| Epson | LS6-B (600 mm) | 600 mm, 6 kg max / 2 kg rated, RP ±0.020 mm, cycle 0.39 s, 6,800 mm/s J1+J2, RC90 controller | quote | — | STEP on Epson support (same pattern) | [122] |
| Epson | GX8-B 650 (GX8-C with RC800-A / RC+ 8 in EU) | 650 mm, 8 kg max / 4 kg nominal, RP ±0.015 mm, cycle 0.28 s, 35 kg, 200–240 VAC; RC+ 8 adds SLS/SLP safety-function licence | quote | — | Epson support downloads | [121] |
| Omron | i4L (350/450/550 mm) | 5 kg, cycle 0.38–0.57 s, built-in controller, EtherCAT/Ethernet/PROFINET | quote | — | Omron CAD library (free) | [117] |
| Omron | i4-650H / i4-750H / i4-850H | 15 kg, reach 650/750/850 mm, RP ±0.015 mm XY (650) / ±0.025 mm (750/850), Z ±0.01 mm, Z stroke 210/410 mm, burst cycle 0.39–0.41 s, 50–52 kg, EtherCAT (NJ501-R) or stand-alone Ethernet, 8 pneumatic ports + 2 M23 electrical pass-throughs | quote | — | "CAD Library download" on Omron EU product page | [114][115][116] |
| FANUC | SR-6iA / SR-12iA (SCARA) | SR-12iA: 12 kg; used/refurbished unit listed at USD 17,500 (RobotsDoneRight, used market — not a new-unit price) | USD 17,500 used (2026, reseller) | — | FANUC portal | [123] |
| ABB | IRB 360 FlexPicker -1/1130, -3/1130, -8/1130, -1/1600, -6/1600 | Delta, 1–8 kg, workspace Ø1130 or 1600 mm, RP 0.1 mm, cycle 0.30–0.60 s (25/305/25 mm), 120 kg, inverted mount, integrated vacuum (7 bar), 12-pole signal, OmniCore C30 or IRC5, PickMaster conveyor tracking (1.0–5.0 mm tracking repeatability by speed) | quote | — | "View Variants & CAD Files" on one.robotics.abb.com; ABB Library | [124][125][126] |
| Omron | Hornet 565 / iX3-565 | 3 kg (8 kg 3-axis), Ø1130 mm, RP ±0.10 mm, 1.4 m/s tracking, cycle 0.32–0.42 s | quote | — | Omron CAD library | [127][128] |
| Omron | Quattro 650/800 / iX4 | 4-arm parallel, 15 kg (650) / 10 kg (800), Ø1300 / 1600 mm, cycle 0.30–0.62 s, IP65 | quote | — | Omron CAD library | [127] |
| FANUC | M-2iA/3S (and /3SL 1130 mm) | 4-axis delta, 3 kg, Ø800 mm, RP ±0.03 mm, 130 kg, IP67/IP69K, hollow wrist, R-30iB Plus | quote | — | FANUC datasheet | [129] |
| FANUC | M-1iA/0.5A | 6-axis delta, 0.5 kg (1 kg opt.), 280 mm | quote | — | FANUC datasheet | [130] |
| igus | DLE-DR-0001 / -0050 3-axis delta | Ø360 or 600 mm workspace, 180 mm height, up to 5 kg, precision 0.5 mm, 3.0 m/s, 60 m/s², up to 60 picks/min, drylin ZLW-1040S axes + NEMA 24 steppers, kit form | price via RBTX / igus shop configurator (not captured) | 24 h for stock kits | STEP via igus/RBTX configurator (free) | [131] |
| Codian Robotics | D2/D4 delta (e.g. D2-1500-S030-DR80) | 2-axis delta with 1500 mm workspace listed on DirectIndustry; detailed specs not captured | quote | — | — | [132] |

### F3. Cartesian gantries and linear axes (ST04 planar coverage, ST03 extraction)

Belt vs ball-screw vs linear-motor for a 3 m axis: toothed-belt axes reach 5–10 m/s and 50 m/s² with ±0.05–0.1 mm repeatability and strokes to 8.5–11.5 m (Festo EGC, Rexroth MKR/MLR); ball-screw modules give ±0.005–0.01 mm but ≤2.5 m/s and need spindle supports beyond ~3–5 m (Rexroth CKK/MKK); linear-motor modules give ±0.001 mm and 250 m/s² but cost most and are limited to ~4 m grid lengths (Rexroth LMM). For ±0.5 mm placement of knit plies with vision correction, belt axes are sufficient and cheapest. [133][151]

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Festo | EGC-TB-KF toothed-belt axis (sizes 50/70/80/120/185; e.g. EGC-120-…-TB-KF, part 556815) | stroke 50–8500 mm, max 5 m/s (size ≥70), 50 m/s², RP ±0.08 mm (±0.1 mm size 50), feed force 50–2500 N by size (EGC-120: 800 N, feed 125 mm/rev, Fy/Fz 6890 N), recirculating ball guide, 100 % duty | price not published; configured quote via Handling Guide Online | stock items for ≤1500 mm strokes (ordering data list) | **STEP/all standard formats generated immediately by Handling Guide Online (HGO)**, plus datasheet and EPLAN project | [133][134][139][140] |
| Festo | EXCM-30 / EXCM-40 planar surface gantry | EXCM-30: X 90–700 mm, Y 110–510 mm, 2–3 kg; EXCM-40: X 200–2000 mm, Y 200–1000 mm, 4 kg; RP ±0.05 mm; 0.5–1.0 m/s; stepper drive package; **too small for 3 m × 1.5 m** | quote (HGO) | — | HGO CAD | [135] |
| Festo | EXCH-40 / EXCH-60 H-gantry | X 200–2000 / 500–2500 mm, Y 200–1000 / 500–1500 mm, Z 50–200 mm, rated load 4 / 6 kg, 5 m/s horizontal, 50 m/s², RP ±0.1 mm, needs CPX-E-CEC-M1 multi-axis controller; up to 100 picks/min | quote (HGO) | — | HGO CAD | [136][139] |
| Festo | YXCS planar surface gantry / YXCL linear gantry / three-dimensional gantry (EGC-80/120/185 or EGC-HD) | YXCS strokes to 3000 mm on EGC-80/120/185 and EGC-HD-125/160/220; YXCL Y strokes to 3000 mm; Z modules EGSL/ELGC/ELCC; drive packages CMMT-AS servo | quote (HGO generates quote automatically) | ready-to-install or partially assembled | HGO CAD, datasheet, EPLAN | [137][138][139] |
| igus | drylin ZLW-1040 toothed-belt axis | stroke to 2000 mm, 54–70 mm/rev, 3–5 m/s, max radial load 200–300 N, carriage position variation ±0.2–0.35 mm (load dependent) | from USD 817.56 (ZLW-0660S, 2026-10-21, igus.com list) | 24 h–30 days | free STEP via igus configurator | [141][142][144] |
| igus | drylin ZLW-20120S / ZLX | ZLW-20120S: stroke to 3000 mm, 144 mm/rev, 5 m/s, radial load 3000 N; ZLX: stroke to 3500 mm | upon request (igus.com) | 25–30 working days (ZLX) | free STEP | [143][144] |
| igus | drylin gantry robots (DLE-LG 2-axis, DLE-FG flat 3-axis, DLE-RG room 4-axis) | up to 3000 × 3000 × 750–1000 mm, up to 85 kg, RP ±0.3–0.5 mm, ≤1 m/s, max 20 picks/min, stepper + igus Robot Control (iRC, free) | from EUR 1,065.28 (2-axis, igus.eu list); XY gantry from USD 1,916.40, YZ from USD 2,028.38 (igus.com list, small spans); 3 m × 3 m configurations priced in configurator | 24 h for stock sizes | free CAD download from portal configurator / RBTX | [145][146][150] |
| Bosch Rexroth | MKR (belt) linear modules sizes 40–165 | up to 5 m/s, 50 m/s², travel to 11,560 mm, RP ±0.05 mm, dynamic load to 84,100 N; MLR 10 m/s; MKK ball-screw ±0.005 mm to 4,960 mm; CKK/CKR compact modules; LMM linear motor ±0.001 mm | Rexroth Store shows prices after login (e.g. MKR-040-NN-3, R114066013) | — | CAD via Rexroth store/configurator | [151][152] |
| Parker | HMR (085–240) belt or screw; OSPE B/BHD; HLE-Z | HMR belt: 5 m/s, strokes to 6000 mm, thrust 4000 N, IP54 cover option; OSPE-BHD: 10 m/s, 6 m, ±0.05 mm; HLE-Z rack & pinion to 50 m, ±0.05 mm | quote | — | Parker catalogues/CAD | [153] |
| Rollon | ELM Plus, ROBOT Plus, E-Smart/R-Smart, Uniline A/C/E | belt actuators up to 5 m/s and 50 m/s² (Uniline A 7 m/s); ELM: 50–110 mm bodies, axial loads 530–2650 N, strokes 100–3700 mm, maintenance-free ball guide 20,000 km; multi-axis XYZ kits | quote via myRollon | — | CAD file + datasheet per family on rollon.com / myRollon | [154][155][156] |
| Güdel | ZP 2-axis / FP 3-axis / EP 1-axis gantries (rack & pinion) | industrial steel gantries; TMF track RP ±0.02 mm | quote | — | configurators on gudel.com | [163][161] |
| Bell-Everman | ServoBelt Linear | up to 4 m/s, accuracy ±4 µm/m, bidirectional repeatability ±1 encoder count, travel to 50 m, multiple independent carriages, Rexroth T-slot chassis | quote | — | — | [164] |
| Macron Dynamics | MGS-HBG-08, MGS-PSC-XZ, MGS-R6D belt, MRA-RTU | MGS-R6D: 1150 lbf, 5000 mm/s, 5 g; PSC-XZ: 25 lb, 5000/2000 mm/s, Z 150–600 mm; MRA-RTU-2 carries 3000 lb robots | quote (online configurator) | — | "View and Configure" produces CAD | [165] |
| PBC Linear | MTB055D belt actuator (80 × 80 mm profile, dual ball profile rails; e.g. 2500 mm body) | listed with configurable length; specs/price not captured | quote | — | — | [166] |
| Vention | FastFactory enclosed timing-belt / ball-screw / rack-and-pinion actuators + MachineMotion AI (CE-CL-030-1500) | MachineMotion AI: NVIDIA Jetson, EtherCAT up to 30 servo motors, 3000 W, Python + code-free MachineLogic, IP54, URCap for UR; MachineMotion AI Robot variant; Robot Safety Module AI; Developer Toolkit (Q4 2025) | MachineMotion AI USD 7,476; MachineMotion AI Robot USD 3,503; Robot Safety Module AI USD 2,082.63 (2026-10-21, Vention list); community 3-axis pick-and-place design "230043" USD 11,814; designs priced live in MachineBuilder | 4 weeks (controller); extrusions next day | **3D model download per part and "Open in 3D" per design in MachineBuilder** (STEP export) | [167][168][169][171][8] |
| OpenBuilds | C-Beam / ACRO low-cost actuators | not researched in this pass (no source captured) — **unknown**; treat as hobby-grade, not for production | — | — | — | — |

### F4. Seventh-axis tracks and robot pedestals

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Rollon | Cobot Transfer Unit (CTU; launched March 2025; UR+ certified) | plug-and-play 7th axis for every UR size, stroke "more than 5 m", 3D models downloadable | quote | — | "Download 3D Models" on Rollon CTU page; UR+ marketplace | [157][158][159] |
| Rollon | RTU aluminium (rack & pinion) / RTU steel / sealed-belt & open-belt aluminium RTUs | robots up to 1500 kg (aluminium R&P) | quote | — | CAD on myRollon | [156][160] |
| Güdel | TrackMotion Floor TMF-1 … TMF-6; CoboMover Floor CMF (cobot track) | TMF-1: stroke to 100 m, payload 3000–12,000 N, 180/120 m/min, RP ±0.02 mm; TMF-5: 6300 kg robots, 1 m/s, 1–98 m | quote | — | configurators per type | [161][162][163] |
| Vention | 7th Axis Range Extender (UR / FANUC / Doosan), floor, overhead, telescopic | floor-mounted reach 0.4 → >3 m; overhead to >12 m; telescopic column 870 mm stroke; URCap control from UR pendant; enclosed belt or ball-screw actuators (no pinch points) | community design "UR 7th Axis on Workstation with Pneumatic Gripper" USD 7,842 (2026-10-21, Vention); UR20-compatible range extender on UR+ marketplace (quote) | weeks | STEP via MachineBuilder | [170][171][172][219] |
| igus | 7th-axis RTU for ReBeL and other arms | belt-driven, strokes to 3000 mm, "up to 4× working range" | igus shop/RBTX | — | free CAD | [147] |
| Vention | Heavy Duty Cobot Pedestal ST-RB-033-0945 (945 mm) / community UR10e pedestals | ST-RB-033-0945 USD 1,161.17; UR10e fixed pedestal design USD 1,012.90 (17.96 kg); UR10e short 250 mm pedestal USD 863.91; mounting plate ST-RB-001-0008 fits UR10e/UR16e and FANUC CRX-10iA | USD (2026-10-21, Vention list) | next day | STEP via MachineBuilder | [8][34][174][175] |
| Devonics | RB-PED-24-CB200 / RB-PED-36-CB200 pedestals | 24"/36" pedestals for Rainbow RB cobots | USD 655.89 / 755.63 (2026, reseller) | — | — | [97] |

### F5. Tool changers (ST04 "gripper toolbox")

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| ATI (Novanta) | QC-11 (9120-011M-000-000 master / 9120-011T-000-000 tool; QC-11-E, hollow-wrist variant) | pneumatic, 16 kg suggested payload, locking force 1100 N at 5.5 bar, 20.3 Nm X/Y, 12.4 Nm Z, positional repeatability 0.0102 mm, 6 × M5 air pass-throughs, 245 g coupled, 1.5 mm no-touch locking, 1 flat for an electrical module (e.g. M8-011 8-pin 1.5 A, A15 15-pin); UR kit on UR+ marketplace | price not published; "Add to quote" | — | **3D CAD models tab on product page; drawing 9630-20-011** | [176][177][178][180][190] |
| ATI | QC-1 / QC-5 / QC-7 / QC-21 | QC-1: 1.4 kg, 94 g, for delta robots; QC-7: 16 kg; QC-21: 25 kg, 8 × 1/8 NPT pass-throughs; range to 4080 kg; >100 pass-through modules | quote | — | 3D CAD on ati-ia.com | [176][179] |
| ATI | MC-16R / MC-36R / MC-50 manual changers | 16 / 36 / 30 kg, 4–6 pneumatic pass-throughs | quote | — | 3D CAD | [176] |
| Schunk | SWS 005/007/011/020/021/022 (SWK master / SWA tool) | SWS 011: 16 kg recommended, 61 Nm Mx/My, 38 Nm Mz, 6 × M5 pass-through, pneumatic lock; SWS 020/021/022: 25 kg; SWO electrical modules (A15 15-pin, E10/E20, EM8 8-pin); SWK-011H axial-air version for hollow-wrist cobots | quote (Schunk/distributor) | — | Schunk CAD portal (vendor site) | [181] |
| Stäubli | MPS 015 / 025 / 032 / 055 (small payload) | MPS 015: 10 kg, 15 Nm static, repeatability 0.0015 mm, 46 mm coupled height, 4 module places, ISO 9409-1-31.5; MPS 025: up to 20–25 kg; family to 2500 kg | quote | — | Stäubli site | [182][183] |
| OnRobot | Quick Changer / Dual Quick Changer | manual, 20 kg payload; electrical pass-through for OnRobot tools | USD 713 single / USD 2,836 dual (ThinkBot reseller, 2026) | stock | OnRobot site | [184] |
| Zimmer Group | WWR / SWS-type changers | **not captured in this pass — unknown**; request datasheet | — | — | — | — |

### F6. Force/torque sensing (ST04 sewing presentation, contact-based ply registration)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Universal Robots (built-in) | e-Series / UR Series flange F/T | UR3e ±30 N range, accuracy ±3.5 N; UR7e ±50 N, ±4.0 N; UR12e/UR16e ±100/160 N, ±5.5 N; UR15 ±8.3 N; g-Series ±150 N, ±8.3 N — adequate for contact detection, too coarse for sub-newton ply tension control | included | — | — | [1][5][99] |
| ATI | Axia80 (e.g. Axia80-M50 kit; 9105-FTKIT-NET-AXIA80-M20) | 6-axis, Ethernet/EtherCAT, UR package with URCap | USD 5,435 (Axia80-M50, e-motionsupply reseller, 2026; ships 6–8 weeks) | 6–8 weeks | ATI 3D CAD | [189][190] |
| ATI | Axia90 kit | ±1000 N / ±50 Nm, resolution 0.1 N / 0.0025 Nm, EtherCAT 8 kHz, <1 ms latency, 26.9 mm height, 0.78 kg, IP67 plate, ISO BC50 pattern | quote | — | ATI 3D CAD | [188] |
| Robotiq | FT 300-S | ±300 N / ±30 Nm, 100 Hz, Modbus RTU RS-485, IP65, 0.3–0.44 kg, UR+ certified | from USD 6,100 (All Things Cobots listing, 2026-10-10, indicative); grey-market USD 2,000–2,500 (Alibaba, not recommended) | — | Robotiq site | [191][192] |
| OnRobot | HEX-E QC / HEX-H QC | 200 N Fxy/Fz; HEX-E: 10 Nm Txy / 6.5 Nm Tz, noise 0.035 N (high sensitivity); HEX-H: 20 / 13 Nm; IP67; 0.35 kg; 3-year warranty | quote | — | **STEP download on OnRobot product page** | [186][187] |
| Bota Systems | MiniONE Pro (Ethernet/EtherCAT), Rokubi T5/T15, SensONE T5/T15/T80, PixONE | MiniONE Pro: 50/100 N, 1 Nm, 60 g, 20 mN resolution; Rokubi T15: 500/1200 N, 15 Nm, 120 g; SensONE T15: 500/1200 N, 15 Nm, 240 g; ROS/Python/C++ drivers, EtherCAT, IMU | quote | — | Bota site | [193][194] |
| ATI | Mini45 / Mini40 / Gamma / Nano17 | USD 2,499 / 5,750 / 6,500 / 4,600 (Robotics Center US list, 2026) | USD (2026) | — | ATI 3D CAD | [195] |

### F7. Cable management on arms (dress packs)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| igus | triflex R TRE/TRC/TRL multi-axis e-chains; cobot kits for UR, FANUC CRX, Doosan, Techman, ABB, KUKA, Yaskawa | FANUC CRX dress pack TRE.920.937.LAE30 (sizes 30/40, for CRX-10iA/25iA/30iA; Velcro clamps); UR brackets TR.911.965.xxx (size 30) / TR.911.966.xxx (size 40) for UR3/5/10; triflex RSE/RSP linear retraction; online dress-pack configurator with cart/quote | configurator price (not captured) | stock | igus configurator CAD | [196][197][198][199][200][202] |
| murrplastik | FHS Robotics kit UR (15 variants: UR 10/20/210/220…) and configurator for UR to FANUC | corrugated conduit + end sleeves + Velcro fastening, slit LS version; R-SSR tension clamp, SH-P holder, KEG strain relief | shop price after login (not captured) | — | murrplastik shop | [201] |
| KUKA / igus | Energy supply axis 1–6 for LBR iisy (igus IGU-TR.920.287) | listed as my.KUKA accessory | my.KUKA | — | STEP on my.KUKA ("Energy supply LBR IISY") | [47] |
| Yaskawa / ABB | through-arm utilities | HC series routes air + Cat 6 Ethernet + I/O inside the arm; SWIFTI integrates 4 air lines and Gigabit Ethernet to the wrist — reduces the need for external dress packs | included | — | — | [69][40] |

### F8. What existing sewing-automation products use (robots found, with the evidence level)

| Product | Robot(s) used | Evidence | Source URL |
|---|---|---|---|
| SoftWear Automation LOWRY / SEWBOT (Atlanta) | Custom **four-axis** robots (LOWRY line launched Oct 2015) for fabric handling, pick-and-place and direct sewing; vision ("ThreadVision") steers the material through the sew head; "fully custom-built"; Series B USD 20 M in June 2025 (Tracxn) | vendor site + 2015 press + trade press | [203][204][205][206] |
| sewts VELUM (Munich) | "Combines commercial robots, grippers, and cameras with proprietary AI" (Dassault 3DEXPERIENCE Lab profile); 700 textiles/h, max 3 kg, 30×30 to 100×200 cm — **arm brand not stated in sources found** | vendor + 3DS | [207][208] |
| Silana (Vienna → New York) | Robotic singulation of the top ply with "high-end gripper technology" and computer vision, then autonomous sewing — **arm brand not stated** | vendor | [209][210] |
| KUKA / robotextile (erler GmbH) | KR AGILUS, KR SCARA and LBR iisy small robots with special grippers singulate plies from a stack and feed them to the next step (pocket/collar placement before sewing) | KUKA solutions database 2022 | [211] |
| Dürkopp Adler Group (PFAFF Industrial + KSL) | Robot cells combining PFAFF sewing heads with KSL handling: garment cell doing insertion + removal **and** automatic curve-seam tracking with one robot; automotive 3D sewing-head robot (brand of arm not stated; KSL cells are historically KUKA-based — **unverified**) | DA partner news (Texprocess) | [212] |
| JUKI | JTR-MF7923/BHA bottom-hemming automat (white paper ref. [10]); no JUKI robotic-arm sewing product found in this pass — **unknown** | — | white paper |
| Jack Technology | listed as a sewing-automation vendor in a 2026 market report; no "sewing robot arm" product page found — **unknown** | market report | [213] |
| Tang et al. 2025 (HKU/Tohoku, RA-L 10(9) 8962–8969; ICRA 2026 poster) | Fixture-free sewing of two aligned plies with a **dual-arm manipulator** and an ordinary sewing machine; five-layer architecture (perception, Petri-net task layer, fundamental operations, control primitives, hardware); high-speed deep-learning fabric edge detection (Hi-FEDS); the specific arm model is not in the abstract/poster text captured — read the PDF to confirm | IEEE + poster | [214][215] |
| Jin et al. 2025/2026 (RA-L) | Automated straight-line sewing of stretchable fabrics with different lengths; cites Tokuda et al. 2D fixture-free dual-arm system | arXiv 2607.29464 | [216] |

### F9. ROS 2 driver and URDF status matrix (as of 2026-10-21)

| Robot family | Driver (maintainer) | ROS 2 distros | Real-time external servo rate | URDF/meshes | Notes | Source URL |
|---|---|---|---|---|---|---|
| UR (all) | Universal_Robots_ROS2_Driver (UR official) | Humble, Jazzy, Kilted, Lyrical, Rolling (binaries) | RTDE 500 Hz; ros2_control via External Control URCap | ur_description (BSD-3 code; UR15/18/20/30/8Long meshes under UR Graphical Documentation terms); Menagerie UR5e/UR10e | most mature; PolyScope X and 5 and CB3 | [16][13][113][218] |
| FANUC CRX | fanuc_driver (FANUC official, 2025) + ros2_fanuc_interface (academic) | ros2_control; distro list not captured | ITP 8 ms (125 Hz), 4 ms on R-30iB Plus; Stream Motion | vendor; academic repo has CRX descriptions | new; verify feature set | [30][31][32][28] |
| ABB GoFa/SWIFTI/IRB | abb_ros2 (PickNik) | source build (Humble era) | EGM 4 ms (250 Hz), 10–20 ms lag | only IRB1200-5/0.9 description shipped (March 2022 note); GoFa URDF must be added | community driver; GoFa needs own description | [44][42][43] |
| KUKA iisy/iiwa/KSS | kuka_drivers (kroshu) | Humble, Jazzy binaries (2026-08) | RSI 4/12 ms; FRI 1 ms (iiwa); EAC (iisy) | kuka_robot_descriptions | requires RT kernel client | [50][51] |
| Doosan | doosan-robot2 (Doosan) | Humble (source) | RT external control 1 kHz (UDP) | in repo | no binary release | [60][61][59] |
| Techman S | tm2_ros2 (Techman) | Foxy, Humble, Jazzy | TMscript via Listen Node (not hard-RT) | tm_description TM5S–TM30S | experimental label | [66] |
| Yaskawa HC | MotoROS2 0.2.1 (Yaskawa) | Humble, Jazzy (micro-ROS on controller) | runs on controller; streaming via MotoPlus | motoman descriptions (ros-industrial) | FastDDS only | [76] |
| DENSO Cobotta Pro | denso_robot_ros2 (DENSO) | — (official repo) | b-CAP ~8 ms (secondary) | in repo | — | [79][80] |
| Franka FR3 | franka_ros2 (Franka) | Humble binary (2026-09) | FCI 1 kHz torque/position | franka_description; Menagerie FR3/FR3 v2 | research grade | [90][87][113] |
| Kinova Link 6 / Gen3 | ros2_link6 (Q1 2026) / ros2_kortex | Humble, Jazzy, Rolling (kortex) | Kortex3 API | in repos; Menagerie Gen3 | — | [91][93] |
| Flexiv Rizon | flexiv_ros2 (Flexiv) | Humble, Jazzy (v1 branches for Rizon) | RDK real-time | flexiv_description; Menagerie Rizon4/4s | — | [94][113] |
| Elephant / UFACTORY / Dobot | vendor SDKs; ROS 1/2 packages | varies | xArm ~250 Hz streaming | vendor | low-cost tier | [83][86] |

### F10. Architecture comparison for a 3 m × 1.5 m envelope, 2–5 kg payload, ±0.5 mm placement

Takt context (derived from the white paper target of ≥100 T-shirts per 12 h shift): one garment every 7.2 min; a basic T-shirt has four cut panels plus a neck rib, so the cell needs roughly one ply pick-and-place per 80–90 s plus a few re-grasps per garment. **Throughput is therefore not the constraint for any option below; reliability of grasp/placement and reach/accuracy are.** Costs below use the sourced prices in F1–F7 and are order-of-magnitude estimates for hardware only (no grippers, vision, guarding or integration).

| Option | Hardware (example BOM) | Est. hardware cost (basis) | Cycle-time estimate | Coverage / accuracy | Main risks |
|---|---|---|---|---|---|
| (a) One servo belt gantry with 2–3 pick heads + one 6-axis arm for sewing presentation | Festo EGC-120 X (3000 mm) + 2 × EGC-80 Y (1500 mm) + EGSL/ELGC Z, CMMT-AS servos (HGO quote) **or** Vention/igus belt gantry for a first prototype; UR10e/UR12e (USD 49,596) or Doosan A0912 (EUR 27,500) on Vention pedestal (USD 1,161); 1 × ATI QC-11 or Schunk SWS-011 changer | gantry est. USD 15–45k (basis: Vention community 3-axis designs USD 8–12k at ~1 m spans; igus 2-axis from EUR 1,065; Festo EGC multi-axis systems are quote-only and sit at the top of this range — **est.**) + arm USD 28–50k + changer/F/T USD 3–8k → **≈ USD 50–105k** | gantry 5 m/s, 50 m/s² → 3 m traverse ≈ 1 s; ply pick-move-place incl. vacuum settle ≈ 4–6 s; heads work in parallel; arm presentation ≈ 10–20 s per seam | full 3 m × 1.5 m planar coverage at ±0.08 mm (Festo) or ±0.3–0.5 mm (igus; marginal for ±0.5 mm without vision correction); arm covers a 1.3 m sphere at the sewing zone | custom multi-head carriage design and controls (R05 PLC/EtherCAT motion); 3 m beam stiffness; gantry is non-collaborative (cell is guarded anyway); single arm cannot do two-handed seam presentation |
| (b) Two cobots on seventh-axis tracks | 2 × UR10e (USD 99,192) or 2 × Doosan M1013 (EUR 67,000); 2 × Vention 7th axis (≈ USD 7.8k each at ~1.5 m; Rollon CTU >5 m stroke, quote) or Güdel CMF; pedestals/safety modules (USD 2–4k) | **≈ USD 85–130k** (sourced arm prices + Vention design price; **est.** for tracks >3 m) | arm TCP 1–4 m/s, track ≈ 1–2 m/s; ply transfer ≈ 5–8 s per arm; two arms work in parallel and can do dual-arm handoffs/sewing (Tang et al.) | a 1300 mm-reach arm on a track along the long edge reaches only ~1.3 m across; covering 1.5 m width needs a centre-line track, UR20 (1750 mm, USD 62,990) or UR10g-1750; accuracy ±0.05 mm arm + ±0.05 mm track | highest cost; two arm controllers to coordinate; arms over a vacuum bed need collision-free planning (M09/M13); flange F/T too coarse for ply tension |
| (c) Delta or SCARA for pick + one cobot for sewing | ABB IRB 360-3/1130 or -6/1600 (quote) **or** igus DLE-DR 600 mm (RBTX price) **or** Omron i4-850H / Epson GX8-B 650 SCARA (quote); + UR7e (USD 38,363) or Doosan A0912 | **≈ USD 60–110k est.** (delta/SCARA quote-only; cobot sourced) | fastest picks (0.3–0.5 s cycles, 60–100 picks/min) — >50× more than needed | delta Ø1.13–1.6 m or SCARA 0.65–0.85 m radius covers only part of the 3 m × 1.5 m bed: the cut bed/conveyor must index plies under the picker (acceptable at the ST02→ST03 exit, not for whole-bed coverage); IRB 360 supplementary arm load only 350 g limits large vacuum heads | speed is wasted; two different robot ecosystems to integrate; delta needs overhead frame; reorientation of long sleeves limited to axis 4 |

Recommendation from the comparison: **(a)**, with the gantry sized for ±0.1 mm-class belt axes (Festo EGC-TB-KF family through HGO, or Rexroth MKR) and vision-corrected placement, plus one 1300 mm-class cobot at the sewing-presentation position. Option (c) is the natural upgrade for the ST02→ST03 exit if a single-ply conveyor exits the cutter, and option (b) is the research path for two-arm cooperative sewing (Stage 3 in the white paper roadmap).

