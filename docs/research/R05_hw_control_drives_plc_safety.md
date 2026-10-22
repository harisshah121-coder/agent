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
