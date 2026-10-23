"""Narration and scene plan for the Roll-to-Garment pitch video (about 5.5 minutes).

Sentences are a string (spoken and subtitled as written), a (say, show) pair when the voice
needs a phonetic spelling, or a dict {say, show, at} whose line is cued to a moment in the
scene (seconds). Slide elements carry data-at="k" and appear when sentence k starts.
3D scenes are rendered from the offline viewer (cad/out/cell_viewer_offline.html) at 2x real
speed; segment scenes cut between windows of the simulated cycle, each still at 2x.
Figures: docs/00_PROJECT_MASTER.md sections 2 and 11 (research R13), white paper sections
19-22, sim/results/*.json (robot cycle: sim/results/reach_cycle.json keyframes).
"""
import json, pathlib

RATE = 2.0   # every 3D shot runs at twice real speed
SC = []

def cue(at, say, show=None):
    return dict(at=at, say=say, show=show or say)

def s3d(id, sentences, shot, lowers=()):
    SC.append(dict(id=id, kind="3d", sentences=sentences, shot=shot, lowers=list(lowers)))

def slide(id, sentences, html):
    SC.append(dict(id=id, kind="slide", sentences=sentences, html=html))

def L(a, b, tag, title):
    return dict(a=a, b=b, tag=tag, title=title)

# ---------------------------------------------------------------- opening
s3d("s01", [
    "Fabric goes in one end. A finished, inspected T-shirt comes out the other.",
    ("This is Roll-to-Garment: one guarded machine, directed by A.I., that turns a roll of knit fabric into finished shirts.",
     "This is Roll-to-Garment: one guarded machine, directed by AI, that turns a roll of knit fabric into finished shirts."),
], dict(mode="orbit", c=[3.2, 0.7, -1.5], r=9.6, h=5.2, a0=-62, a1=-30, simT0=40, rate=RATE))

slide("s02", [
    "In the next few minutes: the problem, the machine at work, the software, what our simulations show, and the plan.",
], """
<div class="hero">
  <div class="eyebrow">Investor and partner briefing · October 2026</div>
  <h1>Roll-to-Garment</h1>
  <p class="lede">An AI-directed cell that turns a roll of knit fabric into finished T-shirts</p>
  <div class="chips">
    <span data-at="0">The problem</span><span data-at="0" style="--d:.6s">The machine at work</span><span data-at="0" style="--d:1.4s">The software</span><span data-at="0" style="--d:2s">What simulation shows</span><span data-at="0" style="--d:2.8s">The plan</span>
  </div>
</div>""")

slide("s03", [
    "Almost every T-shirt is sewn by hand, far from where it is sold, in big batches ordered months ahead on a guess.",
    "Small orders cost more, because every new job pays again for setup, cutting and labour.",
    ("And in 2026, U.S. duties on T-shirts from Asia run at roughly 25 to 37 percent, and the duty-free small-parcel exemption ended in August 2025.",
     "And in 2026, US duties on T-shirts from Asia run at roughly 25–37%, and the duty-free small-parcel exemption ended in August 2025."),
    "Local, small-batch production is suddenly valuable. But no machine does it.",
], """
<h2 class="title">The problem</h2>
<div class="grid4">
  <div class="card" data-at="0"><b>Far away</b><span>Cut and sewn by hand, thousands of kilometres from the customer</span></div>
  <div class="card" data-at="0" style="--d:2.2s"><b>Big batches</b><span>Ordered months ahead on a guess</span></div>
  <div class="card" data-at="1"><b>Small orders cost more</b><span>Every new job pays again for setup, cutting and labour</span></div>
  <div class="card hot" data-at="2"><b>25–37 %</b><span>US duties on Asian tees in 2026; small-parcel duty exemption ended Aug 2025</span></div>
</div>
<p class="punch" data-at="3">Local, small-batch production is valuable. No machine does it.</p>
<p class="src">Sources: project research R13; white paper §19</p>""")

slide("s04", [
    "Our research found nobody selling a conventional-stitch, roll-to-garment cell near one hundred thousand dollars.",
    "Our first customers are uniform and teamwear contract sewers, who need re-orders of 50 to 500 pieces in days.",
    ("For scale, the U.S. Defense Logistics Agency obligated about 1.9 billion dollars on clothing and textiles in fiscal 2024.",
     "For scale, the US Defense Logistics Agency obligated about $1.9 billion on clothing and textiles in fiscal 2024."),
], """
<h2 class="title">The opening</h2>
<div class="stats">
  <div class="stat" data-at="0"><b>None</b><span>Conventional-stitch roll-to-garment cells for sale near USD 100k</span></div>
  <div class="stat" data-at="1"><b>50–500</b><span>Piece re-orders that uniform and teamwear sewers need in days</span></div>
  <div class="stat" data-at="2"><b>USD 1.878B</b><span>DLA clothing and textiles obligations, FY2024</span></div>
</div>
<p class="src">Source: project research R13 (DLA FY2024 obligations; market scan)</p>""")

slide("s05", [
    "The target: at least 100 premium T-shirts per 12-hour shift, with one operator, from a cell that sells for about one hundred thousand dollars.",
    "We design for people stepping in. If one shirt in a hundred needs help, a fully hands-off 100-shirt run happens only about 37 percent of the time, so the cell measures every intervention.",
], """
<h2 class="title">The goal</h2>
<div class="stats">
  <div class="stat" data-at="0"><b>100+</b><span>Premium T-shirts per 12-hour shift</span></div>
  <div class="stat" data-at="0" style="--d:2.4s"><b>1</b><span>Operator supervising</span></div>
  <div class="stat" data-at="0" style="--d:4.2s"><b>≈ USD 100k</b><span>Selling price of one cell</span></div>
</div>
<div class="callout" data-at="1"><b>37 %</b><span>Chance a 100-shirt run needs no help at all, if 1 shirt in 100 needs a person. Intervention is designed for and measured.</span></div>
<p class="src">Source: white paper targets (§02, §20)</p>""")

# ---------------------------------------------------------------- the machine at work (2x)
s3d("s06", [
    "Here is the cell, about ten metres by five.",
    "Fabric travels along the back through cutting and extraction, then along the front row through sewing and inspection.",
], dict(mode="path", p=[[3.0, 12.5, 0.6], [2.4, 7.6, 7.2]], t=[[3.0, 0, -1.5], [3.1, 0.4, -1.5]], simT0=60, rate=RATE),
   lowers=[L(0.6, 99, "The cell", "About 10 m × 5 m, one operator")])

# material flow: one continuous 2x shot. simT0 chosen so the gantry's first pick lands at ~11.5 s.
MAT_DUR = 30.0
s3d("s07", [
    cue(0.3, "Now the machine at work, at twice real speed."),
    cue(2.6, "At the back, the roll unwinds with low, steady tension onto the cutter's vacuum bed."),
    cue(7.0, "The knife cuts every panel of the shirt from a single ply of knit."),
    cue(11.4, "The overhead gantry lifts each panel with needle grippers, one ply at a time, and lays the kit out in order on the staging table."),
    cue(21.0, "Sleeves go to their own flat hemming head, so they are hemmed while still flat."),
], dict(mode="keys", hide_guards=True, rate=RATE, segments=[dict(sim0=19.0, sim1=19.0 + RATE * MAT_DUR, keys=[
    dict(at=0.0, p=[-0.3, 2.9, 1.7], t=[0.8, 0.6, -1.7]), dict(at=4.0, p=[-0.1, 2.9, 1.6], t=[0.9, 0.6, -1.8]),
    dict(at=6.5, p=[2.0, 3.4, 1.2], t=[2.6, 0.8, -2.4]), dict(at=9.0, p=[2.3, 3.4, 1.2], t=[2.8, 0.8, -2.4]),
    dict(at=11.2, p=[4.0, 3.6, 1.4], t=[4.2, 1.0, -2.0]), dict(at=20.0, p=[4.6, 3.6, 1.4], t=[4.5, 1.0, -2.0]),
    dict(at=22.5, p=[5.7, 3.4, 1.3], t=[5.1, 1.0, -1.8]), dict(at=MAT_DUR, p=[5.9, 3.3, 1.1], t=[5.3, 1.0, -1.8])])]),
   lowers=[L(0.0, 6.4, "ST01", "Roll handling"), L(6.6, 11.0, "ST02", "Single-ply cutting"),
           L(11.2, 20.6, "ST03–ST04", "Gantry extraction and staging"), L(20.8, MAT_DUR, "ST05", "Flat sleeve hemmer")])

# sewing cycle: nine windows of the simulated robot cycle (sim seconds), each played at 2x.
F1, F2, LOOK = [0.8, 2.4, 2.0], [-0.9, 2.3, 2.0], [0, 0.75, -0.2]
CYCLE = [  # sim0, sim1, follow offset, (tag, title), [(seconds into window, say, show)]
    (0.5, 18.0, F1, ("ST04", "Grasp front and back panels"),
     [(0.3, "Now one full sewing cycle. The U.R. ten E. arm rides a track and grasps the front and back panels.",
            "Now one full sewing cycle. The UR10e arm rides a track and grasps the front and back panels.")]),
    (18.0, 42.0, F2, ("OP-03 · Overlock", "Join both shoulders"),
     [(0.4, "At the overlock, it joins both shoulders.", None),
      (3.6, "Every move is a collision-checked plan from the Moo-Joe-Co simulator, using the real arm's geometry.",
            "Every move is a collision-checked plan from the MuJoCo simulator, using the real arm's geometry.")]),
    (44.0, 68.0, F1, ("OP-05 · Collar module", "Attach the stretched neck rib"),
     [(0.4, "The collar module stretches the rib by the right ratio and sews on the neckband, the hardest seam on a T-shirt.", None)]),
    (77.0, 96.0, F2, ("OP-06 · Coverstitch", "Topstitch the neck"),
     [(0.4, "Then the coverstitch topstitches the neck to keep it flat.", None)]),
    (109.5, 128.5, F1, ("ST04", "Collect sleeves hemmed by the gantry"),
     [(0.4, "It collects both sleeves, already hemmed flat by the gantry-fed hemmer.", None)]),
    (128.5, 158.0, F2, ("OP-08 · Overlock", "Set both sleeves"),
     [(0.4, "Back at the overlock, it sets each sleeve into the armhole, the longest step in the cycle.", None)]),
    (193.5, 216.0, F1, ("OP-09 · Overlock", "Close both sides"),
     [(0.4, "Then it closes both sides.", None),
      (2.8, "Seam times here are estimates from industry tables, until bench tests measure them.", None)]),
    (252.0, 276.0, F2, ("OP-10 · Coverstitch", "Bottom hem"),
     [(0.4, "The coverstitch sews the bottom hem.", None),
      (3.0, "Each shirt takes about 313 seconds of arm time, inside a 328-second budget.", None)]),
    (291.0, 312.8, F1, ("ST07", "Release on the inspection table"),
     [(0.4, "Finally, the shirt goes onto the inspection table, where cameras check every seam, and the arm returns for the next one.", None)]),
]
segs, sents, lows, t = [], [], [], 0.0
for a, b, off, (tag, title), lines in CYCLE:
    n = round((b - a) / RATE * 30)                       # frames in this window
    segs.append(dict(sim0=a, sim1=b, frames=n, keys=[dict(at=0, off=off, look=LOOK)]))
    lows.append(L(t + 0.2, t + n / 30 - 0.1, tag, title))
    sents += [cue(t + at, say, show) for at, say, show in lines]
    t += n / 30
s3d("s08", sents, dict(mode="keys", hide_guards=True, rate=RATE, segments=segs), lowers=lows)

# ---------------------------------------------------------------- software, proof, business, plan
slide("s15", [
    "The software is where most of the value lives.",
    "A designer describes the shirt in plain language. That becomes one garment record, which generates the pattern, packs it onto the fabric, and tunes every step to that fabric.",
    "A compiler turns the garment into sewing operations, a scheduler sequences them, and the skill runtime executes them with perception in the loop.",
    "The same job runs on the digital twin and on the real machine, and every run is logged, including every time a person stepped in.",
], """
<h2 class="title">The software: from conversation to machine</h2>
<div class="flow">
  <div class="node" data-at="1"><i>M01</i>Design workspace<span>Talk or sketch</span></div>
  <div class="node" data-at="1" style="--d:2s"><i>M02</i>Garment record<span>One source of truth</span></div>
  <div class="node" data-at="1" style="--d:4s"><i>M03</i>Pattern engine<span>Parametric panels</span></div>
  <div class="node" data-at="1" style="--d:5.2s"><i>M04</i>Nesting<span>Packs the fabric</span></div>
  <div class="node" data-at="1" style="--d:6.4s"><i>M05</i>Material profiles<span>Tunes every step</span></div>
  <div class="node" data-at="2"><i>M06</i>Assembly compiler<span>Garment → operations</span></div>
  <div class="node" data-at="2" style="--d:1.8s"><i>M07</i>Scheduler<span>Sequences stations</span></div>
  <div class="node" data-at="2" style="--d:3.2s"><i>M08</i>Skill runtime<span>Behaviour trees</span></div>
  <div class="node" data-at="3"><i>M09</i>Motion and hardware<span>Same job: twin or cell</span></div>
</div>
<div class="side">
  <div class="tagx" data-at="2" style="--d:4.4s"><i>M11</i>Perception in the loop</div>
  <div class="tagx" data-at="3" style="--d:1.5s"><i>M13</i>Digital twin</div>
  <div class="tagx" data-at="3" style="--d:3.5s"><i>M14</i>Every run logged, every intervention counted</div>
</div>""")

slide("s16", [
    ("A.I. assistants can read, design and operate jobs through an M.C.P. server.",
     "AI assistants can read, design and operate jobs through an MCP server."),
    ("Approvals stay with people, and an independent hardware safety layer can stop the cell at any time. The A.I. never commands safety.",
     "Approvals stay with people, and an independent hardware safety layer can stop the cell at any time. The AI never commands safety."),
], """
<h2 class="title">Where AI is allowed, and where it is not</h2>
<div class="tiers">
  <div class="tier" data-at="0"><b>Read</b><span>Status, logs, quality data</span></div>
  <div class="tier" data-at="0" style="--d:1.2s"><b>Design-write</b><span>Propose garments, patterns, jobs</span></div>
  <div class="tier" data-at="0" style="--d:2.2s"><b>Operate</b><span>Start and pause approved jobs</span></div>
  <div class="tier lock" data-at="1"><b>Never exposed</b><span>Approvals (people) · Safety (independent hardware, M10)</span></div>
</div>
<p class="src">M12 MCP server · M10 independent safety layer (Software guide)</p>""")

slide("s17", [
    "What do the simulations show today?",
    "The arm needs 313 seconds per shirt against a 328-second budget. It fits, with a 4.7 percent margin, short of our 15 percent target.",
    "Over 300 simulated shifts at 80 percent availability, 79 percent reach 100 shirts, against a 90 percent target.",
    "Seam times and failure rates are still estimates, and fabric behaviour is not simulated. The first bench experiments measure exactly that.",
], """
<h2 class="title">What simulation shows today</h2>
<div class="stats">
  <div class="stat" data-at="1"><b>313 s</b><span>Robot time per shirt, of a 328 s budget (collision-checked, 0 contacts)</span></div>
  <div class="stat warn" data-at="1" style="--d:3.6s"><b>4.7 %</b><span>Time margin · target 15 %</span></div>
  <div class="stat warn" data-at="2"><b>79 %</b><span>Of 300 simulated shifts reach 100 shirts at 80 % availability · target 90 %</span></div>
</div>
<div class="honest" data-at="3">
  <div><b>Simulated</b>Real UR10e and gripper geometry, every move collision-checked (MuJoCo); shift Monte Carlo (SimPy)</div>
  <div><b>Estimated</b>Seam times, regrasp, stoppages and interventions, from industry tables</div>
  <div><b>Not simulated</b>Fabric behaviour. Bench experiments measure it.</div>
</div>
<p class="src">sim/results/reach_cycle.json · sim/results/throughput_des.json</p>""")

slide("s18", [
    "Build-cost scenarios run from 52 to 140 thousand dollars per cell, against a 100 thousand dollar price.",
    "For an operator selling shirts at 12 dollars, the model breaks even near 50 a day, and earns about 74 thousand dollars a year at 100 a day. These are models to be tested, not forecasts.",
], """
<h2 class="title">The economics (model, not forecast)</h2>
<div class="stats two">
  <div class="stat" data-at="0"><b>USD 52–140k</b><span>Build-and-test cost scenarios per cell</span></div>
  <div class="stat" data-at="0" style="--d:3.6s"><b>USD 100k</b><span>Reference selling price</span></div>
  <div class="stat" data-at="1"><b>≈ 50 / day</b><span>Operator break-even at USD 12 per shirt</span></div>
  <div class="stat" data-at="1" style="--d:4.4s"><b>≈ USD 74k / yr</b><span>Operator profit at 100 shirts a day, 250 days</span></div>
</div>
<p class="src">Source: white paper §20–22 (conditional arithmetic, to be replaced by measured cost and yield)</p>""")

slide("s19", [
    "The plan: build the development cell and run three bench experiments: robot-fed overlock, single-ply needle picking, and neckband stretch.",
    "Then film one unattended run, roll to finished shirt, with measured takt time, yield and interventions.",
    "Alongside it, three to five customer letters of intent, and safety certification under way. That is what the seed round funds.",
], """
<h2 class="title">The plan</h2>
<div class="steps">
  <div class="stepx" data-at="0"><i>1</i><b>Development cell</b><span>Build the first cell from the guides</span></div>
  <div class="stepx" data-at="0" style="--d:2.6s"><i>2</i><b>Bench experiments</b><span>Robot-fed overlock · needle pick · neckband stretch</span></div>
  <div class="stepx" data-at="1"><i>3</i><b>Unattended run on video</b><span>Roll to tee, with measured takt, yield, interventions</span></div>
  <div class="stepx" data-at="2"><i>4</i><b>Customers and certification</b><span>3–5 letters of intent · safety certification started</span></div>
</div>
<p class="punch" data-at="2" style="--d:4.5s">That is what the seed round funds.</p>""")

s3d("s20", [
    "Fabric in. T-shirts out. Made close to the customer, in the quantity they actually need.",
    "Roll-to-Garment.",
], dict(mode="orbit", c=[3.2, 0.7, -1.5], r=9.0, h=5.6, a0=-20, a1=-40, simT0=200, rate=RATE))

if __name__ == "__main__":
    for sc in SC:   # segment scenes have a fixed length set by their frames
        if sc["kind"] == "3d" and sc["shot"].get("segments"):
            for sg in sc["shot"]["segments"]:
                sg.setdefault("frames", round((sg["sim1"] - sg["sim0"]) / RATE * 30))
            sc["fixed_frames"] = sum(sg["frames"] for sg in sc["shot"]["segments"])
    out = pathlib.Path(__file__).with_name("scenes.json")
    out.write_text(json.dumps(SC, indent=1), encoding="utf-8")
    words = sum(len((s if isinstance(s, str) else s["show"] if isinstance(s, dict) else s[1]).split()) for sc in SC for s in sc["sentences"])
    print(len(SC), "scenes,", words, "words")
