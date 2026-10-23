# Build Guide 4: Simulation and Digital Twin (v1, 2026-10-23)

How we prove the machine, the robots and the software work before and while we build them. Seven simulation levels, each with a question it answers, the tools, how to build it, and the gate it must pass. Two levels already run in this repository (§8). Identifiers come from `ARCHITECTURE_SPINE.md`; the model comes from Guide 3; the software interfaces from Guide 2 (M09 HAL, M13 twin).

---

## 1. What simulation can and cannot prove
| Simulation proves | Simulation does not prove |
|---|---|
| Geometry, clearances, collisions | How knit fabric curls, stretches and slips |
| Robot and gantry reach, joint limits | Needle-gripper pick reliability |
| Nominal cycle time and the bottleneck | Seam quality, puckering, skipped stitches |
| Shift throughput under assumed failure rates | The real failure rates |
| PLC logic, interlocks and sequences | Safety compliance (that needs validation on hardware) |
| Software end-to-end against a twin | Perception accuracy on real white jersey |
| Camera coverage and synthetic training images | Vacuum leakage, static, lint |

The right-hand column is answered by the bench experiments in Guide 1 §10 and by the shift test. Simulation tells us which of those experiments to run first and what number each must hit. No simulator is validated for knit garment handling in 2026 (R10, R12, R15).

## 2. The seven levels
| Level | Question | Tool | Status |
|---|---|---|---|
| L1 Kinematic twin | Can the robots reach every pose without collision, and how long do moves take? | MuJoCo 3.16 + Menagerie UR10e | **Running** (`sim/reach_cycle.py`) |
| L2 Throughput (discrete-event) | How many accepted shirts per shift, given interventions and stoppages? | SimPy Monte Carlo | **Running** (`sim/throughput_des.py`) |
| L3 Software-in-the-loop | Does the full software stack run a job end to end? | M09 `SimBackend` on MuJoCo; ROS 2 Jazzy; M06–M08 | Build in software sprint S2–S4 |
| L4 Virtual commissioning | Is the PLC logic correct before wiring? | TwinCAT 3 simulation mode (or ctrlX virtual); twin driven over ADS | Build before cabinet wiring |
| L5 Perception twin | Where do cameras go, and can we pre-train perception? | Isaac Sim 6.x + Cosmos Transfer, or Blender renders | Optional; needs RTX 4080-class GPU |
| L6 Cloth exploration | Which grasp and feed strategies look plausible? | MuJoCo flex / Genesis 1.4 / Isaac Lab deformables | Exploratory only; never a gate |
| L7 Calibrated twin | Does the twin match the real cell? | L1–L4 fed with measured timings and failure data from M14 | After the first cell runs |

## 3. L1 kinematic twin (MuJoCo)
**Build**
1. Export each assembly from Guide 3 (STEP → GLB for visuals, decimated convex hulls for collision).
2. Emit URDF from the assembly joint files; convert with `mujoco.MjSpec.from_file(...)`; attach Menagerie UR10e and Robotiq 2F-85 with `MjSpec.attach`.
3. Model the gantry as three slide joints (X 3.0 m, Y 1.5 m, Z 0.9 m) and the 7th-axis track as one slide joint.
4. Encode every station target as a site: handoff, overlock needle, collar module, coverstitch needle, inspection table, cutter exit pick zone, staging places.
5. Solve inverse kinematics (damped least squares, tool axis down) for each target; check joint limits and collisions.
6. Time moves with vendor limits: UR10e joints 120/120/180/180/180/180 °/s; acceleration and settle values as estimates until measured; gantry belt axes at Festo EGC limits.

**Gate**: every required pose reachable with ≥ 50 mm margin; zero collisions; arm occupancy per shirt ≤ 85 % of the 328 s interval (so ≥ 15 % margin).

## 4. L2 throughput (discrete-event, Monte Carlo)
**Build**: one SimPy process per garment flowing cutter → gantry extraction → arm presentation and sewing → inspection, under a work-in-process cap of 4; occupancy from L1 and `spine/takt.csv`; random time variation (8 % standard deviation); interventions per garment with probability p blocking the arm for an exponential recovery time; cell stoppages from mean time between failures and mean time to repair; 5 % inspection rejects. Run 300 shifts per case.

**Gate**: probability of ≥ 100 accepted shirts per 12-hour shift ≥ 90 % at the white paper's 80 % availability and p = 1 %.

## 5. L3 software-in-the-loop
**Build**: implement `SimBackend` (Guide 2 M09) on the L1 twin; run M06 compiler → M07 scheduler → M08 behaviour trees → M09 HAL against it; M11 perception returns ground-truth poses from the twin (with configurable noise); M14 logs runs exactly as on the cell. CI runs one full tee job on every merge.

**Gate**: 100 consecutive simulated jobs with zero software faults; timing within 5 % of L1.

## 6. L4 virtual commissioning (PLC)
**Build**: TwinCAT 3 project runs in simulation mode on the engineering PC; axis NC objects driven against the twin over ADS (pyads) at 10–100 Hz; simulated I/O for sensors (vacuum switches, thread sensors, door switches); test cases for every sequence and interlock: homing, cutter handshake, tool change, door open during motion, e-stop recovery, thread break mid-seam.

**Gate**: every PLC test case passes before the first field wire is connected. Safety logic is tested here too, but its validation (Guide 1 §6) happens on hardware.

## 7. L5–L7
- **L5 perception twin**: import the cell USD into Isaac Sim, place cameras per Guide 1 §3.10, render white jersey panels with domain randomisation (lighting, colour, wrinkles) for pre-training M11 detectors; gate is coverage only (every station's field of view contains its work zone at the planned resolution).
- **L6 cloth exploration**: MuJoCo flex or Genesis cloth to compare grasp patterns (needle bar spacing, edge-roller strategies); results inform bench experiments, never purchase decisions.
- **L7 calibrated twin**: replace every estimate in L1/L2 with measured values from M14 (move times, seam times, intervention rates and recovery times, stoppage data); the twin then forecasts the effect of each design change before it is made.

## 8. Results (2026-10-23, audited layout)
Run from this repository: `sim/reach_cycle.py` (L1) and `sim/throughput_des.py` (L2). Raw results: `sim/results/reach_cycle.json`, `sim/results/throughput_des.json`. The viewer replays the L1 joint solutions on the real UR10e and Robotiq 2F-85 geometry (`sim/export_ur_rig.py`).

### 8.1 Reach: a fixed pedestal fails; the track works
UR10e on a fixed pedestal at (3.30, 0.90) m, base 0.82 m high, gripper 0.17 m, approach 0.05 m:

| Target | Horizontal distance | Fixed pedestal | On the track |
|---|---|---|---|
| Handoff at staging front edge | 1.29 m | reachable | reachable |
| Overlock needle (ST05) | 1.42 m | **114 mm short** | reachable |
| Collar module (ST06) | 0.47 m | reachable | reachable |
| Coverstitch needle (ST05) | 1.14 m | reachable | reachable |
| Inspection table (ST07) | 2.25 m | **1,234 mm short** | reachable |

Decision D-013: the UR10e rides P-ST04-007, a 3.6 m track along the sewing row at y = 0.94 m.

### 8.2 Model audit changed the layout
The first concept model had 30 collisions between stations: gantry columns through the cutter base, the cutter's vacuum blower through the robot track and two sewing tables, and the track through the inspection table. It also placed the "gantry-presented flat sleeve hem" on a coverstitch head the gantry cannot reach. The revised layout (`cad/concept/cell_concept.py`, audit `docs/logs/MODEL_AUDIT.md`, result PASS):
- Cutter split into a 2.5 m cutting zone and a 0.6 m pick-off conveyor; the gantry picks from the pick-off zone, clear of the cutting beam.
- Gantry columns at x 3.76 / 5.89 m; X stroke about 2.1 m over pick-off, staging, flat hemmer and tool stand.
- Vacuum blower outside the back guard, ducted.
- A dedicated flat coverstitch head for sleeve hems under the gantry (P-ST05-006, Jack W4-UT class, USD 2,061 reseller).

### 8.3 Cycle time (collision-checked)
`sim/reach_cycle.py` now plans every arm move in MuJoCo against 131 fixed obstacle boxes exported from the concept model (`cad/concept/export_boxes.py` → `sim/results/cell_boxes.json`): straight-line Cartesian approaches, a fixed tuck pose for track transits, base-offset search at each station, and a closed loop (the last pose returns to the first). An exact replay of the 777 keyframes, interpolated as the viewer does, found **0 contacts in 3,812 samples**.

Arm occupancy per shirt: **312.8 s** against the **328 s** interval, a **4.7 % margin**. The earlier 287 s figure used estimated, non-collision-checked moves and was optimistic. Seam times, the 8 s regrasp, acceleration and settle values are estimates (R16 F1, F9); fabric is not simulated.

### 8.4 Throughput over full shifts
300 simulated 12-hour shifts per case, 1 % of shirts needing a person:

| Scenario | Availability | Mean accepted | 10th percentile | Shifts reaching 100 |
|---|---|---|---|---|
| Audited layout (track + flat hemmer) | ~0.92 | 120.9 | 114 | 100 % |
| Audited layout (track + flat hemmer) | 0.80 | 107.7 | 93 | **79 %** |
| Without flat hemmer (+35 s arm time) | 0.80 | 96.5 | n/a | 46 % |

Gate (≥ 90 % at 0.80 availability): missed (79 %). Availability dominates: at about 0.92 availability every simulated shift reaches 100.

### 8.5 Decisions and next steps from these results
1. Track (done, D-013) and flat hemmer (done, D-015).
2. Close the gap with the cheapest levers first: MTTR ≤ 10 min per stoppage (accessible jam clearing, fast thread recovery) to lift availability toward 0.9, and cut arm time (shorter regrasp, a second gripper finger set, or moving one more seam off the arm) to recover the 15 % margin.
3. Measure the real seam presentation and regrasp times on the bench (Guide 1 §10 experiment 1); they decide the margin.
4. Add the gantry's own timeline to L1 (it now carries extraction, the flat hemmer and the tool changes) and check it stays under the interval.

## 9. Repository layout and how to run
```
sim/
  reach_cycle.py       L1 reach + arm cycle time (MuJoCo, Menagerie UR10e)
  throughput_des.py    L2 shift throughput Monte Carlo (SimPy)
  export_ur_rig.py     Rigged UR10e + Robotiq GLB and joint keyframes for the viewer
  results/             JSON outputs, committed
```
```bash
python3.13 -m venv ~/.venvs/sim && ~/.venvs/sim/bin/pip install mujoco robot_descriptions simpy
~/.venvs/sim/bin/python sim/reach_cycle.py      # ~10 s; first run downloads MuJoCo Menagerie
~/.venvs/sim/bin/python sim/throughput_des.py   # ~1 min
```

## 10. Build order and gates
| Step | Deliverable | Gate | Depends on |
|---|---|---|---|
| 1 | L1 on concept layout | Reach and timing | done |
| 2 | L2 shift model | ≥ 90 % of shifts reach 100 at 80 % availability | done (79 % on the audited layout; availability and arm-time levers in §8.5) |
| 3 | L1/L2 with flat-sleeve-hem plan and audited layout | Both gates pass | done for layout; margin gate open (4.7 % vs 15 %) |
| 4 | L1 with full collision geometry from Guide 3 C3 | Zero collisions on all paths | box-level done (0 contacts); mesh-level waits on Guide 3 C2–C3 |
| 5 | L3 software-in-the-loop | 100 jobs fault-free | Guide 2 S2–S4 |
| 6 | L4 virtual commissioning | All PLC test cases pass | TwinCAT project |
| 7 | L5 camera coverage (optional) | Coverage check | GPU machine |
| 8 | L7 calibration | Twin within ±10 % of the measured cell | First cell runs |
