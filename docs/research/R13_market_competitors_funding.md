# R13 · Market, competitors, funding comps

Research agent R13 · Roll-to-Garment project · snapshot date 2026-10-21. Sources are numbered in `## Sources`; inline citations use `[n]`. Prices carry currency, date seen and basis. Anything not confirmed by a source is marked "unverified".

<!-- SUMMARY_PLACEHOLDER -->

## Findings

Table convention: the common brief's hardware/software columns do not fit companies and markets, so competitor and comps tables use `Company | Approach | Status (date) | Funding (currency, date, basis) | Lessons / relevance | Source`. Every numeric claim cites a numbered source; "est." marks an order-of-magnitude estimate with its basis; "unverified" marks what no source confirmed.

### F1. Direct competitors: automated sewn-garment assembly

| Company (HQ, founded) | Approach | Status (as of 2026-10) | Funding (currency, date, basis) | Lessons / relevance to this project | Source |
|---|---|---|---|---|---|
| SoftWear Automation (Austell/Atlanta GA, 2012) | SEWBOT® machine-vision worklines; LOWRY line for T-shirts (cut panels in, finished tee out); sells "T-shirt supply chain service" and worklines; DARPA and Walmart Foundation R&D history | Closed $20M Series B1 on 2025-08-11 led by BESTSELLER's Invest FWD (CTW Venture Partners, SRI Capital, MacDonald Ventures participated); BESTSELLER CFO joined board; company says it is in "rapid progress towards commercialization"; ~52 employees (Tracxn) | USD 20.0M Series B1, Aug 2025 (press release); total disclosed USD 45.6M (Tracxn, 2026) vs USD 65.6M across 5 rounds incl. Lear Corp (The Company Check) — totals conflict; earlier USD 4.5M from CTW (WWD, undated) | 13 years and >$45M to reach a strategic-led B1; the only direct precedent for a vision-guided T-shirt workline; its buyer model (brand-led, nearshoring) is the same demand thesis as ours; its scale is factory worklines, not a $100k cell | [1][2][3][4][5] |
| SoftWear × Tianyuan Garments (Little Rock AR) | 2017 deal: 21 fully automated LOWRY T-shirt lines for Adidas, 330 robots, USD 20M plant, "one T-shirt every 22 s", "800,000 T-shirts/day", labour cost USD 0.33/shirt, lines "fully operational by end of 2018" | Plant opened May 2019 as a renovated facility with 160 employees sewing manually, investment raised to USD 30M, peak plan "more than four million garments annually", and the state release still described the automated line as "in development"; pandemic pivot reported May 2020; no 2021–2026 status found (unverified whether automated lines ever ran at scale) | n/a (customer project; USD 20M→30M plant investment, press) | The best-known cautionary tale: announced throughput (23M/yr robot output) vs delivered reality (manual sewing, 4M/yr plan). Investors will ask why our 100 tees/shift target is credible when a 21-line plant did not publicly deliver; our answer must be a demonstrated run, not a press claim | [6][7][8][72][73][74][75] |
| Sewbo (Seattle WA, 2014/15) | Temporarily stiffens fabric with water-soluble PVA so off-the-shelf industrial robots can handle it; stiffener rinsed out after sewing | Unfunded per Tracxn (3 employees); focused on blue jeans; ARM Institute projects with Siemens, Bluewater Defense, UC Berkeley (2019–2021, TRL raised to 8–9 via NIST RACER mask microfactory); Apr 2026: planning with a Los Angeles partner factory and "starting to fundraise"; technology not for sale | No disclosed equity (Tracxn "unfunded"); DoD/ARM Institute project funding (amounts not published) | 10 years without a commercial product shows how long the "handle limp fabric" problem resists a one-trick solution; its route adds a wet treatment that the white paper's untreated-textile baseline excludes | [9][10][11][12] |
| Silana (Vienna, 2022; NY office) | Robot cells per step "from fabric roll to printed T-shirt"; claims 90% automation, 82% cost reduction, one worker per ten machines, "Made in USA/Europe at lower cost than Made in China" | Seed round closed May 2024; said first machine deliveries would come in 2025 (Löffler named as paying customer with down payment; "nearly 200 machines pre-ordered", 30M tees/yr); Seed VC-II Dec 2024 and StartX accelerator Sep 2025 (CB Insights); PitchBook lists latest seed deal USD 5.53M (not corroborated elsewhere); 15 employees; no public confirmation of a delivered machine found as of 2026-10 (unverified) | EUR 1.5M seed, May 2024, led by SOSV/HAX with OÖ HightechFonds, Material V, angels (press); ~EUR 0.7M prior Austrian grants (aws, Wirtschaftsagentur Wien, FFG, founder interview); USD 5.53M latest seed (PitchBook, unverified) | Closest architecture to ours (roll-to-tee, cells per step, T-shirt first, polos next); shows that a EUR 1.5M seed buys a prototype plus pre-orders but not deliveries within 18 months; a HAX/SOSV-backed comp for our own seed | [13][14][15][16][17] |
| sewts (Munich, 2019) | AI + material simulation for deformable handling; VELUM cell feeds crumpled towels into folders (up to 700 items/h); e-commerce returns prototype with Otto Group; garment production is stated long-term vision | Series A Aug 2023; no 2025–2026 round found (see F1 note below) | EUR 7.0M Series A, Aug 2023, led by Emerald Technology Ventures with CNB Capital, EquityPitcher, Nabtesco; existing Bayern Kapital, APEX, HTGF; total ~USD 7.7M (CB Insights) | Investors backed "physical AI for textiles" via a narrow laundry niche first; the same "beachhead then moonshot" sequencing is what a seed memo for our cell should show | [18][19] |
| CreateMe Technologies (Newark CA, 2018; CEO Cam Myers) | MeRA™ modular robotic assembly + Pixel™ micro-adhesive bonded seams (<1 mm) instead of thread; Thermo(re)set reversible adhesive; >95 patents; "Physical AI" | Launched MeRA/Pixel 2025-09-11 with first commercial product in women's intimates, T-shirts "in the near future"; claims up to 250 garments/h, 20× speed, 2× precision vs manual sewing, "cost-competitive with offshore"; Dec 2025 promoted a chief engineer/head of manufacturing "toward full-scale manufacturing"; Jun 2026 "Seed to System" partnership with Avalo and Laguna Fabrics (US cotton to garment); PitchBook: later-stage VC, 48 employees, 3 investors | Amounts not disclosed (PitchBook "Later Stage VC"; Tracxn shows no disclosed rounds); grant Mar 2021 (PitchBook) | The best-funded "mechanics + learned control" rival; bonding sidesteps thread handling, so it cannot claim conventional stitched construction, which is our differentiator; its 250/h claim is per platform, not per $100k cell | [20][21][22][23][24][25] |
| Resonance Companies / CreateONE (New York + Santiago DR, 2015) | Software "operating system" that compiles design intent into production instructions for a network of compliant factories (own DR plant); sell-then-make; CreateOne Pro USD 100/month + 10% revenue share | Rounds 2015 (USD 15M seed), 2018 (USD 8M), 2020 (USD 22.5M), May 2025 (USD 3.3M); CB Insights lists latest instrument as debt; ~60 employees; estimated revenue ~USD 19.6M (Tracxn est.) | USD 33.8M total disclosed (Tracxn/CB Insights) vs USD 48.8M (Caplight) — conflicting; USD 3.32M May 2025 (Preqin) | Design-to-production software plus conventional factories, not an autonomous cell; its 2025 raise was small after a USD 22.5M 2020 round, a sign that "on-demand platform" stories need manufacturing economics to hold | [26][27][28] |
| unspun (Emeryville CA) | Vega™ (renamed OneWeave™ in 2026) 3D-weaving machine: yarn to woven pant legs in ~10–20 min, licensed to manufacturers; Walmart agreement for 350 machines; target 350+ machines / 10M garments per year in North America by 2030 | Series A USD 14M (Jun 2023, Lowercarbon lead); Series B USD 32M (Jul 2024, DCVC lead; Lowercarbon, E12, Decathlon, SOSV); Series B-II/B3 USD 14.4M (Aug 2026, Lowercarbon); total ~USD 69.7M (CB Insights); 74 employees (PitchBook) | As stated; basis: press releases and databases | Proof that climate and deep-tech funds will finance garment-making machines when a large retailer signs a machine-count contract; licensing of machines (not selling factories) is a model to study; woven pants, not knit tees, so not a direct product competitor | [29][30][31][32][33] |

Note on sewts: no 2025–2026 funding or product announcement was found in three searches; status after the 2023 Series A is unverified.

### F2. Adjacent and large-company automation

| Company / programme | Approach | Status (as of 2026-10) | Funding or scale (currency, date, basis) | Lessons / relevance | Source |
|---|---|---|---|---|---|
| Inditex (Zara) | Proximity sourcing: sewing factories in Spain (37), Portugal (207), Morocco (334), Türkiye (606) per 2025 supply-chain KPIs; EUR 1.8B ordinary capex 2025; invested in Theker (Barcelona) for AI robots that handle and fold garments | Theker closed EUR 18M / USD 21M seed Jul 2025 led by Kibo Ventures with Inditex as strategic; a EUR 74M follow-on in Jun 2026 backed by Inditex and LVMH is reported by a secondary source (unverified) | Theker EUR 18M seed (press, Jul 2025); EUR 74M (secondary, Jun 2026, unverified) | Inditex is buying garment-handling AI, not sewing cells; nearshore clusters already exist for our target buyers (small contract manufacturers in proximity markets) | [34][35][36][37][38] |
| Levi Strauss Project F.L.X. (2018) | Laser finishing (Jeanologia) replaced manual hand-finishing of jeans; digitised finish design | Announced Feb 2018; retraining of finishing technicians; no 2025–2026 public update found (possibly stale) | n/a (internal programme) | Automation won where the operation was a surface process on a finished garment, not fabric handling | [39] |
| Nike × Flex (Guadalajara, 2015–2018) | Electronics-style automated footwear lines | Wound down by 2018-12-31 (Flex 8-K); 2025 retrospective: robots "struggled to handle the soft, squishy and stretchy parts", staff swelled to ~5,000, costlier than Vietnam | Losses written down (Flex 8-K, Oct 2018) | The canonical soft-goods failure: automation that could not handle compliant materials became a manual plant with higher cost than Asia | [40][41] |
| Grabit (electroadhesion grippers for Nike uppers) | Electroadhesive flat-material handling | Entered restructuring support agreement with lender Burke Porter Group Dec 2019 after project delays; no later activity found (unverified) | n/a | A gripper-only company could not survive on soft-goods demand alone; our gripper toolbox must stay a component, not the business | [42] |
| Amazon (on-demand apparel) | US 9,623,578 B1 "On demand apparel manufacturing" (filed 2015-12-16, granted 2017-04-18): textile printer + cutter + assembly line + order aggregation with camera feedback on cutting | Patent in force (expires ~2035, est. from filing date); Amazon ran a Kornit-based print facility in Norristown PA (2017); no evidence found of Amazon automating sewing | n/a | Prior art to check for our M04/M07 order-aggregation and vision-corrected cutting claims; shows the hyperscaler route is print-on-blank, not cut-and-sew automation | [43][44] |

### F3. Print-on-demand, decoration and equipment vendors (adjacent routes to "small orders")

| Company | Approach | Status (as of 2026-10) | Scale / price (currency, date, basis) | Lessons / relevance | Source |
|---|---|---|---|---|---|
| Printful + Printify (merged) | POD on sourced blanks; Printful in-house plants, Printify network of 85+ print houses in 117 locations | Merger announced 2024-11-05, completed 2024-11-20 as equal partners, brands kept separate; Printful fulfils >1M items/month, 147M items since 2013; Printify >60M orders | Printful raised USD 130M in 2021 at >USD 1B valuation; Printify USD 54.1M (tech.eu); Printify ~USD 103M revenue (PPAI, 2024); Bella+Canvas 3001 unisex tee from USD 11.92 incl. one print on Printful (seen 2026-10-21, list, varies); Printful's cheapest black tee USD 8.17 vs Gelato USD 12.47 (Printful comparison page, 2026) | POD already delivers no-MOQ tees at ~USD 8–12 landed cost per decorated unit; our cell's value must come from construction choice (fabric, fit, seams) and ex-factory cost, not from "small orders" alone | [45][46][47][48][50][51] |
| Gelato (Oslo) | POD network with local production hubs | USD 240M Series D Aug 2021 at USD 1B valuation; third-party revenue estimates only | Total raised USD 269M (GetLatka, est.) | POD unicorns were funded on network software, not machines | [49] |
| Kornit Digital (NASDAQ: KRNT), Apollo DTG platform | Industrial direct-to-garment printer with automation modules | FY2025 revenue USD 208.2M vs 203.8M (FY2024); ARR from All-Inclusive-Click (AIC) usage model ~USD 25M at end 2025, USD 33.8M at Q2 2026; >40% of Apollo customers added a second system in 2025; acquired PrintFactory; Q1 2026 revenue USD 48.5M | Apollo: up to 400 impressions/h (350–400 for prints ≤12.4 in wide), one operator, total cost of ownership USD 0.9–1.3 per standard print, >1.5M prints/yr capacity, ROI 12–18 months above 700k impressions/yr (vendor page); system price not published; request quote | Kornit's AIC usage model (pay per impression, ARR) is the pricing precedent for our software/service package; Apollo is the natural ST08 decoration partner, not a competitor | [52][53][54][55] |
| JUKI (Tokyo) | World top share in industrial sewing machines; "smart factory" with pattern seamers (PS-800), automats, JaNets networking; shirt-factory case: operators 1,227→586, output 11,680→14,400 shirts/day, ROI 1.9 years | 2025 integrated report: results fell short of targets on slow capital investment; launched DX-01 lockstitch Jun 2025 | Automat prices not published (request quote); JTR-MF7923/BHA bottom hemmer cited in white paper | Incumbents sell deskilling automats station by station; our ST05 heads should be JUKI-class machines, and JUKI is a channel/partner risk and opportunity | [56][57][58][59] |
| Brother Industries | NEXIO industrial platform; BAS-341K/342K programmable pattern sewers (May 2026); acquired Konrad Busche automotive division Nov 2025 | Active | Prices not published | Same as JUKI; programmable pattern sewers are the closest "fixture-based" automation to our collar module | [59] |
| Jack Technology (Taizhou, 603337.SH) | Claims largest sewing-equipment production and sales volume globally; owns Bullmer/Topcut cutters (2009), MAICA shirt automats (2017), ViBeMac jeans automats (2018); integrates cutting, hanging, sewing, sorting | Active; revenue est. USD 500M–1B (Similarweb est.) | Prices not published; Chinese template/CNC sewing units list at USD 7,888–15,000 on marketplaces (reseller listings, 2026) | Low-cost template sewing from China sets the price anchor for "automation" in buyers' minds; a $100k cell must do what template machines cannot (no per-style templates) | [60][62] |
| Richpeace (Tianjin) | CNC template sewing machines RPAS-LM-C-1 (800×450 to 1300×900 mm beds, 3,500 rpm, 1-phase 220 V) and automatic sewing lines for home textiles and garments | Active; exhibiting ITMA Asia 2026 | Price not published; request quote | Template sewing is proven for pockets, plackets, cuffs; it is the mature alternative for ST06 collar attach if free-form handling fails | [61] |
| Bluewater Defense (Puerto Rico) | DoD uniform maker; host of ARM Institute robotic sewing demos (pocket flaps for military trousers with Siemens/Sewbo) | Demonstration met quality requirements but cycle time was higher than human operators (2020); later projects moved to masks and jeans | DoD/ARM project funding (amounts not published) | Berry-Amendment uniform makers are willing hosts for automation pilots; a credible early design partner segment | [12][63] |
| Shima Seiki WHOLEGARMENT® (Wakayama) | Knit-to-shape: whole garment from yarn, no cutting or sewing; MACH2XS four-bed with movable sinkers (40 in width); first machine (1995) knit a garment in ~30 min | FY to Mar 2025 net sales JPY 23,229M (−10.3% YoY) on lower WHOLEGARMENT and shaping-machine unit sales | New-machine price not published (request quote); used MACH2XS 153 (2019) listed at USD 25,000 (Made-in-China reseller, 2026) | The real "alternative route" to a seamless tee; slow per garment and gauge-limited, so it complements rather than replaces cut-and-sew jersey tees | [64][65][66] |
| Lectra (Paris) | Single-ply cutting (Virga), SaaS PLM/MES, "Fashion On Demand" bundle (2018) | 2025 revenue EUR 506.7M, EBITDA EUR 79.7M (15.7%), recurring 75% of revenue; Q1 2026 equipment orders −25% YoY; Empower Fashion uptime-guarantee contracts launched Sep 2025; no 2025–2026 "Fashion On Demand" update found | Virga price not published (request quote) | Lectra is the cutting incumbent for ST02 and its uptime-guarantee contract model is a precedent for our service package | [67][68][69] |
| Tukatech (Los Angeles) | TUKAcad/TUKA3D/TUKAcut; claims first apparel microfactory for on-demand (2012); TUKAcut customer cites 50–70k units/day with crew cut from 90 to 14 | Active; TUKAcad 2026 subscription | Prices not published | Pattern/3D software partner or M03 alternative; microfactory claim is marketing, not a product | [70][71] |

### F4. New entrants 2025–2026 (sewing or garment handling)

| Company | Approach | Status | Funding | Source |
|---|---|---|---|---|
| Theker Robotics (Barcelona) | AI vision + control on industrial arms for garment handling/folding; RaaS model; Inditex partner | EUR 18M seed Jul 2025 (largest Spanish seed); EUR 74M Jun 2026 reported (unverified) | EUR 18M (press); EUR 74M (secondary) | [35][36][37] |
| Apparel Robotics Corporation | Listed by Caplight as an 81% comparable to CreateMe; no primary source found | unverified | unverified | [22] |

No other 2025–2026 sewing-automation seed or Series A announcements were found in three searches; the sector's 2025–2026 capital went to SoftWear (B1), unspun (B-II), Theker and CreateMe (undisclosed).

### F5. Funding comps: physical AI and robotics rounds, 2025–2026

| Company (HQ) | What it does | Round | Amount and valuation (currency, date, basis) | Lead / notable investors | Relevance as a comp | Source |
|---|---|---|---|---|---|---|
| Genesis AI (Palo Alto + Paris) | Universal robotics foundation model built on its own physics simulator; targeted customer deployments planned by end 2026 | Seed | USD 105M seed, 2025-07-01 (press release) | Co-led by Eclipse and Khosla Ventures; Bpifrance, HSG, Eric Schmidt, Xavier Niel | Shows "seed" now spans two orders of magnitude; a foundation-model seed is not a comp for a cell builder except to show investor appetite for physical AI | [76][77] |
| mimic robotics (Zurich) | Humanoid hands trained by imitation learning for dexterous manufacturing/logistics tasks | Seed | USD 16M, 2025-11-03; total >USD 20M (press release) | Elaia lead; Speedinvest; Founderful, 10X Founders, Sequoia Scout | European dexterous-manipulation seed; closest in size to a well-funded seed for a manipulation-heavy cell | [78] |
| Sereact (Stuttgart) | Physical AI "Cortex" for picking robots; 200+ systems live; 1B+ picks | Series A → Series B | EUR 25M Series A, 2025-01-20; USD 110M Series B, 2026-04-27; >USD 140M total (company posts) | Creandum (A); Headline (B); Bullhound, Daphni, Felix, Air Street, Point Nine | Series A came with deployed systems and production picks, i.e. the bar for an A is fleet data, not a demo | [79][80] |
| Mytra (Brisbane CA) | 3D warehouse storage/retrieval robots | Series C | USD 120M, 2026-01-15; >USD 200M total; USD 78M through Series B (press release) | Avenir Growth lead; Eclipse, Greenoaks; Lineage, RyderVentures strategic | A 2022 start reaching C in four years on a few large deployments (one "60× largest prior installation" in 2025) | [84] |
| Formic (Chicago) | Robotics-as-a-service for SME factories (pay per hour) | Series A (+ debt) | USD 27.4M Series A, 2024-06-25; latest valuation USD 100M; USD 159M total disclosed incl. facilities (Tracxn) | n/a in excerpt | The RaaS financing structure (equipment debt + equity) is the model if we lease cells to small manufacturers | [81] |
| Chef Robotics (San Francisco) | AI robot arms for food assembly; 44M+ servings | Series A (+ equipment debt) | USD 43.1M, 2025-03-31 = USD 20.6M equity + USD 22.5M equipment financing (SVB); USD 65.6M total (press release) | Avataar Ventures lead; Construct, Bloomberg Beta, Promus, HCVC, MaC | Best single structural comp: deformable-material manipulation, RaaS, equity plus equipment debt so customers avoid capex | [82] |
| Dexterity (Redwood City) | AI manipulation for logistics ("Mech" superhumanoid) | Series B | USD 104.9M, 2026-05-21 at USD 1.7B (Tracxn); USD 1.65B valuation Mar 2025 (Bloomberg); USD 396M total (Tracxn) | n/a in excerpts | Late-stage manipulation comp; shows valuation ceilings investors underwrite for manipulation | [85][86] |
| Physical Intelligence (San Francisco) | Robot foundation models (π0 family) | Series B | USD 600M at USD 5.6B post, Nov 2025 (Sacra); prior USD 400M at USD 2.4B Nov 2024 | CapitalG lead; Jeff Bezos, Thrive | Signals that generalist manipulation policies are being funded as platforms we might license rather than build (M08/M11 build-vs-buy) | [83][77] |
| Dyna Robotics (Redwood City) | Dexterous manipulation foundation models incl. napkin/towel folding demos | Series A | Series A dated 2025-09-15 (Tracxn); amount not shown in excerpt (unverified) | n/a | Textile-folding demos make it the most relevant foundation-model startup for ST03/ST04 skills | [90] |
| Field AI (Irvine) | Risk-aware foundation models for robots in industrial sites | Two rounds | USD 405M across two rounds announced 2025-08-20; USD 314M August round; valuation ~USD 2B (CNBC, person familiar) | Bezos Expeditions, Prysm, Temasek (co-leads); Khosla, NVentures, Canaan | Scale of capital flowing to embodied AI in 2025 | [87][88][89] |
| Skild AI (Pittsburgh) | General robot brain | Series B (2025) | Valued at USD 4B in early 2025 (TechCrunch); later rounds not confirmed here (unverified) | n/a | Same as above | [77] |
| Theker (Barcelona) | Garment handling/folding robots for Inditex | Seed | EUR 18M / USD 21M, Jul 2025 (press); EUR 74M Jun 2026 (secondary, unverified) | Kibo Ventures lead; Kfund; Inditex strategic | The one 2025–2026 apparel-handling round; strategic-led, RaaS | [35][36][37] |
| SoftWear Automation (Atlanta) | Sewn-goods worklines | Series B1 | USD 20M, Aug 2025 | BESTSELLER (Invest FWD) lead | Strategic (brand) capital is what financed the sewing-automation incumbent in 2025 | [1] |
| unspun (Emeryville) | Yarn-to-garment weaving machines | Series B-II/B3 | USD 14.4M, Aug 2026; USD 32M B Jul 2024 at DCVC lead | Lowercarbon; DCVC; Decathlon; SOSV | Climate funds finance garment machines with retailer contracts | [29][30] |
| Silana (Vienna) | Roll-to-tee sewing cells | Seed | EUR 1.5M May 2024 (+ possible USD 5.53M seed per PitchBook, unverified) | SOSV/HAX; OÖ HightechFonds | Direct seed comp: EUR 1.5M bought prototype + pre-orders, not deliveries | [13][15] |

### F6. Typical seed terms, 2025–2026

| Metric | Value | Basis | Source |
|---|---|---|---|
| Median US seed round (Carta) | USD 4.5M raised at USD 23.9M post-money; median seed dilution 19.4% | Carta fundraising benchmarks, Q2 2026 | [91] |
| Median seed post-money (Carta, Q4 2025) | USD 24M (record), vs USD 18M a year earlier; Series A post USD 78.7M; dilution 19–20% at seed and A | Secondary compilation citing Carta "Record seed and Series A valuations" (2026) | [94] |
| Seed pre-money distribution (PitchBook) | Series median ~USD 15M pre-money in 2025; top-decile "consensus" rounds ~USD 40M pre; investor ownership ~20% (top decile) vs ~25% typical | PitchBook analyst note, Nov 2025 | [93] |
| Instrument | ~64% of seed rounds on Carta were SAFEs, 27% priced, ~10% notes (Q4 2023–Q3 2024); post-money SAFE with cap and no discount is the pre-seed standard | Carta | [91][92] |
| Pre-seed caps | Median post-money SAFE cap ~USD 10M for USD 250k–1M raises and ~USD 15M for USD 1–2.5M raises (2025) | Carta State of Pre-Seed 2025 | [92] |
| Pre-seed volume and sector mix | USD 10.4B across 50,316 SAFEs/notes in 2025 (−1% cash, −13% count YoY); hardware was the second-largest industry by pre-seed cash in 2025 (up from third in 2024) | Carta | [92] |
| Graduation to Series A | 25–30% of seed companies reached A within 24 months in a typical year (2018); ~17% for the 2022 seed cohort | Carta via secondary compilation | [94] |
| Hardware/robotics check sizes (first institutional) | SOSV: ~60 pre-seed investments/yr up to USD 550k each; HAX sweet spot USD 250k, applicants need "an initial prototype, customer insight and vision"; Root Ventures initial USD 3–5M (deep-tech seed lead, 2/3 of fund in reserves); Cantos USD 1.5–4M lead checks at pre-seed/seed from a USD 70M Fund IV; Pathbreaker writes first checks at inception stage in robotics, computer vision and novel hardware, listing fashion and laundry among target service industries | Firm websites and fund announcements | [95][96][97][98][99] |

Implication: a credible 2026 seed for this project is EUR/USD 2–5M on a post-money SAFE or priced round at USD 12–25M post, selling ~20%, led by a deep-tech seed fund (Root, Cantos, HAX/SOSV, Pathbreaker) with a strategic (brand, sewing-machine maker or uniform supplier) alongside; the physical-AI "mega-seeds" (Genesis USD 105M) are foundation-model outliers, not cell-builder comps.

### F7. Investors active in robotics, physical AI and apparel tech (as evidenced in 2025–2026 deals above)

| Investor | Evidence of focus | Stage / check (published) | Source |
|---|---|---|---|
| Eclipse Ventures | Co-led Genesis AI seed; Mytra investor; "~USD 5B AUM … physical industry problems … physical AI" | Seed to growth | [76][84] |
| Khosla Ventures | Co-led Genesis AI seed; Field AI investor | Seed to growth | [76][87] |
| SOSV / HAX | Silana, unspun (6 rounds), Smartex (textile inspection), Presso (garment pressing) | Pre-seed up to USD 550k; HAX sweet spot USD 250k | [13][30][98][99] |
| Lowercarbon Capital, DCVC (climate) | unspun Series A lead, Series B lead, B-II | A/B | [29][30][32] |
| Creandum, Headline (EU) | Sereact A and B | A/B | [79][80] |
| Elaia, Speedinvest | mimic seed | Seed | [78] |
| Avataar Ventures, Construct Capital, Bloomberg Beta, HCVC | Chef Robotics A | A | [82] |
| Kibo Ventures, Kfund + Inditex (strategic) | Theker seed | Seed | [35] |
| BESTSELLER Invest FWD (strategic) | SoftWear B1 lead | B | [1] |
| Emerald Technology Ventures, Nabtesco (strategic), HTGF, Bayern Kapital | sewts A | A | [18] |
| Root Ventures | Deep-tech seed lead, USD 3–5M initial; robotics portfolio (Dusty Robotics, Seismic, PhyAgents) | Seed | [95] |
| Cantos Ventures | USD 70M Fund IV; USD 1.5–4M lead checks; advanced manufacturing | Pre-seed/seed | [97] |
| Pathbreaker Ventures | Inception-stage first checks; robotics, CV, novel hardware; names fashion and laundry as target service industries; portfolio includes Presso and GrayMatter Robotics | Pre-seed/seed | [96] |
| Founders Fund, Lux Capital, a16z (American Dynamism), Bessemer, Playground Global | Named in the brief; no 2025–2026 sewing- or apparel-automation deal by these firms was found in this research (Bessemer led Foxglove's USD 40M robotics-data round, Nov 2025, per Pathbreaker's news page); treat as general robotics investors, unverified for apparel | Seed to growth | [96] |

### F8. Milestones investors expect at seed for hardware / robotics

| Stage | What investors expect (2025–2026 guidance) | Source |
|---|---|---|
| Pre-seed (USD 0.5–2M) | Strong team, clear problem definition, initial technical demo; HAX requires an initial prototype and customer insight | [99][100] |
| Seed (USD 2–5M) | Working prototype, an initial data asset, customer LOIs; for deep tech/hardware the Series A bar is "signed LOIs/pilots plus a technical milestone" rather than ARR | [100][101] |
| Series A (USD 10–30M) | Customer pilots with measured metrics (success rate, cycle time, uptime), evidence of a data flywheel, repeatable deployment; one 2026 guide suggests 3+ customer pilots and 5,000+ demonstrations within 12 months; seed→A graduation now ~15–20% | [100][101] |
| Safety | Safety certification (ISO 10218, ISO/TS 15066 for collaborative operation) takes 6–12 months and should start before Series A | [100] |
| What makes an LOI count | Named champion and department, a specific use case tied to a pain, a time-boxed intent to buy on a success trigger, a price range the customer has accepted, and explicit customer-supplied inputs (site, data, materials) | [102] |

Applied to this project, a seed-ready package is: one roll-to-tee run on video with measured takt and yield (ST01–ST07), a BOM-backed cost at the USD 52–83k factory-cost scenarios, three to five LOIs from uniform/teamwear or small contract manufacturers naming price and site, and a safety architecture document (M10/ST09) showing certification is scoped.

### F9. Market numbers

#### F9.1 Apparel and T-shirt market size

| Metric | Value | Source (date) |
|---|---|---|
| Global apparel revenue | USD 1.92T in 2026, CAGR 2.62% 2026–2031; 203.2B pieces/yr by 2031; US largest market at USD 373B (2026); 95% non-luxury | Statista Market Insights (2026) [104] |
| Global apparel market (alternative) | USD 1.8T (2025) → USD 1.9T (2026) → USD 2.5T (2033), 4.1% CAGR; Asia Pacific 40.8% share | Grand View Research (2026) [105] |
| Fashion industry growth outlook | Low single-digit growth in 2026; 76% of executives say trade disruptions and duties will shape 2026 | McKinsey/BoF State of Fashion 2026 [103] |
| US apparel imports | US imports 89% of apparel and leather products sold; top 2024 sources of apparel+footwear imports: China USD 30B (25%), Vietnam 25B (21%), EU 10B, Indonesia 8B, Bangladesh 7B, Cambodia 7B, India 6B, Mexico 4B, Honduras 2B, Pakistan 2B | McKinsey SoF 2026 [103] |
| Global T-shirt market | see F9.1 addendum below (searched separately) | — |

#### F9.2 US apparel manufacturing employment, output and reshoring

| Metric | Value | Source (date) |
|---|---|---|
| US apparel manufacturing employment (NAICS 315) | 94.0k jobs in 2025, down from 101.8k (2024), 107.9k (2023), 118.0k (2022) | BLS productivity program via FRED (Jun 2026) [107] |
| Sewing machine operators employed in NAICS 315 | 25,280 (2025); ~6,200 establishments (Q1 2026) | BLS industry page [106] |
| NAICS 315 sectoral output | USD 8,724M (2025) vs 9,026M (2024) and 9,928M (2022) | BLS via FRED (Jun 2026) [108] |
| Reshoring | Kearney 2026 Reshoring Index: manufacturing import ratio rose to 14.15% (2025) from 13.29%; apparel & accessories imports from Asian low-cost countries USD 88B in 2025 and "even more reliant on offshoring than in previous years"; Sourcing Journal headline on the same index: "US apparel manufacturing fell 17% in 2025" | Kearney (Apr 2026) [109]; Sourcing Journal (May 2026) [110] |

Reading: the domestic base our cell would sell into is small (25k sewing operators) and still shrinking through 2025 despite tariffs, so the first buyers are the ~6,200 establishments already making uniforms, teamwear, military and premium basics domestically, not a reshoring wave.

#### F9.3 US tariffs on apparel, 2025–2026, and de minimis

| Event / rate | Detail | Source |
|---|---|---|
| Trade-weighted US tariff on apparel & footwear imports | 13% (1 Jan 2025) → 54% (Apr 2025 spike) → 36% (mid-Oct 2025); ~USD 27B estimated added duties at constant volumes | McKinsey SoF 2026 [103] |
| De minimis | Duty-free de minimis (≤USD 800) suspended for all countries from 2025-08-29; postal shipments charged ad valorem IEEPA rate or flat USD 80–200/item until 2026-02-28 | CBP factsheet (Aug 2025) [111] |
| IEEPA tariffs struck down | US Supreme Court, Learning Resources v. Trump, 2026-02-20 (6–3): IEEPA does not authorise tariffs; same-day order ended IEEPA duties; a temporary 10% Section 122 surcharge took effect 2026-02-24 | K&L Gates summary; TTU/ICAC brief [113][112] |
| Section 301 replacement (Jul 2026) | Presidential memorandum directs Section 301 tariffs of 10% on economies with reciprocal-trade deals (incl. Bangladesh, Cambodia, Indonesia, Malaysia) and 12.5% on others (incl. Vietnam and China), with a textile TRQ mechanism allowing a volume of apparel at a zero Section 301 rate for Bangladesh, Cambodia, Indonesia and Malaysia | Federal Register 2026-07-28 [114]; Reuters 2026-07-24 [115] |
| Bangladesh deal | Reciprocal-trade agreement 2026-02-09: reduced 19% rate (pre-ruling) and a zero-tariff mechanism for apparel made with US material | Reuters [116] |
| Effective duty rates actually paid | China cotton-dominant apparel peaked at 70% (May 2025), ~31% by Jun 2026; other leading cotton suppliers ~25% in Jun 2026; MMF group 28% (Bangladesh) to 34% (Jun 2026) | TTU/ICAC brief, Oct 2026 [112] |
| Sourcing shifts | China's share of US cotton apparel imports fell from 13.8% (2020–24 avg) to 6.6% (H1 2026); Vietnam 17.8% (largest), Bangladesh 16.6% | TTU/ICAC brief [112] |
| Worked example: cotton knit tee from China (2026) | 16.5% HTS base + 7.5% legacy Section 301 (List 4A) + 12.5% new Section 301 = 36.5% (secondary source; verify against HTSUS before use) | makemine.com [117] |

Reading: tariffs on Asian tees moved from ~16.5% MFN to 25–37% effective in 2026 and remain politically volatile; this narrows but does not close the gap to domestic cost, so our pitch should use the 25–37% range as a sensitivity, not a foundation (see white-paper conflicts).

#### F9.1 addendum: T-shirt market

| Metric | Value | Source (date) |
|---|---|---|
| Global custom T-shirt printing market | USD 5.2B (2024) → 6.3B (2026) → 9.8B (2030), CAGR 11.5%; Asia Pacific 36.4% share (2024); screen printing largest, digital fastest growing | Grand View Research (2026) [118] |
| Same market, different definition | USD 8.93B (2025) → 9.88B (2026) → 14.61B (2030), CAGR 10.3% | Research and Markets (Jan 2026) [119] |
| US custom T-shirt printing | USD 857.6M (2023) → 1,845.6M (2030), CAGR 11.6%; US = 18.2% of global | Grand View Research (2026) [120] |
| Global T-shirt market (all tees, value and units) | Not retrieved from a primary source in this research; Statista's apparel volume forecast (203.2B pieces/yr by 2031) is the only unit-level anchor found. Unknown; owner: R13 follow-up, next: pull Statista "T-shirts" segment or Euromonitor | [104] |

#### F9.4 Labour costs for sewing

| Country | Statutory or typical wage | USD equivalent (basis) | Loaded cost per minute, 2026 industry estimate (est.) | Source |
|---|---|---|---|---|
| United States | BLS OEWS May 2025, sewing machine operators (SOC 51-6031): median USD 17.63/h (USD 36,670/yr), mean USD 18.08/h, employment 104,880 (secondary page citing BLS); BLS OEWS May 2023 primary: median USD 16.56/h, 116,130 employed, cut-and-sew apparel mean USD 15.94/h | ~USD 2,900–3,100/month base at 40 h/wk (est. from median) | USD 0.80–1.30/min (scanerp "USA USD 1.00") | [121][122][129] |
| Bangladesh | RMG minimum Tk 12,500/month (Dec 2023) plus 9% annual increment since Dec 2024; three-year review cycle now in law, revision pressed for Dec 2026 | ~USD 102–133/month (exchange-rate dependent) | USD 0.08–0.12/min | [123][124][129] |
| Vietnam | Regional minimum wage +7.2% from 2026-01-01 (+VND 350,000–500,000/month); Region I ~USD 165/month in 2024 per a sourcing agent | ~USD 180–215/month Region I 2026 (est. from +7.2%) | USD 0.14–0.18/min | [125][130][129] |
| Mexico | General minimum MXN 315.04/day from 2026-01-01 (MXN 9,582/month); border zone MXN 440.87/day; IMSS average registered salary MXN 673/day (Aug 2026) ≈ USD 1,100/month; unskilled operator employer cost ≈ USD 1,030/month (Oct 2026, consultancy) | USD 520 (minimum) to USD 1,030–1,100 (operator cost) per month | USD 0.35–0.50/min | [126][127][129] |
| China | CPM only (minimum wages vary by province; USD ~300/month in a 2023 op-ed, possibly stale) | — | USD 0.20–0.32/min | [129] |

Reading against the white paper's USD 20/h paid-work assumption: the US median sewing wage of USD 17.63/h (May 2025) makes USD 20/h a fair fully-paid rate, but a loaded cost (benefits, payroll tax) is nearer USD 24–26/h (est., +25–30% burden). The cost-per-minute gap (USD 1.00 vs 0.10) is the whole economic argument for the cell: at 15 SAM and 50% efficiency a tee costs USD 30.50 CMT in the US versus USD 3.50 in Bangladesh in one practitioner's model [129].

#### F9.5 Cut-and-make cost of a basic tee by country (2025–2026 quotes and guides)

| Item | USA | Mexico | Vietnam | China | Bangladesh | Source |
|---|---|---|---|---|---|---|
| CMT per basic cotton tee | USD 5.20–6.40 (LA, 180 gsm, 500 units); USD 5–10 (LA, Apex guide); USD 5.20–8.90 (Alibaba guide) | USD 1.95–2.60 | USD 1.05–1.40; USD 1.20–2.50 | USD 1.20–1.60; USD 1.50–3.00 | USD 0.80–1.80; USD 1.00–2.00 | [128][133][134] |
| FOB / ex-factory basic tee (500–1,000 units) | USD 12.50–17.50 (US cut-and-sew); USD 14–22 at 50–150 units (LA small batch); USD 8.20–9.40 landed from LA | USD 4.68 FOB (Guanajuato) | USD 3.08 FOB; Asia ex-factory USD 2.40–3.80 | USD 3.30 FOB | USD 2.85 FOB; USD 2.80–3.60 at 1,000 units; from USD 4.50 at MOQ 500 (agent) | [128][134][135][136][132] |
| 100-tee quotes incl. shipping (Apr 2025, 50 manufacturers) | USD 17.50/shirt (New Jersey) | — | USD 11.48 | USD 13.14 | USD 8.55 (Pakistan USD 11.00) | [131] |
| Premium 240–280 gsm vintage-wash tee FOB (China/Vietnam) | — | — | USD 4.50–8.00 | USD 4.50–8.00 | — | [134-Storiginator, see 149] |
| Labour content | Jersey tee 8–12 SAM; ~12 sewing operations; cost of making = 15.2% of FOB (2023 Bangladesh cost-sheet study); fabric 42–50% of FOB | | | | | [130][132] |
| Importer-side add-on (freight, duty, fees) | Averages 23% of FOB on Asian sourcing before 2025 tariff changes; 2026 duty on a cotton knit tee ~25–37% (F9.3) | | | | | [130][112][117] |

Reading: the white paper's modelled USD 9.02 total cost per accepted shirt at 100/day and USD 12 ex-factory price sit above a landed Asian basic tee (USD 4–6 incl. 2026 duties, est.) and inside the US small-batch band (USD 12.50–22). The cell therefore competes on reorder speed (US 3–5 weeks vs Asia 10–16 weeks [128]), MOQ (tens vs 300–1,000 per style/colour) and Berry/uniform eligibility, not on price against Asia.

#### F9.6 Fabric prices (cotton jersey)

| Item | Price (currency, date, basis) | Source |
|---|---|---|
| Raw cotton, Cotlook A Index | 90.65 US cents/lb on 2026-10-09 (index); briefly >100 c/lb early Sep 2026, ~91 c/lb mid-Oct; China CC Index ~120 c/lb | [140][141] |
| Cotton jersey 180 gsm, Asian mills | USD 2.40–4.20 per metre (2026 guide); ~USD 5.50/kg standard, ~USD 7.50/kg organic (sourcing-agent worked example); 0.35–0.45 kg per tee | [133][130] |
| Single jersey, India (listings) | INR 330–350/kg (IndiaMART listings, 2026) ≈ USD 3.4–3.7/kg at ~INR 96/USD | [142][141] |
| US retail cotton/Lycra jersey | USD 10.48/yd (FabricMart retail, 2026) | [143] |
| US wholesale heavyweight (280 gsm) cotton jersey per yard/kg | Not published online by the US knitters checked; request quotes (Laguna Fabrics, Cotton Heritage, Pine Crest). Unknown; owner: R13 follow-up, next: quote request for 280 gsm combed ring-spun jersey, 60 in tubular/open width, 50–500 yd | — |

#### F9.7 Print-on-demand economics, MOQs and lead times

| Item | Value | Source |
|---|---|---|
| POD unit cost to seller | Bella+Canvas 3001 from USD 11.92 incl. one print (Printful, 2026-10-21); cheapest black tee USD 8.17 (Printful) vs USD 12.47 (Gelato); USD 8.80–14.50 per printed tee with 2–5 day turnaround and no MOQ (2026 guide) | [50][51][134] |
| POD margins | 20–40% net typical; basic tees as low as 10% | [139] |
| MOQ patterns | Small-batch domestic 25–200 units/style (LA from 50/style, activewear 100/style/colour); overseas full package 300–1,000+/style plus colour minimums; Bangladesh 300/style (agent) to 1,000/style/colour at small-mid export factories and 5,000–10,000 at tier-one; custom-dyed fabric MOQ ~3,000 m | [137][136][138][135] |
| Lead times | LA: samples 2–4 weeks, bulk 4–8 weeks after approval (6–12 weeks total); US reorders 3–5 weeks vs 10–16 weeks from Asia; Bangladesh bulk 30–35 days for 300–1,000 pcs plus 18–35 days sea freight (9–14 weeks brief-to-door) or 75–120 days PO-to-FOB for knit programmes; Vietnam 45–75 days; China 30–60 days | [136][128][138][135][133] |

#### F9.8 Berry Amendment, uniform and merchandise segments

| Item | Value | Source |
|---|---|---|
| Berry Amendment | 10 U.S.C. 4862 (formerly 2533a): DoD must buy clothing, fabrics, fibres, yarns and made-up textiles grown/produced in the US, down to components of components (DFARS 252.225-7012) | [146][144] |
| DLA Troop Support Clothing & Textiles obligations | USD 1,878M in FY2024, of which cut-and-sew apparel contractors (NAICS 315210) USD 624M, men's/boys' cut-and-sew (315220) USD 165M, cut-and-sew except contractors (315250) USD 101M; >8,000 items | DLA small-business brief (Apr 2025) [145] |
| DoD textile/apparel procurement | USD 2.3B in FY2021 (clothing USD 1.7B) = 5% of USD 49B US mill shipments; UNICOR ~USD 99M of DoD textile/apparel sales | CRS primer [144] |
| Uniforms and workwear market | USD 84.75B (2025) → 89.71B (2026) → 111.27B (2030), CAGR 5.5–5.9% | Research and Markets (2026) [147] |
| Promotional products industry (PPAI/ASI 2025 sales, apparel share) | Not retrieved in this research. Unknown; owner: R13 follow-up, next: PPAI "2025 Sales Volume Study" or ASI "State of the Industry 2026" | — |

### F5 addendum: comps found after the table above

| Company | Round | Amount and valuation | Investors | Source |
|---|---|---|---|---|
| Dyna Robotics | Seed → Series A | USD 23.5M seed (2025-03-25, CRV and First Round lead; USD 100M post per a secondary tracker); USD 120M Series A (2025-09-15) at >USD 600M (Bloomberg); USD 144M total | Robostrategy, CRV, First Round; NVentures, Amazon Innovation Fund, Salesforce Ventures, Samsung Next, LG Technology Ventures | [148][149][150] |
| Skild AI | Series A → Series C | USD 300M Series A at USD 1.5B (2024); USD 1.4B Series C (2026-01-14) at >USD 14B; revenue "zero to ~USD 30M" in 2025 | SoftBank lead; NVentures, Macquarie, Bezos Expeditions; Lightspeed, Felicis, Coatue, Sequoia; strategics Samsung, LG, Schneider, Salesforce | [151] |
| Formic | Series A (2024) | USD 27.4M (2024-06-25); investors include Lux Capital, Initialized, Blackhorn, Mitsubishi HC Capital America, NEC, TransLink; equipment debt since 2022 | Lux Capital is thereby evidenced as an active industrial-robotics investor | [81] |

## Recommendation for this project

| Decision | Selected option | Alternates | Reasoning and risk |
|---|---|---|---|
| Positioning statement | "The first conventional-stitch roll-to-garment cell priced for a single factory floor (~USD 100k), sold to domestic uniform/teamwear makers, Berry-Amendment contractors and nearshore contract sewers who need 50–500-piece reorders in days, not weeks." | (a) "Physical-AI sewing platform" licensed to JUKI/Jack-class OEMs; (b) decorated-tee microfactory bundling a DTG partner (Kornit Apollo) | CreateMe (bonded seams, 250/h platform), SoftWear (worklines, brand-led B1), Silana (same roll-to-tee thesis, EU-first, undelivered) and Theker (handling only) leave the "stitched, cell-sized, buy-it-yourself" slot open [F1][F4]. Risk: a Silana delivery or a CreateMe T-shirt launch in 2026–27 closes it; mitigation is a public demonstrated run before either. |
| Beachhead segment | DLA/Berry cut-and-sew contractors and uniform/teamwear suppliers (USD 1.88B FY24 DLA C&T obligations; USD 624M to cut-and-sew contractors) [F9.8] | Premium domestic basics brands and LA small-batch sewers (USD 12.50–22 per tee today) [F9.5]; fashion-school/research labs for first two units | Berry buyers cannot offshore, already host automation pilots (Bluewater Defense) and value documented process control; risk is DLA spec compliance (shade, construction specs) and slow procurement cycles. |
| Price positioning for the operator | Target total construction cost ≤ USD 3.00 per accepted tee ex-fabric (est. from the white paper's USD 9.02 at 100/day less USD 6.08 materials) so the operator sells at USD 10–14 ex-factory: below US small-batch (USD 12.50–22) and within reach of landed Asian premium (USD 6–10 incl. 25–37% duty) [F9.3][F9.5] | Sell cell + usage fee (Kornit AIC model, ARR USD 33.8M at Q2 2026 shows buyers accept it) [F3] | Price against Asia is not winnable on basics; it is winnable on 3–5-week reorders, MOQ in tens and Berry eligibility. Risk: tariff reversal after the Feb 2026 IEEPA ruling and Jul 2026 Section 301 reset [F9.3]. |
| Business model | Sell the cell (~USD 100k) with a USD 3k/yr software/service package (white paper) and offer RaaS via equipment debt (Chef Robotics structure: USD 20.6M equity + USD 22.5M SVB equipment line) [F5] | Pure RaaS (Formic) or brand-funded worklines (SoftWear/BESTSELLER) | RaaS removes buyer capex but needs a lender; the white paper's 2% reference-case contribution leaves no room for RaaS write-offs, so the USD 52k factory cost case is a precondition. |
| Seed round | USD 2–5M on a post-money SAFE or priced round at USD 12–25M post, ~20% dilution, led by a deep-tech seed (Root USD 3–5M initial, Cantos USD 1.5–4M, HAX/SOSV up to USD 550k first check, Pathbreaker first check) plus one strategic (uniform maker, JUKI/Jack distributor or a brand's venture arm) [F6][F7] | EU route: aws/FFG-style grants then SOSV/HAX (Silana's path, EUR 0.7M grants + EUR 1.5M seed) | Comps show seed buys a prototype and LOIs, not deliveries (Silana); the raise must be sized for a demonstrated run plus 3 pilots (24–30 months). Risk: investor pattern-matching to SoftWear/Tianyuan; answer with measured runs, not claims. |
| Seed milestones to commit to | (1) one unattended roll-to-tee run on video with measured takt, yield and operator interventions; (2) BOM-backed factory cost at USD 52k/83k; (3) 3–5 LOIs naming price, site and success criteria [F8]; (4) safety architecture (M10/ST09) scoped to ISO 10218/TS 15066 with certification started before Series A | — | These map to what robotics seeds were funded on in 2025–26 (prototype, data asset, LOIs) [F8]. |
| What not to build | Bonded seams (CreateMe's patent estate, >95 patents), stiffener routes (Sewbo), knit-to-shape (Shima: slow, gauge-limited, JPY 23B company with falling unit sales) | — | Keeps the conventional-stitch differentiator and avoids IP collision; check Amazon US 9,623,578 and SoftWear patents in the IP review. |

## Integration notes

Market and funding research has no mechanical or pneumatic interface; its "interfaces" are the data and documents the rest of the project consumes.

- Cost model inputs (M07 scheduler, M14 data): adopt cost-per-minute and SAM as first-class metrics so the cell's measured takt can be expressed as a CMT equivalent (US USD 0.80–1.30/min, Mexico 0.35–0.50, Vietnam 0.14–0.18, Bangladesh 0.08–0.12; tee 8–15 SAM) [F9.4][F9.5]. Log operator interventions per garment because "one operator per cell" is the cost claim buyers will test.
- Tariff and duty feed: the landed-cost comparison depends on HTSUS 6109/6110 base rates (16.5% cotton knit) plus Section 301 layers (7.5% legacy + 10–12.5% new, Jul 2026) and any TRQ at zero rate for Bangladesh/Cambodia/Indonesia/Malaysia; keep a dated tariff table in the sales model and refresh quarterly [F9.3].
- Berry/DLA channel: DLA Troop Support C&T posts solicitations on DIBBS; specifications, patterns and shade standards come from DLA, so the canonical garment record (M02) should be able to ingest a DLA pattern/spec package [F9.8].
- Usage metering: if a Kornit-style usage fee is adopted, M14 must meter accepted garments, attempts and material consumption with tamper evidence, and M12 must expose read-only metering to the buyer.
- Decoration partner interface (ST08): Kornit Apollo takes garments at up to 400/h with one operator, far above the cell's ~8–10/h, so decoration is a shared downstream station, not an inline module; plan a buffer and label hand-off [F3].
- Competitive watch: subscribe to SoftWear, Silana, CreateMe, Theker, unspun press and to ARM Institute project calls (Sewbo/Bluewater); re-run this comp table before each fundraising step.
- LOI template: fields per F8 (champion, site, use case, success metric, price range, trigger and time box).

## Conflicts with the white paper

Checked by grepping the white paper for competitor names, prices, wages, MOQ, tariffs and the USD 100,000 / USD 12 assumptions. No outright contradiction found; four calibration points:

1. Fabric price: the white paper's unquoted USD 12/kg body and USD 14/kg rib assumptions are 2–3× Asian mill jersey (USD 3.4–7.5/kg) and above the USD 2.40–4.20/m guide range; they are plausible only for US-knit heavyweight 280 gsm jersey at small quantities, which is unverified (no US wholesale quote found) [F9.6]. Treat as conservative until Laguna/Cotton Heritage quotes arrive.
2. Ex-factory price: the USD 12 assumed price is above landed Asian premium tees (USD 6–10 est. incl. 2026 duties) and at the bottom of US small-batch pricing (USD 12.50–22); the white paper already says willingness to pay is untested, and this research confirms the price is defensible only in uniform/Berry and fast-reorder segments [F9.5].
3. Silana's "one worker per ten machines" (white paper, competitor table) could not be found on Silana's current site, which now states "90% automation degree" and "82% cost deduction"; the claim may have been removed or restated [F1].
4. The white paper lists SoftWear's offer as "sourcing through enabled factories" without noting its Aug 2025 USD 20M Series B1 led by BESTSELLER or the Tianyuan Little Rock outcome (manual plant opened 2019, automated line still "in development"); both strengthen, not weaken, the paper's caution about public claims [F1].

Labour: the white paper's USD 20/h paid-work rate is consistent with the BLS May 2025 median of USD 17.63/h for sewing machine operators (a loaded rate would be ~USD 24–26/h, est.).

## Open questions and unknowns

| Unknown | Why it matters | Cheapest way to confirm |
|---|---|---|
| Did the Tianyuan Little Rock LOWRY lines ever run at scale (2020–2026)? | Investors will cite it | Email SoftWear IR/press and Arkansas EDC; one call to TY Garments USA |
| Silana: has any machine been delivered; price and throughput per SiBot; is the PitchBook USD 5.53M seed real? | Direct comp and competitor | Request a quote as a prospective buyer; ask SOSV/HAX contacts |
| CreateMe total funding, investors and T-shirt launch date | Best-funded rival | PitchBook/Crunchbase paid pull; ask Avalo/Laguna partners |
| SoftWear LOWRY workline price and lead time | Price anchor for a "workline" vs our cell | Quote request |
| Kornit Apollo system price | ST08 partner economics | Quote request to Kornit |
| Global T-shirt market size in units and value (not printing) | TAM slide | Statista/Euromonitor segment purchase |
| Promotional products industry sales 2025 and apparel share | Merch segment sizing | PPAI 2025 Sales Volume Study (free summary) |
| Vietnam Region I 2026 minimum wage in VND (absolute) and China garment wages 2026 | Labour cost table completeness | MOLISA decree 2026 text; ILO wage database |
| US wholesale 280 gsm cotton jersey price per yard and MOQ | Material cost in the garment model | Quotes from Laguna Fabrics, Cotton Heritage, Pine Crest |
| Section 301 implementation after Jul 2026 memo: final rates and textile TRQ volumes | Landed-cost comparison | USTR Federal Register notices; CBP CSMS messages |
| DLA C&T FY2025 obligations and FY2026 solicitations for knit tees | Beachhead sizing | DLA small-business brief update; DIBBS search for 8415 class |
| Theker EUR 74M round (Jun 2026) confirmation | Inditex's automation bet | Theker press page or Kibo Ventures |
| Shima Seiki FY to Mar 2026 results and WHOLEGARMENT unit sales | Alternative-route trend | Shima Seiki IR PDF (link found, numbers not extracted) |
| Whether Founders Fund, a16z, Playground, Bessemer have any apparel-automation deal | Investor list | Crunchbase investor search |

## Sources

1. https://softwearautomation.com/softwear-automation-secures-20-million-in-series-b1-funding-round-led-by-strategic-partnership-with-bestseller/ — SoftWear USD 20M Series B1, 2025-08-11, BESTSELLER/Invest FWD lead, participating investors, board seat.
2. https://platform.tracxn.com/a/d/company/546c50dee4b08dcc0590c98a/softwear%20automation — Tracxn: SoftWear total disclosed USD 45.6M, 52 employees, Series B stage.
3. https://www.thecompanycheck.com/company/b/softwear-automation/vdu65f33avbc6i18v — Conflicting total (USD 65.6M, 5 rounds, Lear Corp as investor).
4. https://wwd.com/business-news/technology/feature/softwear-automation-announces-investment-10911418 — USD 4.5M investment from CTW Venture Partners (undated).
5. https://www.crunchbase.com/organization/softwear-automation — DARPA and Walmart Foundation R&D funding; fully automated T-shirt workline product.
6. http://usa.chinadaily.com.cn/world/2017-07/25/content_30244657.htm — Tianyuan/SoftWear 2017 claims: 21 lines, one tee per 22 s, 800,000/day, USD 0.33 labour per shirt, USD 20M plant.
7. https://robohub.org/sewing-a-mechanical-future — Robohub: unclear whether the 30M pieces/yr objective was met.
8. https://www.therobotreport.com/chinese-factory-sets-arkansas-make-t-shirts-using-u-s-robots — 330 robots, USD 20M factory.
9. https://sewbo.com/ — Sewbo process (PVA stiffener), jeans focus, not for sale.
10. https://tracxn.com/d/companies/sewbo/__kLgjCyavUqFgPs0FLjSk4tSVYplGSCQq2psSrQ6l0UA — Sewbo unfunded, 3 employees.
11. https://arminstitute.org/news/project-robotic-sewing — ARM Institute Apr 2026 highlight: TRL 8–9 via NIST RACER, LA partner factory, fundraising, >50% of jeans assembly addressable.
12. https://arminstitute.org/projects/robotic-assembly-of-garments/ — ARM project at Bluewater Defense: pocket flaps, quality met, cycle time higher than human.
13. https://www.eu-startups.com/2024/05/vienna-based-robotics-startup-silana-raises-e1-5-million-to-optimise-the-clothing-production-puzzle — Silana EUR 1.5M seed led by SOSV; ~200 machines pre-ordered; 30M tees/yr; one worker per ten machines claim context.
14. https://brutkasten.com/artikel/silana-wiener-naehroboter-startup-erhaelt-15-mio-euro-investment — Silana ~EUR 700k prior grants; Löffler customer; first deliveries planned 2025.
15. https://pitchbook.com/profiles/company/537956-29 — PitchBook Silana: latest seed deal USD 5.53M, 15 employees, 14 investors.
16. https://www.cbinsights.com/company/silana/financials — CB Insights Silana: Seed VC-II Dec 2024, StartX Sep 2025, USD 1.63M disclosed.
17. https://www.silana.com/ — Silana claims: 90% automation, 82% cost reduction, 68% CO2 saving, New York office.
18. https://www.sewts.com/blog/sewts-raises-eu7m-to-shape-the-future-of-robotics-and-automation-in-the-textile-industry — sewts EUR 7M Series A Aug 2023, investors, Otto Group returns prototype.
19. https://tech.eu/2023/08/10/sewts-set-to-enhance-textile-automation-with-successful-eur7-million-series-a-fundraising — VELUM up to 700 items/h.
20. https://www.createme.com/newsroom/createme-launches-robotic-apparel-manufacturing-platform-and-first-commercial-grade-garments — CreateMe MeRA/Pixel launch 2025-09-11; 250 garments/h; 20×; >95 patents; cost-competitive claim; T-shirts next.
21. https://www.therobotreport.com/createme-innovates-robotic-assembly-adhesion-tech-garment-industry/ — First product women's intimates; adhesive replaces thread.
22. https://pitchbook.com/profiles/company/438696-01 — CreateMe: later-stage VC, 48 employees, 3 investors, Newark CA; Caplight comparables list (Apparel Robotics Corporation) via https://www.caplight.com/company/createme.
23. https://www.prnewswire.com/news-releases/createme-expands-c-suite-strengthens-advisory-bench-to-drive-next-wave-of-ai-powered-apparel-manufacturing-302637502.html — CreateMe Dec 2025 promotions toward full-scale manufacturing.
24. https://www.prnewswire.co.uk/news-releases/createme-avalo-and-laguna-fabrics-launch-seed-to-system-the-first-ai-powered-apparel-manufacturing-ecosystem-302807301.html — CreateMe "Seed to System" with Avalo and Laguna Fabrics, 2026-06-23.
25. https://wwd.com/business-news/technology/createme-automated-apparel-manufacturing-1238132784 — WWD: CreateMe claims prices on par with Asian factories.
26. https://app.dealroom.co/companies/resonance_companies — Resonance rounds: USD 15M (2015), 8M (2018), 22.5M (2020), 3.3M (May 2025).
27. https://www.cbinsights.com/company/resonance-companies — Resonance total USD 33.83M; latest round debt; Chelsea Piers HQ.
28. https://www.preqin.com/data/profile/asset/resonance-companies--inc-/745102 — CreateOne Pro USD 100/month + 10% revenue share; Santiago DR plant; USD 3.32M May 2025.
29. https://www.prnewswire.com/news-releases/unspun-raises-32m-in-oversubscribed-series-b-funding-to-transform-fashion-supply-chains-with-groundbreaking-3d-weaving-technology-302208798.html — unspun USD 32M Series B, DCVC lead, Jul 2024.
30. https://www.cbinsights.com/company/unspun/financials — unspun total USD 69.73M; Series B-II USD 14.36M Aug 2026 (Lowercarbon).
31. https://www.unspun.io/blog/post/bringing-vega-to-market — Vega renamed OneWeave; licensing model; 350+ machines / 10M garments by 2030.
32. https://www.dcvc.com/news-insights/unspuns-3d-weaving-a-literal-revolution-for-the-clothing-industry/ — Walmart agreement for 350 Vega machines; pants woven and assembled in 20 min.
33. https://fashiondive.com/news/unspun-series-b-32-million-weaving-technology/722889 — Series A USD 14M (2023); pants in ~10 min; woven = 57% of apparel.
34. https://www.inditex.com/itxcomweb/api/media/2f896a99-1b0f-4757-8242-3256e1701cee/Supply_chain_management_transform_sector.pdf — Inditex 2025 supply-chain KPIs: sewing factory counts by proximity cluster.
35. https://www.modaes.com/global/companies/inditex-enters-the-capital-of-theker-a-robotics-start-up-applied-to-industry — Theker EUR 18M/USD 21M seed, Kibo lead, Inditex strategic, Jul 2025.
36. https://app.dealroom.co/news/feed/inditex-invests-in-spanish-robotics-startup-theker-in-21m-funding-round — Theker garment handling/folding focus.
37. https://foro3d.com/en/2026/junio/theker-recibe-74-millones-para-robotizar-el-doblado-de-ropa-en-catalun.html — Secondary report of Theker EUR 74M round, Jun 2026 (unverified).
38. https://www.inditex.com/itxcomweb/bh/en/press/news-detail/464b3454-3676-469e-8106-2078e38e3435/interim-nine-months-2025-results — Inditex 9M2025: EUR 1.8B capex, proximity sourcing.
39. https://www.levistrauss.com/wp-content/uploads/2018/02/Project-FLX-Press-Release.pdf — Levi's Project F.L.X. 2018 (possibly stale).
40. https://www.sec.gov/Archives/edgar/data/866374/000110465918063948/a18-37071_1ex99d1.htm — Flex 8-K Oct 2018: Nike Guadalajara wind-down by 2018-12-31.
41. https://www.sportsbusinessjournal.com/Articles/2025/04/21/nike-sneaker-companies-see-difficulty-in-automating-shoe-production — 2025 retrospective on Nike/Flex: 5,000 staff, soft parts defeated robots.
42. https://www.prnewswire.com/news-releases/grabit-inc-enters-into-restructuring-support-agreement-300977328.html — Grabit restructuring Dec 2019.
43. https://patents.google.com/patent/US9623578B1/en — Amazon US 9,623,578 B1 on-demand apparel manufacturing.
44. https://www.inquirer.com/philly/blogs/inq-phillydeals/is-amazon-reviving-u-s-manufacturing-20171009.html — Amazon Norristown PA print facility (2017).
45. https://printful.com/news/merger — Printful/Printify merger announcement, >1M items/month, 60M orders, 85 print houses.
46. https://www.printful.com/news/merged+company+leadership+team — Merger completed 2024-11-20.
47. https://tech.eu/2024/11/05/printful-and-printify-merge-a-new-era-for-the-print-on-demand-industry — Printful USD 130M (2021, >USD 1B), Printify USD 54.1M, 117 locations.
48. https://www.ppai.org/media-hub/printify-printful-announce-merger-deal/ — PPAI: Printify ~USD 103M revenue; US share of top POD businesses.
49. https://getlatka.com/companies/gelato.com — Gelato USD 240M Series D Aug 2021 at USD 1B; revenue estimates (est.).
50. https://www.printful.com/custom/mens/t-shirts/unisex-staple-t-shirt-bella-canvas-3001 — Printful Bella+Canvas 3001 from USD 11.92 incl. one print (seen 2026-10-21).
51. https://www.printful.com/printful-vs-gelato — Printful cheapest black tee USD 8.17 vs Gelato USD 12.47; 582 products; 0.24% return rate; 147M items.
52. https://kornit.com/lp2/hq/kornit-apollo-printer/ — Kornit Apollo: 400/h, one operator, TCO USD 0.9–1.3/print, ROI 12–18 months, >1.5M prints/yr.
53. https://ir.kornit.com/static-files/282be503-da5f-4c4a-9233-6b2d143f876b — Kornit FY2025 deck: revenue USD 208.2M, ARR ~USD 25M, 40% of Apollo customers added a second system.
54. https://www.sec.gov/Archives/edgar/data/1625791/000121390026055444/ea029009101ex99-1.htm — Kornit Q1 2026 results: USD 48.5M revenue, PrintFactory acquisition, Atlas MATRIX.
55. https://www.globenewswire.com/news-release/2025/11/05/3181331/0/en/Kornit-Digital-Reports-Third-Quarter-2025-Results.html — Kornit Q3 2025 USD 53.1M; Q2 2026 USD 55.3M and ARR USD 33.8M.
56. https://www.juki.co.jp/en/uploads/ir/integrated-report/2025_E_03_web01.pdf — JUKI integrated report 2025: top share, smart factory, results short of targets.
57. https://www.juki.co.jp/industrial_e/solution_e/case_study/case01.php — JUKI shirt-factory case: operators 1,227→586, 14,400 shirts/day, ROI 1.9 years.
58. https://www.juki.co.jp/industrial_e/solution_e/detail.php?sid=17 — JUKI pattern seamer (PS-800) deskilling.
59. https://www.factmr.com/report/sewing-machine-market — Sewing machine market USD 5.4B (2025); Brother NEXIO BAS-341K/342K May 2026; Konrad Busche acquisition Nov 2025; JUKI DX-01 Jun 2025.
60. https://www.chinajack.com/web/company/index — Jack Technology profile and acquisitions (Bullmer/Topcut, MAICA, ViBeMac).
61. https://www.richpeace.com/cnc_sewing_for_garment-show-1157.html — Richpeace RPAS-LM-C-1 template sewing machine specs.
62. https://www.accio.com/supplier/juki-industrial-sewing-machine-automatic-manufacturer — Marketplace listings of Chinese CNC/template sewing units USD 7,888–15,000 (reseller).
63. https://insights.globalspec.com/article/15719/arm-institute-project-automates-sewing — ARM Institute sewing project participants (Siemens, Bluewater Defense, Sewbo, UC Berkeley).
64. https://www.shimaseiki.co.jp/irj/img_sys/irLib/474/474.pdf — Shima Seiki FY to Mar 2025 net sales JPY 23,229M (−10.3%); WHOLEGARMENT history (30 min garment, 1995).
65. https://www.shimaseiki.com/product/knit/mach2xs — MACH2XS WHOLEGARMENT machine specs.
66. https://m.made-in-china.com/product/Shima-Seiki-Mach2xs-153-Year-2019-Wholegarment-Knitting-Machine-15g-1957065905.html — Used MACH2XS 153 (2019) listed USD 25,000 (reseller).
67. https://www.lectra.com/sites/default/files/2026-02/Lectra%20Full%20Year%20Results%202025_EN%20%281%29.pdf — Lectra 2025 results transcript: revenue EUR 506.7M, EBITDA EUR 79.7M, tariff impact on EU fashion <1%.
68. https://www.lectra.com/sites/default/files/investors_files/Lectra_Press%20Release_Q1%202026_EN.pdf — Lectra Q1 2026: equipment orders −25%.
69. https://www.lectra.com/sites/default/files/investors_files/Lectra_Financial%20Information_Q3%202025.pdf — Lectra Empower Fashion uptime-guarantee contracts (Sep 2025).
70. https://tukatech.com/results — Tukatech customer results: TUKAcut crew 90→14, 50–70k units/day; TUKAcad 2026 subscription.
71. https://www.findglocal.com/US/Los-Angeles/90004751883/Tukatech%2C-Inc. — Tukatech microfactory claim (2012) (weak source).
72. https://www.arkansasbusiness.com/article/chinese-garment-maker-opens-invests-30m/ — TY Garments Little Rock opened May 2019; 160 employees; investment raised to USD 30M.
73. https://www.arkansasedc.com/news-events/newsroom/detail/2019/05/30/gov.-asa-hutchinson-tours-newly-opened-tian-yuan-garments-in-little-rock — AEDC release: peak plan >4M garments/yr; automated line still "in development" (May 2019).
74. https://apparelresources.com/technology-news/manufacturing-tech/chinas-tianyuan-garments-develop-fully-automated-us-facility/ — 2017 promises: lines fully operational by end 2018; 800,000/day; USD 0.33.
75. https://www.arkansasbusiness.com/tag/ty-garments-usa-llc/ — Arkansas factories pandemic pivot (May 2020) tag page for TY Garments.
76. https://www.genesis.ai/news/genesis-ai-emerges-from-stealth-with-dollar105m-to-build-universal-robotics-found — Genesis AI USD 105M seed co-led by Eclipse and Khosla, 2025-07-01.
77. https://techcrunch.com/2025/07/01/genesis-ai-launches-with-105m-seed-funding-from-eclipse-khosla-to-build-ai-models-for-robots/ — TechCrunch on Genesis; notes PI USD 400M round and Skild USD 4B valuation (early 2025).
78. https://www.globenewswire.com/news-release/2025/11/03/3179052/0/en/mimic-robotics-raises-16-million-to-deploy-frontier-physical-ai-across-industries.html — mimic USD 16M seed led by Elaia with Speedinvest, 2025-11-03; total >USD 20M.
79. http://sereact.ai/posts/sereact-fundraising-series-a — Sereact EUR 25M Series A led by Creandum, 2025-01-20.
80. https://sereact.ai/posts/series-b — Sereact USD 110M Series B led by Headline, 2026-04-27; 200+ systems; >USD 140M total.
81. https://platform.tracxn.com/a/d/company/531c9b20e4b0f7e166554b9b/formic — Formic: Series A USD 27.4M (2024-06-25), valuation USD 100M, total disclosed USD 159M incl. facilities, 121 employees.
82. https://www.prnewswire.com/news-releases/chef-robotics-announces-43m-series-a-round-led-by-avataar-ventures-to-scale-the-deployment-of-ai-enabled-robotics-302416039.html — Chef Robotics USD 43.1M Series A (USD 20.6M equity + 22.5M equipment debt), 2025-03-31; total USD 65.6M.
83. https://sacra.com/c/physical-intelligence — Physical Intelligence USD 600M Series B at USD 5.6B post (Nov 2025, CapitalG lead); USD 2.4B valuation Nov 2024.
84. https://mytra.ai/news/mytra-raises-120m-series-c — Mytra USD 120M Series C, 2026-01-15, Avenir Growth lead; USD 78M through Series B; >USD 200M total.
85. https://platform.tracxn.com/a/d/company/5b68ed6ee4b04ba64f5ce66a/dexterity — Dexterity Series B USD 104.9M (2026-05-21), valuation USD 1.7B, total USD 396M.
86. https://www.bloomberg.com/news/articles/2025-03-11/ai-robotics-startup-dexterity-lands-1-65-billion-valuation — Dexterity USD 1.65B valuation, Mar 2025.
87. https://www.fieldai.com/news/fieldai-announces-over-400m-in-funds-raised-to-advance-embodied-ai-at-scale — Field AI USD 405M across two rounds, 2025-08-20.
88. https://www.cnbc.com/2025/08/20/gates-nvidia-fieldai-robotics.html — Field AI ~USD 2B valuation.
89. https://www.latimes.com/b2b/ai-technology/story/2025-09-03/fieldai-raises-405-million-latest-round — Field AI USD 314M August round co-led by Bezos Expeditions, Prysm, Temasek.
90. https://platform.tracxn.com/a/d/company/590566a8e4b05bd9cfe5acab/dyna%20robotics — Dyna Robotics Series A dated 2025-09-15.
91. https://carta.com/learn/startups/fundraising/seed-funding/ — Carta Q2 2026 benchmarks: median seed USD 4.5M at USD 23.9M post; dilution 19.4%; SAFE share.
92. https://carta.com/data/state-of-pre-seed-2025-full-report — Carta State of Pre-Seed 2025: USD 10.4B / 50,316 instruments; SAFE caps USD 10M and 15M; hardware #2 industry.
93. https://files.pitchbook.com/website/files/pdf/Q4_2025_PitchBook_Analyst_Note_Should_Seed_Investors_Ride_the_High_and_Pay_the_Price_20593.pdf — PitchBook: seed median USD 15M pre, top decile USD 40M, ownership 20–25%.
94. https://fundingwatcher.com/research/startup-funding-statistics — Secondary compilation citing Carta: seed post USD 24M (Q4 2025), Series A post USD 78.7M, graduation rates.
95. https://www.root.vc/ — Root Ventures: deep-tech seed fund, initial investments USD 3–5M, 2/3 reserves, robotics portfolio.
96. https://www.pathbreakervc.com/beliefs — Pathbreaker Ventures focus (inception stage; robotics, CV, novel hardware; fashion and laundry among service industries); news page https://www.pathbreakervc.com/news for portfolio rounds.
97. https://cryptorank.io/insights/deals/cantos-raises-70-m-fund-iv — Cantos Ventures USD 70M Fund IV; USD 1.5–4M lead checks at pre-seed/seed.
98. https://sosv.com/ — SOSV: ~60 pre-seed investments/yr up to USD 550k; physical AI focus.
99. https://connect.visible.vc/investors/hax — HAX: prototype + customer insight required; sweet spot USD 250k; >USD 25M/yr; Smartex, Presso.
100. https://www.roboticscenter.ai/blog/robot-startup-guide — 2026 robotics startup guide: stage expectations, safety certification 6–12 months.
101. https://valueaddvc.com/blog/how-traction-requirements-for-series-a-have-changed-since-2021 — Series A bar by sector; deep tech/hardware = LOIs/pilots + technical milestone; graduation 15–20%.
102. https://www.tran.vc/pilot-agreements-and-lois-that-help-fundraising — What makes a fundable LOI/pilot.
103. https://www.mckinsey.com/~/media/mckinsey/industries/retail/our%20insights/state%20of%20fashion/2026/the-state-of-fashion-2026_feb.pdf — State of Fashion 2026: tariff 13%→54%→36%; import sources; 89% imported; ~USD 27B duties; low single-digit growth.
104. https://www.statista.com/outlook/cmo/apparel/worldwide — Statista apparel market USD 1.92T (2026), 2.62% CAGR, US USD 373B, 203.2B pieces (2031).
105. https://www.grandviewresearch.com/industry-analysis/apparel-market-report — Grand View apparel USD 1.8T (2025) → 2.5T (2033).
106. https://www.bls.gov/iag/tgs/iag315.htm — BLS NAICS 315 page: sewing machine operators 25,280 (2025); establishments ~6,200; occupational wages.
107. https://fred.stlouisfed.org/series/IPUEN315W200000000 — NAICS 315 employment 94.0k (2025), 101.8k (2024), 118.0k (2022).
108. https://fred.stlouisfed.org/series/IPUEN315T300000000 — NAICS 315 sectoral output USD 8,724M (2025).
109. https://www.kearney.com/documents/d/asset-library-291362522/2026-reshoring-index-1 — Kearney 2026 Reshoring Index: MIR 14.15%; apparel imports USD 88B from Asian LCCRs; apparel more offshored.
110. https://wwd.com/sourcing-journal/trade/kearney-reshoring-index-usa-domestic-apparel-manufacturing-1238945612 — Sourcing Journal: US apparel manufacturing fell 17% in 2025 (Kearney).
111. https://www.cbp.gov/sites/default/files/2025-08/factsheet_suspension_of_duty-free_de_minimis_treatment.pdf — CBP: de minimis suspended 2025-08-29.
112. https://www.depts.ttu.edu/aaec/icac/files/BP-26-04-apparel-imports.pdf — TTU/ICAC Oct 2026 brief: tariff timeline, effective duty rates, sourcing shares.
113. https://www.klgates.com/thought-leadership/Summary-Supreme-Court-Decision-on-IEEPA-Tariffs-2-20-2026 — SCOTUS IEEPA decision 2026-02-20; Section 122 10%.
114. https://www.govinfo.gov/content/pkg/FR-2026-07-28/pdf/2026-15274.pdf — Presidential memorandum Jul 2026: Section 301 rates 10%/12.5%; textile TRQ mechanism.
115. https://www.reuters.com/world/china/top-apparel-exporter-vietnam-faces-higher-us-tariffs-than-peers-2026-07-24 — Vietnam 12.5% vs 10% for peers with deals.
116. https://www.reuters.com/world/asia-pacific/bangladesh-secures-19-us-tariff-exemption-some-apparel-made-with-us-material-2026-02-09 — Bangladesh 19% deal and zero-tariff mechanism, Feb 2026.
117. https://www.makemine.com/blog/china-tariffs — Cotton knit garment from China 36.5% duty stack (secondary).
118. https://www.grandviewresearch.com/industry-analysis/custom-t-shirt-printing-market — Custom T-shirt printing USD 5.2B (2024) → 6.3B (2026) → 9.8B (2030), 11.5% CAGR.
119. https://www.researchandmarkets.com/reports/5751792/custom-t-shirt-printing-market-report — Custom T-shirt printing USD 8.93B (2025) → 9.88B (2026) → 14.61B (2030).
120. https://www.grandviewresearch.com/horizon/outlook/custom-t-shirt-printing-market/united-states — US custom T-shirt printing USD 857.6M (2023) → 1,845.6M (2030).
121. https://www.bls.gov/oes/2023/May/oes516031.htm — BLS OEWS May 2023: sewing machine operators median USD 16.56/h, 116,130 employed, cut-and-sew apparel mean USD 15.94/h.
122. https://www.nyjobzone.org/salary/sewing-machine-operators — Secondary page citing BLS OEWS May 2025: median USD 17.63/h (USD 36,670), mean USD 18.08/h, employment 104,880.
123. https://www.playroll.com/minimum-wage/bangladesh — Bangladesh RMG minimum Tk 12,500/month ≈ USD 102–133.
124. https://finance.yahoo.com/economy/policy/articles/bangladesh-garment-wage-clock-ticking-195040563.html — Sourcing Journal (Aug 2026): Tk 12,500 (~USD 102), 9% annual increment, three-year review cycle.
125. https://en.baochinhphu.vn/regional-minimum-wage-to-increase-by-72-from-january-1-2026-111251111092833451.htm — Vietnam regional minimum wage +7.2% from 2026-01-01 (+VND 350,000–500,000).
126. https://www.legal500.com/intelligence/mexico/employment-and-hr/mexico-implements-new-subcontracting-inspection-protocol-and-announces-minimum-wage-increase-for-2026 — Mexico 2026 minimum wage MXN 315.04/day general, 440.87 border; MXN 9,582/month.
127. https://tetakawi.com/blog/average-wage-in-mexico/ — Mexico IMSS average registered salary MXN 673/day (Aug 2026) ≈ USD 1,100/month; unskilled operator employer cost ≈ USD 1,030/month.
128. https://www.oneaimapparel.com/blog/made-in-usa-vs-offshore-clothing-brands — CMT per tee by country; landed 500-unit tee LA vs Vietnam; US reorders 3–5 weeks vs 10–16 (sourcing-agent data, 2026).
129. https://scanerp.pro/blog/cmt-cost-country-comparison-2026.html — Cost per minute by country (industry estimates, 2026) and 15-SAM T-shirt worked example.
130. https://www.oneaimapparel.com/blog/clothing-production-cost-breakdown-global/ — Jersey tee 8–12 SAM, 0.35–0.45 kg fabric, fabric 42–50% of FOB, loaded SAM rates, importer-side cost 23% of FOB.
131. https://www.visualcapitalist.com/charted-the-cost-to-make-100-t-shirts-by-origin-country — Apr 2025 quotes for 100 tees incl. shipping by country.
132. https://clothingmanufacturerbangladesh.com/journal/clothing-manufacturing-cost-bangladesh/ — Bangladesh tee from USD 4.50 (MOQ 500); cost of making 15.2% of FOB; ~12 sewing operations; US duty 16.5% + 10%.
133. https://www.apexfashionlab.com/glossary/cut-and-sew — MOQ, CMT and lead-time table by country; cotton jersey 180 gsm USD 2.40–4.20/m.
134. https://apparel.alibaba.com/guide/t-shirt-production-cost-guide-real-2026-breakdown — Ex-factory tee cost by region; POD USD 8.80–14.50; cost components (2026).
135. https://www.oneaimapparel.com/blog/clothing-manufacturing-in-bangladesh — Bangladesh FOB tee USD 2.80–3.60 at 1,000 units; MOQ 1,000/style/colour; lead times.
136. https://pluckyreach.com/services/clothing-manufacturing — LA small batch: 50 units/style, samples 2–4 weeks, bulk 4–8 weeks, basic knit tee USD 14–22.
137. https://www.arcusag.com/cut-and-sew-clothing-manufacturers-costs-moqs-lead-times — MOQ layers (style/colour/size/fabric); domestic 25–200, overseas 300–1,000+; basic knit top USD 8–25+.
138. https://sdfltd.com/streetwear-manufacturer — Bangladesh MOQ 300/style; bulk 30–35 days; sea freight 18–35 days; 9–14 weeks brief-to-door.
139. https://www.printful.com/blog/what-is-a-good-profit-margin-for-print-on-demand — POD margins 20–40%, tees as low as 10%.
140. https://www.cotlook.com/prices/cotlook-a-index — Cotlook A Index 90.65 c/lb, 2026-10-09.
141. https://wwd.com/sourcing-journal/industry-news/cotton-market-analysis-october-2026-1239352311 — Cotton market Oct 2026: A Index ~91 c/lb, CC Index ~120 c/lb, INR ~96/USD.
142. https://dir.indiamart.com/impcat/single-jersey-fabric.html — India single jersey listings INR 330–350/kg (reseller).
143. https://fabricmartfabrics.com/collections/cotton-fabric — US retail cotton/Lycra jersey USD 10.48/yd.
144. https://www.congress.gov/crs_external_products/IF/PDF/IF10609/IF10609.12.pdf — CRS Berry/Kissell primer: DoD textile/apparel USD 2.3B FY2021, clothing USD 1.7B, 5% of mill shipments.
145. https://www.dla.mil/Portals/104/Documents/SmallBusiness/CandT%20SB%20-%20V-4-25-2025.pdf — DLA Troop Support C&T FY2024 obligations USD 1.878B by NAICS.
146. https://www.trade.gov/berry-amendment — OTEXA Berry Amendment description.
147. https://www.researchandmarkets.com/reports/6035401/uniforms-workwear-market-report — Uniforms and workwear market USD 84.75B (2025) → 111.27B (2030).
148. https://www.dyna.co/news/series-a — Dyna Robotics USD 120M Series A (Sep 2025) and investors.
149. https://www.bloomberg.com/news/articles/2025-09-15/dyna-robotics-raises-120-million-in-funding-from-nvidia-amazon — Dyna valuation >USD 600M. (Premium tee FOB USD 4.50–8.00 cited from https://storiginator.com/blogs/blog/cmt-vs-fob-full-package-factory-pricing-model-clothing-brand .)
150. https://tracxn.com/d/companies/dynarobotics/__SQrTmIVEp-T3NjnfTDEZIWLc4jDDBWe4IodOJneuT1Y/funding-and-investors — Dyna seed USD 23.5M (Mar 2025), total USD 144M.
151. https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-%241.4B-Now-Valued-Over-%2414B — Skild AI USD 1.4B Series C at >USD 14B (Jan 2026); USD 300M Series A at USD 1.5B; ~USD 30M 2025 revenue.

Note on recency: items marked 2017–2023 (Tianyuan announcements, Levi's F.L.X., Nike/Flex, Grabit, Amazon patent, BLS May 2023, Bangladesh 2023 wage decision) are possibly stale and are used only as history or baseline; all status claims rely on 2025–2026 sources.
