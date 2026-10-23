"""Sim 2: discrete-event throughput of a 12-hour shift (SimPy), Monte Carlo.

Stations and occupancy come from spine/takt.csv and sim/results/reach_cycle.json.
Each garment flows cutter -> gantry extraction -> arm presentation (sewing) -> inspection,
with a work-in-process cap. Interventions (a person needed) occur per garment with
probability p and block the arm for a random recovery time; random equipment stops model
availability; 5 % of finished garments fail inspection (white paper yield 0.95).
Run: /home/user/.venvs/sim/bin/python sim/throughput_des.py
"""
import json, random, statistics
from pathlib import Path
import simpy

R = Path(__file__).resolve().parent / "results"
arm_s = json.loads((R / "reach_cycle.json").read_text())["layout_B_seventh_axis"]["cycle"]["arm_occupancy_s"]
SHIFT = 12 * 3600
SCEN = {"Audited layout: track + gantry-fed flat hemmer": arm_s,
        "Without flat hemmer (arm also hems sleeves, +35 s)": arm_s + 35}

def shift(arm_time, p_int, seed, wip=4, mtbf=2 * 3600, mttr=600, rec_mean=180, yield_=0.95):
    rnd = random.Random(seed); env = simpy.Environment()
    cut, gan, arm, insp = (simpy.Resource(env, 1) for _ in range(4))
    slots = simpy.Resource(env, wip); out = {"ok": 0, "rej": 0, "int": 0}
    def jitter(t): return max(1.0, rnd.gauss(t, 0.08 * t))
    def garment(env):
        with slots.request() as s:
            yield s
            for res, t in ((cut, 90), (gan, 120), (arm, arm_time), (insp, 60)):
                with res.request() as r:
                    yield r
                    yield env.timeout(jitter(t))
                    if res is arm and rnd.random() < p_int:
                        out["int"] += 1; yield env.timeout(rnd.expovariate(1 / rec_mean))
            out["ok" if rnd.random() < yield_ else "rej"] += 1
    def source(env):
        while True:
            env.process(garment(env)); yield env.timeout(1)
            while len(slots.queue) > 0: yield env.timeout(5)
    def breakdowns(env):  # whole-cell stops: availability
        while True:
            yield env.timeout(rnd.expovariate(1 / mtbf))
            reqs = [r.request(priority=0) if hasattr(r, 'priority') else r.request() for r in (arm,)]
            for q in reqs: yield q
            yield env.timeout(rnd.expovariate(1 / mttr))
            for res, q in zip((arm,), reqs): res.release(q)
    env.process(source(env)); env.process(breakdowns(env)); env.run(until=SHIFT)
    return out

def run_availability_080():
    out = []
    for name, arm in SCEN.items():
        for p in (0.01, 0.05):
            oks = sorted(shift(arm, p, s, mttr=1800)["ok"] for s in range(300))
            out.append({"scenario": name, "availability_case": "~0.80 (MTBF 2 h, MTTR 30 min)", "p_intervention": p,
                        "mean_accepted": round(statistics.mean(oks), 1), "p10": oks[30], "prob_ge_100": round(sum(o >= 100 for o in oks) / 300, 2)})
            print(out[-1])
    return out

if __name__ == "__main__":
    res = {"assumptions": {"cutter_s": 90, "gantry_s": 120, "inspection_s": 60, "wip_cap": 4, "mtbf_s": 7200, "mttr_s": 600,
                           "intervention_recovery_mean_s": 180, "yield": 0.95, "shifts_per_case": 300}, "cases": []}
    for name, arm_t in SCEN.items():
        for p in (0.0, 0.005, 0.01, 0.02, 0.05):
            oks = []; ints = []
            for s in range(300):
                o = shift(arm_t, p, s); oks.append(o["ok"]); ints.append(o["int"])
            oks.sort()
            row = {"scenario": name, "arm_s": arm_t, "p_intervention": p, "mean_accepted": round(statistics.mean(oks), 1),
                   "p10": oks[30], "p90": oks[270], "prob_ge_100": round(sum(o >= 100 for o in oks) / 300, 2),
                   "mean_interventions": round(statistics.mean(ints), 1)}
            res["cases"].append(row)
            print(f"{name[:44]:44s} p={p:<5} mean {row['mean_accepted']:6.1f}  p10 {row['p10']:4d}  P(>=100) {row['prob_ge_100']:.2f}  interventions {row['mean_interventions']}")
    res["cases_availability_080"] = run_availability_080()
    (R / "throughput_des.json").write_text(json.dumps(res, indent=1))
