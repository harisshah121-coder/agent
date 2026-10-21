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
