// Render 3D shots from the offline viewer as JPEG frames, deterministically (simT and camera set per frame).
// Usage: node render3d.js VIEWER_HTML VIDEO_DIR [--preview] [scene ids...]
// Needs playwright (npm) and the pre-installed Chromium.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [viewer, V, ...rest] = process.argv.slice(2);
const preview = rest.includes('--preview'); const only = rest.filter(a => !a.startsWith('--'));
const scenes = JSON.parse(fs.readFileSync(path.join(__dirname, 'scenes.json')));
const timing = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(V, 'timing.json'))).map(t => [t.id, t]));
const FPS = 30, W = 1920, H = 1080;
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--use-gl=angle', '--use-angle=swiftshader'] });
  const p = await b.newPage({ viewport: { width: W, height: H } });
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + path.resolve(viewer));
  await p.waitForFunction(() => typeof model !== 'undefined' && model && links.length === 7, null, { timeout: 90000 });
  await p.addStyleTag({ content: '.rail,.hud,.legend,.pins,.op,.card{display:none!important}.app{display:block!important}.bay{position:fixed!important;inset:0!important}html,body{margin:0;overflow:hidden}' });
  await p.waitForTimeout(800);
  await p.evaluate(([W, H]) => {
    playing = false; controls.enableDamping = false; window.requestAnimationFrame = () => 0;
    renderer.setPixelRatio(1); renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
    const anc = (o, re) => { for (let q = o; q; q = q.parent) if (q.name && re.test(q.name)) return true; return false; };
    window.__guards = []; model.traverse(o => { if (o.isMesh && anc(o, /guard_panel|interlocked_door|light_curtain|guard_post/)) __guards.push(o); });
    window.__hl = [];
    window.__setShot = (hide, hl) => {
      __guards.forEach(o => o.visible = !hide);
      __hl.forEach(([o, m]) => o.material = m); __hl = [];
      for (const pf of hl) byPrefix(model, pf).forEach(n => n.traverse(o => { if (o.isMesh) { __hl.push([o, o.material]); const m = o.material.clone(); if (m.emissive) { m.emissive.set(0xd9a21b); m.emissiveIntensity = 0.22; } o.material = m; } }));
    };
  }, [W, H]);
  const ease = k => 0.5 - 0.5 * Math.cos(Math.PI * Math.min(1, Math.max(0, k)));
  for (const sc of scenes.filter(s => s.kind === '3d' && (!only.length || only.includes(s.id)))) {
    const sh = sc.shot, dur = timing[sc.id].dur, N = Math.round(dur * FPS);
    const dir = path.join(V, preview ? 'preview' : 'frames', sc.id); fs.mkdirSync(dir, { recursive: true });
    await p.evaluate(([h, hl]) => __setShot(h, hl), [!!sh.hide_guards, sh.hl || []]);
    const idx = preview ? [0, Math.floor(N / 2), N - 1] : [...Array(N).keys()];
    let fx = null; const t0 = Date.now();
    for (const i of idx) {
      const t = i / FPS, k = N > 1 ? i / (N - 1) : 0;
      const cam = { mode: sh.mode, k, e: ease(k), sh, simT: sh.simT0 + sh.rate * t };
      if (sh.mode === 'follow') {   // smooth the robot's track position so the camera glides
        const bx = await p.evaluate(s => { simT = s; step(performance.now()); return rig.position.x; }, cam.simT);
        fx = fx === null || preview ? bx : fx + (bx - fx) * 0.05; cam.fx = fx;
      }
      const d = await p.evaluate(c => {
        simT = c.simT; const s = c.sh; let pos, tgt;
        if (c.mode === 'orbit') { const a = (s.a0 + (s.a1 - s.a0) * c.e) * Math.PI / 180; tgt = new THREE.Vector3(...s.c); pos = tgt.clone().add(new THREE.Vector3(s.r * Math.sin(a), s.h, s.r * Math.cos(a))); }
        else if (c.mode === 'path') { pos = new THREE.Vector3(...s.p[0]).lerp(new THREE.Vector3(...s.p[1]), c.e); tgt = new THREE.Vector3(...s.t[0]).lerp(new THREE.Vector3(...s.t[1]), c.e); }
        else { const y = rig.getWorldPosition(new THREE.Vector3()); const base = new THREE.Vector3(c.fx, 0, y.z); tgt = base.clone().add(new THREE.Vector3(...s.look)); pos = base.clone().add(new THREE.Vector3(...s.off)); }
        camera.position.copy(pos); controls.target.copy(tgt); camera.lookAt(tgt);
        step(performance.now()); return canvas.toDataURL('image/jpeg', 0.93);
      }, cam);
      fs.writeFileSync(path.join(dir, `${String(i).padStart(5, '0')}.jpg`), Buffer.from(d.split(',')[1], 'base64'));
    }
    console.log(sc.id, idx.length, 'frames', ((Date.now() - t0) / 1000).toFixed(0) + 's');
  }
  if (errs.length) console.log('page errors:', errs);
  await b.close();
})();
