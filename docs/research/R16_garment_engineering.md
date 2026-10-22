# R16 · Garment engineering: the premium short-sleeve T-shirt

Research agent R16 · date 2026-10-21 · project Roll-to-Garment. Stations and modules referenced by the IDs in the common brief (ST00–ST10, M01–M14).

<!-- SUMMARY_PLACEHOLDER -->

## Findings

Conventions: SAM = standard allowed minutes (basic time plus allowances, one trained operator at 100% rating). SMV is the same quantity under another name. "st/3 cm" is the European stitch-density unit used by Coats; SPI = stitches per inch (st/3 cm × 0.846 ≈ SPI). Stitch numbers are ISO 4915 classes; seam codes are ISO 4916 classes. Stations ST00–ST10 as in the common brief.

### F1. Construction sequence of a basic crew-neck T-shirt and SAM per operation

The industry operation sequence for a round-neck tee with five components (front, back, two sleeves, neck rib) is consistent across the sources below: shoulder join → neck-rib prepare/close → neck-rib attach → neck topstitch / back-neck tape → (labels) → sleeve attach → side seam with care label → sleeve hem → bottom hem → trim and inspect. Several factories hem the sleeves flat before setting them (the 2014 work-study sequence does this), which matters for automation because a flat hem needs no cylinder-bed tubular feeding.

Table F1-A. Operation breakdown with published SAM (minutes). Three independent sources; the operation list is harmonised to the common sequence. "ESJ 2014" is a work-study of a basic single-jersey tee in a Bangladeshi factory (17 operations, 20% allowance, total 6.48 min). "OCS/ScanERP" is an industry reference table compiled from Online Clothing Study data (basic tee 8.5 min, 12–18 operations). Where a source does not list an operation, the cell is "—".

| # | Operation | Stitch (ISO 4915) / machine | ESJ 2014 SAM | OCS/ScanERP SAM | Notes for the cell |
|---|---|---|---|---|---|
| 1 | Match / number front and back | manual | 0.24 | — | Replaced by piece ID and vision at ST03/ST04 |
| 2 | Shoulder join (both shoulders) | 504 or 514 overlock, often with shoulder tape or clear elastic | 0.27 | 0.45 | OCS worked example uses 0.45 min [3]. Reinforcement tape is fed through a tape folder on the overlock |
| 3 | Neck rib make (measure, cut, close ends) | 301 lockstitch (ends) | 0.26 | — (inside "neck rib attach") | ST06 must cut strip, join ends, fold |
| 4 | Neck rib attach to neckline | 504/514 overlock with differential feed | 0.30 | 0.70 | ST06 core operation; rib stretched to neckline, body not stretched [1][14] |
| 5 | Neck piping / back-neck tape / neck topstitch | 406 coverstitch with binder, or 301/401 topstitch | 0.29 + 0.60 (tape) + 0.35 (topstitch) | 0.55 (tape) + 0.60 (topstitch) | Optional in cheap tees, expected in premium tees [1] |
| 6 | Main label attach | 301 lockstitch | 0.30 | 0.35 | Back neck, inside |
| 7 | Sleeve hem (both) | 406/602 coverstitch, 2-needle | 0.30 (flat, before set-in) | 0.50 × 2 = 1.00 | Flat hemming before sleeve attach avoids tubular feeding |
| 8 | Sleeve match + sleeve attach (both) | 504/514 overlock | 0.29 + 0.60 | 0.55 × 2 = 1.10 | Curved seam, ease control |
| 9 | Side seam + underarm (both), care label inserted | 504/514 overlock | 0.80 | 0.60 × 2 = 1.20 | Care label on the wearer's left, ~10 cm above hem [1] |
| 10 | Care label join | 301 lockstitch | 0.29 | 0.30 | Often sewn into the side seam instead |
| 11 | Body turning | manual | 0.32 | — | Needed if hems are sewn from the face after closing |
| 12 | Side topstitch (optional) | 301/401 | 0.60 | — | Not in a basic tee; omit |
| 13 | Bottom hem | 406/602 coverstitch, 2-needle | 0.35 | 0.75 | Tubular on cylinder bed, or flat before side close with customer approval |
| 14 | Thread trim and inspection | manual | — | 0.50 | ST07 |
| | **Total sewing SAM** | | **6.48** (17 ops incl. optional) | **≈8.5** | Textile Learner: tees range 6.5–18 min by style [2]; an AUTEX Research Journal study quotes 4.38 min as the lowest SAM (V-neck tee) in its dataset [5] |

Sources for F1-A: [1] Online Clothing Study, step-by-step T-shirt manufacturing (2016, revised 2023); [2] Textile Learner, T-shirt types and operation sequence (2023); [3] Online Clothing Study, machine requirement calculation (2024), shoulder-join SMV 0.45 and "t-shirt lines work at 80–90% efficiency"; [4] European Scientific Journal 2014, "Effective way to estimate the SMV of a T-shirt by work study" (Table 2); [5] AUTEX Research Journal 2020, statistical analysis of SAM; [6] Scan ERP SAM reference table (secondary compilation; treat values as indicative).

What the SAM numbers mean for the cell: SAM is human work content with handling, not machine sewing time. The pure stitching portion of a tee is small: the seam lengths below total roughly 3.3 m of overlock, 2.0 m of coverstitch and under 0.3 m of lockstitch per size-L shirt (est., from the pattern dimensions in F5), which at 2.5 mm stitch length and a conservative 2,000 st/min effective speed is about 0.66 + 0.40 + 0.06 ≈ 1.1 min of needle-running time. The remaining 5–7 min of SAM is pick-up, align, feed, turn and dispose: exactly the work ST04 and the station fixtures must do.

### F2. Stitch classes, seam classes, allowances, stitch density

Table F2-A. Standards and reference documents.

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 4915 Textiles — Stitch types — Classification and terminology | 1991 (Ed. 2), reviewed and confirmed 2021, still current | Paid, CHF 181 | Stable, the global reference | Defines 301, 401, 406, 503, 504, 512, 514, 516, 602 used in the garment record (M02) and compiler (M06) | https://www.iso.org/standard/10932.html |
| ISO 4916 Textiles — Seam types — Classification and terminology | 1991 (Ed. 2), reviewed and confirmed 2022, still current | Paid, CHF 204 | Stable; to be read with ISO 4915 | Seam-class codes (SSa, EFa, LSa, BSa ...) for the seam_edges field of M02 | https://www.iso.org/standard/10934.html |
| ASTM D6193 Standard Practice for Stitches and Seams | current ASTM edition (not verified in this report) | Paid | US equivalent of ISO 4915/4916 | Alternative reference for US customers; unverified | https://www.astm.org/ (search D6193) |
| Coats, Basic stitch types (info hub) | 2024-01-25 | Free | Vendor reference | Plain-language definitions of each stitch class, used below | https://www.coats.com/en-us/info-hub/basic-stitch-types/ |

Stitch classes as used on the tee (definitions from Coats [7], a primary thread-industry source; ISO 4915 is the normative text):
- 301 lockstitch: one needle thread and one bobbin thread; reversible, strong, low elongation, low productivity because of bobbin changes. Use on the tee: rib-end join, label attach, bar-tack/tack of sleeve seam.
- 406 two-needle bottom-cover chainstitch: two needle threads interlooped with one looper thread on the underside; the standard hem stitch for knits and for binding/elastic attaching. Use: sleeve hems, bottom hem, back-neck binding with a binder.
- 602: 406 plus a top-cover (spreader) thread covering the upper surface. Use: hems and neck tape where the raw edge must be covered on top.
- 503 two-thread overedge: single-ply serging and hemming; "not suitable for seaming operations" because it flattens under lateral load [7].
- 504 three-thread overedge: one needle, two loopers; "excellent extension and does not unravel easily"; for serging and for joining two or more plies [7]. The basic knit seaming stitch.
- 512 / 514 four-thread overedge: 512 "mock safety, half cover", 514 "full cover" (upper looper thread extends to the left needle) [7]. 514 is the usual choice for shoulder, sleeve and side seams in heavier tees; Uçar (2002) studied grinning of ISO 514 seams on knits and found grinning increases with fabric rigidity, thread extensibility and *lower* stitch density [25].
- 515 / 516 safety stitches: 401 chainstitch plus 503 or 504 in one pass; used for wovens and heavy knits, not needed on the tee.

Seam classes (ISO 4916 nomenclature; the first two letters give the class, the third the variant):
- SSa (superimposed, plain): two plies face to face, overedged together; shoulder, sleeve set, side seam, rib attach. Seam code often written "SSa-1" with 504/514.
- EFa/EFb (edge finish): single-ply hem turned once; EFb with 406 is the coverstitch hem.
- BSc (bound seam): binding strip folded over the raw edge; back-neck binding with 406 and a binder.
- LSc/LSq (lapped): tape laid over a seam, as in back-neck tape covering the rib seam.
Exact variant letters should be taken from ISO 4916 when the tech pack is frozen (the standard is paid; the project should buy it, CHF 204).

Seam allowances for knits (industry practice, from the fabric-consumption method taught at Textile School [8] and the Coats/OCS guidance): overlock seams 6–7 mm finished (the overedge width is cut by the knife; typical overedge width 4 mm on a two-needle 4-thread overlock [31]); pattern allowance for overlocked seams 1.0–1.5 cm (Textile School uses 1.5 cm for shoulder join and sleeve join); hem allowances 2.5–3 cm for bottom and sleeve hems (finished hem 2.0–2.5 cm); side seam allowance 3 cm added to half chest [8].

Stitch density for cotton jersey, from the Coats application guide for knitted T-shirts [9] (Coats publishes it for children's T-shirts; the adult ranges on the Coats sweater/knitwear page are the same or one step coarser [10]):

| Operation (stitch) | Stitch density | Needle thread | Looper / under thread | Needle size Nm (metric) |
|---|---|---|---|---|
| 301 lockstitch (labels, rib ends) | 12–14 st/3 cm (≈10–12 SPI) | Coats Epic (polyester corespun) Tex 24 or 30 | Epic Tex 24/30 | 70–90 |
| 401 chainstitch | 12–14 st/3 cm | Epic Tex 24/30 | Epic Tex 24/30 | 70–90 |
| 504 three-thread overlock (seams) | 14–16 st/3 cm (≈12–14 SPI) | Epic Tex 24/30 | Gramax (textured polyester) Tex 18 | 70–90 |
| 514 four-thread overlock (seams) | 14–16 st/3 cm | Epic Tex 24/30 | Gramax Tex 18 | 70–90 |
| 406 coverseam (hems, binding) | 14–18 st/3 cm (≈12–15 SPI) | Epic Tex 24/30 | Gramax Tex 18 | 70–90 |
| 304 bartack | — | Epic Tex 24/30 | Epic Tex 24/30 | 70–90 |

Coats adds: "to avoid damage to the fabric during the sewing of knitted garments, ball point needles are generally recommended" and, for 406 binding on neck and arm openings, Gramax Tex 18 as the looper thread for cover and softness next to skin [9]. For heavier knitwear Coats moves to Tex 30/40 and Nm 80–100 on overlock [10]; for a 280 gsm jersey the project should sample both Tex 24/30 and Tex 30/40 needle threads.

### F3. Needles for cotton single jersey

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| Groz-Beckert | Needle point "light ball point" (FFG/SES family) for T-shirts, underwear, fine sweaters; RG for fine interlock; FFG when material damage appears on single/rib knits | Point selection table: single- and rib-knit, fine knitwear with elastane → FFG; principle "as thin as possible, as thick as necessary" | Not published; reseller example: Groz-Beckert DBxK5 10-pack USD 4.79 (The Thread Exchange, seen 2026-10-21) | Stock item at resellers | Not applicable (consumable) | https://www.groz-beckert.com/en/news/newsletter/sewing/2015/m2_sewing_selectionneedle.html ; https://cag-st-images.s3-us-west-2.amazonaws.com/EducationalCenter/EcPdfs/Groz-Beckert_needle_info.pdf |
| Organ Needles | DBx1 KN / SF (knit) series, BP ball-point series; size chart Nm 60–200 | KN/SF straight-blade long-taper points for knits; BP ball point "spreads fabric gently"; PD titanium coating for durability | Not published; request quote | Stock | Not applicable | https://organ-needles.com/english/wp-content/uploads/2020/07/DBx1_EN.pdf |
| JUKI (coverstitch needle system) | UY128GAS, size #10S standard, #9S–#12S range (≈ Nm 65–80) on MF-7900 | Factory specification for the MF-7900 hemming machine | Not published | — | — | https://juki.com/mf-7900-h11-series ; https://www.juki.co.jp/industrial_e/products_e/apparel_e/cover_e/detail.php?cd=MF-7900D_H24_H25_E |

Needle systems by machine class (from the JUKI/Pegasus specifications and the Groz-Beckert reseller listings above): lockstitch DBx1 (134 for walking-foot/heavier heads); overlock DCx27 (B27) — not verified on a vendor page in this report, treat as unverified; coverstitch UY128GAS (verified, JUKI MF-7900). Recommended sizes for 240–300 gsm combed cotton jersey: Nm 70–80 light ball point (SES/FFG) on overlock and coverstitch, Nm 70–75 on lockstitch, confirmed only by sewing trials (Groz-Beckert's three-step seam test [11]).

### F4. Fabric: cotton single jersey body and 1×1 rib for the premium tee

Table F4-A. Published characteristics of cotton single jersey (and rib) relevant to handling.

| Property | Published value | Source |
|---|---|---|
| Weight classes, single jersey | Light 120–160 gsm, standard retail 160–200 gsm, heavyweight streetwear 220 gsm and up (Burhan Enterprises, 2026); heavyweight 240–300–350 gsm (Turkey Clothing Production); 210–250+ gsm "heavyweight" (Canvas ETC, 2026); single jersey tees 140–200 gsm (AA Enterprises chart); Wikipedia 120–220 gsm | [12] [13] [14] [15] |
| Yarn and gauge typical | 30/1 combed ring-spun on a 28-cut, 26-inch machine for ~166 g/m² relaxed single jersey (Cotton Incorporated guide); 20/1 combed cotton for 180 gsm open-width; 30/1 combed cotton/elastane 250 gsm at 180 cm | [17] [13] |
| Width | Tubular 36–38 in (91–97 cm) flat for 180–190 gsm; tubular 30–36 in or open width 58–72 in (147–183 cm) in general; 180 cm open width listed for 150–250 gsm cotton jerseys | [18] [19] [13] |
| Roll mass | 18–22 kg per tubular roll, MOQ one roll (Plakads, India, 2024); 20 kg roll per colour; relaxing machines accept rolls to 500 mm diameter and 80 kg (Oshima UW-2) | [18] [20] |
| Roll length (derived) | For 280 gsm at 180 cm open width: 20 kg ≈ 40 m, 25 kg ≈ 50 m (est., mass ÷ (0.280 kg/m² × 1.80 m)). For tubular 95 cm flat (two layers): 20 kg ≈ 38 m | est. from [13] [18] |
| Edge curl | Single jersey curls because the single-face structure is unbalanced: side (wale) edges curl toward the back, top/bottom (course) edges curl toward the face; curl consumes 0.5–1.0 in of cross-grain; interlock and rib do not curl | [13] [14] [12] |
| Spirality / skew | Side-seam twist after wash when yarn twist and machine settings are unbalanced; ask for spirality on test reports and hold under about 5% | [12] |
| Relaxation before cutting | Rolls retain tension from knitting, finishing, rolling, storage and transport; relax open on a table about 24 h (OCS); SOP table: 100% cotton single jersey 140–180 gsm 16–24 h, cotton/elastane 24–48 h, interlock/rib 24–36 h, at 22–25 °C and 55–65% RH, accordion-folded on racks, never cut cold; Oshima steam relaxing UW-2S cuts this to approximately 6–8 h | [21] [22] [20] |
| Residual shrinkage | Cotton knit shrinkage depends on construction, relaxed dimensions, moisture during tumble drying, compacting and crosslinking (Cotton Incorporated, 2006, older but fundamental); single jersey shows significant lengthwise change, interlock more widthwise (Beltwide 2012); elastane raises length shrinkage | [17] [24] |
| Stretch and recovery | Rib: high widthwise stretch, excellent recovery; single jersey: moderate stretch, fair recovery; rib body fabrics 180–300 gsm, 3–5% elastane sharpens recovery for necklines | [12] |
| Static and ply adhesion | No published quantitative source found for 100% cotton single jersey; cotton is hygroscopic and the cutting-room literature does not report static as a problem for it (polyester blends do). Treat as unverified; test on the vacuum bed with the chosen fabric. Single-ply pick-up adhesion to the conveyor surface is a vacuum/porosity question, see R02/R03 | unverified |

Sources for F4-A: [12] Burhan Enterprises, single jersey vs interlock vs rib (2026-06-10); [13] Turkey Clothing Production, single jersey technical specifications; [14] Canvas ETC, cotton jersey technical properties (2026-03-29); [15] AA Enterprises GSM chart; [17] Cotton Incorporated, Guide to improved shrinkage performance of cotton fabrics (2006, possibly stale but the underlying physics is unchanged); [18] Plakads Apparel, cotton single jersey 180–190 gsm product page (2024); [19] Calculator Academy fabric consumption guide (2022); [20] Oshima fabric relaxing machines UW-2/UW-2S (2026 site); [21] Online Clothing Study, cutting room overview (2011, stale date, practice unchanged) and functions of the cutting department (2015); [22] Zenivic/AIOC fabric relaxation and ply spreading SOP; [24] Beltwide Cotton Conference 2012, effect of knit structure on dimensional stability.

Proposed fabric specification sheet (to be frozen with the first supplier lot; fields follow the white paper's qualified material profile):

| Field | Body jersey target | Neck rib target | Test / evidence |
|---|---|---|---|
| Composition | 100% combed ring-spun cotton (optionally compact-spun) | 95/5 cotton/elastane 1×1 rib (or 100% cotton 1×1 rib if customer requires) | Supplier declaration; EU 1007/2011 fibre names [68] |
| Construction | Single jersey, 20/1 or 24/1 combed yarn for 240–300 gsm (est.; 30/1 is the 160–200 gsm norm [17]) | 1×1 rib, 30/1 + 40 D elastane typical [22] | Supplier spec |
| Mass per area | 280 ± 5% g/m² relaxed (white paper reference 280) | 360 ± 5% g/m² (white paper reference) | ASTM D3776 / ISO 3801 (not verified in this report) |
| Width | Open width 160–185 cm usable, or tubular 90–97 cm flat (decision in Recommendation) | Tubular rib 35–40 cm flat or open width | Measured at receipt |
| Roll | 20–25 kg, single lot per roll, 76 mm core (verify) | 10–20 kg | Supplier |
| Face/grain | Face = knit (V) side; wale direction along roll | Rib stretch across strip | Visual |
| Stretch under 2 kg load (course direction) | Record value; typical single jersey moderate | Record value; rib high | ASTM D2594/D2594M-21 (fabric stretch and growth, low-power knits) [62] |
| Recovery / growth | Record | Record | ASTM D2594 growth procedure [62] |
| Edge curl | Measure curl height after 30 min flat from a fresh cut, both directions | Low | In-house, no standard found |
| Residual shrinkage after ISO 6330 wash/dry | Target ≤ 5% length and width (common buyer spec; unverified) | Same | ISO 6330:2021 procedure + AATCC TM135-2025 / ISO 3759 marking [59] [60] |
| Spirality | ≤ 5% [12] | — | AATCC TM179 (referenced on the TM135 page) [60] |
| Relaxation state | Relaxed 24 h open before cutting [21][22], or 6–8 h steam-relaxed [20] | Same | Log |
| Heat sensitivity | Cotton: tolerate 150 °C pressing [14]; elastane rib: lower | — | Supplier |

Fabric and thread cost per tee (prices seen 2026-10-21 unless noted, all list/marketplace, not quotes):

| Item | Price | Basis | Source |
|---|---|---|---|
| 100% cotton single jersey knit, rolls | USD 6.20–6.30/kg, MOQ 360 kg (Zhejiang Baoxuan via Accio aggregator) | marketplace list | [16] |
| 92/8 cotton/spandex 1×1 rib 180–190 g | USD 5.40–5.91/kg, MOQ 25 kg (Gift In Collections, HK) | marketplace list | [25] |
| US-milled heavyweight cotton knits (jersey 10 oz, 1×1 rib 12–16 oz) | from USD 9.00/yd (Isee Fabric); 1×1 rib 100% USA cotton from USD 6.00/yd | retail list | [26] [27] |
| 100% combed cotton 1×1 rib | USD 14.95/yd (Eagle Fabrics, retail) | retail list | [28] |
| White paper scenario | USD 12/kg body, 14/kg rib ("unquoted scenario values") | assumption | white paper §21 |
| Material per attempt at white-paper mass balance (0.3788 kg body + 0.0318 kg rib) | USD 4.99 at 12/14 per kg; est. USD 2.9 at 7/8 per kg (premium combed heavyweight, delivered, est.) | calculation | this report |
| Sewing thread | Coats: approx. 45 m per men's sports tee; Coats worked example for an average knitted tee: 67.8 m before 15% wastage, 77.8 m after; A&E ANECALC example for a men's tee: 64 yd with waste, USD 0.0211 per garment (2010 prices) | vendor guides | [29] [30] [31] |

### F5. Pattern pieces, allowances, consumption, marker efficiency, sizing and grading

Pieces: front, back, left sleeve, right sleeve, neck rib (5 cut pieces) [1]; plus back-neck tape (purchased tape or a self-fabric strip), main label, care label. The white paper's panel list (front, back, left_sleeve, right_sleeve, neck_rib) matches.

Allowances used in knit consumption practice [8]: bottom hem 2.5–3 cm, sleeve hem 2.5–3 cm, shoulder join 1.5 cm, sleeve join 1.5 cm (sub-total 9 cm plus 1 cm in hand, 10 cm on length); side seam: half chest + 3 cm; neck rib 1×1 rib, cut across the stretch.

Net area check against the white paper (size L, est.): cut width = half chest 55 cm + 3 cm = 58 cm; cut length = HPS length 74 cm + 3 cm hem + 1.5 cm shoulder ≈ 79 cm; front and back 2 × 0.58 × 0.79 = 0.92 m²; sleeves 2 × ≈0.10 m² = 0.21 m²; total ≈ 1.13 m², consistent with the white paper's 1.15 m² net body area. Rib strip 7.5 cm × 45 cm ≈ 0.034 m² (the white paper's 0.075 m² is about double; it may include tape; harmless but conservative). At 280 gsm the net body mass is 0.32 kg and the finished tee will weigh roughly 0.30–0.33 kg (est.), compared with 0.17–0.22 kg for a 180 gsm tee [19] [43].

Marker efficiency: typically 80–85% of marker area covered by pieces [40]; OCS defines it as pattern area ÷ marker area, excluding end loss [41]; a CAD example for a 24-piece T-shirt marker on 90 cm width gives 84.54% [42]; above 85% is considered strong, cutting loss 10–15% [19]. Single-size, single-garment markers nest worse than multi-size markers: for one tee per marker on 180 cm open width expect 75–82% (est.), recovering to 83–87% when the nester (M04) interleaves pieces of 4–8 shirts across the width.

Sizing standards and a representative size chart:

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ASTM D6240/D6240M-24a Standard tables of body measurements for adult male, chest 34–52, short/regular/tall | 2024 (updated 2024-10-18) | Paid, USD 72 | Current; includes Alvanon 3D avatars | Body baseline for men's tee sizes; pair with ease rules | https://www.astm.org/d6240_d6240m-24a.html |
| ASTM D5585-21 Body measurements for adult female misses, sizes 00–20 | 2021 | Paid | Current | Women's tee sizes | https://www.astm.org/d5585-21.html |
| ISO 8559-2:2025 Size designation of clothes — primary and secondary dimension indicators | 2025-09 (Ed. 2) | Paid, CHF 181 | Current | Size labelling convention for export | https://www.iso.org/standard/85590.html |
| Projob Workwear 647001 T-shirt measurement list (industry example) | 2025-03 | Free PDF | — | Example finished spec with grading | http://corporate-wear.eu/assets/rozmiary/647001.pdf |
| Gildan 2019 measurement sheet (2000/5000 heavy cotton tees) | 2019 | Free PDF | — | Example US basic-tee grading, tolerance ±1 in | https://www.jklclothing.co.uk/upload/attachments/29900e67-661b-4fdc-b5e0-ed03068a9be0.PDF |

Representative finished measurements (cm), laid flat:

| POM | S | M | L | XL | Grade | Tolerance | Source |
|---|---|---|---|---|---|---|---|
| Half chest 2.5 cm below armhole (Projob 647001) | 50 | 53 | 55 | 60 | 3–5 cm | min ±1 cm | [32] |
| Body length from HPS (Projob) | 71 | 72.5 | 74 | 77 | 1.5–3 cm | min ±1 cm | [32] |
| Sleeve length (Projob) | 20 | 21 | 22 | 23 | 1 cm | min ±1 cm | [32] |
| Half chest (Gildan 2000/5000, converted from 18/20/22/24 in) | 45.7 | 50.8 | 55.9 | 61.0 | 5.1 cm | ±2.5 cm (±1 in) | [33] |
| Body length HPS (Gildan 2000, from 28/29/30/31 in) | 71.1 | 73.7 | 76.2 | 78.7 | 2.5 cm | ±2.5 cm | [33] |
| Typical tech-pack tolerances for knits | — | — | — | — | — | ±1.0 cm widths and lengths, ±0.5 cm necks/cuffs/details (Renrui template); ±0.5–1 cm (Bryden); ±1.5 cm half chest, ±2.0 cm length (HRM) | [35] [36] [34] |

Neckband (rib) relationship: hobby and factory sources agree the rib is cut shorter than the neckline and stretched onto it: 70–75% for stretchy rib on a crew neck, 80% for self-fabric (The Last Stitch) [78]; 80–90% general rule, 80–85% for rib, 90% for self fabric (Life Sew Savory) [79]; "commonly 10–20% shorter" i.e. 80–90% for 1×1 rib with 2–5% elastane (LSLONG factory guide, 2026) [80]; neckline minus 15% (Sew Daily) [81]; a recovery-factor analysis shows the right ratio depends on rib recovery (R = 0.8 → ~75%; R = 0.9 → 78–88% depending on band width) [82]. Finished neckband widths run 1.5–2.5 cm; wider rib (≥2 cm) for heavyweight or oversized tees; neck tape at the back stabilises the seam [80]. One factory guide explicitly warns against copying a universal ratio from a template and asks the factory to propose the relationship, then approve it on the physical sample after the care test [83]. The white paper's 0.85 example (50 cm neckline, 42.5 cm rib) is inside the published range.

### F6. GarmentCode T-shirt parametrisation (M03)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| GarmentCode / PyGarment (maria-korosteleva/GarmentCode) | repo created 2023-09-13, 1,512 commits on main as of 2026-10-21; PyPI pygarment 2.0.0 | MIT | Active research code with GUI and pattern sampler; paper ACM TOG 2023 (DOI 10.1145/3618351) | Base for M03: parametric panels, stitch (edge-pair) connectivity, body-measurement driven; lacks seam allowances, stitch classes, rib-band ratio and grading tables | https://github.com/maria-korosteleva/GarmentCode ; https://pypi.org/project/pygarment/2.0.0 ; https://dl.acm.org/doi/10.1145/3618351 |
| GarmentCode web configurator | live 2026 | Free to use | Demo | Shows the parameter groups meta / waistband / shirt / collar / sleeve / left / skirts / pants | https://garmentcode.ethz.ch/ |

The T-shirt parameter file `assets/design_params/t-shirt.yaml` (fetched 2026-10-21) defines, for the upper garment [48]:
- `meta.upper`: `Shirt` (alternatives `FittedShirt`, none). `meta.wb` (waistband) and `meta.bottom` null for a tee.
- `shirt.length` v 1.2, range 0.5–3.5 (fraction of the body `waist_line` length); `shirt.width` v 1.05, range 1.0–1.3 (multiplier on body `bust`, i.e. ease); `shirt.flare` v 1.0, range 0.7–1.6 (hem width relative to chest); `shirt.strapless` false.
- `collar.f_collar` / `b_collar`: `CircleNeckHalf` (also `CurvyNeckHalf`, `VNeckHalf`, `SquareNeckHalf`, `TrapezoidNeckHalf`, `CircleArcNeckHalf`, `Bezier2NeckHalf`); `collar.width` v 0.2 (−0.5–1), `fc_depth` v 0.4 (0.3–2), `bc_depth` v 0 (0–2), `fc_angle`/`bc_angle` 95° (70–110), Bézier control points, `collar.component.style` null (options `Turtle`, `SimpleLapel`, `Hood2Panels`; no rib neckband component).
- `sleeve.sleeveless` false; `armhole_shape` `ArmholeCurve` (also `ArmholeSquare`, `ArmholeAngle`); `sleeve.length` v 0.3 (0.1–1.15, fraction of arm length); `connecting_width` v 0.2 (0–2); `end_width` v 1.0 (0.2–2); `sleeve_angle` 10° (10–50); `opening_dir_mix` 0.1; `standing_shoulder` false; `smoothing_coeff` 0.25; `cuff.type` null (`CuffBand`, `CuffSkirt`, `CuffBandSkirt`).
- `left.enable_asym` false (asymmetric left side off). Values are in cm, degrees or fractions per the docs [84].

`assets/garment_programs/tee.py` [49] builds `TorsoFrontHalfPanel` and `TorsoBackHalfPanel` as four-vertex half panels: width = `shirt.width × bust` split front/back by `back_width`; length = `shirt.length × waist_line` with a shoulder-inclination correction; interfaces `outside`, `inside`, `shoulder`, `bottom`, `shoulder_corner`, `collar_corner` are what sleeves and collars attach to. The repo's `collars.py`, `sleeves.py` and `bands.py` supply neckline shaping, set-in sleeves and bands (waistband/cuff style).

What M03 must add for a manufacturable tee: (1) a stretched ring component for the rib neckband with a length ratio and width parameter (not in GarmentCode); (2) seam allowances per edge (overlock 1.0–1.5 cm, hems 2.5–3 cm) and hem fold lines; (3) notches at shoulder points, centre front/back and sleeve cap; (4) stitch class and seam class per edge pair (ISO 4915/4916) for M06; (5) a size table driven by finished-measurement grade rules (F5) rather than only body measurements; (6) shrinkage compensation per material profile (M05). The MIT licence permits all of this.

### F7. Quality plan: AQL practice, defects, test methods, labelling

Table F7-A. Standards and regulations for the quality plan.

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 2859-1 Sampling procedures for inspection by attributes — AQL-indexed lot-by-lot schemes | 2026-01, Edition 3 (replaces 1999 edition) | Paid, CHF 227 | Current, just revised | Lot acceptance sampling for the human audit of each shift lot and for buyer inspection | https://www.iso.org/standard/85464.html |
| ANSI/ASQ Z1.4-2003 (R2018) Sampling procedures and tables for inspection by attributes | 2018 reaffirmation | Paid, USD 229 (ANSI PDF), USD 199 list (ASQ print) | Current US edition; same master tables | US buyers cite this | https://webstore.ansi.org/standards/asq/ansiasqz12003r2018 ; https://asq.org/quality-press/display-item?item=T1164 |
| ISO 6330:2021 Domestic washing and drying procedures for textile testing | 2021-11, Edition 4; 16 Type A (front-loader) procedures, 6 drying procedures | Paid, CHF 181 | Current | Wash/dry conditioning for dimensional change, appearance, seam and rib recovery checks | https://www.iso.org/standard/75934.html |
| ISO 3759:2011 Preparation, marking and measuring of fabric specimens and garments for dimensional change | 2011, Edition 5, confirmed 2022 | Paid | Current | Marking/measuring protocol before and after ISO 6330 | https://www.iso.org/standard/57309.html |
| ISO 5077:2007 Determination of dimensional change in washing and drying | 2007, Edition 2, confirmed 2022 | Paid, CHF 44 | Current | Reports shrinkage % after ISO 6330 | https://www.iso.org/standard/41877.html |
| AATCC TM135-2025 Dimensional changes of fabrics after home laundering (TM150 for garments, TM179 for skew) | 2025 | Paid (AATCC) | Current | US-market equivalent; TM150 covers finished garments; TM179 covers spirality | https://members.aatcc.org/store/tm135/543/ |
| ASTM D2594/D2594M-21 Stretch properties of knitted fabrics having low power | 2021 | Paid, USD 69 | Current | Fabric stretch and growth for rib and jersey (neckband recovery) | https://www.astm.org/d2594_d2594m-21.html |
| ASTM D1683/D1683M-22 Failure in sewn seams of woven fabrics | 2022 | Paid, USD 80 | Current; scope is woven fabrics | Seam strength and seam efficiency; applied to knit seams by agreement only (scope caveat) | https://www.astm.org/d1683_d1683m-22.html |
| ISO 13935-2:2026 Seam tensile properties — grab method | 2026-04, Edition 3 | Paid, CHF 100 | Current; woven scope, "can be applicable to fabrics produced by other techniques"; straight seams only | Seam rupture force on shoulder/side seam specimens | https://www.iso.org/standard/88344.html |
| ASTM D3776/D3776M-20 Mass per unit area of fabric | 2020 | Paid, USD 86 | Current | Incoming gsm verification of body and rib lots | https://www.astm.org/d3776_d3776m-20.html |
| ISO 3758:2023 Care labelling code using symbols | 2023 | Paid | Current | Care symbols in the order wash, bleach, dry, iron, professional care | https://www.iso.org/standard/74401.html |
| 16 CFR Part 423 Care labeling of textile wearing apparel (FTC) | current eCFR | Free | In force | US care instructions with a "reasonable basis"; ASTM D5489 symbols allowed in lieu of words | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-423 |
| 16 CFR Part 303 Textile Fiber Products Identification Act rules (FTC) | current eCFR | Free | In force | Fibre content, RN/company name, country of origin on the front of the label (§303.15) | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-303 ; https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-303/section-303.15 |
| Regulation (EU) No 1007/2011 textile fibre names and labelling | 2011, in force | Free | In force | Fibre names and % by weight in descending order; products may only be made available on the market if labelled | https://eur-lex.europa.eu/eli/reg/2011/1007/oj |

AQL practice. Apparel buyers normally specify AQL 2.5 for major defects and 4.0 for minor, critical = 0, at General Inspection Level II, single sampling, normal inspection [54] [87]. The master tables (ISO 2859-1 / ANSI Z1.4, reproduced by QC Advisor and AQF [53] [54]) give, for the lot sizes this cell will produce:

| Lot (shirts) | Level II code, n | AQL 2.5 Ac/Re | AQL 4.0 Ac/Re | AQL 1.0 Ac/Re | Level III code, n (new process) | AQL 2.5 Ac/Re at Level III |
|---|---|---|---|---|---|---|
| 51–90 | E, 13 | 0/1 | 1/2 | ↓ G n=32 0/1 | F, 20 | 1/2 |
| 91–150 (one 12-h shift at 100) | F, 20 | 1/2 | 2/3 | ↓ G n=32 0/1 | G, 32 | 2/3 |
| 151–280 (two shifts) | G, 32 | 2/3 | 3/4 | 0/1 | H, 50 | 3/4 |
| 281–500 (one week) | H, 50 | 3/4 | 5/6 | 1/2 | J, 80 | 5/6 |
| 501–1,200 | J, 80 | 5/6 | 7/8 | 2/3 | K, 125 | 7/8 |
| 1,201–3,200 | K, 125 | 7/8 | 10/11 | 3/4 | L, 200 | 10/11 |
| 3,201–10,000 | L, 200 | 10/11 | 14/15 | 5/6 | M, 315 | 14/15 |

Note: one inspection-company page (Tetra) states "L, n=200, AQL 2.5 → Ac 21 / Re 22"; that is the AQL 6.5 plan, and contradicts the master table and the same company's own K example (n=125, Ac 7 / Re 8) [87] [53]. Use the master table. The acceptance decision is on the lot; the cell's own 100% inline inspection is a separate control and does not replace the lot audit.

Common defects on knit tees, causes and where the cell detects them (A&E seam quality defects bulletin [55]; Coats and AMANN on puckering [56] [57]; Uçar 2002 on grinning [86]; ABC Seams 2026 defect guide [58]):

| Defect | Typical cause | Corrective action / detection station |
|---|---|---|
| Skipped stitches (looper misses the needle loop) | Wrong needle point/size, bent needle, thread too thick for eye, fabric flagging (plies lifting with the needle), timing | Light ball point Nm 70–80, correct thread, presser pressure, needle change interval (one source: ~8 h needle life); detect by stitch sensor / camera on seam at ST05/ST06; A&E: looper stitches unravel, so a skip is a seam failure |
| Seam failure / stitch cracking on stretch seams | Too few SPI, wrong stitch type (301 instead of 504/514), weak thread, unbalanced stitch | 14–16 st/3 cm, 504/514 with textured looper thread, balanced tensions; test by stretching seams at ST07 (tactile/force) and offline seam tests |
| Needle cutting / holes along the stitch line | Sharp point, oversize needle, dry fabric | Ball point, smaller needle, silicone needle cooler (MF-7900 has a silicone oil tank for needle tip) [71]; inspect at ST07 |
| Seam puckering (feed, tension, displacement, differential shrinkage) | Plies fed unevenly; thread stretched by tension then relaxing; thread too thick for the knit; thread/fabric shrink differently in wash | Differential feed 1:0.9–1:1.8 (MF-7900), lowest workable tension, Tex 24/30 corespun, ISO 6330 wash trial; camera at ST07 (pucker grade), A&E grade 1–5 scale |
| Seam grin (stitch too loose; seam opens under load) | Low stitch density, extensible thread, rigid fabric, loose looper tension | Raise stitch density, balance tension; 514 grins less than 504 for a given tension; load-and-look check at ST07 |
| Excessive restitched seams / splices | Thread breaks, thread run-out | Thread-break sensors, cone-level monitoring (WP: supplies monitored); reject or rework |
| Uneven hem width, twisted hem, hem wave | Guide/trimmer misaligned, overfeed wrong on the cylinder bed | Left-hand fabric trimmer (H22/H23), fixed guide, differential set per fabric; camera measure hem width at ST07 |
| Twisted or off-centre rib band, band join not at centre back, caught body layer, neckline waviness, rib standing away | Wrong ratio or uneven stretch distribution; loop twisted on loading; layer control lost | ST06 cameras and contact checks before sewing; symmetry check after release (WP requirement); ratio from F5 verified on the physical sample and after wash |
| Spirality (side seams twisting after wash) | Yarn twist/knitting imbalance in the fabric | Fabric spec: spirality ≤ 5% [12]; AATCC TM179 at material qualification |
| Oil stains | Lubricated machine heads | Dry-head / semi-dry-head machines (JUKI MF-7900D) [71]; camera at ST07 |
| Open seams / unravelled chain | Chain cut too short, no back-tack on chain stitches | Chain-off length control, latch-back or tack where required |

Labelling for the tee: a main (brand/size) label at the inside back neck, sewn with 301 under the back-neck tape; a care/content label at the wearer's left side seam about 10 cm above the hem [1]. US content: fibre content (generic names, % by weight), manufacturer/importer identity (name or RN), country of origin on the front of the label [66] [67]; care instructions per 16 CFR 423 with a reasonable basis (wash testing or industry evidence) [65]; EU: fibre names/percentages per Regulation 1007/2011 in the language of the market [68]; care symbols per ISO 3758:2023 [69] (GINETEX symbols are trademarked in some markets; licensing not researched here). Size designation per ISO 8559-2:2025 where exported [39].

### F8. Sewing machine application data relevant to the tee (prices: see R04)

| Vendor | Model / part number | Key specs | Price (currency, date, basis) | Lead time | CAD available? | Source URL |
|---|---|---|---|---|---|---|
| JUKI | MF-7900 / MF-7900D series cylinder-bed top-and-bottom coverstitch; subclasses U11 universal, H22 (light) / H23 (medium) hemming with left-hand fabric trimmer, H24/H25 extra light, E11 elastic; MF-7900DRH24 digital top feed | ISO 406/407/602/605; max 6,500 st/min (U11), 5,000–6,000 on hemming subclasses; stitch length 0.9–3.6 mm; differential 1:0.9–1:1.8 (1:0.6–1:1.1 by link change) with micro-adjustment; needle gauge 3.2/4.0/4.8 mm (2-needle), 5.6/6.4 mm (3-needle); presser lift 5 mm (8 mm bottom-cover); needle UY128GAS #9–#12; head 41–51 kg; single-phase 100–240 V, 500 VA with trimmer; air 0.5 MPa; silicone needle cooler; "best suited to hemming of sleeves and bottoms of T-shirts" | Not published; request quote (R04) | Stock at JUKI distributors | Not published by JUKI; 2D drawings in instruction manual; ask distributor for STEP | https://www.juki.co.jp/industrial_j/download_j/manual_j/mf7900/menu/mf_7900/pdf/instruction_eg.pdf ; https://www.juki.co.jp/industrial_e/admin/pdata/filedata/363/mf7900.pdf ; https://juki.com/mf-7900-h22-series ; https://www.juki.co.jp/industrial_e/products_e/apparel_e/cover_e/detail.php?cd=MF-7900D_H24_H25_E |
| JUKI (JTRON) | JTR-MF7923/BHA bottom hemming automat (MF7923DH23/DH25 head, servo edge trimmer, stacker) | Capacity 2,400–3,000 pcs per 9 h with one operator and one machine, 4,500–5,000 pcs per 9 h with one operator and two machines; air 0.45–0.7 MPa, 23 L/min; reseller: ~1,500 tees per 8 h, hem width 17–30 mm, up to 5,000 st/min, hemmed tube diameter 40–70 cm, start/finish at side seam, thread-break sensor, counter, 230 V | Not published; request quote | — | No | https://www.juki.co.jp/industrial_j/download_j/manual_j/jtr_mf7923bha/menu/pdf/instruction_eg.pdf ; https://impall.eu/product/j-tron-jtr-mf7923-bha/ |
| Pegasus | M952-A-52 (M900neo), 2-needle 4-thread overlock, bottom feed; M952-A-13 variant with tape-attaching presser foot | 7,000 st/min; needle space 2 mm; overedge width 4 mm; light to medium fabrics; push-button stitch length; lever differential; fully automatic lubrication | Not published; request quote | — | No | https://www.pegasus.co.jp/en/machine/detail/series/s106/M952-A-52 ; https://www.pegasus.co.jp/en/machine/detail/option/TK/M952-A-13 |
| JUKI | MO-6700DA series overlock / safety stitch | Stitch length 0.8–4 mm (1.5–4 mm on some subclasses), push-button adjustment | Not published; request quote | — | No | https://www.juki.co.jp/industrial_e/products_e/apparel_e/overlock_e/detail.php?cd=MO-6700DA_E |
| JUKI with Pegasus | M900/DJ overlock developed in alliance with Pegasus | JUKI control on Pegasus stitch-forming mechanism | Not published | — | No | https://www.juki.co.jp/en/business/industrial |

### F9. Takt-time budget per station implied by 100 shirts per 12-hour shift

Arithmetic (white paper §Output arithmetic, reproduced and extended):
- Shift H = 12 h = 720 min. Gross average interval for 100 accepted shirts = 720 / 100 = 7.20 min = 7 min 12 s.
- With the white paper's factors, availability A = 0.80 and acceptable yield Y = 0.95: running completion interval c = H × A × Y / G = 720 × 0.80 × 0.95 / 100 = 5.472 min = 5 min 28 s per attempt. Equivalent: 100 / 0.95 = 105.3 attempts in 576 productive minutes.
- For the higher scenarios: 200 shirts → c = 2.74 min; 300 → 1.82 min; 500 → 1.09 min (same formula; matches the white paper's table to the second).
- Rule from the white paper: for every resource, total active occupancy per garment (including repeated visits, load/unload and setup) divided by the number of parallel copies must be ≤ c. The largest such occupancy is a lower bound on c.
- Consequence: the human SAM for a tee (6.5–8.5 min, F1) exceeds c = 5.47 min. A single manipulator reproducing all human handling at human speed cannot meet the base target; the cell must either pipeline (several shirts in process at once, each station ≤ 5.47 min) and keep the shared manipulator's per-shirt occupancy under 5.47 min, or add station-local loading automation. Lead time per shirt may be 15–25 min while the output interval is 5.47 min.

Table F9-A. Budget allocation per station (minutes per shirt; "est. occupancy" is this report's engineering estimate from seam lengths, machine speeds and assumed handling times, labelled est.; "budget" is the proposed design limit leaving ~15–20% reserve against c = 5.47).

| Station | Work content per shirt | Est. occupancy (min) | Budget (min) | Basis and notes |
|---|---|---|---|---|
| ST01 Roll handling, unwind, edge guide, feed | Advance ≈ 0.75 m of 180 cm open-width fabric per shirt (1.15 m² ÷ 0.85 ÷ 1.80 m); relaxation done offline 24 h [21][22] or 6–8 h steam [20] | 0.2–0.5 | 0.5 | Overlaps cutting; roll change (every ~55–65 shirts at 20–25 kg rolls, est.) must fit in the A = 0.80 allowance |
| ST02 Single-ply knife cutting, piece ID | Cut perimeter ≈ 9 m per shirt (front ≈ 2.8 m, back ≈ 2.8 m, two sleeves ≈ 2.4 m, rib strip ≈ 1.0 m, est.); at 0.3–0.5 m/s effective plus registration and conveyor index | 0.8–1.2 | 1.5 | Cutter speed data in R02; the number is an estimate |
| ST03 Extraction and buffer | 5 piece pick-ups at 10–15 s plus scrap skeleton removal 15–30 s | 1.1–1.8 | 2.0 | Separate from the ST04 arm if ST04 is the bottleneck |
| ST04 Manipulation (shared gantry/arm) | Transfers and alignments: front+back to shoulder station (≈40 s), body to collar (≈20 s), rib strip to ST06 (≈15 s), two sleeves placed and aligned (≈80 s), body to side-seam station with two fold/align cycles (≈50 s), hem loading (≈65 s), to finishing (≈15 s) | ≈4.8 (est.) | 4.5 | Bottleneck candidate with ST06. Reduce by flat-hemming sleeves before set-in (saves two tubular loads), by station-local fixtures that self-load hems (cf. JTR-MF7923/BHA at 0.18–0.22 min per hem with human loading [73]), or by a second arm |
| ST05 Overlock head (504/514) | Seam length ≈ 2.9 m (shoulders 0.32 m with tape, sleeves 1.0 m, sides+underarm 1.54 m; rib attach 0.5 m counted at ST06); at 2.0 mm stitch and 3,500 st/min effective ≈ 0.4 min needle time, ×3 for curves, starts, chain-off ≈ 1.3 min, plus 4 load/unload cycles ≈ 1.3 min | ≈2.6 | 3.5 | Rated speeds 6,000–7,000 st/min [98][76]; effective speed on curves is far lower |
| ST05 Coverstitch head (406/602) | Hems ≈ 1.94 m (two sleeve openings 2 × 0.42 m, bottom 1.10 m); ≈0.3 min needle time at 3,000 st/min effective, ×2.5 for tubular loading and overlap ≈ 0.8 min, plus 3 loads ≈ 1.25 min | ≈2.1 | 3.0 | MF-7900 hemming subclass data [70][71] |
| ST05 Lockstitch head (301) | Rib ends join 0.07 m, main label 0.08 m, care label 0.06 m; ≈0.25 min sewing plus 3 loads | ≈1.0 | 1.5 | Could be merged into ST06 (rib ends) and ST07 (labels) |
| ST06 Collar module (rib attach with split support and differential feed) | Cut/receive strip, join ends, fold, form loop, present with quartering, sew 0.5 m at reduced speed, back-neck tape/topstitch 0.55 m, release and check | ≈2.3 (est.) ; white paper illustration 5.0 | 5.0 | Single module acceptable only if measured occupancy ≤ 5.0; the white paper shows that a 5-min module caps the cell at ~109 shirts, and two modules at ~219 |
| ST07 Finishing, inspection, output | Thread trim (auto-trimmers reduce), turn if needed, camera inspection and measurement, fold, bag, label | ≈1.3 | 2.0 | Inspection time depends on the vision plan (R10/R11) |
| ST08 Optional decoration | Not in the base takt; DTG print and cure alone is 2–4 min per shirt (est.) | — | 0 in base | Needs its own parallel path if included |
| Sum (lead time if sequential) | | ≈16–18 min | | Output interval 5.47 min requires ~3–4 shirts in process concurrently |

Checks against the targets: every single-station estimate is below 5.47 min, so 100 shirts/shift is arithmetically feasible with pipelining, with ST04 (≈4.8 min, est.) and ST06 (unmeasured) as the two resources to measure first. For 200 shirts/shift (c = 2.74) ST04, ST05-overlock and ST06 all exceed c, so that scenario needs at least two manipulators, two overlock paths and two collar modules, as the white paper already anticipates. For 300 (c = 1.82) nearly every station must be duplicated or redesigned.

Yield sensitivity: at Y = 0.90 instead of 0.95, c = 5.18 min; at A = 0.70, c = 4.79 min. The budget column leaves ~15–20% headroom so that these cases remain feasible for all stations except ST04/ST06 at their estimates.

