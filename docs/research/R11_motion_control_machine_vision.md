# R11 · Motion control and machine-vision engineering practice (2026)

Research agent R11 · written 2026-10-21 · scope per `_BRIEFS.md` §R11. Stations and modules use the IDs in `_BRIEF_COMMON.md` (ST00–ST10, M01–M14). All prices carry currency, date seen (2026-10-21 unless stated) and basis. Anything older than 2023 is flagged "possibly stale".

<!-- SUMMARY_PLACEHOLDER -->

## Findings

### 1. Motion architectures

#### 1.1 PLC-centric: Beckhoff TwinCAT 3 (NC PTP / NC I / CNC, XAR runtime)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| TwinCAT 3 XAE (engineering) | 3.1 (current, 2026) | Free of license cost for PLC programming; TExxxx engineering tools and TCxxxx/TFxxxx runtime licenses are paid, priced by "platform level" of the IPC | Industry standard; vendor-maintained | High: deterministic PLC + NC in one runtime on an industrial PC; EtherCAT master included | [1] |
| TwinCAT 3 NC PTP (TF5000, 10 axes; TF5010/5020 more axes) | current | Runtime license, platform-level priced; price not published, request quote via Beckhoff sales | Mature | High for ST01/ST03/ST04/ST06 axes (PLCopen MC function blocks, camming, flying saw add-ons) | [2] |
| TwinCAT 3 Machine Learning: TF3800 (classical ML), TF3810 (neural nets), TF3820 ML Server (separate process, GPU), TF7810 Vision NN | current, "regular delivery" | Runtime licenses by platform level (e.g. TF3810-0v40…-0v94) | Vendor-maintained since 2019; ONNX import | Medium: lets ONNX models run cycle-synchronously in the XAR; useful for small classifiers (e.g. grip-success, tension anomaly) but not for camera DNNs at ST10 rates | [3][4] |
| TwinCAT 3 Vision (TF7100 Base, TF7200 Matching 2D, …) | current | Runtime license, Windows 10/11, platform levels 50…94 | Vendor-maintained | Medium: GigE Vision in the real-time context; limited algorithm set vs OpenCV; useful for simple registration in the PLC | [5] |
| TwinCAT hard real time on VMs | — | — | — | Not supported by Beckhoff for hard real time; run XAR on a physical IPC | [1] |

Key facts (vendor, [1]–[5]): TwinCAT 3 Engineering is free; runtime licensing cost scales with the IPC platform level; Beckhoff states hard real time cannot be guaranteed on a virtual machine. TF3800/TF3810 execute ONNX models "synchronously and deterministically on the CPU" in the XAR; TF3820 runs models in a separate process with GPU support and "near real time" behaviour [3]. EtherCAT (Beckhoff system properties page): update of 1,000 distributed I/Os in 30 µs, communication with 100 servo axes in 100 µs, distributed-clock synchronisation with jitter "significantly less than 1 microsecond" [6]. TwinCAT sets the EtherCAT Sync-Unit cycle equal to the PLC/NC task cycle by default [7].

#### 1.2 PC-centric open-source motion stacks (cutter gantry and secondary axes)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| LinuxCNC | 2.9.10 released 2026-07-09 (2.9.9 withdrawn 2026-07-03); 2.10 is the development branch (2.10.0~pre1 docs) | GPLv2 | Very mature (since EMC, 2000s); active GitHub issue tracker (issues filed Oct 2026); packaged in Debian since Bookworm | High for ST02 cutter gantry: trajectory planner, HAL, servo or step/dir, EtherCAT via external HAL driver (see 1.3), tangential-knife possible via HAL/kinematics (see §2) | [8][9][10] |
| Machinekit (HAL fork of LinuxCNC) | no confirmed 2025–2026 release found in this research | LGPL/GPL mix (per repo) | Low activity compared with LinuxCNC (unverified; no release page located) | Low: superseded by LinuxCNC 2.9/2.10 for new builds | unverified |
| grblHAL | Rolling releases on GitHub; drivers for NXP iMXRT1062 (Teensy 4.x), RP2040/RP2350, STM32F4xx, LPC176x, and others | GPLv3 (core) | Active organisation with many driver repos (2026) | Medium for ST02 if the cutter is a simple XY(+C) step/dir gantry with no EtherCAT; no closed-loop servo feedback in the controller | [11] |
| MASSO G3 Touch (standalone, PC-less) | current; tiers Essential/Core/Advanced/Professional | Proprietary; software tiers unlocked by licence | Commercial, small vendor (Australia) | Medium: up to 5 axes step/dir, 110 kHz pulse rate per axis, 24 inputs / 18 outputs; no EtherCAT; no network motion API documented for AI supervision | [12][13] |
| Centroid Acorn (4 axes) / AcornSix (6 axes) | current | Proprietary; CNC12 "Free" software included, Pro/Ultimate paid | Commercial (USA); 1 GHz ARM Cortex-A8 motion CPU, Ethernet link to a CNC PC | Medium: step/dir only; CNC12 has an API (CentroidAPI) but no EtherCAT; good value for a stand-alone knife gantry | [14][15] |
| PlanetCNC (Mk3/Mk4) | — | Proprietary | Small vendor; tangential-knife function advertised (not verified in this research) | Low–medium: USB/Ethernet step/dir controllers; unverified current pricing | unverified |

Prices (reseller/vendor pages, seen 2026-10-21): MASSO G3 Touch AU$1,546.82 (Essential) to AU$3,632.42 (Professional) on masso.com.au [12]; US$1,039 base + US$300/750/1,350 for Core/Advanced/Professional tiers at cnc4pc.com [13]. Centroid Acorn kit US$369 [14]; AcornSix kit US$999 (product page) / US$1,099 (page schema), vendor shop [15].

#### 1.3 EtherCAT master stacks

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| IgH EtherCAT Master (EtherLab) | 1.6.13 (documentation build 2026-10-14) | GPLv2 kernel module; LGPL 2.1 userspace library | Reference open-source master; Linux only; DC support (offset and drift compensation to the reference clock); used by LinuxCNC-EtherCAT and ros2 ethercat_driver | High for a Linux/ROS 2 or LinuxCNC backend (M09 physical backend) | [16][17] |
| SOEM (Simple Open EtherCAT Master), now maintained by rt-labs | 2.x (OpenEtherCATsociety GitHub) | GPLv3 or commercial licence from rt-labs; users must also obtain an EtherCAT master licence from Beckhoff for products | Mature, portable (no kernel module), weaker DC/error handling than IgH or acontis per acontis' comparison | Medium: good for embedded/bare-metal masters (e.g. a sewing-head coordinator MCU); GPLv3 is viral for closed products | [18][19] |
| acontis EC-Master (Class A/B) | 3.2 (user manual edition 2026-05-18; Class A manual 2026-02-06) | Commercial; runtime license keyed to the EtherCAT NIC MAC address; price not published, request quote | Commercial stack with the most complete DC "DCM" sync and error handling in its own comparison; Linux, Windows, RTOS | High if a supported commercial master with DC sync is wanted on Linux/PREEMPT_RT without GPL obligations | [20][21][19] |
| Beckhoff TwinCAT XAR (integrated EtherCAT master) | current | Part of TwinCAT runtime licence | Industry reference | High when the PLC-centric architecture is chosen (§Recommendation) | [1] |

acontis' own (vendor) comparison states that IgH packs acyclic data into cyclic frames, that SOEM lacks continuous propagation-delay compensation, and that neither open-source stack reports DC out-of-sync or init-command errors "out of the box" [19]. The IgH manual notes a theoretical cycle rate up to ~100 kHz for a ~10 µs realtime cycle but warns this remains theoretical [16].

#### 1.4 ROS 2 ros2_control with EtherCAT and measured real-time behaviour

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ros2_control (controller_manager) | Rolling docs Sept–Oct 2026; Kilted/Jazzy LTS | Apache-2.0 | Core ROS 2 framework | High for ST04 arm/gantry skill execution (M08/M09) above an EtherCAT hardware interface; `update_rate` default 100 Hz, settable to 1,000 Hz; main thread requests SCHED_FIFO priority 50 | [22] |
| ethercat_driver_ros2 (ICube Robotics, Strasbourg) | `jazzy` default branch; repo created 2022-05-13; 91 commits | Apache-2.0 | Builds on IgH master; CiA402 drive examples in a companion repo | High: generic EtherCAT hardware interface (CiA402 drives, Beckhoff EL I/O terminals) for ros2_control | [23][24] |
| PREEMPT_RT (mainline) | Merged for Linux 6.12 (rc1 2024-09-30), x86/arm64/riscv; EXPERT-gated config option | GPLv2 | Mainline since 6.12; Ubuntu "Real-time Ubuntu", Debian `linux-image-rt-amd64/arm64` | High: no out-of-tree patches needed; use `isolcpus`/`nohz_full`/`irqaffinity` and pin the control thread | [25][26][22] |

Measured numbers (user report on the ICube driver issue tracker, Jan 2024, PREEMPT_RT, isolated core for the control loop, IgH module and NIC IRQ threads): cyclictest latencies "consistently under 100 µs even under 100 % system load"; 1 kHz loop achievable; EtherCAT frame-release jitter average ±85 µs, worst ±400 µs; over 1,000,000 frames the average frame release interval was 1.000 ms with a maximum of 2.024 ms and 0.043 ms average receive delay. The reporter attributed jitter to computation inside `read()`/`write()` gating the frame release [27]. Interpretation for this project: a Linux/ROS 2 EtherCAT loop at 1 kHz is practical for gantry/arm coordination, but worst-case jitter of hundreds of µs means the drive-level current/velocity loops must close inside the EtherCAT drives (CiA402 CSP/CSV with distributed clocks), not in the PC.

#### 1.5 Cycle rates and distributed clocks

- EtherCAT: 100 axes in 100 µs; DC jitter well below 1 µs (Beckhoff) [6]. Default DC sync-unit cycle = task cycle [7].
- The IgH master supports DC with master-side offset/drift compensation [16]; acontis adds "DCM" modes to compensate master/slave drift and reports DC status notifications [21].
- Practical rule used in industry (vendor data above + the measured ROS 2 numbers [27]): 1 kHz (1 ms) EtherCAT cycle for PC/ROS 2 masters on PREEMPT_RT; 2–4 kHz (250–500 µs) is routine on TwinCAT with an IPC; sub-100 µs cycles are a TwinCAT/XFC niche. Position-loop update inside modern EtherCAT servo drives is far faster than the bus cycle (see AX8000 figures in §1.6 if confirmed), so the bus cycle sets command granularity and vision-to-motion latency, not loop stability.

#### 1.6 Safety separation: STO/SS1/SLS via FSoE / PROFIsafe

| Vendor | Model / part number | Key specs | Price (currency, date, list/quote/est.) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | EL6910 TwinSAFE Logic | FSoE logic terminal; cycle approx. 1 ms (project-size dependent); 212 safe connections, 512 FBs; FSoE + PROFIsafe master/slave; EN ISO 13849-1 Cat. 4 / PL e, IEC 61508 SIL 3; E-bus 160 mA | price not published; request quote (Beckhoff sells direct) | not published | STEP/EPLAN macros via Beckhoff product page "Documentation and downloads" (vendor) | [28] |
| Beckhoff | EL1918 (8 safe inputs with integrated TwinSAFE Logic; EL1918-2200 without logic) | 8 fail-safe 24 V inputs; integrated logic equivalent to EL6910 limited to 128 connections; Cat. 4 / PL e / SIL 3 | price not published; request quote | not published | vendor product page downloads | [29] |
| Beckhoff | AX8000 multi-axis servo system, option -0100 (STO/SS1 via FSoE); -x2xx safe-motion variants | STO, SS1-r/-t via digital inputs or FSoE; safe motion set (SS2, SOS, SLS, SSM, SMS, SSR, SDIp/n, SLP, SAR, SBC…) listed on the TwinSAFE safe-drive page; ETG listing marks several functions "in preparation" (possibly stale) | price not published; request quote | not published | STEP via Beckhoff product pages | [30][31] |
| Omron | 1S-series servo with built-in EtherCAT and SS1/SLS | SS1/SLS sub-functions over FSoE to NX safety CPU; safety task cycle at the Safety CPU up to 6 ms max in the example timing | price not published; request quote/distributor | — | Omron CAD downloads (vendor) | [32] |
| Yaskawa | White paper: safety functions in servo drives (STO, SS1, SS2, SOS, SLS, SLA, SSR, SSM) | Definitions and velocity/time diagrams; FSoE/PROFIsafe/CIP Safety overview; iC9226-FSoE controller mentioned | — | — | — | [33] |

Design implication: a certified safety PLC (TwinSAFE logic terminal or equivalent) owns e-stops, guard interlocks, light curtains and the drives' STO/SS1 via FSoE; the standard PLC/NC and any AI/ROS 2 process never sit in the safety path. The ~1 ms logic cycle plus FSoE watchdog and drive reaction times gives total safety reaction times in the low tens of ms (project-specific; compute per EN ISO 13855 stopping-distance rules, not covered here).

#### 1.7 Vendor "AI motion" claims and motion-skill products

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| Siemens AI Motion | 2025–2026 product page | Commercial; "contact us for pricing" | Reinforcement learning trained on a digital twin; deployed as SCL function block on SIMATIC S7 PLC or as Python on Industrial Edge via AI Inference Server; Sollas packaging reference 160 vs 120 boxes/min | Low–medium: interesting for ST01 unwind/tension or conveyor-flow optimisation, locked to Siemens PLC/Edge | [34] |
| Beckhoff TwinCAT Machine Learning (TF38x0/TF78x0/TE3850) | current | Commercial runtime licenses | ONNX inference in the real-time XAR; TE3850 "ML Creator" auto-trains models | Medium (see §1.1) | [3][4] |
| Micropsi Industries MIRAI 2 | current product page | Commercial; "get a quote" | Berlin company (founded 2014, Series B 2022, small headcount per Tracxn) ; MIRAI 2 runs on a rail-mount 24 V industrial PC, cloud-based training service plus app; no force-torque sensor required; skills can stop on unexpected conditions | Medium for ST04 fine positioning (edge-to-foot alignment) as a vision-guided "skill"; vendor lock-in and camera-in-hand assumptions | [35][36] |
| Intrinsic Flowstate | technical specifications effective 2026-07-08 | Commercial (subscription; pricing on request) | Google/Alphabet subsidiary; requires an IPC running IntrinsicOS (Linux) between Flowstate and robot controllers; AI capabilities: perception/pose estimation, motion planning, insertion | Low–medium: strong for arm-centric cells; no textile-specific skills; pricing not published | [37][38] |

### 2. Cutter and gantry control (ST02)

| Vendor | Model / part number | Key specs | Price (currency, date, list/quote/est.) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Zünd | G3 / S3 / D3 digital cutters with Zünd Cut Center (ZCC) | Complete systems (controller + software, not sold as separate controllers); S3 sizes M 1330 mm wide × 830/1230/1630 mm, L 1800 × 1230/1630, XL 2270 × 1230 mm; Electric Oscillating Tool (EOT) with 0.5 mm or 1.0 mm stroke, "very high stroke frequency"; Driven Rotary Tool up to 1,000 mm/s; vacuum area divided into zones switchable individually across the width (G3); ITI automatic tool initialisation; D3 dual beam up to 3 tools per beam | price not published; request quote (est. tens of thousands USD for an S3 M, basis: general market knowledge, unverified) | not published | no public STEP; request from Zünd | [39][40][41][42] |
| Zünd | Zünd Cut Center (ZCC) | Modular software: Basic/Advanced editions, file import, cutting-data optimisation, cutter management, remote monitoring | price not published | — | — | [43][44] |
| MASSO | G3 Touch | see §1.2 | AU$1,546.82–3,632.42 (vendor, 2026-10-21) | in stock (vendor) | none (controller enclosure drawings only) | [12] |
| Centroid | Acorn / AcornSix | see §1.2 | US$369 / US$999–1,099 (vendor shop, 2026-10-21) | in stock (vendor) | — | [14][15] |
| LinuxCNC + Mesa or EtherCAT I/O | 2.9.10 | GPLv2 | see §1.2 | best open option for a closed-loop knife gantry with C-axis tangential control and vacuum-zone I/O in HAL | [8] |
| grblHAL on Teensy 4.1 / RP2350 | rolling | GPLv3 | see §1.2 | lowest-cost option for an open-loop step/dir gantry | [11] |

<!-- SECTION2_CONTINUES -->
