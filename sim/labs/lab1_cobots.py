"""Lab 1 Stage 1 bench area: two UR5e-class cobots on his CP-300 pedestals, reach and motion check.

Inputs: cad/labs/lab1/out/lab1_layout.json and lab1_boxes.json (from his STEP parts, build_model.py).
Tasks come from his rig descriptions (Lab Build Packages pages 2, 16-19). Every task point is solved with
damped-least-squares IK (tool pointing down, yaw free); every move is joint-interpolated and checked for
contact against all fixed parts and the other arm. A task that no collision-free solution reaches is reported
as OUT OF REACH, never animated.
Outputs: sim/results/lab1_cobots.json (reach table, keyframes for the viewer), cad/labs/lab1/out/ur5e_rig.glb.
Run: /home/user/.venvs/sim/bin/python sim/labs/lab1_cobots.py
"""
import json, pathlib
import numpy as np, mujoco, trimesh
from robot_descriptions import ur5e_mj_description as urd

ROOT = pathlib.Path(__file__).resolve().parents[2]
LAB = ROOT / "cad/labs/lab1/out"
lay = json.loads((LAB / "lab1_layout.json").read_text())
boxes = json.loads((LAB / "lab1_boxes.json").read_text())
TOOL_L = 0.12            # flange to fabric plane (estimate: quick-change plate + hybrid head stack)
HEADS = {"A": (0.40, 0.30), "B": (0.30, 0.06)}   # Lab 3: hybrid panel head plate 400 x 300 on A; hem-pull bar 300 mm on B (his guide)
HOVER = 0.03             # TCP above the work surface when placing or picking

def build():
    w = mujoco.MjSpec()
    w.option.timestep = 0.002
    for i, b in enumerate(boxes):
        lo, hi = np.array(b["min"]), np.array(b["max"])
        if "floor" in b["name"]: continue
        g = w.worldbody.add_geom(); g.type = mujoco.mjtGeom.mjGEOM_BOX
        g.size = np.maximum((hi - lo) / 2 - 0.002, 0.001); g.pos = (hi + lo) / 2
        g.contype, g.conaffinity = 0, 1; g.name = f"obs{i}:" + b["name"][-60:]
    # folding table moving leaf at 0 deg (his FTMOVE parts are excluded from the static boxes)
    mv = np.array(lay["folding_table"]["moving"]); lo, hi = mv.min(0), mv.max(0)
    g = w.worldbody.add_geom(); g.type = mujoco.mjtGeom.mjGEOM_BOX; g.name = "obs:moving leaf at 0 deg"
    g.size = [(hi[0] - lo[0]) / 2, (hi[1] - lo[1]) / 2, 0.054]; g.pos = [(hi[0] + lo[0]) / 2, (hi[1] + lo[1]) / 2, 0.796]
    g.contype, g.conaffinity = 0, 1
    for k, c in lay["cobots"].items():
        ur = mujoco.MjSpec.from_file(urd.MJCF_PATH)
        w3 = ur.body("wrist_3_link")
        s = w3.add_site(); s.name = "tcp"; s.pos = [0, 0.0996 + TOOL_L, 0]
        hg = w3.add_geom(); hg.type = mujoco.mjtGeom.mjGEOM_BOX; hg.name = "head"
        hg.size = [HEADS[k][0] / 2, 0.02, HEADS[k][1] / 2]; hg.pos = [0, 0.0996 + TOOL_L - 0.02, 0]
        qc = w3.add_geom(); qc.type = mujoco.mjtGeom.mjGEOM_CYLINDER; qc.name = "qc"
        qc.size = [0.04, (TOOL_L - 0.04) / 2, 0]; qc.pos = [0, 0.0996 + (TOOL_L - 0.04) / 2, 0]; qc.quat = [0.7071068, 0.7071068, 0, 0]
        f = w.worldbody.add_frame(); f.pos = c["base"]
        f.attach_body(ur.worldbody.first_body(), f"{k}_", "")
    m = w.compile(); return m, mujoco.MjData(m)

m, d = build()
ROB = {k: dict(qadr=[m.jnt_qposadr[m.joint(f"{k}_{j}").id] for j in ("shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint")],
               dof=[m.jnt_dofadr[m.joint(f"{k}_{j}").id] for j in ("shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint")],
               site=m.site(f"{k}_tcp").id) for k in lay["cobots"]}
robot_geoms = {k: {i for i in range(m.ngeom) if m.body(m.geom_bodyid[i]).name.startswith(f"{k}_")} for k in ROB}
LO, HI = m.jnt_range[:, 0].copy(), m.jnt_range[:, 1].copy()
for k in ROB:   # search natural elbow-up configurations only
    a = ROB[k]["qadr"]; LO[a[1]], HI[a[1]] = -np.pi, 0.0; LO[a[2]], HI[a[2]] = -np.pi, np.pi

def set_q(k, q): d.qpos[ROB[k]["qadr"]] = q

def contacts():
    mujoco.mj_forward(m, d); out = []
    for c in d.contact[:d.ncon]:
        if c.dist > -0.001: continue
        n1, n2 = m.geom(c.geom1).name, m.geom(c.geom2).name
        out.append((n1 or str(c.geom1), n2 or str(c.geom2)))
    return out

def ik(k, target, q0, iters=600):
    r = ROB[k]; q = q0.copy()
    for _ in range(iters):
        set_q(k, q); mujoco.mj_kinematics(m, d); mujoco.mj_comPos(m, d)
        p = d.site_xpos[r["site"]]; R = d.site_xmat[r["site"]].reshape(3, 3)
        err = np.r_[target - p, np.cross(R[:, 1], [0, 0, -1])]
        if np.linalg.norm(err[:3]) < 1e-3 and np.linalg.norm(err[3:]) < 2e-3: return q, True
        J = np.zeros((6, m.nv)); mujoco.mj_jacSite(m, d, J[:3], J[3:], r["site"])
        J = J[:, r["dof"]]
        dq = J.T @ np.linalg.solve(J @ J.T + 2e-3 * np.eye(6), err * np.r_[1, 1, 1, 0.6, 0.6, 0.6])
        n = np.abs(dq).max()
        if n > 0.15: dq *= 0.15 / n
        q = np.clip(q + dq, LO[r["qadr"]], HI[r["qadr"]])
    return q, False

def solve(k, target, prefer):
    """Collision-free IK nearest to 'prefer'; tries several seeds (elbow up, base yaw toward the target)."""
    base = np.array(lay["cobots"][k]["base"]); yaw = np.arctan2(target[1] - base[1], target[0] - base[0]) + np.pi   # UR zero pan faces away
    seeds = [prefer] + [np.array([yaw + o, -1.3, 1.6, -1.9, -1.5708, 0]) for o in (0, 0.4, -0.4)] + \
            [np.array([yaw, a, b, -np.pi / 2 - a - b, -1.5708, 0]) for a, b in ((-0.8, 1.0), (-1.8, 2.3), (-1.0, 1.9))]
    best = None
    for s in seeds:
        q, ok = ik(k, target, s)
        if not ok: continue
        set_q(k, q)
        bad = [c for c in contacts() if hits(k, c)]
        if bad: continue
        cost = np.abs(q - prefer).sum()
        if best is None or cost < best[1]: best = (q, cost)
    return None if best is None else best[0]

def ROB_GEOMNAME(k, n):
    try: gid = m.geom(n).id
    except Exception: gid = int(n) if str(n).isdigit() else -1
    return gid in robot_geoms[k]

def hits(k, c):
    a, b = ROB_GEOMNAME(k, c[0]), ROB_GEOMNAME(k, c[1])
    return a != b            # this arm against anything that is not itself (self-contact of the tool stack ignored)

def path_ok(k, qa, qb, n=40):
    for t in np.linspace(0, 1, n):
        set_q(k, qa + (qb - qa) * t)
        if [c for c in contacts() if hits(k, c)]: return False
    return True

TUCK = np.array([0.0, -1.9, 2.2, -1.9, -1.5708, 0.0])
def tuck(k, yaw): q = TUCK.copy(); q[0] = yaw; return q

# ---------------------------------------------------------------- tasks from his rig descriptions
rt = np.array(lay["registration_table"]); fx = np.array(lay["folding_table"]["fixed"]); form = np.array(lay["collar_form"])
z_rt, z_ft = 0.850 + HOVER, 0.850 + HOVER
TASKS = {
    "A": [
        ("Rig A: lift one ply in the pick zone of the registration table", [2.00, 2.05, z_rt]),
        ("Rig A: place the panel in the live zone (2 mm tolerance)", [2.30, 2.15, z_rt]),
        ("Rig B step 1: carry the butterfly from the registration table", [2.15, 2.15, z_rt]),
        ("Rig B step 1: drape the butterfly over the cradle cone", [form[0], form[1], form[2] + 0.08]),
        ("Rig C: lay the hemmed butterfly on the folding table, shoulder line on the hinge", [float(np.mean(fx[:, 0])) + 0.39, float(np.mean(fx[:, 1])), z_ft]),
    ],
    "B": [
        ("Rig B step 2: lift the folded rib loop off the Lab 2 peg", [3.35, 0.85, 1.05]),
        ("Rig B step 2: lower the rib loop over the form", [form[0], form[1], form[2] + 0.10]),
        ("Rig C: edge-pinch the top layer at the side-seam line", [4.10, 1.90, z_ft + 0.004]),
        ("Rig D: grip the body hem at the fixed leaf edge", [3.72, 1.60, z_ft]),
        ("Rig D: present the hem at the turning tube mouth", [3.25, 1.80, 1.02]),
    ],
}

out = dict(note="Positions provisional (his package has no cell layout); tasks from his rig descriptions; UR5e geometry from MuJoCo Menagerie; tool stack length estimated.",
           tool_length_m=TOOL_L, reach={}, keyframes={})
for k in ROB:
    base = np.array(lay["cobots"][k]["base"])
    set_q(k, tuck(k, 1.5708))
for k in ROB:
    base = np.array(lay["cobots"][k]["base"]); prev = tuck(k, 1.5708); rows, frames, t = [], [dict(t=0.0, q=prev.tolist(), task="park")], 0.0
    other = [o for o in ROB if o != k]
    for name, p in TASKS[k]:
        p = np.array(p, float); dist = float(np.linalg.norm(p[:2] - base[:2]))
        q = solve(k, p, prev); qh = None
        if q is not None:
            for up in (0.12, 0.08, 0.05):            # approach pose straight above the target
                qh = solve(k, p + [0, 0, up], q)
                if qh is not None: break
        ok = q is not None and qh is not None
        moved = False
        if ok:
            # route: current -> tuck(yaw) -> above target -> target, each segment collision-checked
            yaw = qh[0]
            routes = [([tuck(k, prev[0]), tuck(k, yaw), qh, q], (1.2, 1.4, 1.6, 0.8)),
                      ([qh, q], (2.4, 0.8)),
                      ([tuck(k, yaw), qh, q], (2.0, 1.6, 0.8))]
            route = next((r for r in routes if all(path_ok(k, a, b) for a, b in zip([prev] + r[0][:-1], r[0]))), None)
            if route:
                for v, dur in zip(*route):
                    t += dur; frames.append(dict(t=round(t, 2), q=v.tolist(), task=name))
                t += 1.0; frames.append(dict(t=round(t, 2), q=q.tolist(), task=name + " (dwell)"))
                t += 0.8; frames.append(dict(t=round(t, 2), q=qh.tolist(), task=name + " (lift)"))
                prev = qh; moved = True
        rows.append(dict(task=name, point=[round(x, 3) for x in p], horizontal_distance_m=round(dist, 3),
                         status="reached, collision-free" if moved else ("IK reached but path blocked" if ok else "OUT OF REACH")))
        set_q(k, prev)
    t += 1.5; frames.append(dict(t=round(t, 2), q=tuck(k, 1.5708).tolist(), task="park"))
    out["reach"][k] = rows; out["keyframes"][k] = frames
    set_q(k, tuck(k, 1.5708))

(ROOT / "sim/results").mkdir(exist_ok=True)
(ROOT / "sim/results/lab1_cobots.json").write_text(json.dumps(out, indent=1))
for k, rows in out["reach"].items():
    for r in rows: print(k, f"{r['horizontal_distance_m']:.2f} m", r["status"], "|", r["task"])

# rigged UR5e GLB for the viewer: one node per link, rest transforms, joint axes in the JSON
spec = mujoco.MjSpec.from_file(urd.MJCF_PATH); um = spec.compile(); ud = mujoco.MjData(um); mujoco.mj_forward(um, ud)
LINKS = ["base", "shoulder_link", "upper_arm_link", "forearm_link", "wrist_1_link", "wrist_2_link", "wrist_3_link"]
bid = {n: um.body(n).id for n in LINKS}
def T(pos, quat):
    M = np.eye(4); M[:3, :3] = trimesh.transformations.quaternion_matrix(quat)[:3, :3]; M[:3, 3] = pos; return M
def bw(b): M = np.eye(4); M[:3, :3] = ud.xmat[b].reshape(3, 3); M[:3, 3] = ud.xpos[b]; return M
scene = trimesh.Scene(); scene.graph.update(frame_from="world", frame_to="ur5e_root", matrix=np.eye(4)); meta = []
geoms = {b: [] for b in bid.values()}
for gi in range(um.ngeom):
    if um.geom_type[gi] != mujoco.mjtGeom.mjGEOM_MESH or um.geom_group[gi] != 2: continue
    b = um.geom_bodyid[gi]
    if b not in geoms: continue
    mid = um.geom_dataid[gi]; va, vn = um.mesh_vertadr[mid], um.mesh_vertnum[mid]; fa, fn = um.mesh_faceadr[mid], um.mesh_facenum[mid]
    v = um.mesh_vert[va:va + vn]; f = um.mesh_face[fa:fa + fn]
    Gw = np.eye(4); Gw[:3, :3] = ud.geom_xmat[gi].reshape(3, 3); Gw[:3, 3] = ud.geom_xpos[gi]
    mesh = trimesh.Trimesh(trimesh.transform_points(v, np.linalg.inv(bw(b)) @ Gw), f, process=False)
    rgba = um.mat_rgba[um.geom_matid[gi]] if um.geom_matid[gi] >= 0 else um.geom_rgba[gi]
    mesh.visual = trimesh.visual.ColorVisuals(mesh, face_colors=np.tile((rgba * 255).astype(np.uint8), (len(f), 1)))
    geoms[b].append(mesh)
parent = "ur5e_root"
for n in LINKS:
    b = bid[n]; scene.graph.update(frame_from=parent, frame_to=n, matrix=T(um.body_pos[b], um.body_quat[b]))
    if geoms[b]:
        mg = trimesh.util.concatenate(geoms[b]); w = mg.copy(); w.merge_vertices()
        if len(mg.faces) > 6000:
            dec = w.simplify_quadric_decimation(face_count=6000)
            if dec.area / mg.area > 0.95:
                _, _, tri = trimesh.proximity.closest_point(mg, dec.triangles_center)
                dec.visual = trimesh.visual.ColorVisuals(dec, face_colors=mg.visual.face_colors[tri]); mg = dec
        scene.add_geometry(mg, geom_name=n + "_mesh", parent_node_name=n, node_name=n + "_geom")
    j = um.body_jntadr[b]
    meta.append(dict(name=n, axis=um.jnt_axis[j].tolist() if j >= 0 else None)); parent = n
scene.export(LAB / "ur5e_rig.glb")
(LAB / "ur5e_rig.json").write_text(json.dumps(dict(links=meta, tool_length=TOOL_L, tcp_offset_y=0.0996 + TOOL_L, heads=HEADS), indent=1))
print("rig", (LAB / "ur5e_rig.glb").stat().st_size, "bytes")
