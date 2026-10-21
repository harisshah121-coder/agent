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

