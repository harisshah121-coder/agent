"""Sim 1: UR10e reach, collision-checked paths and cycle time in MuJoCo (kinematic level).

What is simulated: the MuJoCo Menagerie UR10e (BSD-3) with the Robotiq 2F-85 (BSD-2) on a
7th-axis track, inside the static cell geometry exported from the CAD model
(sim/results/cell_boxes.json). For every station the robot's joint angles are solved by
inverse kinematics; every move between stations is swept in small steps and checked for
contact between the robot's collision geometry and the cell. Moves that collide are re-planned
through lifted via-poses. Move times use UR10e joint speed limits.

What is NOT simulated (inputs are estimates): seam durations, regrasp time, fabric behaviour.
Outputs: sim/results/reach_cycle.json (consumed by throughput_des.py and export_ur_rig.py).
Run: /home/user/.venvs/sim/bin/python sim/reach_cycle.py
"""
import json, math
from pathlib import Path
import numpy as np
import mujoco
from robot_descriptions import ur10e_mj_description as urd
from robot_descriptions import robotiq_2f85_mj_description as gd

R = Path(__file__).resolve().parent / "results"; R.mkdir(exist_ok=True)
TOOL = 0.17          # flange to fingertip centre of the 2F-85, m (est.)
APPROACH = 0.05      # TCP height above the work surface at a station, m
PEDESTAL_Z = 0.82
TRACK_Y, TRACK_X = 0.94, (1.91, 5.09)
FIXED = (3.30, 0.94)  # fixed-pedestal alternative tested for reach

# Presentation points: free table area behind each head (robot side), from cad/concept/cell_concept.py
TARGETS = {
    "handoff (staging front edge)": (4.85, 1.50, 0.85),
    "overlock (ST05)":              (1.95, 0.70, 0.79),
    "collar module (ST06)":         (3.15, 0.70, 0.79),
    "coverstitch (ST05)":           (4.35, 0.70, 0.79),
    "inspection table (ST07)":      (5.50, 0.62, 0.84),
}
SEQ = [  # (station, dwell s while the arm guides/holds, operation) — dwell values are estimates (R16 F1, F9)
    ("handoff (staging front edge)", 6, "Grasp front and back panels, register on the backlit table"),
    ("overlock (ST05)", 15, "OP-03 Join both shoulders"),
    ("collar module (ST06)", 20, "OP-05 Load body; module attaches the stretched neck rib"),
    ("coverstitch (ST05)", 20, "OP-06 Neck topstitch"),
    ("handoff (staging front edge)", 6, "Grasp both sleeves, already hemmed flat by the gantry-fed hemmer"),
    ("overlock (ST05)", 50, "OP-08 Set both sleeves"),
    ("overlock (ST05)", 50, "OP-09 Close both sides"),
    ("coverstitch (ST05)", 25, "OP-10 Bottom hem"),
    ("inspection table (ST07)", 6, "Release the shirt on the inspection table"),
]
REGRASP = 8.0                                      # s per handling event (est.)
VMAX = np.radians([120, 120, 180, 180, 180, 180])  # UR10e joint speed limits
AMAX = np.full(6, 3.0)                             # rad/s^2 (est.)
STEPS = 80                                         # sweep samples per move

def build(track=True):
    spec = mujoco.MjSpec()
    spec.option.timestep = 0.002
    wb = spec.worldbody
    wb.add_geom(type=mujoco.mjtGeom.mjGEOM_PLANE, size=[10, 10, 0.1], contype=0, conaffinity=1, name="floor")
    for i, b in enumerate(json.loads((R / "cell_boxes.json").read_text())):
        wb.add_geom(type=mujoco.mjtGeom.mjGEOM_BOX, pos=b["c"], size=b["h"], contype=0, conaffinity=1, name=f"obs{i}")
    car = wb.add_body(name="carriage", pos=[0, TRACK_Y, PEDESTAL_Z])
    car.add_joint(name="track", type=mujoco.mjtJoint.mjJNT_SLIDE, axis=[1, 0, 0], range=[0, 7])
    ur = mujoco.MjSpec.from_file(urd.MJCF_PATH)
    g = mujoco.MjSpec.from_file(gd.MJCF_PATH)
    ur.site("attachment_site").attach_body(g.worldbody.first_body(), "g_", "")
    car.add_frame().attach_body(ur.worldbody.first_body(), "ur_", "")
    m = spec.compile()
    names = json.loads((R / "cell_boxes.json").read_text())
    return m, [b["name"] for b in names]

M, OBS = build()
D = mujoco.MjData(M)
SITE = M.site("ur_attachment_site").id
ARM = [M.joint(f"ur_{n}").qposadr[0] for n in ("shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint")]
TRK = M.joint("track").qposadr[0]
ROBOT_BODIES = {b for b in range(M.nbody) if M.body(b).name.startswith(("ur_", "g_")) or M.body(b).name == "carriage"}
OBS_GEOMS = {M.geom(f"obs{i}").id: n for i, n in enumerate(OBS)} | {M.geom("floor").id: "floor"}

def set_pose(x, q):
    D.qpos[:] = 0; D.qpos[TRK] = x; D.qpos[ARM] = q
    mujoco.mj_forward(M, D)

def contacts():
    hits = []
    for c in D.contact[:D.ncon]:
        a, b = c.geom1, c.geom2
        for o, r in ((a, b), (b, a)):
            if o in OBS_GEOMS and M.geom_bodyid[r] in ROBOT_BODIES and c.dist < -0.002:
                hits.append((OBS_GEOMS[o], M.body(M.geom_bodyid[r]).name, round(float(c.dist) * 1000, 1)))
    return hits

def ik(x_base, target, lift=0.0):
    """Position + tool-axis-down IK for the arm with the track fixed at x_base."""
    goal = np.array(target) + np.array([0, 0, APPROACH + TOOL + lift])
    best = None
    for seed in ([0, -1.57, 1.57, -1.57, -1.57, 0], [math.pi, -1.57, 1.57, -1.57, -1.57, 0],
                 [1.57, -1.3, 1.9, -2.2, -1.57, 0], [-1.57, -1.3, 1.9, -2.2, -1.57, 0]):
        q = np.array(seed, float)
        for _ in range(300):
            set_pose(x_base, q)
            p = D.site_xpos[SITE]; Rm = D.site_xmat[SITE].reshape(3, 3)
            e = np.concatenate([goal - p, np.cross(Rm[:, 2], [0, 0, -1.0])])
            jp = np.zeros((3, M.nv)); jr = np.zeros((3, M.nv)); mujoco.mj_jacSite(M, D, jp, jr, SITE)
            J = np.vstack([jp, jr])[:, [M.jnt_dofadr[M.joint(f'ur_{n}').id] for n in ("shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint")]]
            q = np.clip(q + 0.5 * J.T @ np.linalg.solve(J @ J.T + 1e-3 * np.eye(6), e), -2 * math.pi, 2 * math.pi)
        set_pose(x_base, q)
        err = float(np.linalg.norm(goal - D.site_xpos[SITE]) * 1000)
        tilt = math.degrees(math.acos(np.clip(-D.site_xmat[SITE].reshape(3, 3)[2, 2], -1, 1)))
        hit = contacts()
        score = err + (1000 if hit else 0)
        if best is None or score < best[0]:
            best = (score, err, tilt, q.copy(), hit)
    return {"err_mm": round(best[1], 1), "tilt_deg": round(best[2], 1), "q": best[3], "hits": best[4]}

def base_for(t):
    return min(max(t[0], TRACK_X[0]), TRACK_X[1])

def move_time(q0, q1, x0, x1):
    dq = np.abs(np.array(q1) - np.array(q0))
    tj = max(2 * math.sqrt(d / a) if d < v * v / a else d / v + v / a for d, v, a in zip(dq, VMAX, AMAX))
    dx = abs(x1 - x0); tt = 2 * math.sqrt(dx / 2.0) if dx < 0.5 else dx / 1.0 + 0.5  # track 1 m/s, 2 m/s^2
    return max(tj, tt) + 0.25

def sweep(a, b):
    """Check a smoothstep joint-space move between poses a and b; return list of hits."""
    hits = []
    for k in range(1, STEPS + 1):
        u = k / STEPS; e = u * u * (3 - 2 * u)
        set_pose(a["x"] + (b["x"] - a["x"]) * e, a["q"] + (b["q"] - a["q"]) * e)
        h = contacts()
        if h: hits.append((round(u, 2), h[0]))
    return hits

BASE_X = {}  # chosen track position per station (searched once, then reused for lifts)
def pose(station, lift=0.0):
    t = TARGETS[station]
    if station not in BASE_X:
        for off in (0.0, -0.35, 0.35, -0.55, 0.55, -0.75, 0.75):
            x = min(max(t[0] + off, TRACK_X[0]), TRACK_X[1]); s = ik(x, t)
            if s["err_mm"] < 5 and s["tilt_deg"] < 5 and not s["hits"]:
                BASE_X[station] = x; break
        else:
            BASE_X[station] = base_for(t)
    x = BASE_X[station]; s = ik(x, t, lift)
    return {"station": station, "x": x, "q": s["q"], "err_mm": s["err_mm"], "tilt": s["tilt_deg"], "hits": s["hits"], "lift": lift}

TUCK_Q = None
def tuck(x):
    """Compact transit pose with ONE fixed joint configuration (tool down, TCP 0.5 m ahead of the base over the
    track centreline, 1.45 m high), so a track move is a pure translation along the rail."""
    global TUCK_Q
    if TUCK_Q is None:
        # found by a search over candidate poses: collision-free at every track position (2026-10-23)
        for dx, z in ((0.5, 1.45), (0.5, 1.35), (0.5, 1.25)):
            s = ik(3.0, (3.0 + dx, TRACK_Y, z - APPROACH - TOOL))
            if s["err_mm"] < 5 and not s["hits"]:
                TUCK_Q = s["q"]; break
    if TUCK_Q is None: return None
    set_pose(x, TUCK_Q)
    if contacts(): return None
    return {"station": "tuck", "x": x, "q": TUCK_Q.copy(), "err_mm": 0.0, "tilt": 0.0, "hits": [], "lift": -1}

def candidates(a_station, b_station, dst):
    """Paths from the pose at station a to dst at station b, simplest first."""
    yield [dst]
    for lift in (0.25, 0.45):
        yield [pose(a_station, lift), pose(b_station, lift), dst]
    la, lb = pose(a_station, 0.3), pose(b_station, 0.3)
    ta, tb = tuck(la["x"]), tuck(lb["x"])
    if ta and tb:
        yield [la, ta, tb, lb, dst]

JN = ("shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint")
DOFS = None
def ik_seeded(x, tcp, q0, iters=60):
    """IK for a TCP point (tool down) starting from q0, for continuous Cartesian paths."""
    global DOFS
    if DOFS is None: DOFS = [M.jnt_dofadr[M.joint(f"ur_{n}").id] for n in JN]
    goal = np.array(tcp) + np.array([0, 0, TOOL]); q = np.array(q0, float)
    for _ in range(iters):
        set_pose(x, q)
        p = D.site_xpos[SITE]; Rm = D.site_xmat[SITE].reshape(3, 3)
        e = np.concatenate([goal - p, np.cross(Rm[:, 2], [0, 0, -1.0])])
        if np.linalg.norm(e[:3]) < 2e-4 and np.linalg.norm(e[3:]) < 2e-3: break
        jp = np.zeros((3, M.nv)); jr = np.zeros((3, M.nv)); mujoco.mj_jacSite(M, D, jp, jr, SITE)
        J = np.vstack([jp, jr])[:, DOFS]
        q = q + J.T @ np.linalg.solve(J @ J.T + 1e-4 * np.eye(6), e)
    set_pose(x, q)
    return q, float(np.linalg.norm(goal - D.site_xpos[SITE]) * 1000)

def tcp_of(x, q):
    set_pose(x, q); return D.site_xpos[SITE].copy() - np.array([0, 0, TOOL])

def cart(x, q0, p1, n=24):
    """Straight-line TCP move at fixed track position; returns joint waypoints or None if any point fails."""
    p0 = tcp_of(x, q0); out = []; q = q0
    for k in range(1, n + 1):
        q_new, err = ik_seeded(x, p0 + (np.array(p1) - p0) * k / n, q)
        if err > 3 or np.max(np.abs(q_new - q)) > 0.6 or contacts(): return None
        out.append(q_new); q = q_new
    return out

def slide(q, x0, x1):
    """Track move with the arm frozen; collision-checked along the way."""
    for k in range(STEPS + 1):
        set_pose(x0 + (x1 - x0) * k / STEPS, q)
        if contacts(): return False
    return True

def path_time(qs, x0=None, x1=None):
    t = sum(float(np.max(np.abs(np.array(b) - np.array(a)) / VMAX)) for a, b in zip(qs, qs[1:]))
    return t + 0.6 + 0.25 if len(qs) > 1 else 0.0

def leg(a, b_station):
    """Plan from pose a (dict with x, q) to station b, trying several track positions for b."""
    t0 = TARGETS[b_station][0]
    xs = []
    for off in (0.0, -0.35, 0.35, -0.55, 0.55, -0.75, 0.75):
        x = round(min(max(t0 + off, TRACK_X[0]), TRACK_X[1]), 3)
        if x not in xs: xs.append(x)
    for xb in xs:
        BASE_X[b_station] = xb
        r = leg_at(a, b_station)
        if r: return r
    return None

def leg_at(a, b_station):
    b = pose(b_station)
    if b["err_mm"] > 5 or b["hits"]: return None
    if abs(a["x"] - b["x"]) < 1e-6 and not sweep(a, b):
        return [(b["x"], b["q"], "end")], move_time(a["q"], b["q"], a["x"], b["x"]), "direct"
    ta = TARGETS[a["station"]]; tb = TARGETS[b_station]
    for z_tr in (1.45, 1.35, 1.25):
        up = cart(a["x"], a["q"], (*tcp_of(a["x"], a["q"])[:2], ta[2] + APPROACH + 0.30))
        if up is None: continue
        ret = cart(a["x"], up[-1], (a["x"] + 0.5, TRACK_Y, z_tr))
        if ret is None: continue
        q_tr = ret[-1]
        if not slide(q_tr, a["x"], b["x"]): continue
        out = cart(b["x"], q_tr, (tb[0], tb[1], tb[2] + APPROACH + 0.30))
        if out is None: continue
        down = cart(b["x"], out[-1], (tb[0], tb[1], tb[2] + APPROACH))
        if down is None: continue
        t1 = path_time([a["q"]] + up + ret); t2 = abs(b["x"] - a["x"]) / 1.0 + 0.5; t3 = path_time([q_tr] + out + down)
        wps = [(a["x"], q, "w") for q in up + ret] + [(b["x"], q_tr, "slide")] + [(b["x"], q, "w") for q in out] + [(b["x"], q, "w") for q in down[:-1]] + [(b["x"], down[-1], "end")]
        return wps, t1 + t2 + t3, f"lift-retract-slide-reach (transit z {z_tr} m)"
    return None

def plan():
    """Plan the cycle, then re-plan from the configuration the cycle ends in, so the loop closes continuously."""
    r = plan_from(None)
    for _ in range(3):
        if not r.get("feasible"): return r
        end = r.pop("_end")
        r2 = plan_from(end)
        if not r2.get("feasible"): return r2
        e2 = r2["_end"]
        if abs(e2["x"] - end["x"]) < 1e-6 and float(np.max(np.abs(e2["q"] - end["q"]))) < 0.02:
            r2.pop("_end"); kf = r2["keyframes"]
            kf[0]["move_s"] = kf[-1]["move_s"]; kf.pop()          # the last frame equals the first: loop closes
            r2["replay_check"] = verify(kf); r2["loop_closed"] = True
            return r2
        r = r2
    r.pop("_end", None); r["loop_closed"] = False; return r

def plan_from(start):
    keyframes, legs, total = [], [], 0.0
    if start is None:
        first = pose(SEQ[0][0])
        if first["err_mm"] > 5 or first["hits"]: return {"feasible": False, "station": SEQ[0][0], "hits": first["hits"]}
        cur = {"station": SEQ[0][0], "x": first["x"], "q": first["q"]}
    else:
        cur = dict(start)
    keyframes.append({"to": SEQ[0][0], "op": SEQ[0][2], "base_x": round(cur["x"], 4), "q": [round(float(v), 4) for v in cur["q"]], "move_s": 0.0, "dwell_s": SEQ[0][1] + REGRASP, "linear": False})
    total += SEQ[0][1] + REGRASP
    legs.append({"to": SEQ[0][0], "op": SEQ[0][2], "kind": "start", "move_s": 0.0, "dwell_s": SEQ[0][1], "regrasp_s": REGRASP, "leg_s": SEQ[0][1] + REGRASP})
    for station, dwell, op in SEQ[1:] + [(SEQ[0][0], None, "Return to staging for the next shirt")]:
        r = leg(cur, station)
        if r is None: return {"feasible": False, "station": station, "reason": "no collision-free path found"}
        wps, secs, kind = r
        # distribute the leg time over waypoints by joint travel
        qs = [cur["q"]] + [w[1] for w in wps]; xs = [cur["x"]] + [w[0] for w in wps]
        d = [max(float(np.max(np.abs(qs[i + 1] - qs[i]) / VMAX)), abs(xs[i + 1] - xs[i]) / 1.0) + 1e-3 for i in range(len(wps))]
        sc = secs / sum(d)
        for i, (x, q, flag) in enumerate(wps):
            last = i == len(wps) - 1
            keyframes.append({"to": station if last else ("track transit" if flag == "slide" else "moving"), "op": op,
                              "base_x": round(x, 4), "q": [round(float(v), 4) for v in q], "move_s": round(d[i] * sc, 3),
                              "dwell_s": (dwell + REGRASP) if (last and dwell is not None) else 0.0, "linear": not last})
        total += secs + ((dwell + REGRASP) if dwell is not None else 0.0)
        legs.append({"to": station, "op": op, "kind": kind, "move_s": round(secs, 2), "dwell_s": dwell or 0, "regrasp_s": REGRASP if dwell is not None else 0,
                     "leg_s": round(secs + ((dwell + REGRASP) if dwell is not None else 0), 1)})
        cur = {"station": station, "x": wps[-1][0], "q": wps[-1][1]}
    return {"feasible": True, "arm_occupancy_s": round(float(total), 1), "legs": legs, "keyframes": keyframes, "_end": dict(cur),
            "checks": {"obstacles": len(OBS), "sweep_samples_per_joint_move": STEPS, "cartesian_waypoints_per_segment": 24}}

def verify(keyframes, per_second=40):
    """Replay the keyframes exactly as the viewer interpolates them and count robot-cell contacts."""
    n_samples, hits = 0, []
    for i, k in enumerate(keyframes):
        prev = keyframes[i - 1]
        steps = max(4, int(k["move_s"] * per_second))
        for s_ in range(1, steps + 1):
            u = s_ / steps; e = u if k.get("linear") else u * u * (3 - 2 * u)
            q = np.array(prev["q"]) + (np.array(k["q"]) - np.array(prev["q"])) * e
            set_pose(prev["base_x"] + (k["base_x"] - prev["base_x"]) * e, q); n_samples += 1
            h = contacts()
            if h: hits.append({"frame": i, "u": round(u, 2), "hit": h[0]})
    return {"samples": n_samples, "contacts": len(hits), "first": hits[:3]}

def reach_fixed():
    rows = {}
    for name, t in TARGETS.items():
        s = ik(FIXED[0], t)
        rows[name] = {"horizontal_distance_m": round(math.dist(FIXED, t[:2]), 3), "tcp_error_mm": s["err_mm"],
                      "reachable": bool(s["err_mm"] < 5 and s["tilt_deg"] < 5 and not s["hits"]), "collisions": s["hits"][:2]}
    return rows

if __name__ == "__main__":
    res = {"what_is_simulated": "UR10e + Robotiq 2F-85 kinematics (MuJoCo Menagerie) on a 7th-axis track inside the static CAD cell geometry; IK per station; every move swept and collision-checked; joint-speed-limited timing",
           "inputs_that_are_estimates": ["seam/dwell times per operation (R16 SAM tables, not measured)", "regrasp time 8 s", "joint acceleration 3 rad/s^2", "gripper length 0.17 m"],
           "assumptions": {"required_interval_s": 328.3, "regrasp_s": REGRASP},
           "layout_A_fixed_pedestal": {"base_xy": FIXED, "reach": reach_fixed()},
           "layout_B_seventh_axis": {"track_y": TRACK_Y, "track_x": list(TRACK_X), "cycle": plan()}}
    (R / "reach_cycle.json").write_text(json.dumps(res, indent=1))
    for k, v in res["layout_A_fixed_pedestal"]["reach"].items():
        print(f"fixed pedestal | {k:30s} dist {v['horizontal_distance_m']:.2f} m reachable={v['reachable']} err={v['tcp_error_mm']} mm")
    c = res["layout_B_seventh_axis"]["cycle"]
    print("track: feasible", c["feasible"], {k: v for k, v in c.items() if k in ("arm_occupancy_s", "station", "reason", "hits")})
    if c.get("legs"):
        for l in c["legs"]: print(f"  {l['to']:30s} {l['kind']:42s} move {l['move_s']:5.1f}s  leg {l['leg_s']:5.1f}s")
        v = c["replay_check"]; print("replay check:", v)
