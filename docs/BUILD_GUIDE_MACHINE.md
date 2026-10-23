# Build Guide 1: The Machine (v1, 2026-10-22)

The physical roll-to-garment cell: every station, the real parts selected for the first (development) cell, how they connect, how to build, commission and test it. Identifiers come from `ARCHITECTURE_SPINE.md`; every part ID is a row in `spine/parts.csv`; each decision cites the research report that holds its sources (`research/Rnn_*.md`, with URLs).

**How to read prices.** Prices are USD, dated 2026-10-21, labelled list / reseller / estimate in `parts.csv`. Many industrial parts are quote-only; those carry an engineering estimate and a "request quote" action in §7.

**What this cell is.** A development cell that proves the process: roll in, accepted premium T-shirt out, measured interventions. It is deliberately over-instrumented and built from catalogue parts with documented interfaces. The cost-down to the white paper's production price is a separate engineering step (§7.3).

---

## 1. Scope and product specification

### 1.1 The product (first SKU)
| Item | Specification | Source |
|---|---|---|
| Garment | Premium short-sleeve crew-neck T-shirt, 5 cut pieces: front, back, 2 sleeves, neck rib | R16 F1, F5 |
| Body fabric | Cotton single jersey 160–220 g/m², open width ~180 cm, relaxed 24 h before cutting (unrelaxed jersey shrinks 5–7 % × 3–5 %) | R16 F4; R01 §H |
| Rib | 1×1 cotton rib (with elastane optional), strip ~25–40 mm finished | R16 F4; R03 |
| Seams | 514 overlock (shoulders with tape, sleeves, sides); 406 coverstitch (sleeve hems, bottom hem, neck topstitch); 301 lockstitch only if labels are specified | R04 Decision 1–4; R16 F2 |
| Needles | Groz-Beckert SES ball point Nm 65–75 (DC×27 overlock, UY128GAS coverstitch) | R04 Decision 7 |
| Thread | Coats Epic Tex 24 needle, Gramax Tex 18 looper, ~45 m per tee | R04 Decision 7 |
| Quality | AQL-based acceptance, dimensional tolerance per size chart, ISO 6330 wash and ASTM D1683 seam strength in validation | R16 F7; R14 F13 |

### 1.2 Operation sequence the machine executes
| OP | Operation | Station | Machine | Notes |
|---|---|---|---|---|
| OP-01-cut | Single-ply cut of all 5 pieces from relaxed web | ST02 | conveyor knife cutter | Piece identity = cut location + job metadata |
| OP-02-extract | Lift pieces off bed, remove skeleton, stage in kit order | ST03 | gantry pick head T1/T4 | Single ply guaranteed by the cutter bed |
| OP-03-shoulder | Join both shoulders with tape | ST05 | 514 overlock | |
| OP-04-rib-make | Meter, cut, close rib loop | ST06 | in-house rib unit | Lockstitch or overlock end-join |
| OP-05-rib-attach | Attach rib to neckline, rib stretched, body not | ST06 | cylinder-arm overlock + expansion rollers | Stretch comes from handling; no head has electronic differential feed (R04) |
| OP-06-neck-top | Back-neck tape / neck topstitch | ST05 | 406 coverstitch | Premium expectation |
| OP-07-sleeve-hem | Hem both sleeves flat, before set-in | ST05 | 406 coverstitch | Flat hemming avoids tubular feeding (R16 F1) |
| OP-08-sleeve-set | Set both sleeves | ST05 | 514 overlock | Curved seam; the hardest automated seam |
| OP-09-side | Close sides and underarms, insert care label | ST05 | 514 overlock | |
| OP-10-bottom-hem | Bottom hem | ST05 | 406 coverstitch (cylinder bed) | Tubular |
| OP-11-inspect | Trim check, measure, defect check, accept/reject | ST07 | backlit table + 16 MP camera | Sequence finishes right-side-out; no turning machine exists (R08) |

### 1.3 Takt budget (arithmetic)
Shift 720 min; availability A = 0.80; yield Y = 0.95 (white paper factors). Required running completion interval c = 720 × 0.80 × 0.95 / 100 = **5.47 min per attempt** (R16 F9). Human SAM for a tee is 6.5–8.5 min, so the cell must pipeline 3–4 shirts in process at once. Per-station budgets (machine-readable in `spine/takt.csv`):

| Station | Budget / estimate | Status |
|---|---|---|
| ST01 | 0.5 min | overlaps cutting |
| ST02 | 1.5 min | cutter speed data |
| ST03 | 2.0 min | 5 picks + skeleton |
| ST04 | 4.8 min (est. occupancy) | **bottleneck: measure first** |
| ST05 overlock / coverstitch | 3.0 min each (est.) | separate heads, run in parallel |
| ST06 | 2.3–3.0 min (est.) | **unmeasured: measure first** |
| ST07 | 2.0 min | depends on vision plan |

Bottleneck ST04 at 4.8 min gives 720 × 0.8 × 0.95 / 4.8 ≈ 114 accepted shirts per shift. The margin is thin. Mitigation built into the design: ST03 extraction runs on its own gantry carriage so ST04's arm only does sewing presentation (R02 F10, option a).

## 2. Cell architecture and layout

### 2.1 Architecture decision
Selected (R02 F10 option a): **one servo belt gantry with 2–3 pick heads over the cutter exit and staging area, plus one 6-axis cobot at the sewing-presentation position**. Rejected: two cobots on tracks (USD 85–130k hardware, more safety zoning); delta/SCARA pick (fast, but a second controller and small envelope). Evidence: every production textile result in 2025–2026 is a structured cell with deterministic motion and perception; learned models live inside bounded skills (R10 D1).

### 2.2 Floor plan (development cell)
```
 ← 6.0 m guarded envelope (ST00) →
 ┌──────────────────────────────────────────────────────────────┐
 │ ST01 roll   │ ST02 conveyor cutter 1.6×2.5 m bed │ ST03 stage │  ↑
 │ let-off +   │ (over-bed 24 MP camera, ST10)      │ table      │  3.0 m
 │ edge guide  │══════ ST04 gantry X 3 m (Festo EGC) ═══════════│
 │             │ ST05 overlock │ ST05 coverstitch │ ST06 collar  │
 │             │      ← UR10e on pedestal (ST04) →               │
 │ cabinet ST09│ ST07 backlit inspection table → discharge belt  │  ↓
 └──────────────────────────────────────────────────────────────┘
   operator side: HMI, light curtains at roll-load and output openings
```
Footprint ≈ 6 m × 3 m inside guarding plus a 1 m operator aisle (R07 §1e layout assumption). Final positions come from the 3D model reach study (Guide 3, checkpoint C3).

### 2.3 Utilities
| Utility | Requirement (est.) | Basis |
|---|---|---|
| Power | 400 V 3-ph (or 208/480 V US) ~25–30 kW connected: cutter vacuum blower 5.5–7.5 kW, servos, compressor, compute | R01 §I; R05 F10 |
| Air | 6 bar, dry, ~300–500 l/min peak for needle grippers, ejectors, air knife, cylinders | R05 F9; R03 |
| Network | Isolated cell LAN: EtherCAT (control), GigE/5GigE vision VLAN, PTP time; one uplink to office/cloud through a firewall | R05 F8, F12; R14 F16 |
| Environment | 20–25 °C, 50–65 % RH controlled (knit dimension, static and needle behaviour); lint extraction at cutter and heads | R14 F7; R16 F4 |

## 3. Stations: function, parts, integration, build steps, acceptance tests

Each station lists requirements (REQ), selected parts (P-IDs, priced in §7), integration, build steps and acceptance tests (TST).

### 3.0 ST00 Frame, guarding, infrastructure
- **REQ-ST00-01** Rigid modular frame for gantry and machine bases; gantry frame deflection ≤ 0.1 mm under 20 kg payload at mid-span (est. design target).
- **REQ-ST00-02** Full perimeter guarding with interlocked, guard-locking doors (ISO 14120, ISO 14119) and light curtains at material openings (ISO 13855 distances). (R14 F4)
- **Parts**: P-ST00-001 extrusion frame and guarding set, P-ST00-002 fasteners, P-ST00-003 cabling kit, P-ST00-004 air supply, P-ST00-005 printer.
- **Build**: (1) Level floor check; (2) assemble base frames with levelling feet; (3) gantry columns and beams, align to ±0.2 mm with a laser level; (4) mount guarding panels and doors; (5) cable trays and energy-chain routes; (6) air drop with FRL and dump valve.
- **TST-ST00-01** Gantry rail parallelism ≤ 0.1 mm/m; **TST-ST00-02** every door interlock opens STO group within the response time used in the ISO 13855 calculation.
- Note: R07 found the frame+guarding subtotal (≈ USD 17,400) alone exceeds the white paper's conservative USD 15,000 line before air and cabling.

### 3.1 ST01 Roll handling
- **REQ-ST01-01** Accept knit rolls up to 1.8 m open width, 25–60 kg; low-tension unwind (knit must not be stretched before cutting).
- **REQ-ST01-02** Lateral edge position held to ±1 mm at cutter entry.
- **Parts**: P-ST01-001 driven let-off with dancer, P-ST01-002 E+L edge guide, P-ST01-003 static bar, P-ST01-004 roll lifter.
- **Integration**: let-off servo on EtherCAT (IF-ST01-ST09-DATA-01); dancer position analogue; edge sensor IO-Link; web enters the cutter conveyor at belt height (IF-ST01-ST02-MECH-01). Relaxation is done offline 24 h (R16 F9); an in-line relaxing conveyor is a later option.
- **Build**: mount let-off frame; fit shaft/cradle rollers; install dancer and diameter sensor; mount edge guide upstream of the cutter infeed; fit static bar across web 50–100 mm above.
- **TST-ST01-01** Run 50 m of jersey: edge deviation ≤ ±1 mm; web length growth vs. unrelaxed reference measured and recorded to M05.

### 3.2 ST02 Cutting
- **REQ-ST02-01** Single-ply cutting of jersey on a vacuum conveyor; cut accuracy at the fabric ≤ ±0.5 mm on straight edges; notches cut.
- **REQ-ST02-02** Machine-readable job load, start, done and fault; known piece locations after each index.
- **Selected**: P-ST02-001 iECHO TK4S-2516 with conveyor and cradle feeder (FOB USD 20–40k; driven rotary and oscillating tools; DXF/HPGL/ISO input). **Alternate (preferred if budget allows)**: used Zünd G3 L / S3 L with conveyor (est. USD 40–90k), the best-documented integration (ZCC Modbus TCP pick-and-place interface, REST KPIs, hot folders) (R01 §I).
- **Why not build one**: the component route costs ≈ USD 17–20k for cutting plus USD 6–10k for roll handling before labour, about 2× the white paper's allowance, with no safety-certified controller (R01 §I).
- **Fabric facts**: jersey curls when cut free; fabric-side error dominates machine accuracy (machines are ±0.1 mm class, knife-force shift up to 2 mm); use a driven decagonal rotary blade for jersey and a 0.63 mm oscillating blade for tight radii (R01 §H).
- **Integration**: marker from M04 (IF-M04-ST02-DATA-01); vendor API to PLC (IF-ST02-ST09-DATA-01); over-bed 24 MP camera verifies cut completeness and piece pose before pick (IF-ST02-ST10-DATA-01). Inkjet DataMatrix on seam allowance optional for traceability (R01 §F).
- **Build**: place cutter on levelled pads aligned to gantry datum; connect blower, air, power; install vendor software on a dedicated PC in the vision VLAN; calibrate bed to camera with a printed calibration target.
- **TST-ST02-01** Cut 20 front panels: perimeter error vs. pattern ≤ ±0.5 mm (95th percentile) measured by ST10; **TST-ST02-02** 100 consecutive indexes with zero lost piece identities.

### 3.3 ST03 Extraction and buffer
- **REQ-ST03-01** Pick each piece singly off the bed and place it on the staging table in kit order; success ≥ 99.9 % per pick as the long-run target (200-cycle sample test first).
- **Parts**: T1 wide needle bar of 6 × P-ST03-001 Schmalz SNG-M 4 0.8 on an aluminium profile with P-ST03-002 EXAIR air knife; T4 P-ST03-004 Piab KCS 150 pad with P-ST03-005 Festo OVEM ejector; P-ST03-003 ultrasonic double-ply sensor. Tools ride the ST04 gantry carriage via the tool changer (IF-ST03-ST04-MECH-01).
- **Key facts**: needle grippers are the only catalogue technology whose hold does not depend on porosity; use Ø0.8 mm needles, ≤ 2 mm effective stroke and run a 1,000-cycle wash test for needle marks; fabrics reduce achievable vacuum, so foam vacuum is for stabilising, not carrying; electroadhesion is not purchasable in 2026 (R03 Summary).
- **Cutter-bed compatibility**: at a 30° plunge a 3 mm stroke penetrates ≈1.5 mm; confirm the felt/bristle bed tolerates needle tips, or lift an edge first (R03).
- **TST-ST03-01** 200 picks of front/back/sleeve/rib off the bed: zero double picks, ≤ 1 miss, no visible needle marks after ISO 6330 wash.

### 3.4 ST04 Manipulation
- **REQ-ST04-01** Cover 3 m × 1.5 m with 2–5 kg payload; place plies at sewing stations to ±0.5 mm (vision-corrected).
- **Selected**: P-ST04-001 Festo EGC belt gantry (X 3000 mm, 2 × Y 1500 mm, Z) with CMMT-AS EtherCAT drives; P-ST04-002 UR10e on a pedestal at the sewing stations; P-ST04-003 ATI QC-11 tool changer; tools T1–T4 (§3.3, P-ST04-004 Robotiq 2F-85 with printed hard tips as T3); P-ST04-005 GelSight Mini tactile tip; P-ST04-006 RealSense D405 wrist camera. Prototype alternate for the gantry: Vention belt gantry.
- **Why UR10e**: ROS 2 driver (Universal_Robots_ROS2_Driver), RTDE at 500 Hz for external guidance, MuJoCo Menagerie model, free STEP, PL d safety functions (R02 F1.1, F9; R15). Alternates: FANUC CRX-10iA/L, Doosan M1013 (R02 F1).
- **Gripper toolbox**: T1 needle bar (panels), T2 small needle head (rib), T3 pinch/edge gripper with tactile tip (alignment at heads), T4 vacuum pad (stabilise), T5 driven-roller edge feeder (phase 2, in-house) (R03 Recommendation).
- **Integration**: gantry via TwinCAT NC PTP; UR10e via RTDE from ROS 2 (IF-ST04-ST09-DATA-01); STO wiring of both to TwinSAFE (IF-ST04-ST09-ELEC-01).
- **TST-ST04-01** Reach and collision check in simulation before purchase (Guide 3 C3); **TST-ST04-02** place 50 sleeves at the overlock: edge-to-needle offset ≤ ±0.5 mm (measured by needle camera).

### 3.5 ST05 Sewing heads
- **REQ-ST05-01** Permanently threaded 514 and 406 heads, PLC-controlled start/stop/speed/trim/foot, stitch counting, thread-break detection.
- **Selected**: P-ST05-001 JUKI MO-6814S overlock (USD 1,550, 7,000 sti/min, differential 1:0.6–1:4); P-ST05-003 JUKI MF-7923 UT51 coverstitch (USD 7,226; first-rig alternate Jack W4-UT USD 1,924–2,199); P-ST05-002 EFKA AB321A or JUKI SC-922 boxes with documented I/O (EFKA in1–i10/M7–M11 and 512-pulse output; SC-922 CN51 8 in/8 out, 360-pulse output); P-ST05-004 Eltex 15965 thread sensors; consumables P-ST05-005 (R04 Decisions 1, 2, 5, 7).
- **Control pattern**: OEM box driven by PLC I/O for the first rig; move to an EtherCAT servo replacing the OEM motor (DLRoSS pattern) only where the robot must synchronise feed with the needle (R04 Decision 5).
- **Speed**: plan 2,500–4,500 sti/min for robot-fed seams on jersey (est.).
- **Honest risk**: robot-fed overlock of a curling single-jersey free edge with a curved seam has not been demonstrated publicly; research covers stiffened wovens and straight stretch seams with hand-placed lead-ins (R04, R12). This is the program's first bench experiment (§10).
- **Build**: mount heads in custom tables per manual cut-out drawings; fit pneumatic foot lift and trimmers; wire box I/O to EL1008/EL2008; route rotation pulse to a fast counter; fit needle cameras (ST10) and thread sensors.
- **TST-ST05-01** 100 straight 514 seams robot-presented on jersey: seam on-edge within ±1 mm, zero skipped stitches; **TST-ST05-02** 50 set-in sleeves: puckering grade ≥ 4 (AATCC 88B-style visual scale).

### 3.6 ST06 Collar/neckband module
- **REQ-ST06-01** Meter, cut and close the rib loop; attach with rib stretched to neckline and body unstretched; symmetric quartering.
- **Selected**: P-ST06-001 cylinder-arm overlock (JUKI MO-6814S class or Kansai Special JJT5014GH-01M); P-ST06-002 in-house expansion-roller loader and rib meter/cut/close unit modelled on Atlanta Attachment 1289/1278-6 and 1996 (bought-in operator-loaded workstations are quote-only, est. USD 30–60k) (R04 Decision 3).
- **Evidence to copy**: roller stretch sewing of different-length stretch plies (Jin 2025) maps directly onto this module (R12).
- **TST-ST06-01** 50 neck attaches: rib stretch ratio within ±3 % of target, no twist, no captured layer (collar camera).

### 3.7 ST07 Finishing, inspection, output
- **REQ-ST07-01** Measure key dimensions to ±2 mm, detect visible defects, discharge accepted shirts, divert rejects.
- **Selected**: P-ST07-001 Basler 16 MP camera over P-ST07-002 backlight tiles (≈0.15 mm/px over 800 mm); P-ST07-003 mk GUF-P 2000 or Dorner 2200 discharge belt with flipper gate. Thread tails handled by head trimmers plus ionising blow-off; no turning machine (none exists); no pressing needed for cotton jersey (R08 Recommendation A).
- **Optional modules** (outside the base envelope): Thermotron STP1000 folder (USD 50,000) + PV40 bagger; Brother GTXpro DTG trio (est. USD 45–60k); Tajima TMEZ-SC embroidery (R08 B).
- **TST-ST07-01** 30 shirts measured by camera vs. tape measure: chest, length, sleeve within ±2 mm; known-defect set detected ≥ 95 %.

### 3.8 ST08 Optional decoration
Not in the base cell (qty 0 in `parts.csv`). Embroidery is the first decoration to add (Tajima TMEZ-SC 1501, LAN via DG17/PulseID, clamp frame loaded by ST04); DTF pressed in-cell is the easier print route. No vendor publishes a PLC start input; physical start is a button on every machine reviewed (R08).

### 3.9 ST09 Control and safety
See §4. Parts P-ST09-001 to -014.

### 3.10 ST10 Vision and compute
Per-station camera plan from R06 F11 (FOV and resolution math there): 24 MP over-bed camera at 0.28 mm/px (P-ST10-002), needle-area cameras at ≥ 200 fps ROI (P-ST10-003), 5 MP placement/collar cameras with backlights (P-ST10-004), 16 MP inspection (P-ST07-001), cell IPC with RTX 4000 SFF Ada (P-ST10-001), Jetson AGX Thor for policy development (P-ST10-005). Line-scan web inspection (P-ST10-006) deferred. Reference vision build ≈ USD 38–48k; minimum ≈ USD 18–22k (R06 F11).

## 4. Electrical and control architecture

### 4.1 Who does what
| Layer | Hardware | Runs | Never does |
|---|---|---|---|
| Safety | Beckhoff TwinSAFE EL6910 + safe I/O (FSoE) | E-stop, door locks, light curtains, STO/SS1 groups, air dump | Accept commands from software |
| Deterministic control | Beckhoff C6030, TwinCAT 3 NC PTP over EtherCAT | Gantry, let-off, collar module, conveyors, sewing box I/O, interlocks with machines | Perception or planning |
| Robot | UR10e controller (own safety) | Joint control; RTDE external guidance | Override cell safety |
| Planning and perception | Linux PC with ROS 2 (Jazzy LTS) + vision IPC | Skills, behaviour trees, perception, logging | Write safety, command drives directly |

This split is identical on every mainstream platform (R05 F1). Beckhoff is selected for EtherCAT-native drives and I/O, TwinSAFE on the same bus, ADS/OPC UA access from Python and ROS 2, and published terminal prices. Alternates: Bosch Rexroth ctrlX CORE (official ROS 2 support, software safety PLC app since Oct 2025); Siemens S7-1500F if a customer mandates it.

### 4.2 I/O budget (est., R05 F13)
26 axes (12 high-performance, mostly the Festo gantry drives and cutter's own controller; 14 economy), 82 DI, 75 DO, 12 analogue/IO-Link, 26 safe DI, 12 safe DO, 3 lock outputs. Covered by P-ST09-002/003/004 plus the Festo valve terminal P-ST09-014.

### 4.3 Network
EtherCAT ring from C6030 through station couplers (EK1100) → drives → valve terminal; distributed clocks; EL6688 PTP for time sync with the ROS 2 PC and cameras. Vision on a separate 5GigE/2.5GigE VLAN with jumbo frames. PLC ↔ ROS 2 over ADS (pyads) or OPC UA (asyncua), 10–100 Hz for state and commands (R05 F12; R11 §1).

### 4.4 Cabinet
Two Rittal AX enclosures (control; drives/power). Contents per R05 F13 template: main disconnect, MCBs, contactors, surge protection, 24 V supplies + DC-UPS, EtherCAT and safety terminals, drives, terminal blocks, duct, labels. Schematics drawn in QElectroTech (IEC 60617 symbols); EPLAN only if an integrator demands it (R15). Follow IEC 60204-1 for wiring, colours and protective bonding (R14).

## 5. Pneumatics and vacuum
- Supply: P-ST00-004 compressor, dryer and Festo MS FRL with soft-start/dump valve controlled by safety output (safe exhaust on e-stop and door open).
- Distribution: Festo VTUG/CPX valve terminal on the gantry carriage (P-ST09-014); PU tubing 4/6/8 mm; push-in fittings; tool-changer M5 pass-throughs to the active tool.
- Needle grippers: one 5/2 valve per head group; blow-off through the air knife.
- Vacuum: venturi ejector on T4 with IO-Link vacuum level (−60 to −80 kPa nominal; achievable level on knit must be measured).
- Cutter bed: the cutter's own side-channel blower (5.5–7.5 kW) with zoning; lint filter on the exhaust.
- Draw the circuit in SMC PneuDraw (free) to ISO 1219-1 (R15).

## 6. Safety and compliance plan
| Item | Plan | Source |
|---|---|---|
| Legal frame | EU Machinery Regulation 2023/1230 (applies from 20 Jan 2027) or US route: NFPA 79, UL 508A panel, ANSI/A3 R15.06-2025, OSHA 1910.212 | R14 F1, F2, F5 |
| Robot cell | ISO 10218-2:2025 (integration), ISO 10218-1:2025 for the arm | R14 F2 |
| Risk assessment | ISO 12100; integrated manufacturing system ISO 11161 | R14 F15 |
| Safety functions | ISO 13849-1:2023; target PL d for e-stop, guard locking, light curtains, STO/SS1 groups; validate with SISTEMA | R14 F3 |
| Guards and distances | ISO 14120 guards, ISO 14119 interlocks, ISO 13855 minimum distances | R14 F4 |
| Sewing heads | ISO 10821 needle and take-up guards retained | R14 F6 |
| Lint fire risk | NFPA 660:2025 hazard analysis; extraction at cutter and heads; housekeeping schedule | R14 F7 |
| AI in the loop | AI never commands safety (ISO/IEC TR 5469 principles); safety state read-only to software | R14 F10 |
| Cybersecurity | Machinery Regulation EHSRs on corruption protection; Cyber Resilience Act for networked products | R14 F16 |
| Operator handling | Roll lifter for rolls > 25 kg; ergonomics for intervention points | R14 F9 |

Certification route: CE self-declaration for the development cell is not needed while it stays in-house; start the technical file and PL calculations from day one; plan a notified-body or NRTL review before the first customer unit (6–12 months, R13 seed milestones; cost estimates in R14 F5a).

## 7. Complete bill of materials and sourcing

### 7.1 Development-cell BOM (generated from `spine/parts.csv`)
<!-- BOM:START -->
| Part ID | Station | Vendor | Part number | Description | Qty | Unit USD | Basis | Line USD | CAD source |
|---|---|---|---|---|---|---|---|---|---|
| P-ST00-001 | ST00 | Bosch Rexroth / item / 80/20 | 45x45 and 90x90 extrusion set | Cell frame and guarding (6 m x 3 m envelope; extrusion+feet+panels+interlocked doors) per R07 §1e | 1 | 17,400 | estimate | 17,400 | vendor STEP (Rexroth/item/80-20 configurators) |
| P-ST00-002 | ST00 | Bossard / McMaster-Carr / Misumi | ISO 4762 / ISO 7380 / DIN 125 / T-nut kit | Fastener starter kit with spares per R07 §2b | 1 | 1,600 | estimate | 1,600 | code-CAD (bd_warehouse fasteners) |
| P-ST00-003 | ST00 | Lapp / igus / Phoenix Contact | Olflex / chainflex / M12 / ferrules / duct | Cabling and wiring kit (EtherCAT backbone; ~12 servo axes; ~60 sensors) per R07 §3e | 1 | 8,300 | estimate | 8,300 | none: cables routed in model as swept paths |
| P-ST00-004 | ST00 | Atlas Copco / Kaeser + Festo MS | quiet rotary-screw or scroll 6 bar + FRL + dryer | Compressed air supply and preparation sized for needle grippers ejectors and cylinders | 1 | 3,000 | estimate | 3,000 | vendor STEP (Festo MS series) |
| P-ST00-005 | ST00 | Bambu Lab | P1S | 3D printer for EOAT fingertips and gripper bodies (PA-CF/PETG) | 1 | 399 | list | 399 | none: shop tool |
| P-ST01-001 | ST01 | Leadshine + fabricated | EL7-EC750F kit + shaft + dancer | Driven roll let-off with dancer bar and ultrasonic diameter sensor | 1 | 2,200 | estimate | 2,200 | code-CAD + vendor STEP for motor |
| P-ST01-002 | ST01 | Erhardt+Leimer | ELGUIDER DRB class + FR 46 sensor | Web edge guide (alternate: own lateral shaft servo ~USD 800) | 1 | 4,000 | estimate | 4,000 | vendor STEP (E+L CAD download) |
| P-ST01-003 | ST01 | Meech / Simco-Ion | 945IPS / Performax IQ Easy 1.8 m | 24 V DC static elimination bar across the web | 1 | 1,000 | estimate | 1,000 | vendor STEP on request |
| P-ST01-004 | ST01 | Vestil | HYD-ROLL-47 | Roll lifter for 25-60 kg knit rolls | 1 | 1,685 | list | 1,685 | none: envelope model |
| P-ST02-001 | ST02 | iECHO | TK4S-2516 with conveyor and cradle feeder | Single-ply conveyor knife cutter 1.6 x 2.5 m with driven rotary + oscillating tools (alternate: used Zund G3 L with conveyor est. USD 40-90k) | 1 | 30,000 | estimate | 30,000 | none: envelope model until vendor STEP (request under NDA) |
| P-ST02-002 | ST02 | iECHO / Zund | decagonal rotary + 0.63 mm oscillating blades | Blade consumables first year | 1 | 500 | estimate | 500 | none: consumable |
| P-ST03-001 | ST03 | Schmalz | SNG-M 4 0.8 | Needle gripper heads for T1 wide needle bar (4 needles 0.8 mm; 3 mm stroke) | 6 | 300 | estimate | 1,800 | vendor STEP (Schmalz) |
| P-ST03-002 | ST03 | EXAIR | 6 in Super Air Knife kit | Air knife nose on T1 for edge control and blow-off | 1 | 627 | list | 627 | vendor STEP (EXAIR) |
| P-ST03-003 | ST03 | Pepperl+Fuchs | UDC-18GS IO-Link | Ultrasonic double-ply detector (must be validated on knit) | 1 | 505 | list | 505 | vendor STEP (Pepperl+Fuchs) |
| P-ST03-004 | ST03 | Piab | Kenos KCS 150 + COAX SX | T4 foam vacuum pad for stabilising and short lifts | 1 | 1,500 | estimate | 1,500 | vendor STEP (Piab) |
| P-ST03-005 | ST03 | Festo | OVEM-14-H-B-QO-CE-N-LK (8037696) | IO-Link vacuum ejector with integrated sensing for T4 | 1 | 400 | estimate | 400 | vendor STEP (Festo) |
| P-ST04-001 | ST04 | Festo | EGC-120 X 3000 + 2x EGC-80 Y 1500 + Z + CMMT-AS EtherCAT drives | Belt-drive Cartesian gantry over the 3 m x 1.5 m work envelope with 2-3 pick heads (prototype alternate: Vention belt gantry) | 1 | 25,000 | estimate | 25,000 | vendor STEP (Festo configurator) |
| P-ST04-002 | ST04 | Universal Robots | UR10e | 6-axis cobot at the sewing-presentation position (RTDE 500 Hz; ROS 2 driver; Menagerie model) | 1 | 49,596 | reseller | 49,596 | vendor STEP (UR support) + MuJoCo Menagerie (BSD-3) |
| P-ST04-003 | ST04 | ATI Industrial Automation | QC-11 master + 3 tool plates + stands | Pneumatic tool changer (16 kg; 6x M5 air pass-through; 0.01 mm repeatability) | 1 | 3,500 | estimate | 3,500 | vendor STEP (ATI free CAD) |
| P-ST04-004 | ST04 | Robotiq | 2F-85 + printed fingertips | T3 parallel-jaw edge/pinch gripper with WBCD-style hard tips | 1 | 4,700 | estimate | 4,700 | vendor STEP (Robotiq) + MuJoCo Menagerie (BSD-2) |
| P-ST04-005 | ST04 | GelSight | Mini | Tactile fingertip for single-ply verification and slip | 1 | 510 | list | 510 | vendor STEP (GelSight) |
| P-ST04-006 | ST04 | RealSense | D405 | Wrist depth camera 7-50 cm | 1 | 272 | list | 272 | vendor STEP (RealSense) |
| P-ST05-001 | ST05 | JUKI | MO-6814S (belt-drive head) | 514 two-needle four-thread overlock for shoulder sleeve and side seams (7000 sti/min; diff 1:0.6-1:4) | 1 | 1,550 | reseller | 1,550 | scan: no vendor STEP (R04); table cut-out from manual |
| P-ST05-002 | ST05 | EFKA / JUKI | AB321A or SC-922 control box | Sewing drive with documented external I/O and 512/360-pulse rotation output | 2 | 600 | estimate | 1,200 | none: envelope model |
| P-ST05-003 | ST05 | JUKI | MF-7923-U11-B56/UT51 (H23 hemming subclass) | 406 cylinder-bed coverstitch with trimmer for sleeve and bottom hems and neck topstitch (alternate Jack W4-UT USD 1924-2199) | 1 | 7,226 | reseller | 7,226 | scan: no vendor STEP (R04) |
| P-ST05-004 | ST05 | Eltex | 15965 | Six-thread break sensor with PLC output | 3 | 400 | estimate | 1,200 | none: envelope model |
| P-ST05-005 | ST05 | Groz-Beckert / Coats | SES Nm 65-75 needles; Epic Tex 24 + Gramax Tex 18 thread | Needles and thread first 1000 shirts (about 45 m thread per tee) | 1 | 300 | estimate | 300 | none: consumable |
| P-ST06-001 | ST06 | JUKI / Kansai Special | MO-6814S cylinder-arm or JJT5014GH-01M | Cylinder-arm overlock for neck-rib attach | 1 | 1,550 | reseller | 1,550 | scan: no vendor STEP (R04) |
| P-ST06-002 | ST06 | in-house | expansion-roller loader + rib meter/cut/close unit | Collar module modelled on Atlanta 1289/1278-6 and 1996 (built in-house; bought-in est. USD 30-60k) | 1 | 6,000 | estimate | 6,000 | code-CAD |
| P-ST07-001 | ST07 | Basler | a2A5320-23ucPRO + LM16XC lens | 16 MP inspection camera over backlit table (~0.15 mm/px over 800 mm) | 1 | 2,500 | estimate | 2,500 | vendor STEP (Basler) |
| P-ST07-002 | ST07 | Smart Vision Lights | EuroBrite BL-S100150 | Backlight tiles for the inspection table (3 x 3) | 9 | 590 | list | 5,310 | vendor STEP (Smart Vision Lights) |
| P-ST07-003 | ST07 | mk / Dorner | GUF-P 2000 / 2200 series | Discharge belt 2 m x 400-600 mm with reject flipper gate | 1 | 3,000 | estimate | 3,000 | vendor STEP (mk QuickDesigner / Dorner DTools) |
| P-ST08-001 | ST08 | Tajima | TMEZ-SC 1501 + Air Type Clamp Frame | Optional single-head embroidery loaded by ST04 (not in base cell) | 0 | 15,000 | estimate | 0 | none: request STEP under NDA |
| P-ST09-001 | ST09 | Beckhoff | C6030 + TwinCAT 3 (TC1250 NC PTP) | Main PLC/motion IPC | 1 | 3,500 | estimate | 3,500 | vendor STEP (Beckhoff) |
| P-ST09-002 | ST09 | Beckhoff | EK1100 x4 + EL1008 x12 + EL2008 x10 + EL3064 x2 | EtherCAT I/O for ~82 DI and ~75 DO | 1 | 2,540 | reseller | 2,540 | vendor STEP (Beckhoff) |
| P-ST09-003 | ST09 | Beckhoff | EL6910 + EL1918-2200 x4 + EL2904 x4 | TwinSAFE logic and safe I/O (26 safe DI; 12 safe DO; 3 locks) | 1 | 3,270 | reseller | 3,270 | vendor STEP (Beckhoff) |
| P-ST09-004 | ST09 | Delta | ASD-B3A-E + ECM-B3M | Economy EtherCAT servo axes (let-off; extraction Z/C; collar module; conveyors) | 10 | 1,055 | reseller | 10,550 | vendor STEP (Delta) |
| P-ST09-005 | ST09 | Phoenix Contact / PULS | QUINT4-PS 24DC/20 + CP20.241 + UB10.241 + UZK12.261 | 24 V power and DC-UPS | 1 | 2,335 | reseller | 2,335 | vendor STEP (Phoenix/PULS) |
| P-ST09-006 | ST09 | Siemens / Schneider / Phoenix | 3LD2 + iC60N + LC1D + FLT | Main disconnect breakers contactors surge protection | 1 | 1,150 | estimate | 1,150 | vendor STEP |
| P-ST09-007 | ST09 | Rittal | AX 1180.000 | Control and drive enclosures | 2 | 1,100 | estimate | 2,200 | vendor STEP (Rittal) |
| P-ST09-008 | ST09 | Beckhoff | CP2912-0010 + TF2000 | Operator HMI panel | 1 | 1,812 | reseller | 1,812 | vendor STEP (Beckhoff) |
| P-ST09-009 | ST09 | Patlite | LR6-302WJNW-RYG | Tower light | 1 | 140 | reseller | 140 | vendor STEP (Patlite) |
| P-ST09-010 | ST09 | Schneider Electric | XALK178 | E-stop stations | 4 | 108 | reseller | 432 | vendor STEP (Schneider) |
| P-ST09-011 | ST09 | Schmersal | AZM300Z-ST-1P2P | Guard-locking interlocks on access doors | 4 | 788 | reseller | 3,152 | vendor STEP (Schmersal) |
| P-ST09-012 | ST09 | SICK | deTec4 Core 14 mm pair | Light curtains at load and output openings | 2 | 2,650 | estimate | 5,300 | vendor STEP (SICK) |
| P-ST09-013 | ST09 | Pilz | PITenable | Three-position enabling switch for teach/service | 1 | 400 | estimate | 400 | vendor STEP (Pilz) |
| P-ST09-014 | ST09 | Festo | VTUG / CPX-AP-I valve terminal | Fieldbus valve terminal for grippers cylinders and air knives | 1 | 2,500 | estimate | 2,500 | vendor STEP (Festo) |
| P-ST10-001 | ST10 | Neousys | Nuvo-9160GC + RTX 4000 SFF Ada | Cell vision and inference IPC | 1 | 6,500 | estimate | 6,500 | vendor STEP (Neousys) |
| P-ST10-002 | ST10 | Basler | a2A5328-49g10m + Kowa LM25XC | 24 MP over-bed camera for cut verification and piece pose (0.28 mm/px) | 1 | 5,000 | estimate | 5,000 | vendor STEP (Basler) |
| P-ST10-003 | ST10 | Basler | a2A1920-160umPRO + lens | Needle-area seam tracking cameras at 200+ fps ROI (one per sewing head) | 3 | 900 | estimate | 2,700 | vendor STEP (Basler) |
| P-ST10-004 | ST10 | LUCID / IDS | Triton TRI050S / GV-5880 + LM12JC + backlight | 5 MP placement and collar cameras with backlights | 3 | 750 | estimate | 2,250 | vendor STEP |
| P-ST10-005 | ST10 | NVIDIA | Jetson AGX Thor developer kit | Policy-learning and VLA development box | 1 | 3,499 | list | 3,499 | vendor STEP (NVIDIA) |
| P-ST10-006 | ST10 | Teledyne DALSA | Linea Lite 4k + Kubler 5020 encoder | Line-scan web inspection on unwind (optional in v1) | 0 | 4,500 | estimate | 0 | vendor STEP (Teledyne) |

| Station | Subtotal USD |
|---|---|
| ST00 | 30,699 |
| ST01 | 8,885 |
| ST02 | 30,500 |
| ST03 | 4,832 |
| ST04 | 83,578 |
| ST05 | 11,476 |
| ST06 | 7,550 |
| ST07 | 10,810 |
| ST08 | 0 |
| ST09 | 39,281 |
| ST10 | 19,949 |
| **Total** | **247,560** |
<!-- BOM:END -->

### 7.2 What is not yet in the BOM
Engineering labour, machining of custom brackets (Xometry/SendCutSend quotes, R15), shipping and duties, spares beyond first year, the optional ST08 decoration and retail fold/bag modules, and a 15 % contingency on quote-only lines.

### 7.3 Against the white paper's cost scenarios
The development cell totals about **USD 250k in parts**, roughly 2–5× the white paper's USD 52k / 83k / 140k factory build-and-test scenarios. The research shows where the gap sits: the cobot (USD ~50k), the gantry (est. USD 25k), vision (USD 20–48k), a documented-interface cutter (USD 30–90k) and frame/guarding (USD 17k vs USD 15k) (R01, R02, R06, R07). The cost-down path to a sellable USD 100k cell: (1) replace the cobot with a second gantry head plus a low-cost presentation axis once skills are proven; (2) volume pricing on cutter and gantry; (3) minimum vision build; (4) in-house frame weldment. This gap is recorded as GAP-01 in the project master document.

### 7.4 Sourcing actions (quote requests)
| Vendor | Request |
|---|---|
| iECHO and Zünd (used dealer) | TK4S-2516 conveyor quote with API documentation; used G3 L with ZCC licence; STEP of the cutter envelope |
| Festo | EGC gantry quote (HGO configurator) with CMMT-AS drives and STEP |
| Universal Robots distributor | UR10e price, lead time, AI Accelerator option |
| Schmalz / FIPA / Piab | SNG-M heads, FIPA GR04.700 alternative, KCS 150 pad; fabric swatch trials |
| JUKI dealer / EFKA | MO-6814S heads, MF-7923 UT51, AB321A/SC-922 engineer's manuals with I/O pin-outs; NDA request for head CAD |
| Beckhoff | C6030, TwinCAT licences, terminal set |
| Atlanta Attachment / Kansai | Collar loader references (1289/1278-6/1996) and JJT5014GH price |
| Basler / LUCID / Neousys | Camera, lens and IPC quote against the R06 station plan |

## 8. Assembly sequence and commissioning plan
1. **Bench rigs first (before the cell)**: (a) needle-gripper pick tests on fabric swatches; (b) overlock head on a table with PLC I/O and a needle camera; (c) rib stretch rig with two rollers.
2. **Frame and guarding** (ST00) with utilities stubbed; safety circuit wired and validated with all motion disabled.
3. **Cabinet** built and tested (insulation, continuity, safety function tests) before connecting field devices.
4. **ST01 + ST02**: cutter placed, calibrated; roll fed; cut tests (TST-ST01-01, TST-ST02-01/02).
5. **ST04 gantry** installed; homing, soft limits, STO tests; then ST03 tools and pick tests (TST-ST03-01).
6. **UR10e** on pedestal; safety configuration (speed/force limits, zones) matched to the risk assessment.
7. **ST05/ST06 heads**: I/O, stitch counting, thread sensors; robot presentation skills one seam at a time.
8. **ST07** inspection and discharge.
9. **Integration**: full job package from the software (Guide 2) driving the cell; first complete shirt; then pipelined runs.

## 9. Test and validation protocol
| Test | Pass criterion |
|---|---|
| Station acceptance | Every TST-STxx above passes |
| First article | 10 shirts, each size, measured and wash-tested (ISO 6330), seam strength (ASTM D1683) |
| Shift test | Repeated 12-hour runs from a declared starting condition (white paper §23): ≥ 100 accepted shirts, interventions logged with cause, availability and yield measured |
| Autonomy statistic | Interventions per 100 garments with confidence interval; target trend toward ≤ 1 % per garment (at 1 % per garment, a 100-garment intervention-free run has ~37 % probability) |
| Safety validation | Every safety function tested and documented against its required PL |

## 10. Risks, unknowns and the experiments that retire them
| # | Risk | Experiment | Cost / time (est.) |
|---|---|---|---|
| 1 | Robot-fed curved overlock seam on curling jersey | Bench overlock + needle camera + UR or gantry presentation, 100 seams | USD 5k, 4–6 weeks |
| 2 | Single-ply pick reliability and needle marks | 200-cycle pick test + ISO 6330 wash | USD 3k, 2 weeks |
| 3 | Rib stretch and neck attach | Two-roller stretch rig + cylinder-arm overlock | USD 4k, 4 weeks |
| 4 | ST04 occupancy above budget | Timed simulation (Guide 3 C4), then timed bench transfers | 2 weeks |
| 5 | Cutter integration API | Vendor demo with our DXF and a status/handshake test | 1 week |
| 6 | Ultrasonic double-ply sensing on knit | Sample sensor on swatches; tactile fallback (ReSkin/GelSight showed 10/10 vs 3/10 for image classifier, R03) | USD 600, 1 week |
| 7 | Cost vs. USD 100k price | Cost-down plan §7.3 after skills are proven | ongoing |
