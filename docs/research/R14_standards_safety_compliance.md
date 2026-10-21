# R14 · Standards, safety and compliance for the roll-to-garment cell

Research report for the Roll-to-Garment project. Date of research: 2026-10-21. Scope: the machinery-safety, functional-safety, electrical, fire, noise, ergonomics, AI-governance, data-protection, garment-quality and labelling rules that the machine guide (ST00–ST10) and the software guide (M01–M14) must follow in the EU and the US. Every claim carries a source number from the Sources section or is marked "est." / "unverified".

<!-- SUMMARY_PLACEHOLDER: the Summary section is prepended after the findings are complete -->

## Findings

### F1 · The EU legal frame: Machinery Regulation (EU) 2023/1230

- Regulation (EU) 2023/1230 repeals and replaces the Machinery Directive 2006/42/EC. It applies from **20 January 2027** with no overlap period: until 19 January 2027 only the Directive may be applied, from 20 January 2027 only the Regulation [11][13]. (The originally published OJ text reads "14 January 2027"; the date was corrected to 20 January 2027 by corrigendum, which is why the EUR-Lex summary, DGUV Test and EU-OSHA all state 20 January 2027 [11][12][13][14].) Articles 26–42 (notified bodies) have applied since 20 January 2024 [11].
- Consequence for this project: a cell first placed on the EU market or put into service before 20 January 2027 is CE-marked under the Directive; anything placed on the market from that date must meet the Regulation. Declarations of conformity may reference both texts at once when the product technically meets both, which DGUV Test recommends for products straddling the date [13].
- Conformity assessment: internal production control (self-assessment, Module A) remains available for most machinery, including robot cells, provided the product is not in Annex I [11]. Annex I **Part A** lists six categories that must go through a notified body regardless of standards used; items 5 and 6 are "safety components with fully or partially self-evolving behaviour using machine learning approaches ensuring safety functions" and "machinery that has embedded systems with fully or partially self-evolving behaviour using machine learning approaches ensuring safety functions… in respect only of those systems" [12]. Annex I **Part B** products may be self-assessed only when designed to harmonised standards covering all relevant EHSRs [11].
- Recital 55 limits the third-party requirement for software to systems with "fully or partially self-evolving behaviour using machine learning approaches ensuring safety functions"; it explicitly does not apply to "software incapable of learning or evolving, and programmed only to execute certain automated functions" [12]. Annex II (safety components) now lists "Software ensuring safety functions" (item 18) and the self-evolving ML variant (item 19) [12].
- The Regulation adds EHSRs for cybersecurity ("protection against corruption"), for safety and reliability of control systems including self-evolving behaviour, for autonomous mobile machinery, and allows digital instructions with a paper copy on request [14][34]. Germany's implementing act (MaschinenDG) entered into force on 6 December 2025 [34].
- Design rule derived: keep every safety function (ST09/M10) deterministic and non-learning so the cell stays out of Annex I Part A and can be self-certified under Module A with harmonised standards (see F2–F4). Learned models (M06–M08, M11) may only act through the deterministic safety layer.

### F2 · Robot safety: ISO 10218-1:2025 and ISO 10218-2:2025 (and ANSI/A3 R15.06-2025)

| Name | Version or date | License | Maturity (stars, last release) | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots | Edition 3, 2025-02, 95 pp., CHF 227 | ISO copyright, purchase | Published; replaces ISO 10218-1:2011 (withdrawn) | Applies to the ST04 arm/gantry as partly completed machinery; the robot vendor's declaration of incorporation must reference it | https://www.iso.org/standard/73933.html |
| ISO 10218-2:2025 Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | Edition 2, 2025-02, 223 pp., CHF 227 (package with Part 1 CHF 408) | ISO copyright | Published; replaces ISO 10218-2:2011 (withdrawn) | The primary C-type standard for the whole cell (integration, safeguarding, collaborative applications, commissioning, verification) | https://www.iso.org/standard/73934.html |
| ISO/TS 15066:2016 Collaborative robots | 2016 | ISO copyright | Still listed as published; content incorporated into ISO 10218-2:2025 | Reference only; the power-and-force-limiting requirements now live in ISO 10218 | https://www.iso.org/standard/62996.html |
| ANSI/A3 R15.06-2025 (Parts 1+2) and ANSI/A3 R15.06-3-2025 (Part 3) | 2025, PDF USD 884 | A3/ANSI copyright | National adoption of ISO 10218-1:2025 and -2:2025 "in their entirety"; replaces ANSI/RIA R15.06-2012 (to be withdrawn) | The US route for the robot cell; identical technical content to ISO 10218:2025 | https://webstore.ansi.org/standards/ria/ansia3r15062025 |

What changed in 2025 (from the ISO foreword as quoted by ANSI, and from TÜV Rheinland and SICK summaries) [1][2][3][4][5]:
- Robot **classification into Class I and Class II** for functional-safety requirements. Class I: light, slow, limited-force robots with reduced requirements; Class II: all other industrial robots. A test methodology for maximum force per manipulator for Class I robots is specified [3][4].
- **Annex C of Part 2 lists every safety function** with a classification (mandatory / conditionally required / optional) and assigns each a required performance level per ISO 13849-1, so integrators no longer rely on the generic "PL d, Category 3" default of the 2011 edition [3][5].
- **ISO/TS 15066 incorporated**: collaborative applications (hand guiding, speed and separation monitoring, power and force limiting) and test methods for force/pressure measurement are now in ISO 10218-2:2025; TS 15066 remains valid only as a reference [3][5].
- **Cybersecurity** requirements "to the extent that it applies to industrial robot safety" (unauthorized access, manipulation, data loss) [3][4].
- Operating **mode requirements** (automatic, manual reduced speed, manual high speed) with a lockable mode selector [4]; additional design requirements and clarified functional-safety requirements [4].
- EU-OSHA/ISO note: Part 1 scope excludes service robots, consumer products and lifting people; application-specific hazards (here: knives, needles, heat press, vacuum) are handled in Part 2 application design [1].

Fit: the cell is an "industrial robot application" (ST04 gantry + arm with grippers inside guarded zones), so ISO 10218-2:2025 is the governing C-standard and ANSI/A3 R15.06-2025 its US twin. Collaborative operation is not needed for 100 shirts/shift with one operator outside the guard; the simplest compliant architecture is full perimeter guarding with interlocked access and no collaborative claims (see Recommendation).

### F3 · Safety-related control systems: ISO 13849-1:2023 and IEC 62061:2021

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 13849-1:2023 Safety-related parts of control systems — Part 1 | Edition 4, 2023-04, 152 pp., CHF 227 | ISO copyright | Published; replaces 2015 edition | Primary method for PL determination of every ST09 safety function; applies to electrical, pneumatic, hydraulic and mechanical SRP/CS, high-demand/continuous mode | https://www.iso.org/standard/73481.html |
| IEC 62061:2021 (+AMD1:2024) Functional safety of safety-related control systems | 2021 (CSV with AMD1 2024), CHF 430 | IEC copyright | Published; replaces 2005+A1+A2 | Alternative SIL-based method; now covers non-electrical technologies, adds security reference (6.8), periodic testing (6.9), software use cases | https://webstore.iec.ch/en/publication/59927 |

Key 2023 changes in ISO 13849-1 (DGUV/IFA analysis) [8][9]: a precise safety-function specification is now required (title, triggering event, safe state, response time, PLr, etc.); categories are assigned per **subsystem**; "well-tried components" moved to 6.1.11 with reference to ISO 13849-2 lists; Category 2 test-rate and test-channel reliability conditions now apply generally; the old simplified Table 6 bar chart was removed; software requirements were expanded; security is out of scope but referenced to ISO/TR 22100-4 and IEC TR 63074 [8]. SISTEMA v3.0 implements the new edition [9]. The standard does not itself set PLr for applications; the integrator derives PLr with Annex A (risk graph) unless a C-standard (ISO 10218-2:2025 Annex C) assigns it [8][9].

IEC 62061:2021 changes [10]: restructured around the safety-function design process; extended to non-electrical technologies; functional safety plan and configuration management; parametrization requirements; "maximum SIL" of a subsystem replaces SILCL; software use cases and independence of verification.

Practical fit: use ISO 13849-1:2023 (PL) as the single method for the cell; it is the one ISO 10218-2:2025 Annex C uses and the one safety-PLC and light-curtain vendors publish data for. IEC 62061 is only needed if a customer specifies SIL.

### F4 · Safeguarding B-standards (current editions)

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 12100:2010 Risk assessment and risk reduction | 2010 (reviewed and confirmed; still current) | ISO | Type-A standard; basis of all others | Mandatory framework for the cell risk assessment (iterative three-step method) | https://www.iso.org/standard/51528.html |
| ISO 13855:2024 Positioning of safeguards | Edition 3, 2024-11, 72 pp., CHF 204; replaces 2010 | ISO | Published | Sets the minimum distance of light curtains, scanners, mats and interlocked guards from hazards; new 2024 formula S = (K × T) + D_DS + Z, K = 2000 mm/s (upper limbs) or 1600 mm/s (walking), S ≥ 100 mm; adds dynamic approach, step-surface definition, extended interlocking-guard calculations | https://www.iso.org/standard/80590.html |
| ISO 14119:2024 Interlocking devices associated with guards | Edition 3, 2024-09, 106 pp., CHF 227; replaces 2013 | ISO | Published | Selection of guard interlocks (type 1–4), guard locking, anti-defeat measures, trapped-key systems for ST00 access doors | https://www.iso.org/standard/75942.html |
| ISO 14120:2015 Guards | Edition 2, 2015; reviewed and confirmed 2021 | ISO | Current | Fixed and movable guard construction (mesh, polycarbonate panels, fixings that stay captive) for ST00 | https://www.iso.org/standard/59545.html |
| ISO 13850:2015 Emergency stop function | 2015 | ISO | Current (referenced by IEC 60204-1 AMD1:2021) | E-stop device and function design (ST09) | https://www.iso.org/standard/59970.html |
| IEC 60204-1:2016 + AMD1:2021 (Ed. 6.1 CSV) Electrical equipment of machines | 2016, amendment 2021-09, stability date 2027 | IEC, CHF | Current | Electrical design of ST09 cabinets: supply disconnect, SCCR determination, stop categories 0/1/2, STO of power drive systems, EMC, bonding, documentation, verification tests | https://webstore.iec.ch/en/publication/71256 |

ISO 13855:2024 detail (Pilz) [16]: K may be reduced to 1600 mm/s if S > 500 mm (then S rounded up to at least 500 mm); T is the total system response time (highest of 10 measurements when measured); Z covers measurement uncertainty, reflection and decreasing braking torque; new forms for manual and foot switches and changed two-hand formula; new limits for vertical ESPE; calculation must include movement of the hazard after the safeguard is tripped.

### F5 · The US route

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ANSI B11.0-2023 Safety of Machinery (type-A) | 2023, revises 2020, PDF USD 275 | AMT/ANSI | Current | US equivalent of ISO 12100; required risk assessment basis for OSHA general-duty compliance | https://webstore.ansi.org/standards/amt/ansib112023 |
| ANSI B11.19-2019 (R2024) Performance requirements for risk reduction measures | 2019, reaffirmed 2024 | ANSI | Current | Safeguarding performance (guards, devices, awareness means) | https://webstore.ansi.org/standards/amt/ansib112023 (listed alongside) |
| ANSI B11.26-2024 Functional safety for SRP/CS | 2024 | ANSI | Current | US functional-safety design standard (parallel to ISO 13849-1) | https://webstore.ansi.org/standards/amt/ansib112023 (listed alongside) |
| ANSI/A3 R15.06-2025 (Parts 1+2) + R15.06-3-2025 | 2025, USD 884 | A3 | Current; replaces R15.06-2012 | Robot cell (see F2) | https://webstore.ansi.org/standards/ria/ansia3r15062025 |
| NFPA 79-2024 Electrical Standard for Industrial Machinery | 2024 edition, USD 165 print | NFPA | Current; 2024 adds a cybersecurity section in Ch. 4, control-circuit conductor protection clarifications, SCCR/labeling and surge updates | US electrical design of the machine (companion to NEC/NFPA 70 and NFPA 70E) | https://www.nfpa.org/product/nfpa-79-standard/p0079code/nfpa-79-electrical-standard-for-industrial-machinery-2024/7924 |
| UL 508A Industrial Control Panels | current UL edition | UL | In OSHA NRTL scopes | The ST09 control cabinet should be built in a UL 508A-listed panel shop and bear a UL 508A label; simplifies field evaluation | https://www.osha.gov/nationally-recognized-testing-laboratory-program/tuvam |
| UL 1740 Industrial Robots and Robotic Equipment | current UL edition | UL | In OSHA NRTL scopes | Product-safety standard an NRTL may evaluate the robot cell against | https://www.osha.gov/nationally-recognized-testing-laboratory-program/tuvam |
| UL 1594 Sewing and Cutting Machines | current UL edition | UL | In OSHA NRTL scopes | Product standard for the sewing heads (ST05/ST06) and cutter (ST02) when listed as components | https://www.osha.gov/nationally-recognized-testing-laboratory-program/tuvam |
| OSHA 29 CFR 1910.212 General requirements for all machines | regulation | US Gov | In force | Legal minimum for point-of-operation guarding; cites ANSI standards by reference in enforcement | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212 |
| OSHA 29 CFR 1910 Subpart S (1910.301–.399) and NEC 90.7/110.2/110.3 | regulation | US Gov | In force | Electrical equipment must be "approved" (listed by an NRTL or field-evaluated) [26][27] | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303 |

NRTL field evaluation (the realistic path for a one-off or low-volume custom cell) [25][26][27][28]:
- A CE mark is **not accepted** by US/Canadian AHJs; unlisted equipment must receive a field evaluation from an OSHA-recognized NRTL / Field Evaluation Body (Intertek ETL, TÜV Rheinland, UL Solutions, CSA, etc.) [26].
- Field evaluation is specific to one piece of equipment at one installation (serial-numbered label); listing is a blanket certification for a product family. Intertek's 2026 guide: field labeling is "used for one-of-a-kind, custom equipment or prototype equipment that is not intended to be mass produced", and changes made after NRTL approval void that approval [25].
- Process: documentation review (schematics, component certifications, ratings), construction review (conductor sizing, motor/component protection, enclosures, markings), tests (grounding continuity, dielectric withstand, input current, strain relief, e-stop/interlock function); non-compliant machines receive a Construction Issues Report; passing equipment gets the FEB label and an acceptance report [26][27]. Intertek evaluates against product standards plus the NEC and NFPA 790/791 [28]. TÜV Rheinland offers a two-stage service with pre-evaluation at the factory of origin (e.g., in Europe) and a simplified final on-site audit [27].
- Cost and timeline: see F5a (below) for sourced figures.

### F6 · Sewing-machine safety: ISO 10821:2005 (+Amd 1:2009)

- ISO 10821:2005 "Industrial sewing machines — Safety requirements for sewing machines, units and systems" (Edition 1, 76 pp., CHF 204) was last reviewed and confirmed in 2015 and is currently at ISO stage 90.60 (close of review); it has one amendment, Amd 1:2009 [38]. EN ISO 10821:2005+A1:2009 is the European version listed by the UK HSE among textile-machinery safety standards [41].
- Scope: sewing machines, sewing units (head + stand + drive) and sewing systems for professional use in clothing, knitwear, hosiery etc.; it covers hazards from needles, knife trimmers, belt drives, noise, heat, ergonomics and electricity; **it is explicitly not applicable to integrated sewing systems within the scope of ISO 11161 (integrated manufacturing systems)**, nor to large shuttle embroidery machines (ISO 11111) [38][40][41].
- Amd 1:2009 sets minimum control performance per ISO 13849-1: machines whose hazards originate mainly from stitch-forming elements need at least **PL b**; other industrial sewing machines **PL c**; adds marking/documentation and spare-parts requirements; it also carries noise criteria (80 dB keyword) [39].
- Guarding specifics: belt intake points at the drive pulley must be guarded so fingers cannot reach (Annex E); needle guards / finger deflectors, eye-protection shields against needle break on programmable pattern and bartack machines (Annex D) [39][40].
- Fit: the ST05/ST06 heads are bought-in sewing machines (overlock 504/514, coverstitch 406/602, lockstitch 301) and inherit ISO 10821 compliance from their manufacturer; **the cell as a whole falls outside ISO 10821 and inside ISO 11161 + ISO 10218-2**, so the head-level guards (needle guard, belt guard, eye shield) must be retained even though the heads sit inside the cell guard, because a technician reaches them in manual mode.

### F7 · Lint and combustible-dust fire risk: NFPA 660:2025 and NEC Class III

- NFPA 660 (2025 edition, current) consolidates NFPA 61, 484, 652, 654, 655 and 664 into one combustible-dust standard; effective 6 December 2024; the next revision moved to the Fall 2027 cycle [42][43]. NFPA 652 no longer exists as a separate document; its dust-hazard-analysis (DHA) requirement is now in NFPA 660 [43].
- NFPA/NEC terminology: "combustible dust" includes powders, fines, fibers and flyings; **combustible fibers/flyings** (> 500 µm, can form an explosible mixture) are treated as combustible dust (NEC Class II or Zone 20–22 group IIIB-type installations), whereas **ignitible fibers/flyings** (e.g., cotton lint) "do not present a flash-fire or explosion hazard" but "present a fire hazard when in a layer" and lead to NEC **Class III** locations [44].
- NEC 500.5(D) Class III locations "usually include some parts of rayon, cotton, and other textile mills… clothing manufacturing plants" where easily ignitible fibers/flyings are handled; Division 1 where they are handled/manufactured/used, Division 2 where stored [45]. Whether a given sewing/cutting room is classified is an AHJ/owner determination based on accumulation, not automatic.
- Fit: the cutter (ST02) with its vacuum bed and the overlock trimmers (ST05/ST06) generate lint; the white paper already calls for accessible lint collection, cleaning intervals and blockage detection near moving or hot parts (section 16). Design rules derived: (1) lint extraction at the ST02 vacuum exhaust and at each overlock/coverstitch knife with a filter housing outside the hot/electrical zones; (2) ST08 heat press and any motor/drive enclosures rated for lint (IP5x or Type 12) and kept clear of layer accumulation; (3) DHA per NFPA 660 Chapter 7 at the customer site when fibre handling is significant; (4) the cell must not be marketed as suitable for Class III Division 1 areas unless the electrical equipment is listed for it.

### F8 · Noise

- EU workers' noise directive 2003/10/EC: lower exposure action value 80 dB(A) daily/weekly, upper 85 dB(A), exposure limit 87 dB(A) including hearing-protector attenuation [47].
- OSHA 29 CFR 1910.95: permissible exposure limit 90 dBA (8-h TWA, 5 dB exchange rate), action level 85 dBA TWA triggering a hearing conservation program, 140 dB peak impulsive limit [46].
- ISO 10821 Amd 1:2009 adds noise measurement/declaration criteria for sewing machines (ISO 3744/3747, ISO 11204 referenced) [39].
- Fit: a single operator supervising the cell for 12 h is covered by the 8-h TWA rules; the 12-h shift shortens the allowed level (OSHA Table G-16a allows 12.1 h at 87 dBA, 8 h at 90 dBA) [46]. The cell's noise emission must be declared in the instructions (EU) — see F1a below for the Regulation's thresholds.

### F9 · Ergonomics for operator intervention and roll loading

| Name | Version or date | License | Maturity | Fit for this project | Source URL |
|---|---|---|---|---|---|
| ISO 14738:2002 Anthropometric requirements for the design of workstations at machinery | 2002, reviewed and confirmed 2023 (still current) | ISO, CHF 135 | Current (EN ISO 14738:2008 harmonised under the MD) | Working heights, reach and clearance for the ST07 output station, HMI and roll-loading position | https://www.iso.org/standard/27556.html |
| EN 1005-2+A1:2008 Manual handling of machinery and component parts of machinery | 2008 | CEN | Harmonised under MD | Roll loading (ST01) and spare-part handling limits | https://ec.europa.eu/docsroom/documents/9484/attachments/1/translations/en/renditions/native |
| EN 1005-3+A1:2008 Recommended force limits; EN 1005-4+A1:2008 Working postures | 2008 | CEN | Harmonised under MD | Door forces, drawer/buffer handling, HMI reach | same |
| ISO 11228-1:2021 Manual handling — lifting, lowering, carrying | Edition 2, 2021, CHF 204 | ISO | Current | Applies to objects ≥ 3 kg; covers 8-h and up to 12-h working days — directly relevant to the 12-h shift | https://www.iso.org/standard/76820.html |
| ISO 11226:2000 Static working postures | 2000 | ISO | Current (old) | Evaluation of operator posture during recovery tasks | https://webstore.ansi.org/standards/iso/iso112282021 |

Design rules derived (details and roll masses in F9a): roll loading must be mechanically assisted (lift table, cradle or crane) rather than a two-person manual lift; service points (needles, knives, filters, grippers) at 800–1 200 mm height with free access of at least the ISO 14738 clearance; every intervention done from outside the guard or in a dedicated safe mode.

### F10 · Functional safety with AI in the loop: ISO/IEC TR 5469:2024 and what follows

- ISO/IEC TR 5469:2024 "Artificial intelligence — Functional safety and AI systems" (Edition 1, 2024-01, 73 pp., CHF 204; JTC 1/SC 42) is a Technical Report, not a certifiable standard. It covers three situations: AI inside a safety function; non-AI safety functions protecting AI-controlled equipment; AI used to develop safety functions [35].
- Its Clause 6 defines **AI technology classes** and **usage levels**: A1 (AI in a safety-relevant system with automated decision-making), A2 (AI in a safety-relevant system without automated decision-making), B1/B2 (AI only as a development tool), C (AI not part of the safety function but with indirect impact), and **D: AI not part of a safety function and with no impact on it "due to sufficient segregation and behaviour control", e.g., separation through a sandbox or hypervisor** [36]. The TR notes that mature functional-safety standards do not treat AI and that some explicitly forbid it, and that continuous model improvement undermines verification because behaviour "progressively moves away from the rigorously tested, ideally deterministic and repeatable behaviour" [36].
- ISO/IEC TS 22440 (functional safety and AI systems, JWG 4 of SC 42 with IEC TC 65/SC 65A, the IEC 61508 committee) is the normative follow-on being developed from TR 5469 [37]; its publication status is checked in F10a.
- Fit: the white paper's architecture (safety path independent of inference and cloud; "AI never commands safety") maps to **Usage Level D**. The design rule is therefore: the safety PLC (M10/ST09) and its I/O are physically and logically segregated from the inference PC (ST10); AI outputs reach actuators only through the deterministic motion controller and can at most request a stop, never inhibit one. Documented this way, the cell needs no AI-specific conformity assessment under the Machinery Regulation (not Annex I Part A) and the AI stack is not a "safety component" (see F1 and F11).

