const { chromium } = require('playwright'); const fs = require('fs');
const FK = JSON.parse(fs.readFileSync('fk_expect.json'));
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--use-gl=angle','--use-angle=swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  const errs = []; p.on('console', m => { if (m.type()==='error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + process.cwd() + '/page.html'); await p.waitForTimeout(14000);
  const res = await p.evaluate(async (FK) => {
    playing = false; const fails = []; const f3 = v => +v.toFixed(3);
    const B = o => new THREE.Box3().setFromObject(o);
    const top = pfx => byPrefix(model, pfx)[0];
    const toModel = v => new THREE.Vector3(v.x, -v.z, v.y);             // three world (Y up) -> model frame (Z up)
    const frame = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    const R0 = B(top('A01 fabric roll')).getSize(new THREE.Vector3());
    const rail = B(top('A04 7th-axis rail 1')), xb = B(top('A04 Festo EGC-120'));
    const statics = []; model.traverse(o => { if (o.isMesh && o.visible) statics.push(o); });
    const gantryOwn = new Set(['A04_Festo_EGC-80','A04_Y_carriage','A04_Z_axis','A04_ATI_QC-11','A03_T1_needle_bar','A03_EXAIR','A03_Schmalz','A03_double-ply'].flatMap(s => byPrefix(model, s.replace(/_/g,' '))));
    const isGantry = o => { for (let q = o; q; q = q.parent) if (gantryOwn.has(q)) return true; return false; };
    const ignore = /floor|guard_panel|interlocked_door|fabric|kit_|cut_|finished_tee|rib_strip|EGC-120|A04_gantry_column/;
    const nm = o => { for (let q = o; q; q = q.parent) if (q.name && /^A\d\d_/.test(q.name)) return q.name; return o.name; };
    const others = statics.filter(o => !isGantry(o) && !ignore.test(nm(o)) && !(rig && (()=>{for(let q=o;q;q=q.parent) if(q===rig) return true; return false;})()));
    let n = 0;
    for (let t = 0; t <= 330; t += 1) {
      simT = t; await frame(); n++;
      const rs = B(top('A01 fabric roll')).getSize(new THREE.Vector3());
      for (const r of [...anim.roll, ...anim.rollers]) { const ax0 = new THREE.Vector3(0,0,1).applyQuaternion(r.rest), ax = new THREE.Vector3(0,0,1).applyQuaternion(r.o.quaternion);
        if (ax.angleTo(ax0) > 0.01) fails.push(`t=${t} ${r.o.name} axis tilted`);
        const c0 = r.o.position; if (!r.p0) r.p0 = c0.clone(); if (c0.distanceTo(r.p0) > 1e-6) fails.push(`t=${t} ${r.o.name} moved off its shaft`); }
      const ped = B(top('A04 UR10e pedestal')), car = B(top('A04 7th-axis carriage')), base = B(rig.getObjectByName('base'));
      const pc = (ped.min.x + ped.max.x) / 2, cc = (car.min.x + car.max.x) / 2, bc = rig.getWorldPosition(new THREE.Vector3()).x;
      if (Math.abs(pc - bc) > 0.005 || Math.abs(cc - bc) > 0.005) fails.push(`t=${t} robot base ${f3(bc)} vs pedestal ${f3(pc)} carriage ${f3(cc)}`);
      if (Math.abs(base.min.y - ped.max.y) > 0.01) fails.push(`t=${t} robot base bottom ${f3(base.min.y)} vs pedestal top ${f3(ped.max.y)}`);
      if (car.min.x < rail.min.x - 0.005 || car.max.x > rail.max.x + 0.005) fails.push(`t=${t} carriage off the rail`);
      const yb = B(top('A04 Festo EGC-80')), yc = B(top('A04 Y carriage')), za = B(top('A04 Z axis')), nb = B(top('A03 T1 needle bar'));
      if (yb.min.x < xb.min.x - 0.005 || yb.max.x > xb.max.x + 0.005) fails.push(`t=${t} Y beam off the X beams`);
      if (yc.min.z < yb.min.z - 0.005 || yc.max.z > yb.max.z + 0.005) fails.push(`t=${t} carriage off the Y beam`);
      if (za.max.y < yc.min.y + 0.02) fails.push(`t=${t} Z column left its carriage (top ${f3(za.max.y)} < carriage ${f3(yc.min.y)})`);
      if (nb.min.y < 0.855) fails.push(`t=${t} tool below table height ${f3(nb.min.y)}`);
      for (const part of ['A03 T1 needle bar','A04 Z axis','A03 Schmalz']) {
        for (const g of byPrefix(model, part)) { const gb = B(g);
          for (const o of others) { const ob = B(o); if (gb.clone().intersect(ob).isEmpty()) continue; const s = gb.clone().intersect(ob).getSize(new THREE.Vector3()); if (s.x > 0.003 && s.y > 0.003 && s.z > 0.003) fails.push(`t=${t} gantry ${part} overlaps ${nm(o)}`); } }
      }
    }
    // robot pose in the viewer matches the MuJoCo forward kinematics
    const fk = [];
    for (const e of FK) {
      let tt = 0; for (let i = 0; i < e.i; i++) tt += Math.max(KF[i].move_s, 0.02) + KF[i].dwell_s; tt += Math.max(KF[e.i].move_s, 0.02);  // end of move into frame i
      simT = tt; await frame();
      const w = toModel(rig.getObjectByName('wrist_3_link').getWorldPosition(new THREE.Vector3()));
      const d = Math.hypot(w.x - e.flange[0], w.y - e.flange[1], w.z - e.flange[2]) * 1000;
      fk.push(+d.toFixed(1)); if (d > 5) fails.push(`keyframe ${e.i}: viewer flange differs from MuJoCo by ${d.toFixed(1)} mm`);
    }
    // pins and cards
    const pinsOk = []; for (const pp of pins) { pp.b.click(); await frame(); if (document.getElementById('card').hidden || !document.getElementById('cardTitle').textContent) fails.push('pin without card: ' + pp.h.title); }
    const f = flow(); open(f[0]); let steps = 1; while (!document.getElementById('cardNext').disabled && steps < 60) { document.getElementById('cardNext').click(); steps++; }
    if (steps !== f.length) fails.push(`next-step walk covered ${steps} of ${f.length}`);
    // station list highlight
    for (const s of STATIONS) if (s.group && !model.getObjectByName(san(s.group))) fails.push('station group not found: ' + s.group);
    const cats = {}; fails.forEach(x => { const k = x.replace(/t=\d+ /,'').replace(/[0-9.]+/g,'#'); cats[k] = (cats[k]||0)+1; }); return { samples: n, fk_mm: fk, pins: pins.length, flowSteps: f.length, categories: cats, nfails: fails.length };
  }, FK);
  console.log(JSON.stringify(res, null, 1)); console.log('console errors:', errs.slice(0, 5));
  await b.close();
})();
