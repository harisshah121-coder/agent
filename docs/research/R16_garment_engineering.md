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

