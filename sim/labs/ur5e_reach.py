"""Reach envelope of a UR5e on his CP-300 pedestal (base on the 700 mm top plate) with the tool pointing down.

Tool: Lab 3 hybrid panel head on a manual quick-change plate; length from flange to the fabric contact
plane taken as TOOL_L (estimate, his guide gives the plate size 400 x 300 but not the stack height).
Prints the largest horizontal radius reachable at each working height (m). MuJoCo Menagerie UR5e geometry.
"""
import numpy as np, mujoco
from robot_descriptions import ur5e_mj_description as urd

TOOL_L = 0.12
BASE_Z = 0.700

def build():
    spec = mujoco.MjSpec.from_file(urd.MJCF_PATH)
    w3 = spec.body("wrist_3_link")
    s = w3.add_site(); s.name = "tcp"; s.pos = [0, 0.0996 + TOOL_L, 0]     # flange is +y of wrist_3 in Menagerie UR5e
    m = spec.compile(); return m, mujoco.MjData(m)

m, d = build()
sid = m.site("tcp").id
def ik(target, q0, iters=200):
    q = q0.copy()
    for _ in range(iters):
        d.qpos[:6] = q; mujoco.mj_kinematics(m, d); mujoco.mj_comPos(m, d)
        p = d.site_xpos[sid]; R = d.site_xmat[sid].reshape(3, 3)
        ez = R[:, 1]                                   # tool axis (site y follows the flange axis)
        err = np.r_[target - p, np.cross(ez, [0, 0, -1])]
        if np.linalg.norm(err[:3]) < 1e-3 and np.linalg.norm(err[3:]) < 1e-3: return q, True
        J = np.zeros((6, m.nv)); mujoco.mj_jacSite(m, d, J[:3], J[3:], sid)
        dq = J.T @ np.linalg.solve(J @ J.T + 1e-3 * np.eye(6), err * np.r_[1, 1, 1, 0.5, 0.5, 0.5])
        q = np.clip(q + dq[:6], m.jnt_range[:6, 0], m.jnt_range[:6, 1])
    return q, False

seeds = [np.array([0, -1.2, 1.5, -1.9, -1.57, 0]), np.array([0, -0.6, 0.9, -1.9, -1.57, 0]), np.array([0, -1.8, 2.2, -2.0, -1.57, 0])]
if __name__ == "__main__":
    for zf in (0.60, 0.85, 0.95, 1.05, 1.20):
        z = zf - BASE_Z; best = 0
        for r in np.arange(0.30, 1.0, 0.01):
            ok = any(ik(np.array([r, 0, z]), s)[1] for s in seeds)
            if ok: best = r
        print(f"work height {zf:.2f} m: max horizontal TCP radius {best:.2f} m")
