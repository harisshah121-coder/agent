# R05 · Control, drives, PLC, safety hardware (ST09)

Research report for the Roll-to-Garment cell. Date of research: 2026-10-21. Author: research agent R05.
Scope: PLC/IPC and safety PLC selection, servo drives and motors, I/O and fieldbus, pneumatic valve terminals, cabinet build, HMI/operator interface, PLC <-> ROS 2 links, and a cabinet parts-list template for the cell.

(Report under construction; sections are appended as research completes.)


<!-- WAVE-1 RAW NOTES (2026-10-21). Kept so nothing is lost; restructured into Findings below as sections are completed. -->
<!--
Beckhoff CX7000: Arm Cortex-M7 480 MHz, 8 DI/4 DO integrated, TwinCAT/RTOS (FreeRTOS-based, closed), TC1200 PLC licence included, platform level Basic(10), < 2 W. https://www.beckhoff.com/en-us/products/ipc/embedded-pcs/cx7000-arm-r-cortex-r/cx7000.html
Beckhoff CX5230: Atom x5-E3930 1.3 GHz dual-core, 4 GB DDR4, 2x GbE, 4x USB3, DVI-D, Win10 IoT LTSC or TwinCAT/BSD, platform level Performance(40); order codes CX5230-0100/-0170/-0175/-0185/-0190/-0195; TwinCAT licences ordered separately. https://www.beckhoff.com/en-en/products/ipc/embedded-pcs/cx5200-intel-atom-r-x/cx5230.html
Beckhoff C6030-0060: ultra-compact IPC 132x133x76 mm, 0..55 C, IP20; CPU options Celeron/Pentium 2 cores (TC3 platform 50) up to Core i7. https://www.beckhoff.com/en-en/products/ipc/pcs/c60xx-ultra-compact-industrial-pcs/c6030-0060.html
TwinSAFE EL6910: TwinSAFE Logic, 212 safe connections, 128 groups, 512 FBs, analog processing, PROFIsafe master/slave, TwinSAFE SC, EN ISO 13849-1 Cat.4 PL e / SIL 3, cycle ~1 ms. https://www.beckhoff.com/en-en/products/automation/twinsafe/twinsafe-hardware/el6910.html ; reseller price USD 670 (plcpartssolution.com). 
TwinSAFE EL1918: 8 safe inputs + integrated TwinSAFE Logic (EL6910 function set, 128 connections), Cat.4 PL e SIL 3; EL1918-2200 = inputs only. https://www.beckhoff.com/en-en/products/automation/twinsafe/twinsafe-hardware/el1918.html
TwinSAFE tabular overview incl. EL2904 (4 safe outputs), EL2912, EK1960 (20 in/24 out), EP1908, AX5801/AX5805 cards, EP7412-9071 STO via FSoE motor box. https://www.beckhoff.com/en-us/products/automation/twinsafe/twinsafe-hardware/tabular-product-overview
AX8000: AX8108-0100-0000 single-axis 8 A rated / 20 A peak, STO/SS1 via hardwire or FSoE; -0200 Safe Motion (SLS, SLP etc. with EL6910-type logic in drive); OCT + EnDat3; EtherCAT cycle <= 100 us, DC; AX8000 TwinSAFE meets EN ISO 13849-1 Cat 4 PL e, SIL 3. https://www.beckhoff.com/en-us/products/motion/servo-drives/ax8000-multi-axis-servo-system/ax8108.html
AX5000: 1- and 2-channel, 100..480 V AC, OCT, AX58xx safety cards STO/SS1 (AX5801) and Safe Motion (AX5805). https://www.beckhoff.com/en-en/products/motion/servo-drives/ax5000-digital-compact-servo-drives
TME reseller prices (USD net, 2026): AX5103-0000-0202 (3 A, 1 ch) 1,228.27; AX5118-0000-0202 (18 A) 2,137.91; AX5801-0200 STO card 121.29. https://www.tme.eu/en/katalog/motor-control_112596/p,beckhoff-automation_1557
AM8000 torque table: AM8021 0.50 Nm, AM8031 1.37-1.40 Nm (F3 72 mm), AM8041 2.37-2.45 Nm, AM8051 4.8-6.3 Nm. https://www.beckhoff.com/en-en/products/motion/rotary-servomotors/am8000-servomotors/tabular-product-overview/
ROS 2 <-> PLC: beckhoff_ads_hardware_interface (b-robotized, ros2_control SystemInterface over ADS sum commands, v1.0.0 2025-09-17, Apache-2.0, jazzy/kilted) https://index.ros.org/p/beckhoff_ads_hardware_interface ; ads_vendor 1.0.2 https://index.ros.org/p/ads_vendor ; ethercat_driver_ros2 (ICube, IgH master, Apache-2.0, jazzy branch) https://github.com/ICube-Robotics/ethercat_driver_ros2 ; soem_vendor_ros2 exists.
Phoenix AXC F 2152 (2404267): Arm A9 2x800 MHz, RT Linux (Yocto), PLCnext Engineer / C++ / MATLAB; safety via AXC F XT SPLC 1000/3000 ext.; 1 ms cycle; OPC UA server. https://www.phoenixcontact.com/en-gb/products/controller-axc-f-2152-2404267
CODESYS Control for PLCnext SL (2302000033) includes EtherCAT master etc.; v4.22 2026-08-18. https://www.codesys.com/ecosystem/release-lifecycle/releases-updates/control-for-plcnext-sl
ctrlX: Basic Set (ctrlX CORE PLUS X3 + 16DI/16DO + PLC, Node-RED, EtherCAT apps) EUR 799 recommended, via partners. https://www.boschrexroth.com/en/pl/c/ctrlx-automation ; ctrlX OS Ubuntu-Core based, kernel 6.1.33-rt11 in 02.06 release. 
Siemens: 6ES7512-1SK01-0AB0 cancelled 2024-10-01, successor 6ES7512-1SM03-0AB0. https://www.industry-mobile-support.siemens-info.com/en/product/6ES75121SK010AB0
Rockwell 5069-L306ERS2 Compact GuardLogix SIL2: USD 1,936.56 (Turtle & Hughes, 2026). https://shop.turtle.com/product/ab-5069l306ers2/01t4v000009KvQUAA0
Pilz eshop EUR: PNOZ m B0 772100 712.19; PNOZ m B1 772101 541.76; PNOZ m ES EtherCAT 772136 363.67; PNOZ m EF 8DI2DOT 772144 607.38; PNOZ m ES 14DO 772181 386.97. https://www.pilz.com/en-FI/eshop/Small-controllers-PNOZmulti/Small-controllers-PNOZmulti-2/c/A0300B0300
Sick Flexi Soft FX3-CPU000000 (1043783) SIL 3 Cat 4 PL e; Flexi Compact FLX3-CPUC100 (1085349); Newark FLX3-CPUC200 USD 1,976.05. https://www.sick.com/media/pdf/7/77/477/dataSheet_FX3-CPU000000_1043783_en.pdf
Sick nanoScan3 NANS3-AAAZ30AN1 (1100333): 3 m protective field, 275 deg, 70 ms, Type 3 SIL 2 PL d, PFHd 8e-8, 106.6x80x117.5 mm; Lesman price USD 3,444.30. https://www.sick.com/media/pdf/9/79/979/dataSheet_NANS3-AAAZ30AN1_1100333_en.pdf https://www.lesman.com/nans3-aaaz30an1 ; sick.com page: CAD + technical drawings download (login required).
Sick deTec4 Core Set 14/1500 (1062904): Type 4 PL e, 14 mm, 10 m, kit incl. brackets, cables, RLY3-OSSD2; deTec4 Core Set 30/900 nexinstrument USD 4,154 (lead 6-8 wk). deTec4 Set 30/1800 (1103385) 30 m, 13 ms, PFHd 15.3e-9. https://www.sick.com/media/pdf/7/37/937/dataSheet_deTec4-Core-Set-14-1500_1062904_en.pdf
Keyence GL-V: Type 4 PL e SIL3, 14/25/45 mm. https://www.keyence.com/products/safety/light-curtain/gl-v/specs
Kollmorgen AKD2G: single/dual axis, SafeMotion Monitor incl. FSoE, dual-channel STO, AKD2G-6V03D 3&3 A dual. https://www.kollmorgen.com/en-us/products/drives/servo/akd2g/akd2g-servo-drive
Delta ASD-A3-0421-E: 400 W, 2.65 Arms, EtherCAT, STO, 24-bit enc. https://www.plclogiccontroller.com/asd-a3-0421-e-delta-servo-drive ; ETG product guide lists Delta ASDA-B3A-E, A3-E, Teknic ClearPath-EC, Oriental AZ, Leadshine. https://www.ethercat.org/en/products.html
Yaskawa Sigma-7 EtherCAT: SGD7S-2R8AA0A 400 W amp, SGM7J-04A7D6S motor (Centroid reseller). Sigma-X SGDXS EtherCAT new. https://www.centroidcnc.com/yaskawa_sigma_7_servopak.html
Beckhoff EL6224 IO-Link master 4 ch, EL6224-0090 TwinSAFE SC. https://www.beckhoff.com/en-us/products/i-o/ethercat-terminals/el-ed6xxx-communication/el6224.html
EtherCAT P: 24 V Us + Up 3 A each in one 4-wire cable, EK1300/EK1322/EPP modules. https://www.beckhoff.com/en-us/products/i-o/ethercat-p
ifm AL1332 IO-Link master EtherCAT 8 ports IP67. https://www.ifm.com/au/en/product/AL1332
Festo VTUG 573606: 10/14/18 mm valves, up to 24 positions, I-Port/IO-Link/fieldbus via CPX-AP-I, IP65/67. https://www.festo.com/us/en/a/573606 ; CPX-AP-I-EC-M12 (8086609) EtherCAT interface, login for price, CAD data on page. https://www.festo.com/us/en/a/8086609
SMC SY3000/5000/7000 Cv 0.30/0.66/1.1, EX600 SI unit EtherCAT. https://www.smcworld.com/webcatalog/en-hk/seriesList/?id=SY-5-E
Schmalz SNG-V needle gripper. https://www.schmalz.com/en-us/products/automation-743270/other-gripping-technologies-746237/needle-grippers-306131/needle-grippers-sng-v-306144
Phoenix QUINT4-PS/1AC/24DC/10 (2904601) 10 A, 20 A dyn boost; QUINT4 24DC/20 (2904602) RSP Supply USD 550.99. https://rspsupply.com/p-36893-phoenix-contact-2904602-power-supply-quint4-ps1ac24dc20.aspx
PULS QT20.241 480 W USD 775 (Standard Electric Supply). https://www.standardelectricsupply.com/PULS-QT20-241-Power-Supply-Unit
Rittal AX 1380.000 380x380x210 IP66 (datasheet). https://www.rittal.com/pdf-creator/variant/us-en/1380000
Siemens KTP700 Basic 6AV2123-2GB03-0AX0 7" 800x480 PROFINET, phase-out since 15.12.2026 per Industry Mall. https://sieportal.siemens.com/en-ww/products-services/detail/6AV2123-2GB03-0AX0
Beckhoff CP29xx: CP2907-0010 7", CP2912-0010 12" 800x600, CP2915 15", CP-Link 4 up to 100 m; CP39xx IP65 arm-mount. https://www.beckhoff.com/en-us/products/ipc/control-panels/cp29xx-cp39xx-multi-touch-control-panels/cp29xx-0010.html
Red Lion Graphite G10C0000 USD 4,433 (Lesman). https://www.lesman.com/g10c0000
Standards: EU Machinery Regulation 2023/1230 applies 20 Jan 2027 (EUR-Lex). ISO 10218-2:2025 published 2025-02, 223 pp, CHF 227. EN ISO 13849-1:2023 in OJEU May 2024; 13849-1:2015 withdrawn 15 May 2027 (Pilz). https://www.pilz.com/en-CA/support/law-standards-norms/functional-safety/en-iso-13849-1
Gearboxes: Neugart PLE 40/60/80/120/160, backlash <15/<10/<7 arcmin 1-stage, IP54, NCP configurator + Tec Data Finder (CAD). https://cdn.neugart.com/fileadmin/user_upload/Downloads/Catalog_Chapters/05_2026/PLE/PLE_2026_05_EN.pdf ; Wittenstein CP alpha Basic Line <=12 arcmin, ratio 3-100, CAD via cad-point.wittenstein-group.com. https://www.wittenstein-group.com/en-us/product/cp ; Beckhoff AG2250-+PLE60 = Neugart PLE factory-fitted. 
-->
<!-- WAVE-2 RAW NOTES (2026-10-21)
Beckhoff reseller prices (TME, USD net, 2026-10): EK1100 149.15 (38 in stock); EL2008 56.90; EL2904 249.78; EL1008 (TME) ~? ; iqelectro EL1008 USD 77.00. https://www.tme.eu/en/katalog/p,beckhoff-automation_1557 https://iqelectro.com/products/el1008-beckhoff-ethercat-terminal-8-channel-digital-input-24-v-dc-3-ms
Beckhoff TC1250 (PLC/NC PTP 10) includes TC1200 + TF5000; platform levels -0v20 (Economy, only Beckhoff RT Linux), -0v30, -0v40 (Performance, = CX5230), -0v50 (C6030 Celeron/Pentium) ...; prices not public (TwinCAT 3 Price List via sales). https://www.beckhoff.com/en-us/products/automation/twincat/tcxxxx-twincat-3-base/tc1250.html
TF2000 HMI Server: 1 client + 1 controller standard, platform levels -0v20..-0v94. https://www.beckhoff.com/en-en/products/automation/twincat/tfxxxx-twincat-3-functions/tf2xxx-hmi/tf2000.html
TF6100 OPC UA server/client, runs on Win/TwinCAT BSD/Beckhoff RT Linux. https://www.beckhoff.com/en-us/products/automation/twincat/tfxxxx-twincat-3-functions/tf6xxx-connectivity/tf6100.html
CP2912-0010 reseller price USD 1,812 lead 5-7 wk (e-motionsupply). https://www.e-motionsupply.com/product_p/cp2912-0010.htm
Beckhoff pricing guide (IMD, pre-2020 US est.): EL1008 ~48, EL2008 ~80, CX20xx 1,200-2,200. https://industrialmonitordirect.com/blogs/knowledgebase/beckhoff-plc-documentation-and-pricing-resources-guide
Schmersal AZM300Z-ST-1P2P USD 788 (Applied Automation, Sep 2026); AZM300Z-ST-1P2P-A-T USD 909. https://www.appliedautomation.com/part/schmersal/azm300z-st-1p2p/2060086
Euchner MGB2-L1-MLI-U-Y0000-BJ-136776 locking module USD 399.99 (Platinum International, reseller); CTP-L1 on request. https://platinum-international.store/product/euchner-ctp-l1-ar-m-ha-az-sab-123307-safety-switch
Pilz PSENmlock PSEN ml b 1.1 unit 570400 — price on request in eshop; PITenable PIT en1.0p-5m-s 401110 on request. https://www.pilz.com/en-INT/eshop/Sensor-technology/Safety-switches-with-guard-locking/PSENmlock-safety-locking-devices/PSENmlock/c/0010600222712380OR
Pilz PNOZ s4 750104 GBP 211.66 ex VAT (RS UK, 2026-05). https://uk.rs-online.com/web/p/safety-relays/0156106
Leuze RSL410-S/CU408-M12 53800201 list USD 6,027, ~25 business days. https://www.leuze.com/en-us/rsl410-s-cu408-m12/53800201
Sick microScan3 Core MICS3-AAAZ40AZ1 (1067360) 4 m PF, 40 m WF; Lesman microScan3 from USD 4,674. https://www.lesman.com/microscan3
Keyence SZ-V32N: 190 deg, 20-150 mm res, 32 banks, up to 3 heads, CAD on page; price only via Keyence (no public list). https://www.keyence.eu/products/safety/laser-scanner/sz-v/models/sz-v32n
Keyence GL-V light curtain Type 4 PL e (GL-R similar); no public price.
Oriental Motor AZD-KEP (EtherNet/IP) EUR 476 list, AZD-AED (AC EtherCAT) EUR 618 list, 5 wk (orientalmotor.eu); AZD-KED2 EtherCAT DC driver (catalog.orientalmotor.com), AZD4A-KED 4-axis EtherCAT. https://www.orientalmotor.eu/es/products/detail?hinmei=AZD-AED
Teknic ClearPath-EC NEMA17/23 integrated EtherCAT servo (manual rev 1.14 2026-10-07); ClearPath CPM-SDSK-2321S-RLN USD 299 (automationtechnologiesinc); Teknic publishes prices on its site (login-free tables). https://teknic.com/files/downloads/ClearPath-EC_NEMA17_User_Manual.pdf
Leadshine EL8-EC: 400-2000 W, STO SIL3, EtherCAT; price not on site. https://www.leadshine.com/products/servo/servo-drive/el8-series.html
Delta: Digi-Key ASD-B3A-0421-E USD 632.80 (lead 32 wk std), ECM-B3M-C20604RS1 motor USD 421.60, ASD-B3A-0721-E USD 711.20. https://www.digikey.com/en/products/detail/delta-electronics-industrial-automation/ASD-B3A-0421-E/21852600 ; grey-market ASD-B3-0421-E ~USD 66 (tashannet) — not recommended.
Yaskawa SGD7S-2R8AA0A price on request (IAC). CAD drawings on yaskawa.com downloads.
Moxa EDS-2008-EL 8-port unmanaged, 12/24/48 VDC, metal, 5-yr warranty; price not on site. https://www.moxa.com/en/products/industrial-network-infrastructure/ethernet-switches/unmanaged-switches/eds-2008-el-series
ifm AL1326 (EtherNet/IP sibling of AL1332) list USD 464.20 (ifm US, 2026-10). https://www.ifm.com/us/en/product/AL1326
EtherCAT DC: all DC devices synchronized to reference clock "generally less than 100 ns". https://infosys.beckhoff.com/content/1033/ethercatsystem/2469102219.html
EL6688 IEEE1588 PTPv1/v2 terminal, master/slave, usable as TwinCAT reference clock. https://www.beckhoff.com/en-en/products/i-o/ethercat-terminals/el-ed6xxx-communication/el6688.html
Schmalz SNG-V 10 1.2 V-7 (10.01.29.00176): 10 needles 1.2 mm, 7 mm stroke, 3-7 bar, 265 g, 149x32x56 mm, CAD download on page, price login. https://www.schmalz.com/en-se/products/automation-743270/other-gripping-technologies-746237/needle-grippers-306131/needle-grippers-sng-v-306144/10.01.29.00176
Festo OVEM: nozzle 0.45-3.0 mm, suction 13-348 l/min, air consumption curve, IO-Link; CAD on festo.com; price login. https://www.festo.com/media/catalog/203487_documentation.pdf
SMC ZK2: nozzle 0.7/1.0/1.2/1.5 mm -> air consumption 24/40/58/90 l/min ANR, suction 29/44/61/67; energy-saving cutoff 93%. https://www.smcworld.com/products/pickup/en-hk/vacuum_device/related_system/zk2.html
Rittal AX 1180.000 800x1000x300 IP66 Type 4/12 (datasheet; price not shown). https://www.rittal.com/pdf-creator/variant/hr-hr/1180000
PULS UB10.241 DC-UPS USD 553.50 (automationdistribution) / 615 (RITEC); UZK12.261 battery module 670. https://automationdistribution.com/ub10-241/
Mean Well NDR-480-24: 20 A 480 W, MXN 1,923.54 (HTD). https://meanwellmexico.mx/products/ndr-480-24
Patlite LR6-302WJNW-RYG USD 140; LR6-302PJNW-RYG USD 166 (shop.patlite.com). https://shop.patlite.com/60mm-Signal-Tower-Red-Green-Amber-p/lr6-302wjnw-ryg.htm
IgH EtherCAT master: GitLab etherlab.org/ethercat, GPLv2, 3,079 commits, 16 releases, stable-1.6 recommended for production. https://gitlab.com/etherlab.org/ethercat https://etherlab.org/en_GB/ethercat
SOEM v2.0.0 (OpenEtherCATsociety, 2k stars): dual-licensed GPLv3 or commercial; legacy API removed. https://github.com/OpenEtherCATsociety/SOEM/releases
Omron NX1P2-9024DT: 24 DI/10 DO built-in, up to 4 EtherCAT axes (NX1P2-9024DT: 4 axes? table says 4/0/4), NX-SL3300 safety CPU via EtherCAT coupler. https://www.ia.omron.com/products/family/3650/lineup.html
Siemens 6ES7512-1SM03-0AB0 CPU 1512SP F-1 PN active, lead 25 days, price group 216, list via Industry Mall login. https://mall.industry.siemens.com/mall/en/internationalenergytechnikltd/Catalog/Product?SiepCountryCode=OE&mlfb=6ES7512-1SM03-0AB0
Siemens price increase +10..23% effective 2026-03-25 (secondary source accio). 
RevPi Connect 4 EUR 448 (shop); Connect 5 = CM5-based, PiBridge gateways incl. RevPi Gate EtherCAT (slave gateway, not master). https://revolutionpi.com/en/docs/revpi-connect-5
IEC 61800-5-2 functions STO/SS1/SS2/SOS/SLS/SSM/SSR/SDI (Phoenix). https://www.phoenixcontact.com/en-us/industries/functional-safety/safe-motion
FSoE: black channel, IEC 61508, up to SIL 3, TUV-assessed, IEC 61784-3. https://www.ethercat.org/en/safety.html https://www.ethercat.org/download/documents/Safety_over_EtherCAT_Overview.pdf
EMC: AX8000 C3 with integrated mains filter; C2 needs AX2090-NF80 filter; mains choke for long motor cables; grounding via serrated nuts, shields both ends. https://infosys.beckhoff.com/content/1033/ax8000_ba/13910148747.html https://infosys.beckhoff.com/content/1033/ax8000_ba/7919288715.html ; AX5000 C3 std, <25 m motor cable without choke. Siemens SINAMICS EMC config manual 2024/03 (zone concept, HF equipotential bonding, toothed discs). https://cache.industry.siemens.com/dl/files/610/103704610/att_1277149/v1/EMC_configuration_manual_202403_en-US.pdf
Muting: IEC 62046:2018 clause 5.7 (muting to allow access by materials/persons, anti-manipulation). https://webstore.ansi.org/preview-pages/IEC/preview_iec62046%7Bed1.0%7Den.pdf ; TwinSAFE EL6900/EL6910 certified muting FBs.
-->

## Findings

Conventions: prices are as seen on 2026-10-21/22 unless dated otherwise; "list" = vendor list price, "reseller" = named reseller web price, "est." = my estimate with basis, "quote" = not published. CAD column states where STEP (or native) geometry can be downloaded. Items older than 2023 are flagged "possibly stale".

### F1. Control architecture pattern: who does motion, who does safety, how ROS 2 attaches

The white paper requires deterministic local control with an independent safety path that AI can never command. Every mainstream platform below implements that split the same way: a real-time PLC/motion runtime commands drives over a deterministic fieldbus, a separately certified safety logic (safety PLC or safety terminals) owns e-stops, guards and the drives' safe-motion functions, and the non-real-time ROS 2 stack (M08/M09/M11) sits above the PLC on Ethernet. Differences are in openness and cost.

| Platform | Motion executed by | Safety executed by | ROS 2 attachment (2026) | Notes |
|---|---|---|---|---|
| Beckhoff TwinCAT 3 + EtherCAT | TwinCAT NC PTP (TC1250) on IPC/embedded PC; AX8000/AX5000 or EL72xx/economy EtherCAT drives | TwinSAFE: EL6910 logic terminal (or logic inside EL1918/AX8000) over FSoE; Cat 4/PL e, SIL 3 capable [S2][S3] | ADS: `beckhoff_ads_hardware_interface` (ros2_control SystemInterface, v1.0.0 2025-09-17) [S22]; OPC UA via TF6100 [S27]; TwinCAT runtime for real-time Linux (Debian + PREEMPT_RT) allows ROS 2 and TwinCAT on one IPC in containers [S30][S31] | Lowest-cost scalable I/O; free XAE engineering; licences per platform level |
| Bosch Rexroth ctrlX CORE (ctrlX OS, Ubuntu Core + PREEMPT_RT) | ctrlX MOTION app on CORE; ctrlX DRIVE; EtherCAT master app | ctrlX SAFETY (SafeLogic hardware) and, since Oct 2025, a software safety PLC app [S36] | Official ROS 2 SDK (`ctrlx-automation-sdk-ros2`, MIT, v3.1.0 2026-02-05, Jazzy) bridging ctrlX Data Layer to ROS 2 topics [S35] | Basic Set (CORE plus X3 + 16DI/16DO + PLC/Node-RED/EtherCAT apps) EUR 799 recommended [S9] |
| Siemens S7-1500F / ET 200SP F + SINAMICS S210 | S7-1500 T-CPU technology objects over PROFINET IRT | F-CPU (integrated safety program) + PROFIsafe to S210 (STO, SS1, SLS, SOS, SDI; SIL 3 / PL e) [S41] | No official ROS 2 product; OPC UA server on CPU; community Snap7/OPC UA bridges | Strongest one-vendor safety story; Siemens list prices are login-only; +10-23 % price adjustment announced for 2026-03-25 (secondary source) [S38] |
| Rockwell CompactLogix/Compact GuardLogix 5380 + Kinetix | Logix motion over EtherNet/IP CIP Motion | Compact GuardLogix 5380: SIL 2/PL d 1oo1, SIL 3/PL e 1oo2 with safety partner [S42]; CIP Safety STO in Kinetix | No official ROS 2; EtherNet/IP or OPC UA bridges | 5069-L306ERS2 USD 1,936.56 (Turtle & Hughes) [S8] |
| Omron NX1P2/NJ + NX-SL safety | NX CPU EtherCAT motion (NX1P2: up to 4-8 axes) | NX-SL3300/3500 safety CPU via EtherCAT coupler (FSoE) [S40] | No official ROS 2; OPC UA/EtherNet/IP | Sysmac Studio licence; prices via distributors |
| B&R X20 + ACOPOS P3 | X20 CPU, POWERLINK, ACOPOS P3 (50 us sampling) [S43] | openSAFETY SafeLOGIC, SafeMOTION in ACOPOS P3 | No official ROS 2; OPC UA | X20CP0484 EUR 1,340 (JC-Electronics reseller) [S44]; quote-only from B&R |
| Codesys-based (WAGO PFC200, Festo CPX-E, Phoenix PLCnext + Codesys runtime) | Codesys SoftMotion over EtherCAT master (runtime add-on) [S10][S11] | Separate safety controller (Pilz/Sick/Phoenix PSR) or Codesys Safety for EtherCAT | OPC UA (Codesys server); no official ROS 2 bridge | PLCnext AXC F 2152 has RT Linux and OPC UA; safety needs AXC F XT SPLC extension [S6] |
| Open: Linux PREEMPT_RT + IgH/SOEM EtherCAT + ros2_control | `ethercat_driver_ros2` (ICube, Apache-2.0, IgH master) or SOEM-based drivers [S23]; ros2_control main loop SCHED_FIFO 50 [S33] | Must be an external certified safety PLC (Pilz PNOZmulti 2, Sick Flexi, Phoenix PSRmodular) hard-wired to drive STO inputs; no certified FSoE master in open software | Native | PREEMPT_RT in mainline since Linux 6.12 (Sept 2024) [S34]; SOEM v2.0.0 is now GPLv3 or commercial licence [S25]; IgH is GPLv2 kernel module, stable-1.6 recommended [S24] |

### F2. PLC / IPC options

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | CX7000 (CX7080 with RS232/485) | Arm Cortex-M7 480 MHz, 8 DI/4 DO multifunction, TwinCAT/RTOS (closed FreeRTOS), TC1200 PLC licence included, platform level 10, < 2 W | price not published; request quote | regular delivery | Beckhoff product page "Documentation and downloads"; TraceParts hosts Beckhoff catalog (check per part) [S45] | [S1a] |
| Beckhoff | CX5230-0185 (TwinCAT/BSD) / -0195 (Win10 IoT 2021) | Atom x5-E3930 2-core 1.3 GHz, 4 GB DDR4, 2x GbE, 4x USB 3, DVI-D, 1-s UPS, E-bus/K-bus I/O, platform level 40 | price not published; request quote (TwinCAT licences separate) | regular delivery | as above | [S1b] |
| Beckhoff | C6030-0060 | ultra-compact IPC 132x133x76 mm, Celeron/Pentium 2-core (platform 50) up to Core i7, 0..55 C, IP20 | price not published; request quote | regular delivery | as above | [S1c] |
| Beckhoff | TwinCAT 3.1 licences TC1250-0vXX (PLC + NC PTP 10; includes TC1200 + TF5000) | platform levels 20 (Economy, Beckhoff RT Linux only) to 94; XAE engineering free | TwinCAT 3 Price List via sales; not public | n/a | n/a | [S26] |
| Beckhoff | TwinCAT runtime for real-time Linux / Beckhoff RT Linux (C9900-S62x/S63x, CXxxxx-021x) | Debian-based, mainline kernel with PREEMPT_RT, several TwinCAT runtimes in Docker/Podman/LXC on one IPC, GPU access from real time; first on CX82x0/CX9240, "successively rolled out" to other IPCs | included with OS option; request quote | n/a | n/a | [S30][S31][S32] |
| Phoenix Contact | AXC F 2152 (2404267) PLCnext | Arm A9 2x800 MHz, Yocto RT Linux, 1 ms task, PLCnext Engineer / C++ / Matlab, OPC UA server, PROFINET; safety only with AXC F XT SPLC 1000/3000 | price not published (login) | n/a | Phoenix product page (CAD tab) | [S6] |
| Bosch Rexroth | ctrlX CORE X3 / CORE plus X3/X5/X7 | ctrlX OS (Ubuntu Core, PREEMPT_RT kernel 6.1.33-rt11 in 02.06), EtherCAT master on RJ45, 2-16 GB RAM, apps from store | Basic Set EUR 799 recommended (CORE plus X3 + 16DI/16DO + PLC/Node-RED/EtherCAT apps), via partners | n/a | ctrlX configurator / product information PDF (dimensions); STEP via Rexroth media (not verified) | [S9][S37] |
| Siemens | CPU 1512SP F-1 PN 6ES7512-1SM03-0AB0 (successor of -1SK01) | ET 200SP-based F-CPU, 600 KB/2 MB, PROFINET IRT 3-port | list via Industry Mall login; grey market USD 399-699 (not recommended) [S38] | 25 days ex-works (Industry Mall) | SiePortal M-CAD/E-CAD download | [S39] |
| Rockwell | 5069-L306ERS2 Compact GuardLogix 5380 | SIL 2/PL d (1oo1); EtherNet/IP; CIP Safety | USD 1,936.56 (Turtle & Hughes, 2026) | 6 in stock | Rockwell product drawings (login) | [S8] |
| Omron | NX1P2-9024DT | 24 DI/10 DO built in, EtherCAT up to 4 synchronous axes; NX-SL3300 safety CPU via coupler | price via distributors (Digi-Key lists it) | n/a | Omron CAD download | [S40] |
| B&R | X20CP0484 / X20CP0484-1 | Arm A9 667 MHz, POWERLINK, fanless, base/PSU ordered separately | EUR 1,340 (JC-Electronics reseller) | in stock (reseller) | B&R downloads (login) | [S44] |
| Revolution Pi (KUNBUS) | RevPi Connect 5 | Raspberry Pi CM5-based 24 V IPC, EN 61131-2 design, PiBridge I/O, RevPi Gate EtherCAT is a slave gateway, not an EtherCAT master | Connect 4 from EUR 448 (shop); Connect 5 price not captured | 5-8 working days (Connect 4) | STEP on revolutionpi.com (not verified) | [S46][S47] |
| Autonomy Logic | OpenPLC Runtime v4 (MIT) | headless IEC 61131-3 runtime, SCHED_FIFO core, PREEMPT_RT optional; v3 (GPL-3.0, 1,573 stars) is end-of-life | free | n/a | n/a | [S48][S49] |

Who does what: in the Beckhoff case motion is TwinCAT NC on the IPC (drives in CSP/CSV mode over EtherCAT), safety is TwinSAFE logic (EL6910, or the logic inside EL1918/AX8000) communicating by FSoE to safe I/O and to the drives' STO/SS1/Safe Motion; ROS 2 never touches either path.

### F3. Safety controllers (logic)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | EL6910 TwinSAFE Logic | 212 safe connections, 128 groups, 512 FBs, analog processing, PROFIsafe master/slave, muting FBs, EN ISO 13849-1 Cat 4/PL e, SIL 3, ~1 ms cycle, 12 mm terminal | USD 670 (plcpartssolution.com reseller) | regular delivery | Beckhoff page downloads; TraceParts | [S2][S2b] |
| Beckhoff | EL1918 (8 safe DI + integrated TwinSAFE Logic, 128 connections); EL1918-2200 inputs only | Cat 4/PL e, SIL 3; test-pulse configurable per channel | price not published; request quote (est. USD 350-450 from EL2904 price ratio) | regular delivery | as above | [S3] |
| Beckhoff | EL2904 (4 safe DO 0.5 A) | Cat 4/PL e, SIL 3 | USD 249.78 (TME, 2026-10) | 0 in TME stock | as above | [S4][S50] |
| Beckhoff | EK1960 (20 safe DI + 24 safe DO + logic), EP1908/EP1918 IP67, EL6900 (older Boolean logic, 128 connections) | alternatives in the same family | request quote | regular delivery | as above | [S5] |
| Pilz | PNOZ m B0 (772100) | PNOZmulti 2 base, 20 safe DI, 4 safe semiconductor DO, PL e/SIL 3, expandable; PNOZ m ES EtherCAT (772136) fieldbus module | EUR 712.19 (Pilz eShop FI, 2026); PNOZ m B1 EUR 541.76; ES EtherCAT EUR 363.67; EF 8DI2DOT EUR 607.38 | ex-stock/on request | Pilz product page downloads | [S7] |
| Sick | Flexi Soft FX3-CPU000000 (1043783) + system plug | SIL 3, Cat 4, PL e; expansion modules | price via Sick login | n/a | sick.com CAD (login); sick.partcommunity.com | [S12][S51] |
| Sick | Flexi Compact FLX3-CPUC100 (1085349) / FLX3-CPUC200 | compact modular safety controller | FLX3-CPUC200 USD 1,976.05 (Newark) | n/a | as above | [S13][S14] |
| Phoenix Contact | PSRmodular / PSR-M-B1; PSRmotion zero/over-speed relays (PSR-MM25/MM30/MM35) | TUV-certified to PL e / SIL 3; sensor-free speed monitoring | price not captured; request quote | n/a | Phoenix CAD tab | [S52] |
| Pilz | PNOZ s4 (750104) safety relay | 3 N/O + 1 N/C, 22.5 mm, e-stop/gate/light-curtain monitoring | GBP 211.66 ex VAT (RS UK, 2026-05) | in stock | Pilz downloads | [S53] |
| Siemens | ET 200SP F-modules / 3SK1-3SK2 relays | PROFIsafe with S7-1500F | login pricing | n/a | SiePortal | [S39] |

### F4. Safety devices: e-stops, interlocks, light curtains, scanners, enabling switches, muting

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Schneider | XALK178 e-stop control station (XB4BS8445 head) | 1 NC trigger-action, twist release; XB4BS8445 head alone | USD 108.05 (Digi-Key, 2026); XB4BS8445 USD 121.28 (Digi-Key) | in stock | Digi-Key CAD models | [S54][S55] |
| Pilz | PITestop sets (e.g., SET4.1 PIT es3.1/box/2 n/c, 400520) | ISO 13850 e-stop sets | on request (eShop) | n/a | Pilz downloads | [S56] |
| Schmersal | AZM300Z-ST-1P2P (103001435) | RFID guard lock, power-to-unlock, M12 8-pin, PL e, IP69, series wiring | USD 788.00 (Applied Automation, Sep 2026); -A-T escape release USD 909 | 6 in stock | Schmersal product page CAD | [S15][S16] |
| Euchner | CTP-L1-AR-U-HA-AEE-SH (137164) / CTP-AP series | transponder-coded guard locking, PL e, escape release, M23 plug | on request (Euchner); MGB2 locking module MGB2-L1-MLI-U-Y0000-BJ (136776) USD 399.99 (Platinum International reseller) | n/a | Euchner product page (dimension drawings, CAD) | [S17][S18] |
| Euchner | MGB2 Modular / Classic gate box with MSM submodules (e-stop, buttons, key switch) | PROFINET/EtherCAT bus modules; full operator station at the door | request quote | n/a | Euchner page | [S19] |
| Pilz | PSENmlock PSEN ml b 1.1 unit (570400) | interlock + guard lock PL e/SIL 3, 7,500 N, bistable | on request (eShop) | n/a | Pilz page | [S20] |
| Pilz | PITenable PIT en1.0p-5m-s (401110) 3-stage enabling switch | ISO 13849 enabling for teach/jog | on request | n/a | Pilz page | [S21] |
| Sick | deTec4 Core Set 14/1500 (1062904) | Type 4, PL e/SIL 3, 14 mm, 10 m, kit with brackets, cables, RLY3-OSSD2 relay | deTec4 Core Set 30/900 USD 4,154 (nexinstrument, lead 6-8 wk); 14/1500 price via login | 6-8 weeks (reseller) | sick.com CAD (login) | [S57][S58] |
| Sick | deTec4 Set 30/1800 (1103385) | 30 mm, 30 m, 13 ms, SP2/DMM4 muting packages, cascade | login | n/a | as above | [S59] |
| Banner | EZ-Screen LS pair SLLP14-1050P88 (14 mm, 1050 mm) | Type 4 pair; cascade variants SLLCP23-1050-B16 | SLSP14-150P88 (150 mm) USD 1,154.01; SLLCP23-1050-B16 USD 2,273.01; SLLP23-840P88 USD 1,815.01 (SINLIN / zhschip resellers; treat as indicative) | in stock (resellers) | Banner site CAD | [S60][S61] |
| Keyence | GL-V / GL-R light curtains; SZ-V32N safety laser scanner | Type 4 PL e SIL 3 (GL-V); SZ-V: 190 deg, 20-150 mm resolution, 32 banks, up to 3 heads, CAD/CAE on page | Keyence publishes no list prices; quote | n/a | keyence.com CAD/CAE download | [S62][S63] |
| Sick | nanoScan3 Core I/O NANS3-AAAZ30AN1 (1100333) | 3 m protective field, 275 deg, 70 ms, Type 3, SIL 2, PL d, PFHd 8e-8, 106.6x80x117.5 mm; system plug separate | USD 3,444.30 (Lesman, 2026) | call for availability | sick.com CAD (login) | [S64][S65] |
| Sick | microScan3 Core MICS3-AAAZ40AZ1 (1067360) | 4 m protective field, 40 m warning | from USD 4,674 (Lesman) | n/a | as above | [S66][S67] |
| Leuze | RSL410-S/CU408-M12 (53800201) | safety laser scanner, 4-field | USD 6,027 list (Leuze US), ~25 business days | 25 days | Leuze page | [S68] |
| Pepperl+Fuchs | safety laser scanner | not confirmed as a current P+F product in this research; use Sick/Keyence/Leuze | unverified | - | - | - |
| Muting | IEC 62046:2018 clause 5.7 (muting for material access, anti-manipulation, two-sensor crossed-beam) | implemented with TwinSAFE/EL6900-EL6910 certified muting FBs or light-curtain function packages (deTec4 SP2/DMM4) | n/a | n/a | n/a | [S69][S2] |

### F5. Safe motion functions, fieldbus safety and standards

- IEC/EN 61800-5-2 defines STO (stop category 0), SS1 (monitored ramp to STO, category 1), SS2/SOS (controlled stop, drive stays in control), SLS, SSM, SSR, SDI; implemented inside the drive and triggered by hard-wired inputs or by the safety fieldbus [S70][S71].
- FSoE (Safety over EtherCAT, ETG.5100) uses the black-channel principle, is TUV-assessed, developed to IEC 61508 and standardized in IEC 61784-3; suitable up to SIL 3 [S72][S73]. PROFIsafe is the equivalent on PROFINET (Siemens S210: STO/SS1/SBC standard, SS2/SOS/SLS/SSM/SDI/SLA/SBT licensed) [S41].
- Beckhoff AX8108-01x0 gives STO/SS1 via hard wiring or FSoE; AX8108-02x0 adds Safe Motion (SLS, SLP etc. built from EL6910-type FBs inside the drive); the AX8000 TwinSAFE option meets EN ISO 13849-1 Cat 4/PL e, EN 61508 SIL 3, EN 62061 SIL CL3 [S74][S75]. AX5000 uses AX5801 (STO/SS1, USD 121.29 at TME) or AX5805 (Safe Motion) cards [S76][S50].
- Economy drives with STO: Delta ASDA-B3A-E/A3-E (STO, EtherCAT) [S77]; Leadshine EL8-EC (STO SIL 3) [S78]; Kollmorgen AKD2G (dual-channel STO, SafeMotion Monitor incl. FSoE) [S79]; Yaskawa SGD7S EtherCAT with FSoE variant [S80]. Steppers/integrated servos (Oriental AZ, Teknic ClearPath-EC) generally rely on external power removal or a hardware "power shutdown" input (AZD-AED lists 2 power-shut-down inputs) [S81].
- Standards status (2026): EN ISO 13849-1:2023 listed in the OJEU May 2024; the 2015 edition is withdrawn 15 May 2027; the EU Machinery Regulation 2023/1230 applies from 20 January 2027, which shortens the practical transition [S82][S83]. ISO 10218-1/-2:2025 published Feb 2025 (Part 2: 223 pages, CHF 227) [S84]. PL d per ISO 13849-1 requires a designated architecture (typically Cat 3: dual channel with diagnostics), MTTFd and DCavg targets and CCF measures per subsystem; the 2023 edition restructures around "subsystems", reworks parameter P in Annex A and adds EMC and software annexes [S82].

### F6. Servo drives and motors

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | AX8620 supply + AX8108-0100-0000 single-axis module (8 A rated / 20 A peak, STO/SS1), AX8206 dual-axis 2x6 A, AX8108-0200 Safe Motion | EtherCAT cycle <= 100 us, DC, OCT one-cable, EnDat 3, integrated C3 mains filter in supply, AX-Bridge tool-less linking | price not published; request quote | regular delivery | Beckhoff product page downloads (STEP/DXF); TraceParts catalog | [S74][S75][S85] |
| Beckhoff | AX5103-0000-0202 (3 A, 1 ch), AX5118-0000-0202 (18 A); AX5801-0200 STO card | 100-480 V AC, OCT, 62.5 us loops; 2-channel AX52xx variants | USD 1,228.27 / 2,137.91 / 121.29 (TME net, 2026-10, 0 in stock) | check | as above | [S50][S76] |
| Beckhoff | AM8021 (0.5 Nm), AM8031 (1.37-1.40 Nm, F3 72 mm), AM8041 (2.4 Nm), AM8051 (4.8-6.3 Nm) | OCT, electronic nameplate, 100-480 V | price not published; request quote (est. USD 600-1,000 per AM803x class, basis: AX5103 reseller price and typical servo-motor/drive ratio) | regular delivery | Beckhoff page; TraceParts | [S86][S87] |
| Beckhoff | AG2250-+PLE60 planetary gears (Neugart PLE factory-fitted) | ratios 3-512, lifetime lubrication | request quote | regular delivery | Beckhoff page | [S88] |
| Siemens | SINAMICS S210 + SIMOTICS S-1FK2 (e.g., 6SL3210-5HB10-4UF0 400 W + 1FK2104-4AK, 1.27 Nm) | PROFINET IRT/PROFIsafe, OCC one cable, SIL 3/PL e safe functions, 0.05-7 kW, EtherNet/IP from V6.3 | login pricing; request quote | n/a | SiePortal CAD | [S41][S89] |
| Delta | ASD-B3A-0421-E (400 W, 2.65 A, EtherCAT, STO) + ECM-B3M-C20604RS1 motor; ASD-B3A-0721-E 750 W | 24-bit encoder, STO | USD 632.80 drive, USD 421.60 motor, USD 711.20 (750 W) (Digi-Key, 2026); Digi-Key quotes 32-week standard lead time | 3 in stock / 32 wk | Delta CAD via Misumi/Delta site | [S77] |
| Delta | ASD-A3-0421-E | 400 W, 3.1 kHz bandwidth, EtherCAT, STO, full-closed loop | request quote | n/a | Delta site | [S90] |
| Yaskawa | SGD7S-2R8AA0A (400 W EtherCAT) + SGM7J-04A7D6S; Sigma-X SGDXS EtherCAT (new) | FSoE variant available | price on request (IAC); Centroid resells | n/a | yaskawa.com CAD drawings | [S80][S91] |
| Kollmorgen | AKD2G-6V03D (dual 3 A), -6V06D, -6V12S | EtherCAT + FSoE, SafeMotion Monitor, single-cable, 24 A max | request quote | n/a | Kollmorgen downloads | [S79] |
| Teknic | ClearPath-EC NEMA 17/23 integrated servo (EtherCAT, DC bus 24-75 V); ClearPath CPM-SDSK-2321S-RLN (step/dir) | integrated motor+drive+controller, daisy-chain EtherCAT, manual rev 1.14 2026-10-07 | SDSK-2321S USD 299 (automationtechnologiesinc reseller); EC pricing on teknic.com selector (not captured) | typically stock (Teknic) | Teknic site (STEP) | [S92][S93] |
| Oriental Motor | AZ series: AZD-AED (AC EtherCAT), AZD-KED2 (24/48 V DC EtherCAT), AZD4A-KED 4-axis EtherCAT | battery-free absolute stepper, CiA402 CSP/CSV, 2 power-shut-down inputs | AZD-AED EUR 618 list, AZD-KEP EUR 476 list (orientalmotor.eu, 5 wk) | 5 weeks | orientalmotor CAD download | [S81][S94] |
| Leadshine | EL8-EC (400-2000 W) / EL7-EC | EtherCAT, STO SIL 3, 23-bit encoders | price not on site; distributors | n/a | Leadshine downloads | [S78] |
| Nanotec / Synapticon / Elmo / STEPPERONLINE | PD4-E, Circulo/SOMANET Node, Gold Twitter, EtherCAT closed-loop steppers | not reached in this research (3-attempt rule) | unverified | - | - | - |

### F7. Gearboxes

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Neugart | PLE040/060/080 (Economy), PLFE (flange output), PLPE | backlash < 15/< 10/< 7 arcmin 1-stage (PLE40/60/80), IP54, ratios 3-512, catalog 05/2026 | PLE060 USD 197-500, PLE080 USD 350-700 (sigmasurplus surplus/reseller; indicative only); new price via NCP configurator quote | n/a | Neugart NCP configurator + Tec Data Finder (STEP) | [S95][S96][S97] |
| Wittenstein alpha | CP (Basic Line) / NP (Value Line) | CP <= 12 arcmin, NP <= 8 arcmin, ratio 3-100 | request quote | n/a | cad-point.wittenstein-group.com configurator (STEP) | [S98][S99] |
| Apex Dynamics | AB/PE series | high-precision planetary | request quote | n/a | apexdyna.com | [S100] |

### F8. I/O, fieldbus, switches, time sync

Why EtherCAT: all candidate drive families (Beckhoff, Delta, Yaskawa, Kollmorgen, Oriental, Teknic, Leadshine) speak it; distributed clocks synchronize every DC-capable device to the reference clock "generally less than 100 ns" [S101]; FSoE carries safety on the same cable; and both open masters (IgH, SOEM) and ros2_control drivers exist, so the same I/O works under TwinCAT or under a Linux research stack.

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | EK1100 EtherCAT coupler | 2x RJ45, 5 V/2 A E-bus, 10 A power contacts | USD 149.15 (TME, 38 in stock) | stock | Beckhoff page; TraceParts | [S50][S102] |
| Beckhoff | EL1008 (8 DI 3 ms), EL2008 (8 DO 0.5 A), EL3064 (4 AI 0-10 V) | 12 mm HD terminals | EL1008 USD 77 (iqelectro); EL2008 USD 56.90 (TME); EL3064 est. USD 200-250 (IMD guide pre-2020: EL3008 USD 240, possibly stale) | stock | as above | [S103][S50][S104] |
| Beckhoff | EL6224 (4-port IO-Link master), EL6224-0090 (TwinSAFE SC) | IO-Link V1.1, 500 mA/port | request quote (grey-market USD 20-47 not credible) | regular | as above | [S105] |
| Beckhoff | EL6688 IEEE 1588 PTP v1/v2 terminal; EL6685 reference clock | master/slave, usable as TwinCAT reference clock; external synchronization | request quote | regular | as above | [S106][S107] |
| Beckhoff | EtherCAT P (EK1300 coupler, EK1322 junction, EPP boxes) | 24 V Us + Up 3 A each on one 4-wire cable, IP67 | request quote | regular | as above | [S108] |
| ifm | AL1332 (EtherCAT IO-Link master, 8 ports, IP67); AL1930 DIN-rail | AoE/CoE/EoE/FoE, MQTT | AL1326 (EtherNet/IP sibling) list USD 464.20 (ifm US, 2026-10); AL1332 login | 1 pc expected 2026-10-19 (AL1326) | ifm product page CAD | [S109][S110] |
| Turck / Balluff | TBEN-L5-8IOL multiprotocol; BNI ECT-508 | 8-port IO-Link | request quote | n/a | vendor pages | [S111] |
| Moxa | EDS-2008-EL (8-port unmanaged, metal, 12/24/48 V) | 5-yr warranty, -10..60 C | price via distributors | n/a | 2D CAD on Moxa page | [S112] |
| Phoenix Contact | FL SWITCH 1008N | unmanaged 8-port | not captured | - | - | - |

### F9. Pneumatics: valve terminals, vacuum, needle grippers, compressor sizing

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Festo | VTUG valve terminal (573606) + CPX-AP-I-EC-M12 EtherCAT interface (8086609) | 10/14/18 mm valves, up to 24 positions, 13 pressure zones, 330/630/1200 l/min, IP65/67, vacuum-capable; CPX-AP-I 2048 B I/O | login to see price; request quote | n/a | festo.com "CAD data" on each product page (STEP) | [S113][S114] |
| Festo | VTEM Motion Terminal; CPX-E controller | app-controlled piezo valves; Codesys PLC | request quote | n/a | festo.com | [S115] |
| SMC | SY3000/5000/7000 manifold + EX600 SI unit (EtherCAT) | Cv 0.30/0.66/1.1, 0.35 W coils | request quote (SMC distributors) | n/a | smcworld.com CAD | [S116][S117] |
| Festo | OVEM vacuum generator (539074) | nozzle 0.45-3.0 mm, suction 13-348 l/min, IO-Link, ejector pulse, air-saving | login | n/a | festo.com CAD | [S118][S119] |
| SMC | ZK2 ejector | nozzle 0.7/1.0/1.2/1.5 mm: air consumption 24/40/58/90 l/min ANR, suction 29/44/61/67 l/min, energy-saving cut-off (-93 %) | request quote | n/a | smcworld.com CAD | [S120] |
| Schmalz | SNG-V 10 1.2 V-7 needle gripper (10.01.29.00176) | 10 needles 1.2 mm, 7 mm stroke, 30 deg, 3-7 bar, 265 g, 149x32x56 mm, double-acting cylinder; SNG-BV adds Bernoulli float cup | login to see price | n/a | schmalz.com Live CAD (STEP) | [S121][S122] |
| Festo | MS4/MS6 FRL, VPPM proportional regulator, DSNU/ADN cylinders | standard | login | n/a | festo.com | [S113] |

Compressor sizing (est., method): sum ejector consumption at duty cycle plus actuator volume per cycle. Example for this cell: 8 ZK2x10 ejectors (40 l/min each) at 30 % duty = 96 l/min; 20 needle grippers (double-acting, est. 0.02 l free air per stroke at 6 bar, 2 strokes/cycle, 10 cycles/min) = 8 l/min; 40 cylinders/valves est. 60 l/min at duty; purge/blow-off est. 40 l/min; subtotal ~200 l/min (7 cfm); with 1.5 safety factor ~300 l/min (10.6 cfm) at 6-7 bar, i.e., a 2.2-3 kW screw or a 3 kW piston compressor with dryer. Basis: SMC ZK2 and Festo OVEM consumption data [S120][S118]; actuator volumes are estimates until the ST03/ST04 gripper counts are fixed. The white paper's requirement to meter air/vacuum as a utility stands [WP lines 563-568].

### F10. Cabinet components, power, EMC and grounding

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Rittal | AX 1180.000 compact enclosure | 800x1000x300 mm, sheet steel, IP66, UL Type 4/12, mounting plate | price not shown on rittal.com; request quote (est. USD 900-1,300, basis: typical AX 800x1000 pricing, unverified) | n/a | rittal.com CAD data (STEP via product page / RiPanel) | [S123][S124] |
| Rittal | AX 1380.000 (380x380x210) | small sub-panel (e.g., station I/O boxes) | request quote | n/a | as above | [S125] |
| Phoenix Contact | QUINT4-PS/1AC/24DC/20 (2904602); /10 (2904601) | 20 A, SFB, dynamic boost 30 A/5 s; 10 A unit 20 A boost | USD 550.99 (RSP Supply) | n/a | Phoenix CAD tab | [S126][S127] |
| PULS | CP20.241 (480 W, 95.6 %) ; QT20.241 | 20 A | USD 560 (Powermatic Associates); QT20.241 USD 775 (Standard Electric) | 20 in stock | PULS page STEP | [S128][S129] |
| Mean Well | NDR-480-24 (20 A) | economy DIN PSU | USD 105.80 (Digi-Key, 17-wk mfr lead, 894 in stock) | stock | Digi-Key CAD | [S130] |
| PULS | UB10.241 DC-UPS controller + UZK12.261 battery module | 24 V/10 A buffer | USD 553.50 (automationdistribution) / 615 (RITEC); battery module USD 670 | stock | PULS page | [S131][S132] |
| Schneider | XB4BS8445 e-stop head; XALK178 station | see F4 | USD 121.28 / 108.05 (Digi-Key) | stock | Digi-Key CAD | [S54][S55] |
| Schneider / ABB / Siemens | iC60N MCBs, LC1D contactors, 3LD2 disconnect; Phoenix PT 2,5 terminals; WAGO 2002; Panduit duct; Brady/Thermomark labels; Phoenix FLT surge | commodity items | not individually priced in this research; est. USD 800-1,500 per cabinet set (basis: typical panel-shop BOMs, unverified) | stock | vendor CAD portals | [S133] |

EMC and grounding practice (from vendor manuals): AX8000 supply modules have an integrated category C3 mains filter; category C2 (first environment) needs the AX2090-NF80 filter plus a mains choke for long motor cables; ground all modules with large-area, low-impedance connections on an unpainted galvanized mounting plate using the supplied serrated nuts; terminate motor-cable shields 360 degrees at both ends [S134][S135]. AX5000: category C3 standard, motor cables < 25 m without choke, C2 only with AX2090-NF50 filter [S136]. Siemens' SINAMICS EMC configuration manual (2024/03) prescribes HF-capable equipotential bonding with toothed contact discs, a zone concept separating line filter/converter/motor zones, shield clamps over a large area, and limiting transient overvoltages on 24 V interfaces [S137]. EN 61800-3 category C2/C3 definitions apply [S135].

### F11. HMI and operator interface

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | CP2912-0010 (12", 800x600, CP-Link 4, multi-touch, IP65 front); CP2907 7"; CP2915 15"; CP39xx arm-mount IP65 | CP-Link 4 up to 100 m over Cat.6A | USD 1,812 (e-motionsupply, lead 5-7 wk) | 5-7 weeks | TraceParts has CP29xx (e.g., CP2915) STEP [S45] | [S138][S139] |
| Beckhoff | TF2000 TwinCAT 3 HMI Server (web HMI, 1 client + 1 controller base) | platform-level licence | request quote | n/a | n/a | [S140] |
| Siemens | KTP700 Basic 6AV2123-2GB03-0AX0 (7", 800x480, PROFINET) | phase-out from 15.12.2026 per Industry Mall; successor Unified Basic MTP700 | login list price (EGP 53,481 incl. tax at MET Egypt as indicative) | 1 day ex-works | SiePortal M-CAD | [S141][S142] |
| Red Lion | Graphite G10C0000 10" | protocol converter HMI, OPC UA client, MQTT | USD 4,433 (Lesman) | call | Red Lion downloads | [S143] |
| Patlite | LR6-302WJNW-RYG (3-tier, direct mount) / LR6-302PJNW-RYG (pole) | 24 V, IP65; IO-Link/M12 variants exist | USD 140 / 166 (shop.patlite.com, 50 in stock) | stock | Patlite CAD | [S144] |
| Werma | KombiSIGN 71 / 696 / eSIGN | modular tower lights | AUD 73.20 ex GST per module (Pacific Automation, indicative) | n/a | Werma site | [S145] |
| Web HMI | TwinCAT HMI (HTML5), Node-RED (ctrlX app), browser on operator PC | no panel hardware required beyond a touch display | - | - | - | [S140][S9] |

### F12. PLC <-> ROS 2 links and time synchronization

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| beckhoff_ads_hardware_interface (b-robotized) | 1.0.0, 2025-09-17 (jazzy, kilted) | Apache-2.0 | new; built on official Beckhoff/ADS; sum-commands = 2 network transactions per update | Primary M09 physical backend to TwinCAT (joint states/commands, GPIO) | [S22] |
| ads_vendor | 1.0.2 | Apache-2.0 | vendors Beckhoff ADS C++ library into ROS 2 build | dependency of the above | [S146] |
| Beckhoff/ADS (official C++ library) | ongoing | MIT (per repo) | official | ADS over TCP, also ADS-over-MQTT for TwinCAT for Linux deployments [S147] | [S22] |
| TwinCAT TF6100 OPC UA | 4026 | commercial | Data Access, HDA, A&C | non-RT interface for M07/M12/M14; ROS 2 via open62541-based clients | [S27] |
| ethercat_driver_ros2 (ICube) | jazzy branch, 2022- | Apache-2.0 | 91 commits; IgH master; CiA402 generic plugins; examples repo | fallback "open" backend if no PLC; cannot provide certified safety | [S23][S148] |
| soem_vendor_ros2 / soem ROS package | tracks SOEM 1.4.x; SOEM v2.0.0 (11 Jul, GPLv3 or commercial) | GPL | 2k stars | licence change matters for a product | [S25][S149] |
| IgH EtherCAT master | stable-1.6 recommended; 16 releases | GPLv2 | 3,079 commits | kernel module; needs matching NIC drivers | [S24][S150] |
| ctrlx-automation-sdk-ros2 | 3.1.0, 2026-02-05 (Jazzy) | MIT | 31 stars, 12 forks | official bridge Data Layer <-> ROS 2 if ctrlX chosen | [S35] |
| ros2_control controller_manager | Rolling docs 2026 | Apache-2.0 | mature | SCHED_FIFO 50, memory locking, real-time kernel recommended; overrun handling | [S33][S151] |
| Linux PREEMPT_RT | mainline since 6.12-rc1 (2024-09-29) | GPLv2 | mainline | basis for Beckhoff RT Linux, ctrlX OS, and the ROS 2 PC | [S34] |
| OpenPLC Runtime v4 | 2025- | MIT | v3 EOL; v4 993 commits | research only; no safety certification, no EtherCAT motion | [S48] |

Time sync: inside EtherCAT, distributed clocks keep all DC devices within < 100 ns of the reference clock [S101]; TwinCAT can itself be slaved to an external PTP grandmaster via EL6688, or act as master, so the ROS 2 PC (linuxptp ptp4l/phc2sys, hardware-timestamping NIC) and the PLC can share one IEEE 1588 timebase; TwinCAT readjusts its clock by up to half a cycle per step ("external synchronization") [S106][S107][S152]. For this cell, sub-millisecond agreement between camera timestamps (ST10) and PLC I/O timestamps is enough; PTP achieves microseconds.

### F13. Cabinet parts-list template with estimated counts from station I/O

I/O estimate per station (est., basis: mechanisms named in the white paper for each station; counts are planning placeholders to be replaced by the station designs from R01-R04/R06-R08):

| Station | Servo/stepper axes | DI | DO (incl. valve coils unless on a fieldbus valve terminal) | AI/IO-Link | Safety I/O |
|---|---|---|---|---|---|
| ST01 roll handling | 3 (unwind, edge guide, feed) | 8 | 6 | 3 (tension, 2 edge sensors) | 2 safe DI (local e-stop) |
| ST02 cutting | 6 (X, Y, Z, C knife, conveyor, vacuum VFD) | 10 | 8 | 2 | guard 2 safe DI + lock 1 |
| ST03 extraction/buffer | 4 (X, Y, Z, C) | 16 | 12 | 4 vacuum switches (IO-Link) | guard 2 safe DI + lock 1 |
| ST04 manipulation (gantry; arm has its own controller) | 4 | 14 | 12 | - | arm STO 2 safe DO + 2 safe DI; light curtain pair 2 safe DI |
| ST05 sewing heads (3) | 6 (3 main motors + 3 feed assist) | 14 | 10 | 3 | guard 2 safe DI + lock 1 |
| ST06 collar module | 2 | 4 | 4 | - | - |
| ST07 finishing/output | 1 | 10 | 14 | - | light curtain pair 2 safe DI, muting 4 DI |
| ST09 operator | - | 4 (reset, mode) | 3 (tower light) | - | 4 e-stop stations 8 safe DI; enabling 2 safe DI; STO groups 8 safe DO; air dump 2 safe DO |
| ST10 vision | - | 2 | 6 (triggers, lights) | - | - |
| Totals (est.) | 26 axes (12 high-performance, 14 economy) | 82 | 75 | 12 | 26 safe DI, 12 safe DO, 3 lock outputs |

Cabinet parts list template (quantities derived from the table; prices as found in F2-F11, "est." where not published):

| # | Item | Qty | Candidate part | Unit price basis |
|---|---|---|---|---|
| 1 | Main controller | 1 | Beckhoff C6030 (or CX5230) with TwinCAT/BSD or Beckhoff RT Linux, TC1250-0v50/0v40 licence | quote |
| 2 | EtherCAT couplers / junctions | 4 | EK1100 (one per station cluster), EK1122 junctions as needed | USD 149 ea (TME) |
| 3 | Digital input terminals | 12 | EL1008 (96 ch for 82 DI) | USD 77 ea |
| 4 | Digital output terminals | 10 | EL2008 (80 ch for 75 DO) | USD 57 ea |
| 5 | Analog input terminals | 2 | EL3064 | est. USD 200-250 ea |
| 6 | IO-Link masters | 3 | EL6224 (12 ports) or 1x ifm AL1332 in field | quote / USD 464 (AL1326 sibling) |
| 7 | Safety logic | 1 | EL6910 | USD 670 |
| 8 | Safe inputs | 4 | EL1918-2200 (32 ch for 26) | quote (est. USD 350-450) |
| 9 | Safe outputs | 4 | EL2904 (16 ch for 12 + 3 locks) | USD 250 ea |
| 10 | PTP terminal | 1 | EL6688 | quote |
| 11 | Power feed / end terminals | 6 | EL9410, EL9011, EL9100 | small |
| 12 | High-performance axes | 12 | AX8620 supply + 6x AX8206 dual-axis (STO/SS1 option) + AM803x/AM804x OCT motors | quote (est. USD 1,500-2,500 per axis incl. motor; basis AX5103 USD 1,228 + motor est.) |
| 13 | Economy axes | 14 | Oriental AZD-AED/AZD-KED2 + AZ motors, or Delta ASD-B3A-E + ECM-B3M, or ClearPath-EC | EUR 618 drive list; USD 633 + 422 (Delta) |
| 14 | 24 V power supplies | 2 | QUINT4-PS/1AC/24DC/20 (control) + PULS CP20.241 (field/valves) | USD 551 / 560 |
| 15 | DC-UPS | 1 | PULS UB10.241 + UZK12.261 | USD 554 + 670 |
| 16 | Main disconnect, MCBs, contactors, surge | 1 set | Siemens 3LD2, Schneider iC60N, LC1D, Phoenix FLT | est. USD 800-1,500 |
| 17 | Enclosures | 2 | Rittal AX 1180.000 (control) + AX 1180.000 (drives/power) or one VX25 | quote (est. USD 900-1,300 ea) |
| 18 | HMI | 1 | CP2912-0010 + TF2000 licence (or browser on operator PC) | USD 1,812 + quote |
| 19 | Tower light | 1 | Patlite LR6-302WJNW-RYG | USD 140 |
| 20 | E-stop stations | 4 | Schneider XALK178 | USD 108 ea |
| 21 | Guard-locking interlocks | 4 | Schmersal AZM300Z-ST-1P2P or Euchner CTP-L1 | USD 788 ea |
| 22 | Light curtains | 2 pairs | Sick deTec4 Core set or Banner EZ-Screen LS 14 mm pairs | USD 1,150-4,150 per pair |
| 23 | Enabling switch | 1 | Pilz PITenable | quote (est. USD 300-500) |
| 24 | Safety laser scanner (optional, loading side) | 0-1 | Sick nanoScan3 Core | USD 3,444 |
| 25 | Ethernet switch | 1 | Moxa EDS-2008-EL | est. USD 150-250 |
| 26 | Valve terminals | 3 | Festo VTUG + CPX-AP-I-EC or SMC SY5000 + EX600 | quote |
| 27 | Terminal blocks, duct, rail, ferrules, labels, cables (OCT, M12, EtherCAT) | 1 set | Phoenix PT 2,5, Panduit, Beckhoff ZK4xxx OCT cables | est. USD 2,000-4,000 |

Order-of-magnitude total for ST09 (est.): control + I/O + safety logic USD 7-9k; safety devices USD 8-12k; cabinet, power, HMI, switch, misc USD 7-10k; drives for the 26 axes USD 25-40k if 12 axes are AX8000-class and 14 economy (drives may be booked to their stations). Hence ST09 proper (without drives) is about USD 22-31k reference; with drives USD 47-71k.
