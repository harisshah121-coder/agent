# R07 · Frame, pneumatics, vacuum, cabling, fasteners, consumables (ST00) — "every nail and wire"

Research agent R07 · written 2026-10-21 · Roll-to-Garment project · station ST00 (with cross-references to ST01–ST10 where the item is shared infrastructure).

> Status: in progress — sections are appended incrementally; the Summary is written last.

## Findings

Conventions used in every table below: prices are the figure shown on the cited page on the date given (2026-10-21 unless stated), with the basis in brackets: **list** = manufacturer web price, **reseller** = distributor web price (reseller named), **quote** = not published, **est.** = my order-of-magnitude estimate with the basis stated. "CAD" says whether a STEP/native model is downloadable and where. Items marked **unverified** could not be confirmed from a primary or reseller page within three attempts.

Scope note: the white paper budgets "Frame, guarding and base utilities" at $6,000 / $9,000 / $15,000 (optimized / reference / conservative) and "Single-ply cutting and hold-down" at $8,000 / $14,000 / $25,000 (white paper lines 1961–1971). The vacuum blower is costed against the cutting line, the compressor and air preparation against base utilities. The starter BOMs at the end of each sub-section are sized for one cell of roughly 6 m × 3 m guarded footprint (my assumption: ST01 roll stand + ST02 1.8 m wide cutter bed + ST03/04 gantry + two ST05/06 sewing stations + ST07 output, laid out in an L; the white paper assigns no footprint, line 558).

### 1. Frame: aluminium extrusion systems

The five candidate systems differ mainly in (a) slot size and series (10 mm slot / 45 mm pitch for Rexroth and Vention, 8 mm slot / 40 mm pitch for item and Misumi 8-series, 0.32 in slot for 80/20 15-series), (b) whether a free native CAD configurator exists, and (c) how price is exposed. Only Vention, Misumi and 80/20 publish prices online; Rexroth and item price on configuration or login.

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? (format, where) | Source URL |
|---|---|---|---|---|---|---|
| Vention | ST-EXT-002-2025 (45×90 mm, 2025 mm) | 6005-T5, dark-blue anodized, Ix 1,111,757 mm⁴ / Iy 287,967 mm⁴, 1229 mm², 6.72 kg; cut in 45 mm increments | USD 165.31 each (2026-10-21, list) | "Ships next day" | Yes: 2D + 3D model download on part page; full assembly export from MachineBuilder (browser CAD) | https://vention.com/parts/45x90mm-2025mm-aluminum-extrusion-1680 |
| Vention | ST-EXT-002-0990 / -0900 / -0720 / -0630 / -0450 (45×90) | same section, 990 / 900 / 720 / 630 / 450 mm | USD 93.93 / 75.83 / 61.53 / 54.38 / 45.37 (2026-10-21, list) → ≈ USD 80–100 per metre | next day | Yes (as above) | https://vention.com/parts/45x90mm-990mm-aluminum-extrusion-45 ; https://vention.io/parts/45x90mm-630mm-aluminum-extrusion-162 |
| Vention | ST-EXT-002-2250 / -3330 | 2250 / 3330 mm | USD 207.57 / 269.11 (2026-10-21, list) | next day | Yes | https://vention.com/parts/45x90mm-2250mm-aluminum-extrusion-1684 ; https://vention.io/parts/45x90mm-3330mm-aluminum-extrusion-557 |
| Vention | ST-EXT-001 (45×45) and ST-EXT-003 (90×90) | same family; per-length prices not captured in this pass | price not captured; request from parts library (list pricing is public) | next day | Yes | https://vention.com/software/machine-builder |
| Bosch Rexroth | Strut profile 45×45 3842990520 / 45×45L 3842992953 / 3842992401 | 10 mm slot, 45 mm modular dimension, anodized; "Price dependent on configuration" in the Rexroth store | price not published online; request quote (est. USD 35–60 per metre for 45×45 based on Vention 45×90 at ≈ USD 90/m and 80/20 1515 at USD 0.98/in ≈ USD 38.6/m) | quote | Yes: FRAMEpro plug-in for Inventor/SolidWorks (free, >1,500 parts) and CAD files page | https://store.boschrexroth.com/en/at/p/strut-profile-3842990520 ; https://www.boschrexroth.com/en/us/c/framepro-cad-plug-in ; https://www.boschrexroth.com/en/us/downloads/cad-files |
| Bosch Rexroth | T-nut 10 M6 3842530285 (and M8 3842530287) | steel galvanized, 10 mm slot, ESD; pack of 100 | USD 0.78 each list (Rexroth US); USD 78.00 / 100-pack (BuyRexroth, 2026-10); USD 0.77 each (Airline Hydraulics); GBP 8.97 / bag of 10 (RS UK) | in stock (2,832 at BuyRexroth) | Yes: "Download 3D CAD" on BuyRexroth / Rexroth page | https://buyrexroth.com/product/3842530285 ; https://www.boschrexroth.com/en/us/p/t-nut-3842530287 ; https://uk.rs-online.com/web/p/connecting-components/3900278 ; https://www.airlinehyd.com/product/BRL-MT-3842530285/1664515 |
| Bosch Rexroth | Gusset / bracket 45×45 set 3842523561 | die-cast aluminium bracket with centering lugs, 2× T-bolt M8×25 + 2× flange nut M8 | USD 7.52 list (Rexroth US page) | stock | Yes: 3D CAD download | https://www.boschrexroth.com/en/us/p/gusset-3842523561 ; https://buyrexroth.com/product/3842523561 |
| item Industrietechnik | Profile 8 40×40 natural 0.0.026.03 (standard), 0.0.026.33 (light), E variants | 8 mm slot, Line 8, anodized; cut to length in configurator | price shown only after login/configuration; request quote (est. EUR 25–40 per metre based on comparable 40×40 8-slot profiles) | configurable, cut lengths | Yes: "Get CAD Data and Downloads" on every part page (item Engineeringtool) | https://www.item24.com/en-us/profile-8-40x40-natural-2603 ; https://www.item24.com/en-fr/profile-8-40x40-light-natural-2633 |
| 80/20 Inc | 1515 (1.5" × 1.5", four open slots) | 6105-T5, 15 series | USD 0.98 per inch (≈ USD 38.6/m) + USD 3.00 cut charge (2026-10, list) | stock | Yes: 80/20 site CAD downloads (STEP, DWG) per part | https://8020.net/1515.html |
| 80/20 Inc | 1515-Lite | lighter 15-series section | USD 0.83 per inch (list) | stock | Yes | https://8020.net/1515-lite.html |
| 80/20 Inc | 4302 (15-series 2-hole inside corner bracket), 40-4332 (40-series gusseted bracket) | external fastening, no machining | 4302 USD 5.20 (TECO reseller, 2026-10); 40-4332 USD 7.73, 4302-Black USD 8.05 (80/20 list) | same day | Yes | https://tecotechnology.com/products/80-20-15-series-ready-tube-2-hole-inside-corner-bracket-4302 ; https://8020.net/fasteningmethods/externalfasteners.html |
| TNUTZ (80/20-compatible) | EX-1515 | compatible with 80/20 1515-S, McMaster 60585K104 | USD 0.55 per inch class (list range USD 0.55–50.42 by length) | stock | drawings on page | https://www.tnutz.com/product/ex-1515/ |
| Misumi | HFS5-2020 / HFS6-3030 / HFS8-4040 (configurable length 50–4000 mm, 0.5 mm steps) | 6005A-T5 (A6N01SS-T5) clear anodize; 8-series = 8 mm slot | price shown on configuration (login not required for HFS5-2020 page, but price appears after length entry); HFC6-3030-S end cap USD 2.68 (1–9), USD 1.08 (20+) | 1–4 days | Yes: CAD download on part page; also PARTcommunity / 3Dfindit Misumi catalogue | https://us.misumi-ec.com/vona2/detail/110302683830/ ; https://misumi.partcommunity.com/3d-cad-models?countryIso=US&info=misumi%2Fmetric%2F38_al_extrusions_blackets%2F8%2Fhfs8_4040.prj&languageIso=en ; https://us.misumi-ec.com/vona2/detail/110300446540?HissuCode=HFC6-3030-S |
| Misumi | HNTT6-6 pre-assembly insertion nut, M6, 6-series | 1010 steel, trivalent chromate | USD 0.63 (1–99), 0.57 (100–499), 0.50 (1000+) (2026-10-21, list) | stock | Yes: CAD download on page | https://us.misumi-ec.com/vona2/detail/110302251050?HissuCode=HNTT6-6 |
| Kanya (UK/CH) | PVS profile system | >150 profiles, >1,500 accessories | price not published; request quote | quote | CAD via Kanya on request (unverified) | https://kanya-uk.co.uk/profile-system |
| Generic (Alibaba/Accio aggregator) | 4040 / 4545 T-slot, 6063-T5 | 8 or 10 mm slot, anodized | USD 2.35–11.58 per metre at 1–20 m MOQ (2026-10, marketplace; quality and straightness unverified) | weeks (import) | No vendor CAD | https://www.accio.com/plp/4040-extrusion |

**Reading of the table.** Vention is the only vendor that gives public list prices, next-day shipping, downloadable 3D per part *and* a browser CAD that exports the whole frame, which is exactly what the 3D-model guide needs. It is ≈ 2× the per-metre cost of 80/20 1515 and probably 1.5–2.5× Rexroth at quote. Rexroth's FRAMEpro plug-in is the best path if the owner standardises on SolidWorks/Inventor. Misumi is the cheapest "engineered" option with configurable lengths and CAD, but its 8-series (8 mm slot) does not interchange with Rexroth/Vention 10 mm slot hardware; pick one slot standard for the whole cell.

### 1b. Steel weldment alternative for the cutter bed and gantry

No vendor publishes a price for a welded steel machine base of this size; it is a fabrication quote. Basis for an estimate: a 2.0 m × 2.2 m bed frame in 80×80×4 mm steel RHS (≈ 9.4 kg/m, ≈ 30 m of section ≈ 280 kg) plus stress relief, machining of the rail mounting faces and powder coat is typically quoted at USD 8–15 per kg finished in US/EU job shops, i.e. **est. USD 2,500–4,500** for the bed frame alone (basis: section mass × typical fabricated-steel rate; unverified for 2026, confirm with two local quotes). The reason to consider it: linear rails for the cutter gantry (R-section 4) want a mounting face flat to ≈ 0.02 mm/m, which extrusion cannot hold without a machined plate on top. The hybrid most cutter OEMs use (Zünd G3 "robust aluminum construction, designed as a perforated sheet"; Eastman "static table" with blower underneath) is an aluminium or steel frame carrying a machined aluminium vacuum plate (see section 5). Sources: Zünd G3 operating manual https://serwis.integart.com.pl/wp-content/uploads/2019/09/instrukcja_obslugi_zund_G3-CUTTER_1.71_en-gb.pdf ; Eastman Eagle S125 manual https://www.eastmancuts.com/wp-content/uploads/2019/03/E-578.pdf .

### 1c. Levelling feet, casters, vibration isolation, tabletops

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Elesa (Elesa+Ganter) | LV.A levelling mount (technopolymer base, steel stem) | 208 variants; glass-fibre PA base | from USD 5.15 each (2026-10, Elesa US web list) | stock | Yes: Elesa CAD download (100,000+ products) | https://www.elesa.com/en/elesab2bstoreus/leveling-feet-us--1 |
| Elesa | LS.A levelling mount | 236 variants | from USD 3.36 (list) | stock | Yes | https://www.elesa.com/en/elesab2bstoreus/leveling-feet-us--1 |
| Elesa | LV.F / LV.F-AS levelling feet for ground mounting | two 180° anchor holes, optional NBR no-slip disk 70 Shore A; base and stem shipped separately | price by variant on page (not captured; same family as LV.A) | stock | Yes | https://www.elesa.com/en/elesab2bstoreus/Levelling-feet-and-supports--Levelling-feet-for-ground-mounting--LVF |
| Ganter | GN 36 / GN 37 machine feet; GN 148 / GN 248 with vibration damping; GN 343.2 | GN 148/248 are the damped machine-foot options for sewing heads | price via Ganter webshop/distributor; request quote | stock | Yes: GN 343.2 page has 3D configurator | https://www.ganternorm.com/en/leveling-foot ; https://www.elesa-ganter.com/en/www/Levelling-elements--Levelling-feet--GN3432 |
| McMaster-Carr | Swivel levelling mounts with threaded stud, M12 / M16 / M20 (e.g. 6992K74 stay-put M20, 7,500 lb) | 107 swivel variants; vibration-damping variants with rubber cushion; T-slotted-framing levelling mounts (3 products) | price shown only on McMaster page (not exposed to search); typical USD 8–40 each (est., McMaster category) | same/next day | Yes: McMaster 3D (STEP) per part | https://www.mcmaster.com/products/feet/thread-size~m12-3 ; https://www.mcmaster.com/products/feet/thread-size~m20 |
| McMaster-Carr | Locking swivel casters, 4–6 in, polyurethane, total-lock | plate mount; <1,000 lb to >2,000 lb per caster | price on McMaster page (est. USD 25–70 each) | same/next day | Yes (STEP) | https://www.mcmaster.com/products/locking-swivel-caster |
| Vention | ST-CST / ST-LVL casters and levelling feet | 45-mm-pitch compatible | price in Vention parts library (list; not captured) | next day | Yes | https://vention.com/software/machine-builder |
| Sorbothane | anti-vibration pads (viscoelastic) | isolate shock/vibration under sewing heads | price by size on reseller pages (est. USD 15–40 per 4"×4"×1/2" pad) | stock | No CAD needed (sheet) | https://www.sorbothane.com/technical-data/articles/anti-vibration-pads |
| McMaster-Carr | Vibration-damping mounts (253 products) and natural-rubber damping pads | "Place under equipment such as drill presses"; threaded-stud mounts M6–M16 | price on McMaster page | same/next day | Yes | https://www.mcmaster.com/products/vibration-control-mounts ; https://www.mcmaster.com/products/natural-rubber-vibration-damping-pads |
| Alcobra Metals | 0.75" cast aluminium tooling plate (MIC-6 class) | 12×12 in to 36×48 in; saw cut | USD 140.63 (12×12) to USD 1,687.50 (36×48) + USD 25 cut fee (2026-10, reseller) | days | No (stock plate) | https://alcobrametals.com/product/3-4-cast-tooling-plate/ |
| McMaster-Carr | MIC6 aluminium plate (>250 sizes); vacuum workholding plates | flat, stress-relieved cast plate for vacuum bed / fixture tops | price on page | same/next day | drawings | https://www.mcmaster.com/products/plates/material~aluminum-2/material~mic6-aluminum ; https://www.mcmaster.com/products/tables |
| NPS (National Public Seating) via Bush Furniture | SLT 3 series 24×48 in steel table, phenolic top | ready-made phenolic-top bench as sewing-station staging table | USD 645.80 (reseller; list USD 1,076) ; HPL-top equivalents USD 413.17 | stock | No | https://www.bushfurniturecollection.com/National-Public-Seating--B5377--1.htm |
| Tablex | Justice 30×72 in HPL table, 3P | 500 lb; industrial locking casters set USD 332 | USD 1,506 list (2025 price list) | weeks | No | https://tablex.com/wp-content/uploads/2024/12/Justice-Sell-Sheet-2025.pdf |

Note on the sewing-head isolation: an industrial sewing head on its own table (ST05) is normally bolted to a stand with rubber feet; the white paper's sewing stations will be fixed to the cell frame, so the right place for isolation is between the sewing-head mounting plate and the frame (Ganter GN 148/248 or McMaster vibration-damping mounts with M10/M12 stud, 4 per head), not under the whole cell. Quantify the need in the first vibration test; many integrators run without isolation when heads are on a stiff 90×90 frame.

### 1d. Machine guarding (ST00 ↔ ST09 interlocks)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Axelent | X-Guard mesh panel, Classic 50×30 mesh (heights 750/1300/1900/2200/2400 mm, 13 widths) and Premium 50×20 mesh (2200 mm, 6 widths) | 30×20 mm frame, Ø3/Ø2.5 mm wires, RAL 9011; tested to ISO 14120, Machinery Regulation 2023/1230; Classic needs ≥200 mm safety distance, Premium ≥120 mm | price not published; "Get your quote" (est. EUR 110–180 per 1000-mm-wide × 2200-mm panel incl. post, basis: typical EU modular-guarding quotes, unverified) | quote; stock items | Yes: "Show available 3D models" per panel; Axelent Safety Design app | https://www.axelent.com/en/safety-solutions/protect/machinery-and-robots/machine-guarding/x-guard/panels/mesh-panel |
| Axelent | X-Guard Contour W32R90-130/-190/-220/-240 (90° rounded-corner panels) | 1300–2400 mm, 50×30 mesh | quote | quote | Yes (CAD column on page) | https://www.axelent.com/en/safety-solutions/protect/machinery-and-robots/machine-guarding/x-guard/panels/mesh-panel-contour |
| Axelent | X-Guard doors (12 types), locks and switches (9), X-Tray cable trays | interlock-ready door frames; X-Tray certified to IEC 61537, UL | quote | quote | Yes | https://www.axelent.com/en/safety-solutions/protect/machinery-and-robots/machine-guarding/x-guard ; https://www.axelent.com/us/safety-solutions/protect/machinery-and-robots/machine-guarding/x-guard/cable-trays/wire-tray/x-tray |
| Troax | Panel ST PC 2050×200…1500 mm, 3 mm polycarbonate: 31020606 (200), 31030606 (300), 31050606 (500), 31070606 (700), 31080606 (800), 31100606 (1000), 31120606 (1200), 31150606 (1500) | 30×20 frame, RAL 9005; 1,600 J impact with Smart Fix; transparent, flame-retardant | price not published; request quote (est. EUR 150–250 per 1000-mm PC panel, unverified) | quote | Troax provides CAD on request (unverified) | https://www.troax.com/product/panel-st-pc |
| Troax | Smart Fix system with Post 60×40 (heights 1400/2200/3000 mm), mesh panels ST20 (20×100 mesh) / ST30 | panels + posts tested 309 J to 6,000 J | quote | quote | — | https://source.thenbs.com/en/gb/product/machine-guarding/9q2uMegrB3fWE1cfsEoVfV/9f15KANGdyBtvgyJdWFRsh |
| Satech | Basic / Strong modular guards | not retrieved in this pass | unverified | — | — | (no source captured) |
| DIY on extrusion | 4 mm or 6 mm clear polycarbonate sheet in the extrusion slot with panel gasket | lowest cost; requires own ISO 14120 / ISO 13857 reach-distance check | polycarbonate sheet est. USD 60–120 per 1.2 × 2.4 m × 4 mm (reseller range, unverified) | days | n/a | — |

Guarding note: the interlocked-door switches, light curtains and safety relays belong to ST09 (R-report on control and safety); here only the fence, posts, door frames and cable trays are costed. ISO 13857 reach distances decide mesh aperture and panel-to-hazard distance (Axelent states 200 mm for 50×30 mesh and 120 mm for 50×20 mesh).

### 1e. Starter BOM — frame, feet, guarding (one cell, 6 m × 3 m guarded envelope)

Quantities are my sizing for the layout assumption above; prices are the labelled basis from the tables. Totals are indicative only.

| # | Item | Vendor / part | Qty | Unit price (basis) | Line total | CAD |
|---|---|---|---|---|---|---|
| F-01 | 45×90 extrusion, main longitudinal/transverse members | Vention ST-EXT-002-2025 | 24 | USD 165.31 (list) | USD 3,967 | yes |
| F-02 | 45×90 extrusion, legs and short cross members (990 mm) | Vention ST-EXT-002-0990 | 24 | USD 93.93 (list) | USD 2,254 | yes |
| F-03 | 45×45 extrusion, guarding frames and brackets (as 80/20 1515 for cost reference) | 80/20 1515, 60 m ≈ 2,362 in | 60 m | USD 0.98/in (list) | USD 2,315 | yes |
| F-04 | T-nuts 10 mm slot M6 / M8 | Rexroth 3842530285 / 3842530287 | 600 | USD 0.78 (list) | USD 468 | yes |
| F-05 | Gussets 45×45 with fasteners | Rexroth 3842523561 | 120 | USD 7.52 (list) | USD 902 | yes |
| F-06 | Levelling feet, M16 swivel, ground-anchorable | Elesa LV.F (or Ganter GN 37) | 16 | est. USD 12 (Elesa list from USD 5.15 for LV.A; LV.F larger) | USD 192 | yes |
| F-07 | Vibration-damping mounts under sewing heads | Ganter GN 148 / McMaster damping mount M10 | 12 | est. USD 20 | USD 240 | yes |
| F-08 | Cast aluminium tooling plate for cutter vacuum bed, ≈ 1.9 m × 2.2 m × 19 mm (as 4 × 36×48 in plates) | Alcobra 0.75" cast tooling plate 36×48 | 4 | USD 1,687.50 + cut (reseller) | USD 6,850 (costed to the cutting line, not the frame line) | no |
| F-09 | Phenolic-top staging tables (ST03 buffer, ST07 output) | NPS SLT 3 24×48 phenolic | 2 | USD 645.80 (reseller) | USD 1,292 | no |
| F-10 | Mesh guarding, 2200 mm high, ≈ 18 m perimeter incl. 2 interlocked doors | Axelent X-Guard Classic panels + posts + 2 door frames | 18 m | est. USD 160/m panel+post, doors est. USD 900 each (quote needed) | USD 4,680 | yes |
| F-11 | Polycarbonate viewing panels at sewing/cutting stations | Troax Panel ST PC 2050×1000 (31100606) | 4 | est. USD 220 (quote needed) | USD 880 | on request |
| F-12 | Wire-mesh cable tray along guarding, 100 mm | Axelent X-Tray or generic 100 mm wire tray | 20 m | est. USD 12/m (unverified) | USD 240 | yes (Axelent) |
| | **Frame + feet + guarding subtotal (excl. F-08)** | | | | **≈ USD 17,400** | |

This subtotal alone exceeds the white paper's conservative frame/guarding/base-utilities figure of USD 15,000 before any compressor, air preparation or cabling is added; see "Conflicts with the white paper". The two cheapest levers are (1) Misumi or imported 6063 profile for non-precision members (≈ 30–60 % saving on F-01..F-03) and (2) DIY polycarbonate-in-slot guarding instead of a modular fence system (≈ 50 % saving on F-10/F-11), at the cost of CAD convenience and of doing the ISO 14120/13857 checks in-house.

### 2. Fasteners

Standard choice for the cell: metric only; ISO 4762 / DIN 912 socket head cap screws class 12.9 (black) or A2-70 stainless where lint/moisture is present; ISO 7380-1 button heads where a snag-free surface faces fabric; DIN 7991 countersunk for flush gripper and guide surfaces; T-nuts/hammer nuts matched to the slot standard chosen in section 1; Nord-Lock pairs on anything that vibrates (sewing heads, blower, gantry drive mounts); Loctite 243 (medium, serviceable) by default, 270 (high strength) only on set screws and pulleys that are never meant to come off.

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| McMaster-Carr | DIN 912 socket head screws, class 12.9 (category; e.g. 91290A-series black alloy steel) | M3–M24; DIN 912 / ISO 4762 | per-pack price shown only on McMaster page (est. USD 8–15 per 50–100 pack for M6×16 12.9, basis: McMaster category pricing seen in prior years; verify) | same/next day | Yes: STEP/IGES/SolidWorks per part number | https://www.mcmaster.com/products/socket-head-screws/specifications-met~din-912 |
| McMaster-Carr | ISO 7380-1 button head hex-drive, 316 SS (e.g. 90943A111 M3×6) and 18-8 | low-profile heads | price on page (small pack, each) | same/next day | Yes | https://www.mcmaster.com/products/screws/specifications-met~iso-7380-1 |
| McMaster-Carr | DIN 7991 countersunk socket screws (category) | flush mounting | price on page | same/next day | Yes | https://www.mcmaster.com/products/din-7991-socket-head-cap-screws |
| McMaster-Carr | DIN 985 nylon-insert locknuts, class 8/10, zinc plated (small and large packs; large pack ≥30 % cheaper per nut) | reusable a few times; insert max temp limits | price on page | same/next day | Yes | https://www.mcmaster.com/products/din-985-nuts |
| McMaster-Carr | Nord-Lock washers 93281A103 (M8/5/16", 0.340×0.530 in) and 93281A113 (wide, 0.650 in OD) | zinc-flake coated steel, sold each | price on page | same/next day | Yes | https://www.mcmaster.com/products/nord-lock-washers |
| Nord-Lock | NL6 (6.5×10.8×1.8 mm, 200/box), NL8, NL10, NL6ss stainless; user manual 2026 gives installation torques (12.9 bolt + NL: M6 17.4 Nm, M8 42 Nm, M10 82 Nm; 10.9 bolt: M6 15.5, M8 37, M10 73 Nm) | boxes of 200 | price via distributor; request quote (McMaster sells singles) | stock | drawings in manual | https://www.nord-lock.com/globalassets/mediavalet/web-assets/downloads/user-manual/00095_nl_user_manual_nlo_2026_v01_digital2.pdf |
| CDE Fasteners (US distributor) | MI416CTBA2: M4-0.7×16 ISO 7380 six-lobe button head A2 stainless | box of 6,000 | USD 502.65 / box = USD 0.0838 each; 5-box USD 0.0736 (2026-10, reseller) | stock | 2D PDF | https://cdefasteners.com/order-online/iso7380-metric-6-lobe-button-head-cap-screw-a2-stainless-steel/549369 |
| CDE Fasteners | MI416CTB10Z: same, class 10.9 zinc; M4NKA2 K-lock nut A2 (2,500/box USD 351.19); M4D982A2 DIN 982 nylon locknut A2 (4,000/box USD 218.14 = USD 0.055 each); MD04WSHA2 DIN 7980 lock washer A2 (5,000/box USD 109.20) | bulk boxes | USD 654.85 / 6,000 (10.9 zinc); others as listed (2026-10, reseller) | stock | 2D PDF | https://cdefasteners.com/order-online/iso7380-metric-6-lobe-button-head-cap-screw-a2-stainless-steel/549369 |
| Bosch Rexroth | T-nut 10 M6 3842530285 / M8 3842530287 (see section 1) | 10 mm slot | USD 0.78 each list | stock | Yes | https://www.boschrexroth.com/en/us/p/t-nut-3842530287 |
| Misumi | HNTT6-6 insertion nut M6 (6-series, 8 mm slot) and PACK-HNTT6 bulk | steel, chromate | USD 0.63 / 0.57 / 0.50 (1 / 100 / 1000) list | stock | Yes | https://us.misumi-ec.com/vona2/detail/110302251050?HissuCode=HNTT6-6 |
| Ruthex | RX-M3x5.7 brass heat-set inserts (100 pcs), RX-M4x8.1 (50), M3S/M4S/M5S short bundle, M2/M3/M4/M5 assortment box, complete set incl. M6/M8 + soldering tips | for 3D-printed EOAT parts; CAD (STEP) for each insert on product page | EUR 8.99 / 100 (M3, EUR 0.09 each); EUR 9.49 / 50 (M4); EUR 29.99 assortment; EUR 99.99 complete set; tips set EUR 16.90 (2026-10, list) | 1–3 days | Yes: STEP download per insert | https://www.ruthex.de/en/collections/gewindeeinsatze/m3 ; https://www.ruthex.de/en/products/ruthex-m3s-m4s-m5s-short-gewindeeinsatz-bundle-100-50-50-stuck-gewindebuchsen-aus-messing |
| McMaster-Carr | 97338A140 tapered heat-set insert assortment (M3/M4/M5/M6, 200 pcs) with 3 installation tips; 92160A327 installation tip (M5/M6, 1/4" shank); 92160A233 extraction tip M6 | brass | price on page | same/next day | Yes | https://www.mcmaster.com/products/heat-set-insert-tips/thread-size~m6-2 |
| PEM (PennEngineering) | S-M6-1ZI self-clinching nut, M6, for 1 mm+ sheet; hole 8.75 mm | zinc plated steel | price via distributor; request quote | stock | Yes: PEM product finder gives CAD | https://www.pemnet.com/products/product-finder/s-m6-1zi |
| Heli-Coil (Stanley) | Metric coarse kits M3–M20; master set 5626-125 (M5, M6, M8, M10×1.5) | wire inserts + tap + tool | genuine kit price via distributor (not captured); generic M6 30-pc kits USD 49.93 (VXB reseller, 2026-10) | stock | n/a | http://www.noblefix.com/helicoil/HeliCoil-Metric-Kit.html ; https://vxb.com/products/m6-thread-repair-kit-with-helicoil-inserts-and-hss |
| Henkel | Loctite 243 threadlocker 50 ml | medium strength, oil tolerant, hand-tool removable | GBP 39.59 ex VAT (Silmid UK, 2026-10, reseller); marketplace listings USD 9–18 are of uncertain authenticity | stock | n/a | https://www.silmid.com/ |
| Henkel | Loctite 270 50 ml; Loctite LB 8008 C5-A copper anti-seize | high strength (permanent) | price not captured from an authorised reseller; est. USD 25–40 per 50 ml (basis: 243 price), anti-seize est. USD 15–25 per 8 oz; verify | stock | n/a | — (unverified) |
| DIN 6325 dowel pins, DIN 125/9021 washers, DIN 934 nuts, Schnorr washers, rivnuts/tool, Bossard, Würth, Fabory, RS, Grainger, Zoro, Bolt Depot, Accu | — | all standard catalogue items | not captured in this pass; est. per 100: dowels 6 m6×20 USD 15–25, DIN 125 M6 USD 3–6, DIN 934 M6 USD 4–8, Schnorr S6 USD 10–20; rivnut kit with hand tool USD 40–90 (Amazon/Zoro class) | stock | McMaster/Misumi give CAD | unverified in this pass |

#### 2b. Starter fastener kit (one cell + spares)

Based on the extrusion count in section 1e (≈ 120 gussets × 2 bolts, ≈ 600 T-nuts) plus EOAT, sensor, guard and drive-mount fastening. Prices are labelled; where only McMaster "price on page" exists I give an estimate from the CDE bulk price × 2.5 (small-pack premium).

| # | Item | Spec | Qty | Unit (basis) | Line | Note |
|---|---|---|---|---|---|---|
| K-01 | SHCS DIN 912 12.9 M6×16 / ×20 / ×25 | black | 300 / 300 / 200 | est. USD 0.10 (CDE M4 bulk ×1.2 for M6; McMaster small packs ≈ ×2.5) | USD 80 | mains frame, brackets |
| K-02 | SHCS DIN 912 12.9 M8×20 / ×25 / ×30 | black | 200 / 200 / 100 | est. USD 0.18 | USD 90 | gussets, feet, drive mounts |
| K-03 | SHCS A2-70 M4×10 / ×12 / ×16; M5×12 / ×16 | stainless | 200 each | est. USD 0.08 (CDE A2 M4 = USD 0.084) | USD 80 | sensors, EOAT, covers |
| K-04 | Button head ISO 7380-1 A2 M4×16, M5×12, M6×12 | stainless | 200 each | USD 0.084 (CDE, bulk box basis) | USD 50 | fabric-facing surfaces |
| K-05 | Countersunk DIN 7991 A2 M4×10, M5×12 | stainless | 100 each | est. USD 0.10 | USD 20 | flush guides |
| K-06 | T-nuts 10 mm slot M6 / M8 | Rexroth 3842530285 / 3842530287 | 400 / 200 | USD 0.78 (list) | USD 468 | counted in F-04 |
| K-07 | Nylon locknuts DIN 985 M4 / M5 / M6 / M8 | zinc or A2 | 200 / 200 / 300 / 200 | USD 0.055 (CDE A2 M4 basis) | USD 50 | |
| K-08 | Washers DIN 125 M4–M10, DIN 9021 M6/M8 | zinc / A2 | 1,000 | est. USD 0.03 | USD 30 | |
| K-09 | Nord-Lock NL6 / NL8 / NL10 | 200-boxes | 1 box each | quote (McMaster singles on page) ; est. USD 60–120 per box | USD 270 | sewing heads, blower, drives |
| K-10 | Dowel pins DIN 6325 6 m6×20, 8 m6×30 | hardened | 50 each | est. USD 0.25 | USD 25 | repeatable fixture location |
| K-11 | Heat-set inserts M3 / M4 / M5 + tips | Ruthex assortment + complete set | 1 + 1 | EUR 29.99 + 99.99 (list) | ≈ USD 140 | EOAT prototypes |
| K-12 | Helicoil-type M6 and M8 repair kits | generic / Heli-Coil | 1 each | USD 49.93 (VXB) | USD 100 | |
| K-13 | PEM S-M6-1 nuts for sheet brackets | 100 | 100 | quote | — | |
| K-14 | Loctite 243 50 ml ×2, 270 50 ml ×1, anti-seize | Henkel | — | GBP 39.59 (243, Silmid); 270 est. | ≈ USD 150 | |
| K-15 | Rivnut kit M4–M10 with hand tool | generic | 1 | est. USD 60 | USD 60 | |
| | **Fastener kit subtotal** | | | | **≈ USD 1,600** (of which T-nuts USD 468 already in F-04) | |

### 3. Cabling and wiring

#### 3a. Power, control and chain-rated cable

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Lapp | ÖLFLEX CLASSIC 110 5X1,5 art. 1119905 (also 16G1 art. 1119216; CLASSIC 110 CY BK 0,6/1kV 5G1,5 art. 1121311 shielded) | 300/500 V, PVC, numbered cores, flexible; copper index 483.8 lb/10,000 ft (5X1,5); VDE reg. 7030 | price shown only to logged-in business customers on the Lapp US shop ("solid metal prices without additional charges"); request quote (est. USD 1.8–3.0 per m for 5G1.5, basis: typical distributor pricing, unverified) | stock | datasheet PDF per article; no 3D needed | https://api-shop.lapp.com/occ/v2/us/products/export/specification-sheet-file/1119905?curr=USD&lang=en_US ; https://api-shop.lapp.com/occ/v2/us/products/export/specification-sheet-file/1121311?curr=USD&lang=en_US |
| Lapp | ÖLFLEX FD 855 P (chain-rated, PUR, halogen-free, UL/cUL AWM): 0027530 2×0.5, 0027531 3G0.5, 0027532 5G0.5 (OD 5.1–6.6 mm); larger cross-sections in the same family | flexing −40 to +80 °C; copper basis EUR 150/100 kg | catalogue price via Lapp distributor; request quote | stock | datasheet | https://products.lappgroup.com/online-catalogue/power-and-control-cables/power-chain-applications/harsh-conditions-certified/oelflex-fd-855-p.html |
| igus | chainflex CF10.02.04 control cable (TPE, overall shield, oil/coolant resistant, chainflex class 7.6.4.1; CFRIP) | guaranteed for energy chains (igus 36-month guarantee programme) | price on igus page per metre (not captured); request quote | cut to length | datasheet | https://www.igus.com/product/CF10?artnr=CF10.02.04 |
| SOOW portable cord (US) | 14/4, 12/4 | for the mains drop to the cell disconnect | not captured; est. USD 2.5–4.5 per ft (unverified) | stock | n/a | unverified |

#### 3b. Pre-made servo, encoder and EtherCAT cables

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Beckhoff | ZK4800-8002-xxxx motor cable 1 mm² itec (fixed install; 4×1.0 + 2×0.5 + 2×AWG26; OD 10.0 mm; UL/CSA; for AM801x–AM803x, AM853x, AX8000 ≤12 A; max 25 m) | not for TwinSAFE SBC/SBT (use -8022) | price via Beckhoff sales (login) | stock | Beckhoff provides 2D/3D for connectors | https://www.beckhoff.com/en-en/products/i-o/i-o-specific-accessories/pre-assembled-cables/zk4800-8002-xxxx.html |
| Beckhoff | ZK4800-8003-xxxx motor cable 1.5 mm² M23 speedtec (fixed); ZK4800-8022-xxxx drag-chain 1 mm² itec; ZK4500-8022/-8023/-8024/-8025 drag-chain PUR 1/1.5/2.5/4 mm² (M23/M40 speedtec) | OCT one-cable (power + feedback) | reseller examples (PLC West, EUR, 2026): ZK4500-8023-0080 8 m EUR 181.39; ZK4500-8022-0100 10 m EUR 220.01; ZK4800-8022-0100 10 m EUR 232.88; ZK4500-8025-0090 9 m EUR 349.91; ZK4800-8003-0010 1 m EUR 242.72 new | stock | — | https://www.beckhoff.com/en-en/products/i-o/i-o-specific-accessories/accessories-overview/cables-and-connectors-overview-drive-technology ; https://www.plcwest.com/catalog?brand=Beckhoff |
| Beckhoff | Compact-drive cabling set: ZK4704-0421-2xxx (OCT motor 0.75 mm² itec, drag chain), ZK4000-5100-2xxx (encoder M12, drag chain), ZK2050-5200-0xxx (power 5G1.5 PUR drag chain), ZK1090-3191-0xxx (EtherCAT M8–RJ45 PUR), ZS2030-4812 (M12 L-coded T splitter), ZB8500 shield strap, ZB8511 shield busbar clamp | xxx = length in dm | login pricing | stock | — | https://www.beckhoff.com/en-en/products/i-o/i-o-specific-accessories/accessories-overview/cables-and-connectors-overview-compact-drive-technology/index.html |
| Beckhoff | EtherCAT patch cables: ZK1090-9191-0xxx (Cat.5 PUR 4×2×AWG26 RJ45–RJ45, 0.17 m…); ZK1090-9191-1xxx (PUR 1×4×AWG22, drag-chain, 3 million cycles, 0.15–4 m+); ZK1090-9191-Bxxx (PVC fixed, 0.5–85 m, D-series to 140 m); ZK1090-3131-3xxx (M8–M8 A-coded PVC AWG26, 0.1–50 m) | 160 V / 1 A rated; green | reseller quote only (Platinum International lists but no price); est. USD 20–45 per 1–3 m patch (unverified) | stock | datasheet PDF | https://www.beckhoff.com/en-en/products/i-o/i-o-specific-accessories/pre-assembled-cables/zk1090-9191-0xxx.html ; https://www.beckhoff.com/en-en/products/i-o/i-o-specific-accessories/pre-assembled-cables/zk1090-9191-1xxx.html ; https://www.beckhoff.com/en-us/products/i-o/i-o-specific-accessories/pre-assembled-cables/zk1090-3131-3xxx.html |
| Siemens | MOTION-CONNECT 500 (6FX5002-5❑❑…) and 800PLUS (6FX8002-5❑❑…) pre-assembled power/signal cables; sold-by-metre 6FX5008-1B❑… / 6FX8008-1B❑… | article-number code on SiePortal; 6FX5002-5CS01 phased out since 2016 | SiePortal login pricing | stock | — | https://sieportal.siemens.com/en-us/products-services/10204425 |

#### 3c. Sensor cables, connectors, glands, terminals, duct, EMC

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Phoenix Contact | SAC-4P-5,0-PUR/M12FS 1668124 (M12 A-coded socket, 4-pos, PUR halogen-free, open end, 5 m); family 1/1.5/2/3/5/10/15/20 m; -186 PUR POWER 0.75 mm² variant 1509490; SAC-3P…B (pins 2+4 bridged) and -2L (LED) variants | IP67 | USD 27.12 list / USD 22.60 sale (RSP Supply, 2026-10, reseller) | stock | Phoenix gives STEP via product page | https://www.phoenixcontact.com/en-nz/products/sensoractuator-cable-sac-4p-50-purm12fs-1668124 ; https://rspsupply.com/p-74389-phoenix-contact-1668124-sensoractuator-cable-sac-4p-50-purm12fs.aspx |
| Balluff | BCC M415-0000-1A-003-PX0434-050 (M12 female straight 5-pin A-coded, PUR, 5 m, drag-chain) ; BCC M415-0000-1A-001-PX0334-050 (3-wire) | drag-chain compatible | USD 28.26 / USD 24.77 (Balluff US list, 2026-10) | stock | Yes (Balluff product page) | https://www.balluff.com/en-us/products/dynamic/Z01A01 |
| Phoenix Contact | PT 2,5 feed-through terminal block 3209510 (push-in, 800 V, 24 A, 0.14–4 mm², NS 35 rail; pack 50) | tool-free push-in | "prices not currently available" on Phoenix site; est. USD 0.90–1.30 each (distributor class, unverified) | stock | Yes | https://www.phoenixcontact.com/us/products/3209510/pdf |
| Phoenix Contact | Shield clamps: SK 8 3025163 (busbar), SKS 8/14/20 3240210/-11/-12 (DIN rail), SKS 20-D 3240215 (direct mount, 10–20 mm) | EMC termination of servo cable shields | SKS 20-D EUR 9.46 incl. VAT (WSU Industrials, 2026-10, reseller; regular EUR 13.99) | stock | Yes | https://www.phoenixcontact.com/en-us/products/shield-connection-clamp-sk-8-3025163 ; https://wsu-industrials.com/en/phoenix-contact-3240215-schirmanschlussklemme-sks-20-d |
| Panduit | F1X2LG6 Panduct Type F narrow-slot wiring duct 1"×2"×6 ft, light grey; C2LG6-F cover | panel wire management | USD 45.56 (qty 1) / USD 23.65 (qty 24) at DigiKey (2026-10, reseller, backorder) | days | drawings | https://www.digikey.com/en/products/detail/panduit-corp/F1X2LG6/317480 ; https://www.omnicable.com/products/c2lg6-f |
| HARTING | Han 6B kit 10330060000 (6 poles + PE, hood/housing/inserts) ; Han 16B hood coupler 19300160736 ; Han 16B side-entry hood M25 19300161541 ; Han 16B inserts 09330162601/-2701 | station power/signal disconnects for modular stations | Han 6B kit USD 77.43 (RS US, 2026-10, reseller); Han 16B hood 19300160736 USD 46.54 new (Maverick Industrial, reseller) | stock | HARTING provides STEP via product pages | https://us.rs-online.com/product/harting/10330060000/70103911 ; https://maverickindustrialsales.com/products/harting-19300160736-cable-housing-han-16b-hood-coupler-hc ; https://www.harting.com/en-BR/p/Han-16B-Hood-side-entry-M25-19300161541/product-inquiry |
| Molex | Micro-Fit 3.0: receptacle housing 43025 (e.g. 430250200, 2-ckt), plug housing 43020 (430200200), headers 43045, OTS cable assemblies 214755/214756/214757/214758 | 3.0 mm pitch wire-to-wire for end-effectors | USD 0.13–0.40 each housing (distributor ranges on Molex page, 2026-10); JRready 8-pin kit USD 22.44 (reseller) | stock | Yes: Molex 3D on part page | https://www.molex.com/en-us/products/part-detail/430250200 ; https://www.jrdtools.com/products/jrready-jrn009-8-pin-8-circuits-micro-fit-connector-kit-male-female-receptacle-housing-plug-wire-connector-20-24awg-terminals-pin-sockets-3-0mm-pitch-20-sets |
| HellermannTyton | T50R cable tie 200×4.6 mm (PA66), 100/pack; MB4A adhesive mounts | general | price not captured (RS listing) ; est. USD 4–8 per 100 | stock | n/a | https://za.rs-online.com/web/p/cable-ties/1703918 |
| Lapp / Hummel | SKINTOP ST-M20×1.5 / M25 glands; Hummel HSK-M | IP68 strain relief at enclosures | not captured; est. USD 2–5 each (unverified) | stock | Lapp STEP on article page | unverified |
| Consolidated Electronic Wire & Cable | tinned copper flat braid (grounding straps, EMI) | 1/4–1 in widths | price per spool via vendor; est. USD 1–3 per ft for 1/2 in (unverified) | stock | n/a | https://www.conwire.com/product-category/wire-cable/tinned-copper-braid |
| Axelent | X-Tray wire mesh cable tray (IEC 61537, UL, E90, DNV-GL), X5 fittings, hinged cover | integrates with X-Guard posts | quote | quote | Yes (3D models on page) | https://www.axelent.com/us/safety-solutions/protect/machinery-and-robots/machine-guarding/x-guard/cable-trays/wire-tray/x-tray |
| Weidmüller / Phoenix / Knipex | ferrules (Phoenix AI 0,5-8 WH class), crimpers (Weidmüller PZ 6 Roto, Phoenix CRIMPFOX 6, Knipex 97 53 04 / 97 43 200), Brady M211 label printer | panel-build tools | not captured in this pass; est. crimper USD 120–250, ferrule assortment USD 25–60, label printer USD 150–250 (unverified) | stock | n/a | unverified |

#### 3d. Wire sizes and colours (control panel practice)

The cell will be CE-marked (IEC 60204-1) or UL 508A/NFPA 79 listed depending on market; the two sets of colour conventions overlap but are not identical, so fix one at design time and print it on the schematic cover sheet. The conventions below are stated from the standards themselves (IEC 60204-1:2016+A1:2021 clause 13.2.4; NFPA 79-2024 section 13.2.4); the URL in the Sources list points at a secondary summary because the standards are paywalled — treat the clause numbers as "verify against the purchased edition".

| Circuit | IEC 60204-1 colour | NFPA 79 colour | Minimum size used here |
|---|---|---|---|
| AC/DC power conductors | black | black | 1.5 mm² / 14 AWG (motor branch), per drive manual |
| AC control (e.g. 120/230 V) | red | red | 0.75–1.0 mm² / 18–16 AWG |
| DC control (24 V) | blue | blue | 0.5–0.75 mm² / 20–18 AWG (I/O), 1.5 mm² / 16 AWG (24 V distribution) |
| Interlock circuits powered from an external source (live when main disconnect is off) | orange | yellow (NFPA 79 uses yellow for this) | 0.75 mm² / 18 AWG |
| Protective earth | green-yellow | green or green-yellow | ≥ equal to largest power conductor up to 16 mm² |
| Grounded (neutral/earthed) circuit conductor | light blue | white or grey | — |

Note: NFPA 79 uses **yellow** for externally powered circuits and IEC 60204-1 uses **orange**; this is the single most common mix-up on cells built in Europe and shipped to the US. The white paper says nothing about wire colours; this is a build-guide decision (R-report ST09 should carry it).

#### 3e. Starter BOM — cabling and wiring (one cell, EtherCAT backbone, ≈ 12 servo axes, ≈ 60 sensors)

| # | Item | Vendor / part | Qty | Unit (basis) | Line |
|---|---|---|---|---|---|
| C-01 | Mains drop to cell disconnect, 3-ph 400 V / 480 V | SOOW 12/4 or ÖLFLEX CLASSIC 110 5G4 | 15 m | est. USD 6/m (unverified) | USD 90 |
| C-02 | Control cable, fixed runs (station power, valves, lamps) | ÖLFLEX CLASSIC 110 5X1,5 (1119905) and 16G1 (1119216) | 100 m + 50 m | est. USD 2.4/m and 3.5/m (quote) | USD 415 |
| C-03 | Chain-rated control cable on gantry / arm | ÖLFLEX FD 855 P 5G0.5 (0027532) or igus CF10 | 60 m | est. USD 4/m (quote) | USD 240 |
| C-04 | Servo OCT motor cables, drag-chain | Beckhoff ZK4800-8022-xxxx (gantry) / ZK4500-8022 | 12 (3–10 m) | EUR 181–233 per 8–10 m (PLC West reseller) ≈ USD 150 avg for shorter | USD 1,800 |
| C-05 | EtherCAT patch cables, drag-chain and fixed | ZK1090-9191-1xxx (6), ZK1090-9191-0xxx (14) | 20 | est. USD 30 (unverified) | USD 600 |
| C-06 | M12 sensor cables 5 m, PUR, drag-chain | Balluff BCC M415-…-050 / Phoenix SAC-4P-5,0-PUR/M12FS | 40 | USD 22.60–28.26 (reseller/list) | USD 1,000 |
| C-07 | M12 sensor cables 2 m | Phoenix SAC-4P-2,0-PUR/M12FS | 30 | est. USD 15 (family of 1668124) | USD 450 |
| C-08 | Station disconnect connectors (power + signal) | HARTING Han 16B hood/housing/insert sets | 8 | est. USD 140 per complete set (hood USD 46.54 + inserts + housing, reseller) | USD 1,120 |
| C-09 | EOAT connectors | Molex Micro-Fit 3.0 kits + crimp terminals | 2 kits | USD 22.44 (reseller) | USD 45 |
| C-10 | Terminal blocks push-in 2.5 mm² + PE + end brackets | Phoenix PT 2,5 (3209510) ×200, PT 2,5-PE ×40 | 240 | est. USD 1.10 (unverified) | USD 265 |
| C-11 | Shield clamps for servo and encoder cables | Phoenix SKS 20-D 3240215 / SKS 8 | 30 | EUR 9.46 (reseller) ≈ USD 10 | USD 300 |
| C-12 | Wiring duct 1"×2" and 2"×3" with covers | Panduit F1X2LG6 / F2X3LG6 + C covers | 12 lengths | USD 23.65–45.56 (DigiKey) | USD 420 |
| C-13 | Cable glands M20 / M25 | Lapp SKINTOP ST-M20/M25 | 60 | est. USD 3 (unverified) | USD 180 |
| C-14 | Energy chain, gantry X (≈ 3 m travel) and Y, with brackets | igus E2.1 / E4.1 (see section 6) | 2 runs | quote (est. USD 60–120/m incl. brackets, unverified) | USD 700 |
| C-15 | Cable ties, mounts, heat-shrink kit, labels | HellermannTyton T50R ×500, MB4A ×100, label printer + cartridges | lot | est. (unverified) | USD 350 |
| C-16 | Grounding braid, PE bar, bonding jumpers | 1/2 in tinned braid 10 m + lugs | lot | est. USD 1–3/ft | USD 100 |
| C-17 | Ferrule crimper + ferrule assortment + stripper | Weidmüller PZ 6 Roto / Knipex 97 43 200 | 1 set | est. USD 250 (unverified) | USD 250 |
| | **Cabling subtotal** | | | | **≈ USD 8,300** |

