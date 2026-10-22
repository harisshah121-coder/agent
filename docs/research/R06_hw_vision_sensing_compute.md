# R06 · Vision, sensing and compute (ST10 and sensors across stations)

Research agent R06 · written 2026-10-21 · scope per `_BRIEFS.md` §R06. All prices carry currency, date seen and basis (list / reseller / quote / est.). "CAD?" records whether vendor geometry is downloadable and where, because the 3D model (BUILD_GUIDE_3D_MODEL) is built from vendor geometry.

<!-- SUMMARY_PLACEHOLDER -->

## Findings

### F0. Resolution and optics math for ±0.5 mm over a 1.5 m field (cut bed, ST02)

Assumptions: the cut-piece geometry check must confirm panel outlines to ±0.5 mm over a single-ply bed field of about 1.5 m × 1.5 m (fabric width up to ~1.6 m open width; one T-shirt marker length ≈ 1.2–1.5 m). Knit ply thickness 0.5–1.2 mm, held flat by vacuum. Numbers below are arithmetic from these assumptions, not vendor claims.

1. **Pixel size target.** Sub-pixel edge detection on a well-lit, high-contrast silhouette gives 0.1–0.3 px repeatability, but lens distortion residuals, perspective (ply height) error, calibration drift and fabric relief eat most of a ±0.5 mm budget. Design rule used here: ground sample distance (GSD) ≤ tolerance/3 ≈ **0.17 mm/px** for a metrology-grade check, or ≤ tolerance/2 = **0.25 mm/px** if a 0.3 px sub-pixel edge locator is qualified on real knit edges. 1 px = tolerance (0.5 mm/px) is not acceptable for a ±0.5 mm claim.
2. **Pixels needed across 1.5 m.** 1500 mm / 0.17 mm = **8,800 px**; 1500 / 0.25 = **6,000 px**; 1500 / 0.5 = 3,000 px.
3. **What single sensors give over 1.5 m (long axis):**
   - 24 MP Sony IMX530, 5328 × 4608 px (Basler a2A5328-49g10m, 1.2" format) → 1500/5328 = **0.28 mm/px**, field 1.50 × 1.30 m [S1].
   - 20.4 MP IMX541, 4504 × 4504 px (Lucid TRT204S, 1.1") → **0.33 mm/px**, 1.50 × 1.50 m [S13].
   - 16 MP IMX532, 5320 × 3040 px (Basler a2A5320-75g10m, 1.1") → **0.28 mm/px**, but only 0.86 m in the short axis [S2].
   - 12 MP IMX535/IMX304, 4096 × 3000 px → 0.37 mm/px over 1.5 m [S3].
   - Conclusion: **no single ≤24 MP camera meets 0.17–0.25 mm/px over 1.5 m.** Options are (a) a 45–65 MP+ large-format camera (Basler boost 45 MP CXP-12, Lucid Atlas10/Atlas25 61–105 MP; cost $7.5k+ for camera alone and a frame grabber or 10/25GigE NIC) [S4][S14]; (b) **tile 4 cameras** of 12–16 MP each over ~0.8 × 0.8 m quadrants with 10 % overlap → 0.19–0.26 mm/px, mosaic-calibrated with one bed-wide target; (c) **line-scan during bed motion**: 4k over 1.5 m = 0.37 mm/px, **8k = 0.18 mm/px**, 16k = 0.09 mm/px, encoder-triggered from the conveyor so the field length is unlimited [S20][S21]. Option (c) is the cheapest way to hit 0.17 mm/px and is what fabric-inspection and cutter vendors do; option (b) is the cheapest area-scan route and also gives live (non-moving) images for ST03 extraction.
4. **Perspective (ply-height) error with non-telecentric lenses.** A point at radial offset *r* from the optical axis imaged at working distance *WD* is displaced by *Δ = h · r / WD* when its height differs by *h* from the calibration plane. Example: one camera over 1.5 × 1.5 m at WD = 2.0 m, corner r = 1.06 m, h = 1 mm (calibrated to the bed instead of the ply top) → Δ = **0.53 mm**: the whole tolerance. Mitigations: calibrate the plane to the ply top surface (not the bare bed), keep the ply flat (vacuum), limit the half-field angle to ≤ 15° (r/WD ≤ 0.27, Δ ≤ 0.27 mm per mm of height error) by using longer focal lengths / larger WD, or tile cameras. **Telecentric lenses are not an option at this scale**: the largest catalogue telecentrics cover ~242 mm fields (Edmund TitanTL, 4/3" format) [S30]; 1.5 m telecentric optics do not exist as products.
5. **Focal length.** f ≈ sensor width × WD / field width. For a 1.2" sensor (IMX530, 14.6 × 12.6 mm) covering 1.5 m at WD 2.0 m: f ≈ 14.6 × 2000 / 1500 ≈ **19.5 mm** → 20 mm lens (or 16 mm at WD 1.65 m). For a 0.8 m tile at WD 2.0 m with a 1.1" sensor (14.5 × 8.3 mm): f ≈ 36 mm → 35 mm lens. Lens must resolve 2.74 µm pixels (≥ 180 lp/mm): Fujinon CF-ZA-1S (1.2", 2.74 µm) or Kowa XC series; the 3.45 µm-class HC/JC series are marginal at the corners [S31][S32].
6. **Line-scan geometry.** 8k line over 1.5 m at 0.18 mm/px: with bed/feed speed 0.3 m/s the line rate needed = 0.3 / 0.00018 = 1.7 kHz (any Linea Lite 8k at 25 kHz is 15× headroom) [S21]. A 1.5 m line at WD 1.5 m has a 26.6° half-angle at the edges; the same Δ formula applies across the web but not along it, and a line-scan backlight (Ai BL168-class) under a transparent stage, or a dark bed with dark-field bars, gives the silhouette.
7. **Frame rate at the needle (ST05/ST06).** Area-scan frame rate scales roughly with ROI height; a 2.3 MP sensor at 160 fps full frame (Basler a2A1920-160um) reaches > 500 fps at 1920 × 200 px ROI; a 0.3 MP IMX287 camera runs 525 fps full frame [S9][S10]. At 5,000 stitches/min (83 Hz needle) a 200 fps edge tracker samples every 2.4 stitches; 500 fps every stitch. USB3 (≤ 5 m) or 2.5GigE (M12, PoE) are both adequate; latency is dominated by the PC side (budget 5–10 ms end-to-end).

### F1. 2D area-scan cameras (industrial, GenICam)

All vendors below publish STEP/IGES through their own sites (Basler: per-model page "CAD/technical drawing"; Lucid: "Drawings" tab; FLIR/IDS/Allied: product-page downloads; Hikrobot/Daheng: download centre). Prices are single-unit; volume discounts of 10–25 % are normal at 10+ units.

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Basler | ace 2 R a2A5328-49g10m (24 MP, 10GigE) | Sony IMX530 1.2" global shutter, 5328 × 4608, 2.74 µm, 45.5 fps GVSP / 49.7 fps RDMA (GigE Vision 3.0), 1/2.5/5/10GigE, C-mount, 54.9 × 29 × 29 mm, 105 g | price not published on docs page; request quote (order via Basler shop; est. USD 2,500–3,500 based on ace 2 10GigE class, est.) | Basler shop "ready for dispatch" typical; 10GigE models newer (datasheets dated 2026-10-01) | Yes: STEP/drawing on docs.baslerweb.com model page | [S1] |
| Basler | ace 2 R a2A5320-75g10m (16 MP, 10GigE) | IMX532 1.1", 5320 × 3040, 69 fps, GigE Vision 3.0 RDMA | not published; quote | as above | Yes (Basler docs) | [S2] |
| Basler | ace 2 R a2A4096-98g10m (12 MP, 10GigE) | IMX535 1/1.1", 4128 × 3008, 90.5/98.9 fps | not published; quote | as above | Yes | [S3] |
| Basler | ace 2 R a2A1920-160umPRO (2.3 MP, USB3) | IMX392 1/2.3", 1920 × 1200, 160 fps, global shutter, 36.3 × 29 × 29 mm, –10…60 °C | USD 620 (Edmund Optics, 2026-10, reseller, 2 in stock); USD 527 (Soda Vision, reseller); EUR 535 (Edmund EU) | in stock | Yes (Basler docs; Edmund drawing) | [S9][S11] |
| Basler | ace 2 R a2A1920-160umBAS | same sensor, Basic feature set | USD 395 (Soda Vision, reseller) | stock | Yes | [S11] |
| Basler | ace 2 R a2A1920-51gcPRO (2.3 MP GigE, PoE) | IMX392, 51 fps, GigE | not captured; est. USD 500–650 | "ready for dispatch" | Yes | [S12] |
| Basler | ace U acA720-520um (0.3 MP, 525 fps USB3) | IMX287 1/2.9", 720 × 540, 525 fps | not published on page; quote | shop | Yes | [S10] |
| Basler | boost CXP-12 (e.g. 45 MP boA8100-… class) | CoaXPress-12, up to 150 fps at lower resolution; needs CXP frame grabber | "list price USD 7,559" shown on family page for one model (model not resolved in excerpt), 2026-10 | quote | Yes | [S4] |
| Teledyne FLIR | Blackfly S BFS-PGE-50S5M-C (5 MP GigE PoE) | IMX264 2/3", 2448 × 2048, 3.45 µm, 24 fps, C-mount, 29 × 29 × 30 mm | USD 1,320 (Edmund, 2026-10, reseller); Teledyne page shows USD 878 (2026-10) — conflicting, treat Teledyne direct price as list | 3–4 weeks (Clearview UK for board-level variant) | Yes (Teledyne product page: 3D model) | [S15][S16] |
| Teledyne FLIR | Blackfly S BFS-U3-16S2M (1.6 MP USB3) | IMX273 1/2.9", 1440 × 1080, **226 fps**, global shutter, 36 g, CS-mount | not captured; est. USD 500–600 (FLIR BFS 1.6 MP class, est.) | stock | Yes | [S17] |
| IDS | uEye+ GV-5880CP-C-HQ (5 MP GigE PoE) | 1/1.8" sensor, 29 × 29 × 29 mm, 51 g | USD 530 (Edmund, 2026-10, reseller, in stock) | in stock | Yes (IDS download centre: STEP) | [S18] |
| Allied Vision | Alvium 1800 U-508 (5.1 MP USB3) | IMX250 2/3", 2464 × 2056, 84 fps, status "Available" | not published; quote (Alvium 5 MP class est. USD 500–700) | quote | Yes (AV product page downloads) | [S19] |
| Lucid Vision Labs | Triton TRI050S-MC (5 MP GigE PoE, IP67) | IMX264, 2448 × 2048, 22 fps, M12 X-coded, 29 × 29 × 45 mm, 67 g | login required for price (Lucid web store) | stock | Yes ("Drawings" tab, STEP) | [S13a] |
| Lucid Vision Labs | Triton2 TRT050S / TRT051S (5 MP 2.5GigE) | IMX264 35.6 fps / IMX547 49.2 fps, 2.5GBASE-T PoE, IP67 | login required | stock | Yes | [S13b] |
| Lucid Vision Labs | Triton2 TRT162S (16.2 MP) / TRT204S (20.4 MP) / TRT245S (24.5 MP) 2.5GigE | IMX542 17.5 fps / IMX541 13.5 fps / IMX540 11.3 fps, 2.74 µm, 1.1–1.2" | login required | stock | Yes | [S13] |
| Hikrobot | MV-CS050-10GC (5 MP GigE) | IMX264, 2448 × 2048, GigE Vision 2.0, GenICam, 100 m cable | USD 206–350 (Chinese resellers via Accio aggregator, 2026-09/10, reseller; not official) | 1–3 weeks typical | Yes (Hikrobot download centre, registration) | [S22][S23] |
| Daheng Imaging | MER2-503-36U3M (5 MP USB3) | IMX264, 36 fps, 29 mm cube, 65 g, 1.75 W, 0–45 °C | not published; USD 222–277 seen for 12 MP MER2-1220-9GM (HK reseller, Accio, 2026-10) | 1–3 weeks | Yes (Daheng downloads) | [S24][S25] |

Interface guidance (from the datasheets above): 1GigE ≈ 125 MB/s (5 MP mono8 at ≤ 24 fps), 2.5GigE ≈ 300 MB/s, 5GigE ≈ 600 MB/s, 10GigE ≈ 1.2 GB/s with RDMA (GigE Vision 3.0) to offload the CPU; USB3 ≈ 380–440 MB/s but ≤ 5 m passive cable; CoaXPress-12 needs a frame grabber (USD 1–2k) and is only justified for > 10GigE throughput [S1][S13][S14]. Basler's pylon 26.08 notes recommend dual-channel DDR4-3600 or better hosts for 5GigE/1GigE multi-camera streaming [S40].

### F2. Lenses (fixed focal and telecentric)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Kowa | LM16XC (XC series, 4/3", 20 MP, 3.0 µm pixels) | 16 mm, F2–22, 160 lp/mm centre, TV distortion 0.02 %, Ø45 × 79.5 mm, 250 g; same series LM8XC/LM12XC/LM25XC/LM35XC/LM50XC; covers 1.1"/1.2" sensors (IMX540/541/542/530/532) | EUR 1,055 (LM16XC), EUR 899 (LM25XC, LM35XC), EUR 1,087 (LM12XC), EUR 1,154 (LM8XC); kowa-lenses.com list ex VAT, 2026-10 | stock (web shop) | Yes: STEP after free registration on kowa-lenses.com | [S32] |
| Kowa | LM12HC / LM8HC / LM25HC / LM50HC (HC series, 1", 5 MP, ≥ 5 µm pixels) | 12.5 mm F1.4–16, 2/3"–1" sensors (3.45 µm class marginal) | EUR 368 / 452 / 415 / 434 list ex VAT, 2026-10 (LM12HC out of stock) | stock except LM12HC | Yes (registration) | [S33] |
| Kowa | LM8JC / LM12JC / LM16JC (2/3", JC series) | low-cost 2/3" megapixel lenses for 5 MP IMX264 cameras at sewing heads | EUR 143 each, list, 2026-10 | stock | Yes (registration) | [S33] |
| Fujinon (Fujifilm) | CF25ZA-1S (CF-ZA-1S series, 1.2", 2.74 µm class, 23 MP) | 25 mm F1.8–16, C-mount; series 8–50 mm for 1.1"/1.2" sensors | USD 749 net list (Basler shop, 2026-10, "express delivery"); USD 790.20 sale / 1,955 regular (Machine Vision Direct) | express | Yes (Fujifilm downloads; Basler shop drawings) | [S34] |
| Fujinon | HF-XA-5M series (HF6XA-5M … HF50XA-5M, 2/3", 3.45 µm) | "4D high resolution", anti-shock; 6–50 mm | price not captured; est. USD 350–600 (est., class) | stock | Yes (Fujifilm) | [S31] |
| Computar | MPY series V0828…V5028-MPY (1.1", 24 MP) | 8–50 mm F2.8; **marked "Discontinued" on computar.com (2026-10)**; do not design in | n/a | n/a | n/a | [S35] |
| Basler | C125-0418-5M f4 mm (C125 5 MP series) | 1/2.5", 4 mm; example of Basler-branded lens pricing/lead time | USD 178 net list, Basler shop 2026-10, "standard approx. 12 weeks"; USD 238.21 Graftek in stock | 12 weeks (Basler) / stock (Graftek) | Yes (Basler docs) | [S36] |
| Edmund Optics | TECHSPEC TitanTL telecentric (max FOV 242 mm, 4/3") | largest catalogue telecentrics; 1.5 m fields impossible; 2017 brochure (possibly stale but still current family) | not captured; est. USD 3,000–8,000 per lens (est.) | stock | Yes (Edmund CAD per SKU) | [S30] |

Lens rule for this project: pixel 2.74 µm sensors need ≥ 180 lp/mm lenses (Kowa XC, Fujinon CF-ZA-1S); 3.45 µm sensors (IMX264/IMX392/IMX273) are fine with Kowa JC/HC or Fujinon HF-XA-5M. Use 1.2" format lenses on 1.1" sensors for corner illumination margin.

### F3. Line-scan cameras (ST01 unwind inspection, optionally ST02 bed scan)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Teledyne DALSA | Linea Lite L2-GM-04K02B-00-A (4k mono) | 4096 × 2 bilinear, 7 µm, 25 kHz, GigE PoE, 46 × 46 × 37 mm, 111 g, M42 mount, –10…65 °C | price not captured; 4k colour L2-GC-04K01B-00-A EUR 880 (Edmund EU, 4 in stock, 2026-10) | stock | Yes (Teledyne product page downloads; Edmund drawing) | [S20][S21] |
| Teledyne DALSA | Linea Lite L2-GM-08K02S-00-A (8k mono) | 8192 × 1 (two 4k rows, ½-px offset), 3.5 µm, 25 kHz, GigE PoE | SGD 1,603 (Edmund SG, 1 in stock, 2026-10) ≈ USD 1,200 (est. conversion) | stock | Yes | [S21] |
| Teledyne DALSA | Linea Lite L2-GM-02K05B-00-A (2k mono, 50 kHz, 14 µm) | lowest cost line scan; 2k over 1.5 m = 0.73 mm/px (only for gross defects) | not captured | stock | Yes | [S20] |
| Teledyne DALSA | Linea GigE LA-GM-04K08A (4k, 7.04 µm, up to 80 kHz TurboDrive); CL/CLHS versions to 16k | higher-end Linea family | not captured | — | Yes | [S21] |
| Basler | racer 2 (2k–16k, up to 240 kHz, GigE/CXP, "ready for dispatch") | family pages show net list prices USD 1,967 and USD 2,759 (specific models not resolved in the excerpt) | USD 1,967–2,759 list, 2026-10 (model unresolved) | stock | Yes (Basler docs) | [S5][S6][S7] |
| Lucid | Triton2 line scan TRT04KG (4k 65 kHz / 2k 130 kHz, 2.5GigE PoE, IP67); Triton TRI02KA 2k 60 kHz | IP67 line scan on M12 connectors | login for price | stock | Yes | [S13] |

Line-scan lighting: a line backlight (Ai BL168 class, 540,000 lux) under a transparent gap/roller, or a high-angle line light on a dark background roller; fabric inspection vendors (Uster EVS, Shelton WebSpector) were not researched in this pass (unknown, see §Open questions).

### F4. Smart cameras with on-board AI

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Cognex | In-Sight 3800 (IS3801 1.6 MP 125 fps; IS3803 3 MP 47 fps; IS3805 5 MP 32 fps; IS3808 8 MP), C-mount, integrated/external light | edge-learning AI + rule tools, trains from 5–10 images; In-Sight Vision Suite; EtherNet/IP, PROFINET, OPC UA | price not published ("get product pricing"); an aggregator claims USD 2,935–2,950 (unverified) | quote | Yes (Cognex 3D models via support site, login) | [S26][S39] |
| Cognex | In-Sight 2800 series | AI OCR / classification / presence; HDR; TCP/IP, PROFINET, EtherNet/IP, SLMP, OPC UA, FTP | not published; quote | quote | Yes (login) | [S27] |
| Keyence | IV3 series AI vision sensor (10 heads, install 50–3000 mm, FOV up to 2730 × 2044 mm) | AI presence/difference checking; CAD/CAE downloads on site | price via sales engineer only | same-day shipping (Keyence) | Yes (Keyence CAD, registration) | [S28] |
| Keyence | CV-X series vision system | PC-less multi-camera vision controller | price via sales only | — | Yes (registration) | [S28] |
| SICK | InspectorP62x V2D621P-2MDFCB5 (p/n 1130942) | 2D snapshot, Nova Inspector, Quality Inspection licence, HALCON/AppSpace, encoder input ≤ 300 Hz, M12 Ethernet + 17-pin I/O | not published; quote | — | Yes (sick.com/1130942 CAD models) | [S29] |
| SICK | Inspector83x V2D8305P-1CCICXAF1SXXXX (p/n 1142976) | 5 MP, built-in illumination, Intelligent Inspection licence incl. deep learning (datasheet 2026-10-01) | not published; quote | — | Yes (sick.com) | [S29] |
| Zebra | VS70-CM20S5-0C00W (2.3 MP C-mount smart camera) | sensor toolset, dual Ethernet (1 PoE), industrial protocols | USD 3,833.43 (Barcodesinc, 2026-10, reseller; backorder) | backorder | Yes (Zebra support) | [S37] |
| Zebra (Matrox) | Iris GTX + Aurora Design Assistant | deep-learning inference on camera | not published; quote | — | Yes | [S37] |
| Banner | VE202G1A (2 MP) / VE205G1A (5 MP) smart cameras | Vision Manager (free), IP67, 12–30 V DC; models VE200/201/202/205 | USD 4,571.03 (VE202G1A, seekcomp distributor, 2026-10); USD 6,418.96 (VE205G1A, RS US, backorder) | backorder (RS) | Yes (Banner downloads) | [S38] |

Verdict: smart cameras cost 3–8× a GenICam camera of the same resolution (Banner 5 MP USD 6.4k vs IDS 5 MP USD 530) and lock inference into a vendor runtime, which conflicts with M11 (perception on the cell's edge PC) and M08 skill runtime. They are worth it only for isolated PLC-native gates (label OCR / "garment present" at ST07) where the integrator wants a check independent of the AI stack.

### F5. 3D sensors and suitability for matte white knit

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Zivid | Zivid 2+ MR60 (robot-mount, high resolution) | structured light 5 MP 2448 × 2048 colour; focus 600 mm; working 300–1100 mm; FOV 570 × 460 mm at 600 mm; spatial res 0.24 mm; **point precision 80 µm**; trueness 99.8 %; 25–1500 ms; 169 × 124 × 56 mm, 1 kg, IP65, 0–45 °C | price not published; request quote (est. USD 9,000–14,000, basis: industrial structured-light class; market report average for all 3D area cameras USD 4,223/unit in 2025 [S53]) | quote (Stemmer: "request prices") | Yes (Zivid downloads: STEP; Zivid ROS/URDF via zivid-ros) | [S41][S42][S53] |
| Zivid | Zivid 2+ MR130 (stationary) | focus 1300 mm, working 800–2700 mm, FOV 790 × 650 mm at 1300 mm, 0.32 mm spatial res, 210 µm precision, 50–150 ms captures | quote (est. same class) | quote | Yes | [S41] |
| Zivid | Zivid 2+ LR110 (SKU ZVD2P-LR110) | focus 1100 mm, 700–1700 mm, FOV 1090 × 850 mm at 1100 mm, 0.44 mm, 260 µm precision; datasheet rev 1.3 (7/2025) | quote | quote | Yes | [S41] |
| Zivid | Zivid 3 XL250 | focus 2500 mm; FOV 1750 × 1750 mm at 2500 mm; 0.62 mm; 250 µm; 336 × 133 × 70 mm, 2.7 kg; 8 MP 2D | quote | quote | Yes | [S41] |
| Zivid | accessories: stationary mount EUR 350; on-arm mount EUR 400; calibration board 7 × 8 30 mm EUR 370; Ethernet data cable from EUR 160; protective housing EUR 480; PSU EUR 150 | — | EUR list, shop.zivid.com, 2026-10 | stock | — | [S42] |
| Photoneo | MotionCam-3D M+ (Blue/Red) | parallel structured light; range 630–1574 mm; camera mode 0.9 Mpx @ 20 fps, accuracy < 0.6 mm, noise < 0.1 mm; scanner mode 2 Mpx (1680 × 1200), accuracy < 0.3 mm, noise < 0.05 mm, point size 0.52 mm @ 900 mm; 10 ms acquisition; on-board Pascal GPU; S 366–558 mm, M 497–939 mm, L 778–3034 mm, L+ 1300–3780 mm | not published; quote | quote | Yes (Photoneo downloads: STEP) | [S43] |
| Photoneo | PhoXi 3D Scanner S/M/L/XL (Gen3) | sequential structured light for static scenes | not published; quote | quote | Yes | [S43] |
| Mech-Mind | Mech-Eye PRO S-GL / PRO M-GL | Z repeatability 0.05 mm @ 1.0 m (PRO S), 0.2 mm @ 2.0 m (PRO M); VDI/VDE 0.1 / 0.2 mm; GigE; docs v2.6.0 | not published; quote | quote | Yes (Mech-Mind download centre) | [S44] |
| Mech-Mind | Mech-Eye LSR L | FOV 1200 × 1000 mm @ 1.2 m to 3000 × 2400 @ 3 m; 2048 × 1536 depth, 4000 × 3000 RGB; Z repeat 0.5 mm @ 3 m; 0.5–0.9 s; 638 nm Class 2 laser; 2.9 kg; IP65; 24 V 3.75 A | not published; quote | quote | Yes | [S44] |
| Basler | blaze-102 ToF (order no. 108711) | Sony IMX556 640 × 480, 67° × 51°, 0.3–10 m, accuracy ±5 mm, temporal noise < 0.8 mm, 30 fps, latency < 85 ms, IP67, 690 g, 24 V ≤ 38 W peak, GigE/GenTL, PTP | net list price shown only after login (not captured); est. USD 1,800–2,500 (est., ToF class) | shop | Yes (Basler docs; ace 2-to-blaze bracket) | [S45] |
| Lucid | Helios2+ ToF | 640 × 480 ToF, GigE | USD 2,692.50 (Edmund, 2026-10, reseller) | stock | Yes | [S46] |
| RealSense (ex-Intel; independent since 2025-07-11, USD 50 M Series A) | D455 / D455f / D456 | stereo, 87° × 58°, 0.6–6 m, < 2 % at 4 m, 1280 × 720 @ 90 fps, global shutter, IMU, USB-C | USD 419 (D455), 439 (D455f), 469 (D456); store.realsenseai.com 2026-10, list; **tariff surcharge added 2026-02-03** | in stock | Yes (RealSense downloads, STEP; realsense-ros URDF) | [S47][S48] |
| RealSense | D555 (PoE, Vision SoC V5, on-camera AI) | long-range stereo over single PoE cable; NVIDIA Holoscan/Jetson Thor integration announced Oct 2025 | USD 499 list, 2026-10 | in stock | Yes | [S47][S48] |
| RealSense | D405 (close range 7–50 cm) / D435f / D436 / D421 module | D405 for eye-in-hand close-up; D421 bare module | USD 272 (D405), 334 (D435f), 354 (D436); D421 10-pack USD 800 | in stock | Yes | [S47][S49] |
| Orbbec | Gemini 335 (G40155-170) | active/passive stereo, 0.26–3 m optimal, 1280 × 800 @ 30 fps, ≤ 1.5 % RMSE at 2 m, 90° × 65°, USB-C, 97 g, trigger + multi-device sync, Orbbec SDK (ROS 2 wrapper) | USD 264, store.orbbec.com 2026-10, list, in stock | in stock | Yes (Orbbec downloads) | [S50] |
| Orbbec | Gemini 336L (G40155-180) | IR-pass filter, IP65, 0.25–6 m, ≤ 0.8 % at 2 m, 1280 × 800 @ 30, 135 g | USD 379, 2026-10, list | in stock | Yes | [S50] |
| Ensenso (IDS/Optonic) | C57 (replaced by **C67**), B57, N31/N36, X36, XR36 | stereo + pattern projector, industrial | not published; quote | quote | Yes (IDS/Ensenso downloads) | [S51] |

Suitability for matte white knit (reasoning from the datasheets; no vendor publishes a textile application note, which is an open question):
- Structured light (Zivid, Photoneo, Mech-Mind) is designed for texture-less surfaces ("no texture on surfaces required") and performs best on matte, high-albedo Lambertian material: white cotton knit is close to the ideal target for pattern projection, far easier than the shiny/transparent parts these vendors benchmark [S52]. The hard part is geometry, not reflectance: a single ply is 0.5–1.2 mm thick, so **layer counting from Z needs a point precision well under 0.3 mm**: Zivid 2+ MR60 (80 µm at 600 mm) and Photoneo M+ scanner mode (< 0.05 mm noise) qualify; Zivid LR110/MR130 (210–260 µm) and Mech-Eye LSR L (0.5 mm) do not for ply counting but do for pile/fold/drape state.
- Consumer-class stereo (RealSense, Orbbec: 0.8–2 % of distance ≈ 4–10 mm at 0.5 m) cannot resolve ply height or a knit edge; it is adequate for gross cloth state (crumpled vs flat, bin empty, gripper clearance) and as eye-in-hand coarse localisation. Zivid's own comparison pages show the RealSense/structured-light gap, but they are vendor marketing [S52].
- ToF (blaze-102 ±5 mm, Helios2) is unsuitable for anything but presence/volume.
- Recommendation: 2D silhouette imaging with backlight does the precision work (edges to 0.1–0.2 mm); 3D is only needed where the cloth is not flat (ST03 pick point, ST04 placement, ST06 collar loop). Validate on the actual knit with sample captures before committing to a USD 10k-class camera.

### F6. Lighting, backlights, strobe controllers, enclosures

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Smart Vision Lights | SOBL series backlights (e.g. SOBL-150x150-470 blue) | built-in driver, PNP/NPN strobe or continuous, 0–10 V intensity, 30 mm thick; active sizes 150 × 50 up to 450 × 450, 600 × 150, 1200 × 150 (IVS also lists 600 × 600) | USD 758 (SOBL-150x150-470, Machine Vision Direct, 2026-10, reseller) | built-to-order, 0–3 working days (MVD) | Yes (SVL product page: STEP) | [S54] |
| Advanced Illumination | BL2-XXYY high-intensity back-lit backlights (replaces BL, discontinued 2024-04-13); BL-S100150 EuroBrite; BL168 line-scan backlight | BL2 86,000 lux, 470/530/625/850/white; BL-S100150 65,500 lux in stock; BL168 540,000 lux for line scan; custom sizes at standard lead time | prices not published (quote); est. USD 1,500–3,500 for 600 × 600 class (est.) | 2 weeks (BL2, BL168); in stock (BL-S) | Yes (Ai product pages: STEP) | [S55] |
| Effilux (Effilux/Effilux-Edmund) | EFFI-BL large-format backlight; EFFI-BL-IP69K; EFFI-SBL compact; EFFI-MBL IR | 24 V DC via M12 5-pin / power 4-pin; large formats; metrology/deflectometry masks | not published; quote | quote | Yes (Effilux configurator) | [S56] |
| CCS Inc. | TH2 series high-output flat backlights; PD4-A/PD4 digital controllers | note: CCS discontinued LFV3 (34/40 mm), LN series and PD2 controllers in Sept 2026 | price via engineers/reseller; not published | quote | Yes (CCS CAD downloads) | [S57] |
| Gardasoft | RT220-20 (2-channel, 24–48 V DC) LED strobe controller | pulse/strobe with SafePower; RT family; also RT420 4-ch, PP420 (PoE), TR-HT 150 W/channel (50 A pulsed), CC320 encoder-based timing controller, TR-CL180 liquid-lens controller | USD 418 (Radwell new, 2026-10); USD 300 Radwell-warranty; USD 400 used (Next Day Automation) | stock (Radwell) | Yes (Gardasoft downloads) | [S58] |
| Dark-field / bar lights (SVL LXE series, Ai LL series, CCS LDL2) | for seam relief at ST07 | not researched in this pass | unknown; est. USD 300–900 per bar | — | Yes | [S54][S55] |

Lighting plan notes: the cutting bed (bristle/perforated vacuum conveyor) cannot be backlit, so ST02 silhouette contrast comes from a **dark bed surface under diffuse white top light** (or 850 nm NIR with a bandpass filter to reject ambient); backlights are used where the cloth lies on a translucent stage (ST03 buffer, ST04 placement tables, ST06 collar support, ST07 final stage) and as a small insert in the throat-plate area at ST05. All strobed lights run from a Gardasoft RT controller triggered by the camera's exposure-active output; continuous lights use the SVL built-in driver on 24 V. Enclosures: IP67 cameras (Lucid Triton, Basler ace 2 with IP67 housing) or IP54 polycarbonate camera housings with an air purge for lint (the sewing area generates lint that settles on optics within hours: schedule lens wipes and specify sealed housings).
