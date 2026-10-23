"""Export the MuJoCo Menagerie UR10e + Robotiq 2F-85 as a rigged GLB for the viewer.

Each UR10e link becomes a glTF node with its rest transform relative to its parent;
cad/out/ur10e_rig.json lists each joint axis so the viewer can rotate links with the
same joint angles the MuJoCo IK produced (sim/results/reach_cycle.json). The gripper
is attached at the flange in its rest (open) pose. Frames: metres, Z-up, as the cell model.
Run: /home/user/.venvs/sim/bin/python sim/export_ur_rig.py
"""
import json
from pathlib import Path
import numpy as np, mujoco, trimesh
from robot_descriptions import ur10e_mj_description as urd
from robot_descriptions import robotiq_2f85_mj_description as gd

ROOT = Path(__file__).resolve().parents[1]
spec = mujoco.MjSpec.from_file(urd.MJCF_PATH)
g = mujoco.MjSpec.from_file(gd.MJCF_PATH)
spec.site("attachment_site").attach_body(g.worldbody.first_body(), "g_", "")
m = spec.compile(); d = mujoco.MjData(m); mujoco.mj_forward(m, d)

UR_LINKS = ["base", "shoulder_link", "upper_arm_link", "forearm_link", "wrist_1_link", "wrist_2_link", "wrist_3_link"]
bid = {n: m.body(n).id for n in UR_LINKS}

def T(pos, quat):
    M = np.eye(4); M[:3, 3] = pos
    w, x, y, z = quat
    M[:3, :3] = trimesh.transformations.quaternion_matrix([w, x, y, z])[:3, :3]
    return M

def body_world(b):
    M = np.eye(4); M[:3, :3] = d.xmat[b].reshape(3, 3); M[:3, 3] = d.xpos[b]; return M

def owner(b):
    """UR link that carries body b (gripper bodies ride on wrist_3_link)."""
    while b not in bid.values() and b != 0: b = m.body_parentid[b]
    return b

scene = trimesh.Scene(); meta = {"links": []}
geoms_by_link = {b: [] for b in bid.values()}
for gi in range(m.ngeom):
    if m.geom_type[gi] != mujoco.mjtGeom.mjGEOM_MESH or m.geom_group[gi] not in (0, 1, 2): continue
    if m.geom_contype[gi] != 0 and m.geom_conaffinity[gi] != 0 and m.geom_group[gi] == 3: continue
    b = m.geom_bodyid[gi]; o = owner(b)
    if o not in geoms_by_link: continue
    mid = m.geom_dataid[gi]
    va, vn = m.mesh_vertadr[mid], m.mesh_vertnum[mid]; fa, fn = m.mesh_faceadr[mid], m.mesh_facenum[mid]
    v = m.mesh_vert[va:va + vn].copy(); f = m.mesh_face[fa:fa + fn].copy()
    Gw = np.eye(4); Gw[:3, :3] = d.geom_xmat[gi].reshape(3, 3); Gw[:3, 3] = d.geom_xpos[gi]
    Gl = np.linalg.inv(body_world(o)) @ Gw            # geom pose in its owning link frame
    v = trimesh.transform_points(v, Gl)
    rgba = m.geom_rgba[gi].copy()
    if m.geom_matid[gi] >= 0: rgba = m.mat_rgba[m.geom_matid[gi]].copy()
    mesh = trimesh.Trimesh(v, f, process=False)
    mesh.visual = trimesh.visual.ColorVisuals(mesh, face_colors=np.tile((rgba * 255).astype(np.uint8), (len(f), 1)))
    geoms_by_link[o].append(mesh)

parent_name = "ur10e_root"
scene.graph.update(frame_from="world", frame_to=parent_name, matrix=np.eye(4))
for n in UR_LINKS:
    b = bid[n]
    rest = T(m.body_pos[b], m.body_quat[b])
    scene.graph.update(frame_from=parent_name, frame_to=n, matrix=rest)
    meshes = geoms_by_link[b]
    if meshes:
        merged = trimesh.util.concatenate(meshes)
        if len(merged.faces) > 6000:  # keep the page light: decimate per link, keep colours per face via nearest
            colors = merged.visual.face_colors
            dec = merged.simplify_quadric_decimation(face_count=6000)
            _, _, tri = trimesh.proximity.closest_point(merged, dec.triangles_center)
            dec.visual = trimesh.visual.ColorVisuals(dec, face_colors=colors[tri])
            merged = dec
        scene.add_geometry(merged, geom_name=n + "_mesh", parent_node_name=n, node_name=n + "_geom")
    jid = m.body_jntadr[b]
    axis = m.jnt_axis[jid].tolist() if jid >= 0 else None
    meta["links"].append({"name": n, "rest_pos": m.body_pos[b].tolist(), "rest_quat_wxyz": m.body_quat[b].tolist(), "axis": axis})
    parent_name = n

out = ROOT / "cad/out"; scene.export(out / "ur10e_rig.glb")
cyc = json.loads((ROOT / "sim/results/reach_cycle.json").read_text())["layout_B_seventh_axis"]["cycle"]
assert cyc["feasible"] and cyc["replay_check"]["contacts"] == 0, "robot cycle must be collision-free before export"
meta["keyframes"] = cyc["keyframes"]   # collision-checked waypoints, replayed by the viewer exactly as verified
meta["base_y"], meta["base_z"] = 0.94, 0.82
(out / "ur10e_rig.json").write_text(json.dumps(meta, indent=1))
print("rig glb bytes", (out / "ur10e_rig.glb").stat().st_size, "links", [l["name"] for l in meta["links"]], "keyframes", len(meta["keyframes"]))
