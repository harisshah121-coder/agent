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

### F7. Edge compute, industrial PCs, training GPUs, NICs

**NVIDIA raised all Jetson prices in July 2026** (memory shortage; quietly, via the Jetson FAQ) [S59]; the NVIDIA marketplace confirms the new prices and shows the AGX Orin developer kit out of stock (2026-10) [S60]. New lower-cost Blackwell modules Thor T3000/T2000 were announced 2026-07-16 and are emulated on the AGX Thor dev kit until they ship [S62].

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| NVIDIA | Jetson AGX Thor Developer Kit | T5000: 2070 FP4 TFLOPS (sparse), 2560-core Blackwell, 14-core Neoverse V3AE, 128 GB LPDDR5X 273 GB/s, 40–130 W, 1 TB NVMe, up to 20 HSB cameras, 243 × 112 × 57 mm | USD 5,499 (was 3,499), NVIDIA marketplace 2026-10, list | in stock (marketplace) | Yes (NVIDIA developer downloads: STEP of module/dev kit) | [S59][S60][S61] |
| NVIDIA | Jetson T5000 / T4000 modules (1KU+) | 2070 / 1200 TFLOPS; 128 / 64 GB | USD 4,999 / 2,999 (1KU+), from 2,999 / 1,999 | — | Yes | [S59][S61] |
| NVIDIA | Jetson AGX Orin Developer Kit (64 GB) | 275 TOPS, 2048 CUDA, 12-core A78AE, 64 GB LPDDR5 204.8 GB/s, 15–60 W, 110 × 110 × 72 mm | USD 3,499 (was 1,999), NVIDIA marketplace, **out of stock**; EUR 3,470.25 ex VAT (Aetherix, 3 in stock, same-day) | 0–weeks (reseller) | Yes | [S59][S60][S63] |
| NVIDIA | Jetson AGX Orin 64 GB / Industrial / 32 GB modules | 275 / 248 / 200 TOPS | USD 2,999 / 3,199 / 1,799 (1KU+), from 1,599 / 2,149 / 899 | — | Yes | [S59] |
| NVIDIA | Jetson Orin NX 16 GB / 8 GB modules | 157 / 117 TOPS (Super), 10–25 W, 70 × 45 mm | USD 999 / 649 (1KU+), from 599 / 399; Waveshare Orin NX module USD 911–1,461 (reseller) | stock | Yes | [S59][S63] |
| NVIDIA | Jetson Orin Nano Super Developer Kit | 67 TOPS, 8 GB, 7–25 W | USD 399 (was 249), marketplace list | in stock | Yes | [S59][S60][S61] |
| Neousys | Nuvo-9160GC | 13th/14th-gen Core (LGA1700), 150 W RTX GPU cassette (RTX 2000 Ada / RTX 4000 SFF Ada), DDR5 up to 64 GB (page says 128 GB), 6 × GigE (4 × PoE+ optional, 100 W budget), 8 × USB3, 8–48 V DC, –25…60 °C, 240 × 225 × 110 mm, 3.89 kg | price not published; quote (Elmark) ; est. USD 3,500–5,000 barebone + GPU (est.) | quote | Yes (Neousys: STEP on request/download) | [S64] |
| Neousys | Nuvo-10108GC (350 W GPU) / Nuvo-10109GC (600 W Blackwell) / Nuvo-11160GC (Core Ultra 200S) | larger GPU classes | quote | quote | Yes | [S64] |
| Advantech | MIC-770 V3 (modular fanless IPC, 12/13/14-gen Core, –20…60 °C, 9–36 V DC) | GPU via i-Module expansion; 3D model downloadable from product page | from EUR 1,024 net barebone (Elmark, 2026-10, reseller) | stock | Yes (Advantech "Download 3D Model") | [S65] |
| Vecow | ECX/RCX GPU IPCs | not captured in this pass | unknown | — | — | — |
| Beckhoff | C6040-0090 ultra-compact IPC (Intel Core 3/5/7/9 Series 2 up to 12 cores; 132 × 202 × 76 mm; TwinCAT 3 platform level 50–81); C6030 smaller sibling | PLC + HMI + light vision in one box; no discrete GPU | price not published; quote via Beckhoff sales | quote | Yes (Beckhoff product page STEP) | [S66] |
| NVIDIA | RTX PRO 6000 Blackwell Workstation Edition (training) | 96 GB GDDR7 ECC, 24,064 CUDA, 4000 FP4 TOPS, 600 W (Max-Q 300 W) | est. MSRP USD 10,999 (PNY at Newegg/B&H, June 2026); street Oct 2026 USD 21.8–23.5k (GPU Poet, eBay lowest-3 average; up 25–48 %) | volatile | Yes (Advantech SKY-QUAD page: 3D model) | [S67] |
| NVIDIA / Advantech | RTX 4000 SFF Ada 20 GB (70 W, single slot) for the edge PC; RTX PRO 4000 SFF Blackwell successor exists | fits Nuvo-9160GC cassette | not captured; est. USD 1,300–1,800 (est.) | stock | Yes | [S67] |
| NICs | 10GBASE-T (Intel X710-T2L class) for the 24 MP/10GigE camera; 4-port PoE+ GigE Vision card (Neousys PCIe-PoE354at class) for 1GigE cameras | not researched in this pass | unknown; est. USD 300–600 each (est.) | — | — | — |

Compute sizing (arithmetic): 10 cameras at the station plan below produce ≈ 450 MB/s peak (one 24 MP at 5 fps = 120 MB/s; four 12 MP tiles at 2 fps = 100 MB/s; three 1.6–2.3 MP trackers at 250 fps ROI ≈ 150 MB/s; 5 MP stations ≈ 60 MB/s). A single Nuvo-9160GC-class PC with an RTX 4000 SFF Ada handles this plus 10–20 small CNN/segmentation inferences per second; the 200 fps edge-tracking loops should run on the same PC (USB3/2.5GigE, < 10 ms) or on a Jetson Orin NX at each sewing head if cabling forces it. Basler's pylon notes require dual-channel DDR4-3600+ hosts for multi-camera 5GigE/1GigE streaming [S40].

### F8. Other sensors (encoders, photoelectric, laser distance, edge, double-sheet, thread, vacuum, tension, climate)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Kübler | Sendix 5020 incremental (Ø50, ≤ 15 mm hollow shaft) | up to 5000 ppr, push-pull/TTL/open collector, IP67, –40…85 °C, 12,000 rpm | price not published; quote (est. USD 250–400) | stock | Yes: STEP ZIP + ePlan on product page | [S68] |
| Heidenhain | ECN 1313 (768295-03) absolute EnDat01, 8192 pos/rev, 2048 lines 1 Vpp; ERN 1387 (749144-05) incremental 2048 lines | motor-feedback class | USD 521 (768295-03, mtechsupply, backorder); USD 1,042 (768295-06) | backorder | Yes (Heidenhain "CAD Download") | [S69] |
| Renishaw | RESOLUTE absolute ring/readhead; TONiC incremental (RTLC20 scale, up to 10 m interface) | sub-µm, for gantry axes if needed | USD 1,110–1,652 (RESOLUTE variants, e-motionsupply, 2026-10) | stock | Yes (Renishaw downloads) | [S70] |
| Posital | IXARC incremental/absolute (programmable PPR) | lower-cost programmable encoders | price not captured (quote) | stock | Yes (Posital configurator STEP) | [S70] |
| SICK | WTB4S-3P2261 (p/n 1042041) BGS photoelectric 10–180 mm; WTB4S-3P2232 (p/n 1054282) 10–120 mm | PinPoint red, M8 4-pin, 12 × 42 × 17 mm | GBP 178.19 inc VAT (Drive Outlet, independent reseller, 2026-10) ≈ USD 190 | stock | Yes (sick.com CAD) | [S79] |
| Banner | Q4XTBLAF300-Q8 (p/n 94118) laser BGS 25–300 mm, IP69K; Q4XTILAF300-Q8 analog | ±0.5 mm (25–50 mm) / ±1 % repeatability | USD 433 (Powermatic) / 476.34 (RS US, 133 in stock); analog USD 507.50 (Lesman) | stock | Yes (Banner CAD) | [S79] |
| Keyence | IL-065 laser displacement head | 55–105 mm range, 2 µm repeatability, 0.33–5 ms sampling, Class 2, IP67, CAD/3D-PDF online | price via Keyence only (est. USD 600–900 head + amplifier) | same-day | Yes | [S71] |
| Micro-Epsilon | optoNCDT 1220 / 1320 / 1420 laser triangulation | list from EUR 470, up to 8 kHz, repeatability 0.5 µm, integrated controller | EUR 470+ list (Micro-Epsilon, 2026-10) | stock | Yes (ME downloads STEP) | [S72] |
| Erhardt+Leimer | FR 52 infrared edge sensor (retroreflection) | ±10 mm, 0.02 mm resolution, ±0.1 mm linearity, 200 Hz, 850 nm, IP54, 105 × 50 × 40 mm; explicitly shown "for mesh fabric acquisition"; FR 46 PoE (±2.5 mm, 0.01 mm) | not published; quote (est. USD 800–1,500) | quote | Yes (E+L downloads) | [S73] |
| Erhardt+Leimer | FE 46 infrared wide-band sensor (textiles) | web edge/centre/width up to 3800 mm operating width, ±1 mm resolution, CAN, 15–30 kg; FR 60 broadband for woven/knitted up to 70 % transparency | quote | quote | Yes | [S73] |
| Erhardt+Leimer | FX 46 / FX 42 / FX 52 ultrasonic edge sensors | ±3 / ±3 / ±10 mm; **for sound-impervious webs (paper, plastic, metal foil) — not porous knit** | quote | quote | Yes | [S73] |
| Maxcess / Fife | SE-37A / SE-44 ultrasonic; DSE-17 digital wideband IR (4 edges); SE-38 first-edge (varying opacity "impossible with air or ultrasound"); SE-42 IR; H3662 line-scan IR | textile-capable options are the IR types | not published; quote | quote | Yes (Maxcess downloads) | [S74] |
| Pepperl+Fuchs | UDC-18GM-400-3E3 ultrasonic double-sheet sensor | 20–60 mm gap (opt. 45 mm), 395 kHz, 10 g/m² to > 2000 g/m², "preferably papers", 3 PNP outputs, no teach-in | USD 1,408 "your price" / 2,011 retail (quicktimeonline, reseller, out of stock); 3 distributors on Octopart | stock varies | Yes (P+F CAD) | [S75] |
| SICK | UD18-2 (UD18-22CC222 PNP p/n 6058912; NPN 6058913), 2.5 ms; UM18-20014 (p/n 6037880) 37–43 mm, 400 kHz | double layer/splice detection for paper, cardboard, metal, plastic; 4 teachable sensitivity levels | not published; quote (est. USD 700–1,200) | stock | Yes (sick.com) | [S76] |
| Eltex | Thread sensor 15965 (up to 6 threads, piezoelectric, M12; replaces 15961/15962); Eltex Tension Monitor 14630 (RS422, miniature head) | detects no-movement and continuous-movement faults; insensitive to dust/humidity | not published; quote (est. USD 400–900) | quote | drawings in leaflet | [S77] |
| Brother | KE430H-TBK thread breakage sensor (machine option) | OEM thread-break option on bar-tack/sewing machines | quote | — | — | [S77] |
| SMC | ZSE30AF-01-E / -E-P digital vacuum switch | 2-colour display, NPN/PNP, 2.5 ms response | price not captured on smcpneumatics (quote; est. USD 80–130) | stock | Yes (SMC CAD) | [S78] |
| Montalvo | strain-gauge tension load cells / tension sensing roller | web tension at ST01 unwind | not published; quote (est. USD 800–1,500 per pair) | quote | Yes (Montalvo) | [S78] |
| Temperature/humidity transmitter (any industrial RH/T, e.g. ifm, Sensirion-based) | material-profile logging (knit shrink/stretch varies with RH) | not researched | unknown; est. USD 100–300 | — | — | — |

Single-ply verification: no vendor confirms ultrasonic double-sheet sensing on air-permeable knit (their stated targets are paper, film, foil, cardboard, metal). Expect weak and porosity-dependent attenuation; the dependable methods are (a) a laser-displacement thickness check against a reference plate at the pick point (IL-065 / optoNCDT, 2 µm vs 0.5–1.2 mm ply), (b) camera top-layer segmentation (see F10), and (c) weight. Treat the ultrasonic option as a bench test, not a design assumption.

### F9. Software pointers (GenICam/GenTL, drivers, ROS 2, calibration)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| Basler pylon Software Suite | 26.08 (2026-08-20) | proprietary, free | mature; Windows/Linux x86/ARM; GenTL ≤ 1.4 limited | first choice SDK for Basler cameras; pypylon for Python; official pylon-ros-camera (ROS 1/2) and gst-plugin-pylon on GitHub | [S40][S80] |
| Aravis | main branch, 2,914 commits (2026-10) | LGPL-2.1 | mature, active (Discourse forum, releases on GitHub) | vendor-neutral GigE Vision + USB3 Vision on Linux; Basler documents Aravis samples for blaze ToF; use as the M11 fallback for any GenICam camera | [S80] |
| Harvesters (genicam/harvesters) | current GitHub | Apache-2.0 (verify on repo) | maintained by GenICam community | Python GenTL consumer over any vendor .cti producer (pylon, Spinnaker, Arena) | [S80] |
| Teledyne Spinnaker SDK | 4.4.0.248 (docs 2026-08-25) | proprietary, free | mature; GenTL 1.5 producer (.cti) | required for FLIR Blackfly S; ROS 2 via spinnaker_camera_driver | [S81] |
| ros-drivers/flir_camera_driver (spinnaker_camera_driver, synchronized driver) | ros2-release, updated 2026-05-08 | BSD | MAINTAINED, released for humble/jazzy/kilted/rolling | multi-camera hardware-synchronised capture in ROS 2 | [S81] |
| Lucid Arena SDK (+ JupyterLab) ; Triton Smart open-source AI toolkit | 2026-08 | proprietary / open toolkit | mature | Lucid cameras; GigE Vision 3.0 RDMA for 10/25GigE | [S14] |
| Orbbec SDK / OrbbecSDK_ROS2; realsense-ros; zivid-ros; Photoneo ROS 2 | current | Apache/BSD/MIT (vendor repos) | not verified in this pass | needed for the 3D options; verify ROS 2 distro support before purchase | — |
| Calib.io targets | ChArUco 200 × 150 USD 134; sizes to 800 × 600 × 6 mm (fine 30 mm / coarse 60 mm checkers); checkerboard from EUR 103; Kalibr AprilGrid from EUR 176 (made to order); ceramic small targets | commercial | shipping with US duties prepaid | 800 × 600 ChArUco boards (3–4) as a network across the 1.5 m bed; Calibrator software supports multi-target networks and N-camera bundle adjustment (price not captured) | [S82] |
| moveit_calibration (hand-eye) | ROS 1 Melodic/Noetic; 120 commits | BSD-3 | stable but ROS 1 | — | [S83] |
| moveit2_calibration (AndrejOrsula ros2_port) | 145 commits, 45 stars | BSD-3 | community port, not released | ROS 2 hand-eye GUI; alternative: OpenCV calibrateHandEye in a short script, or the Zivid hand-eye API (factory-calibrated point clouds, fewer poses) | [S83][S41] |

### F10. Research pointers (2025–2026, alphaXiv)

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| Robotic Fabric Alignment System for Sewing Using Global-Local Weighted ICP | 2026-08-10 (arXiv 2608.09528) | paper | preprint | top/bottom fabric pose estimation before sewing: directly ST04/ST05 alignment | [S84] |
| Automated Straight-line Sewing of Stretchable Fabrics with Different Lengths | 2026-07-31 (2607.29464) | paper | preprint | differential-length seam control on knits (ST05/ST06 neckband) | [S84] |
| Seam-to-Graph Reconstruction for Garment Configuration Alignment (HKU) | 2026-06-13 (2606.15171) | paper | preprint | seam-based garment state from partial views (ST06/ST07 inspection) | [S84] |
| Precise Top-Layer Fabric Segmentation for Fabric Destacking | 2026-08-11 (2608.10648) | paper | preprint | camera-based single-ply/top-layer verification (ST03) | [S84] |
| Synthetic Data Generation and Vision-based Wrinkle and Keypoint Detection for Bimanual Cloth Manipulation | 2026-06-04 (2606.06292) | paper (code likely) | 12 votes | synthetic training data for M11 cloth-state nets | [S84] |
| AI Visual Inspection for Garment Production (CityU HK / Intel) | 2026-08-16 (2608.21426) | paper | preprint | ST07 defect inspection architecture | [S84] |
| Robotic Automation in Apparel Manufacturing (Siemens, Sewbo, Levi's) | 2025-02-28 (2503.00249) | paper | — | end-to-end robotic sewing cell lessons | [S84] |
| Deployment Case Study in Robotic Apparel Automation: Digital Twin, Interoperability | 2026-06-15 (2606.16078) | paper | — | M13 twin and workforce enablement | [S84] |
| Vision-Based 6-DoF Grasp Pose Estimation for Robot Cloth Unfolding (Ljubljana/JSI) | 2026-09-25 (2609.31452) | paper | 8 votes | ST03/ST04 grasp selection from depth | [S84] |

### F11. Per-station camera and sensor plan (FOV and resolution math per station)

| Station | Task | Camera (qty) | Lens | Light | Mount / WD | FOV and GSD | Interface → compute | Est. cost (USD, est.) |
|---|---|---|---|---|---|---|---|---|
| ST01 roll handling | web defects, holes, stains, skew, end-of-roll; edge guiding; tension | Linea Lite 4k mono (1) encoder-triggered from feed roller (Kübler 5020); E+L FR 52 IR edge sensor (1–2); Montalvo load-cell roller (1) | Kowa LM35XC / line-scan 35–50 mm (M42 adapter) | Ai BL168 line backlight under a glass gap, or dark roller + high-angle bar | 1.2 m above web | 1.6 m web / 4096 px = **0.39 mm/px** (8k: 0.2 mm/px) | GigE PoE → edge PC | 2,500 + 1,500 edge + 1,200 tension |
| ST02 cutting | cut-geometry check ±0.5 mm, piece ID, incomplete-cut recovery | 4 × 12 MP tiles (Basler a2A4096-… 5GigE/10GigE or Lucid TRT124S 2.5GigE) **or** 1 × 24 MP (a2A5328-49g10m) accepting 0.28 mm/px | Kowa LM25XC (tiles, WD 2.0 m, 0.8 m tile) / LM16XC (single, WD 1.65 m) | diffuse white top light bars, dark bed; strobed by Gardasoft RT220 | frame above bed, 1.65–2.0 m | 4 tiles: 0.8 m / 4096 = **0.20 mm/px**; single 24 MP: 1.5 m / 5328 = 0.28 mm/px | 2.5/5/10GigE → edge PC (X710 NIC) | 4 × 1,200 cams + 4 × 1,000 lenses + 2,500 light + 1,500 calibration targets ≈ 12,700 |
| ST03 extraction/buffer | top-layer segmentation, grasp point, layer count | 5 MP GigE (Triton TRI050S or IDS GV-5880) (1); Keyence IL-065 thickness check at pick point (1); optional Zivid 2+ MR60 (1) | LM12JC | SOBL 450 × 450 backlight under translucent staging table | 0.6 m | 0.6 × 0.5 m / 2448 = **0.24 mm/px** | GigE PoE | 600 + 150 + 900 + 1,200 (+ 10,000 if Zivid) |
| ST04 manipulation | ply pose before placement, edge alignment at sewing stations, gripper state | fixed 5 MP per placement stage (2) + eye-in-hand Orbbec Gemini 335 or RealSense D405 (1) | LM12JC | SOBL 300 × 300 backlights in stages | 0.5 m | 0.5 × 0.4 m / 2448 = **0.20 mm/px** | GigE PoE + USB-C on arm | 2 × 600 + 264 + 2 × 900 |
| ST05 sewing heads (3 heads) | seam/edge tracking at the needle, stitch presence, thread break | a2A1920-160umPRO USB3 (or Triton2 TRT016S 2.5GigE) per head (3) at ≥ 200 fps ROI; Eltex 15965 thread sensor per head (3) | Kowa LM25JC / 25 mm at WD 150 mm | small backlight insert or dark-field ring, strobed | 150 mm | 60 × 40 mm / 1920 = **0.03 mm/px**; 1920 × 200 ROI > 500 fps | USB3 ≤ 3 m to edge PC (or Orin NX per head) | 3 × 620 + 3 × 143 + 3 × 600 thread + 3 × 400 light |
| ST06 collar/neckband | loop present, twist, captured layer, symmetry | 5 MP GigE (1) over split support | LM12JC | SOBL 150 × 150 backlight in the split support | 0.4 m | 0.35 × 0.3 m / 2448 = 0.14 mm/px | GigE PoE | 600 + 143 + 758 |
| ST07 finishing/inspection | dimensions, seam path, visible defects, label OCR | 20–24 MP (Triton TRI245S / a2A5328) (1) + low-angle dark-field bars; optional In-Sight 2800 for PLC-native label gate | LM16XC | SOBL 600 × 600 (or BL2) backlit stage + dark-field bars | 1.3 m | 1.0 × 0.8 m / 5320 = **0.19 mm/px** | 2.5/10GigE | 2,800 + 1,055 + 2,500 light |
| ST09/ST10 compute | all inference, logging, calibration | Neousys Nuvo-9160GC + RTX 4000 SFF Ada (1); optional Jetson Orin NX 16 GB per sewing head (3); training: RTX PRO 6000 workstation or cloud | — | — | cabinet | — | X710-T2L 10GbE + 4-port PoE+ GigE card; NVMe 2–4 TB for image logs | 5,500 (+ 3 × 1,300 Orin NX kits) (+ 11,000–23,000 training GPU) |

Totals (est., list/reseller prices above; excludes PLC/safety/drives): **reference build ≈ USD 38–48k** with one Zivid 2+ and a tiled bed; **minimum build ≈ USD 18–22k** (single 24 MP bed camera at 0.28 mm/px, consumer 3D only, no Jetsons, training in the cloud); training workstation extra. Camera count: 9–13.
