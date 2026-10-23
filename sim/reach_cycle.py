"""Sim 1: UR10e reach and ST04 cycle-time study in MuJoCo (kinematic level).

Uses the MuJoCo Menagerie UR10e (BSD-3) placed in the concept cell layout from
cad/concept/cell_concept.py. Targets are tool-centre points (TCP) above each
station work surface with the gripper pointing down. Outputs JSON to sim/results/.
Run: /home/user/.venvs/sim/bin/python sim/reach_cycle.py
"""
import json, math
from pathlib import Path
import numpy as np
import mujoco
from robot_descriptions import ur10e_mj_description as d

OUT = Path(__file__).resolve().parent / "results"; OUT.mkdir(exist_ok=True)
TOOL = 0.17          # Robotiq 2F-85 + coupling length below the flange, m (est.)
APPROACH = 0.05      # TCP height above the work surface, m
PEDESTAL = 0.82      # base height used in the concept model, m

# TCP targets (x, y, surface z) in metres, from the concept layout
TARGETS = {
    "handoff (staging front edge)": (4.30, 1.50, 0.85),
    "overlock needle (ST05)":       (1.95, 0.55, 0.82),
    "collar module (ST06)":         (3.10, 0.55, 0.82),
    "coverstitch needle (ST05)":    (4.25, 0.55, 0.82),
    "inspection table (ST07)":      (5.45, 0.60, 0.84),
}

def build(base_xy):
    spec = mujoco.MjSpec.from_file(d.MJCF_PATH)
    base = spec.worldbody.first_body()
    base.pos = [base_xy[0], base_xy[1], PEDESTAL]
    return spec.compile()

def ik(model, data, target, iters=400):
    """Damped least squares on position + tool-axis-down; returns (err_mm, tilt_deg, q)."""
    site = model.site("attachment_site").id
    goal = np.array(target) + np.array([0, 0, APPROACH + TOOL])
    best = None
    for seed in ([0, -1.57, 1.57, -1.57, -1.57, 0], [math.pi, -1.57, 1.57, -1.57, -1.57, 0],
                 [1.57, -1.2, 1.8, -2.2, -1.57, 0], [-1.57, -1.2, 1.8, -2.2, -1.57, 0]):
        data.qpos[:6] = seed
        for _ in range(iters):
            mujoco.mj_kinematics(model, data); mujoco.mj_comPos(model, data)
            p = data.site_xpos[site]; R = data.site_xmat[site].reshape(3, 3)
            ep = goal - p
            z = R[:, 2]; eo = np.cross(z, np.array([0, 0, -1.0]))  # align tool z with world -z
            jp = np.zeros((3, model.nv)); jr = np.zeros((3, model.nv))
            mujoco.mj_jacSite(model, data, jp, jr, site)
            J = np.vstack([jp, jr])[:, :6]; e = np.concatenate([ep, eo])
            dq = J.T @ np.linalg.solve(J @ J.T + 1e-3 * np.eye(6), e)
            data.qpos[:6] = np.clip(data.qpos[:6] + 0.5 * dq, model.jnt_range[:6, 0], model.jnt_range[:6, 1])
        mujoco.mj_kinematics(model, data)
        err = np.linalg.norm(goal - data.site_xpos[site]) * 1000
        tilt = math.degrees(math.acos(np.clip(-data.site_xmat[site].reshape(3, 3)[2, 2], -1, 1)))
        if best is None or err < best[0]:
            best = (err, tilt, data.qpos[:6].copy())
    return best

def reach_table(base_xy):
    m = build(base_xy); dd = mujoco.MjData(m); rows = {}
    for name, t in TARGETS.items():
        err, tilt, q = ik(m, dd, t)
        dist = math.dist(base_xy, t[:2])
        rows[name] = {"horizontal_distance_m": round(dist, 3), "tcp_error_mm": round(err, 1),
                      "tool_tilt_deg": round(tilt, 1), "reachable": bool(err < 5 and tilt < 5), "q_rad": [round(x, 3) for x in q]}
    return rows

# ---------------- cycle time ----------------
VMAX = np.radians([120, 120, 180, 180, 180, 180])   # UR10e joint speed limits (deg/s) per UR spec sheet
AMAX = np.full(6, 3.0)                                # rad/s^2, conservative (est.)
def move_time(q0, q1, v=VMAX, a=AMAX):
    dq = np.abs(np.array(q1) - np.array(q0))
    t = [2 * math.sqrt(x / ai) if x < vi * vi / ai else x / vi + vi / ai for x, vi, ai in zip(dq, v, a)]
    return max(t) + 0.25  # settle (est.)

def track_time(x0, x1, v=1.0, a=2.0):
    dx = abs(x1 - x0)
    return (2 * math.sqrt(dx / a) if dx < v * v / a else dx / v + v / a)

# Per-shirt presentation sequence for the arm (station, seam/dwell seconds while the arm guides, est.)
SEQ = [("handoff (staging front edge)", 6, "grasp front+back, register"),
       ("overlock needle (ST05)", 15, "OP-03 shoulders"),
       ("collar module (ST06)", 20, "load body for OP-05 rib attach (module sews ~40 s on its own)"),
       ("coverstitch needle (ST05)", 20, "OP-06 neck topstitch"),
       ("handoff (staging front edge)", 6, "grasp sleeves"),
       ("coverstitch needle (ST05)", 24, "OP-07 two sleeve hems"),
       ("overlock needle (ST05)", 50, "OP-08 set two sleeves"),
       ("overlock needle (ST05)", 50, "OP-09 close two sides"),
       ("coverstitch needle (ST05)", 25, "OP-10 bottom hem"),
       ("inspection table (ST07)", 6, "release on inspection table")]
REGRASP = 8.0  # s per handling event: regrasp/align with vision (est.)

def cycle(base_xy=None, track=None):
    """Arm occupancy per shirt. track=(y, x_min, x_max) puts the base on a 7th axis."""
    times, legs = [], []
    pos = None; q = None; tx = None
    for name, dwell, op in SEQ:
        t = TARGETS[name]
        bx = min(max(t[0], track[1]), track[2]) if track else base_xy[0]
        by = track[0] if track else base_xy[1]
        m = build((bx, by)); dd = mujoco.MjData(m)
        err, tilt, q1 = ik(m, dd, t)
        if err > 5: return {"feasible": False, "unreachable": name}
        mv = 0.0 if q is None else move_time(q, q1)
        tr = 0.0 if (tx is None or not track) else track_time(tx, bx)
        leg = max(mv, tr) + dwell + REGRASP
        legs.append({"to": name, "op": op, "move_s": round(max(mv, tr), 2), "dwell_s": dwell, "regrasp_s": REGRASP, "leg_s": round(leg, 1)})
        times.append(leg); q = q1; tx = bx
    return {"feasible": True, "arm_occupancy_s": round(sum(times), 1), "legs": legs}

if __name__ == "__main__":
    fixed = (3.30, 0.90)
    res = {"assumptions": {"tool_length_m": TOOL, "approach_m": APPROACH, "pedestal_m": PEDESTAL,
                           "joint_vmax_deg_s": [120, 120, 180, 180, 180, 180], "joint_amax_rad_s2": 3.0,
                           "regrasp_s": REGRASP, "required_interval_s": 328.3},
           "layout_A_fixed_pedestal": {"base_xy": fixed, "reach": reach_table(fixed)}}
    res["layout_A_fixed_pedestal"]["cycle"] = cycle(base_xy=fixed)
    track = (0.95, 2.0, 5.2)
    res["layout_B_seventh_axis"] = {"track_y": track[0], "track_x": [track[1], track[2]], "cycle": cycle(track=track)}
    (OUT / "reach_cycle.json").write_text(json.dumps(res, indent=1))
    for k, v in res["layout_A_fixed_pedestal"]["reach"].items():
        print(f"A fixed  | {k:32s} dist {v['horizontal_distance_m']:.2f} m  err {v['tcp_error_mm']:7.1f} mm  reachable={v['reachable']}")
    print("A cycle:", {k: v for k, v in res["layout_A_fixed_pedestal"]["cycle"].items() if k != 'legs'})
    cb = res["layout_B_seventh_axis"]["cycle"]
    print("B cycle: feasible", cb["feasible"], "arm occupancy s", cb.get("arm_occupancy_s"), "vs required 328 s")
