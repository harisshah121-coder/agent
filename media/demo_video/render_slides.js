// Render slide scenes (animated reveals timed to narration) and 3D overlays (lower thirds, end title).
// Usage: node render_slides.js VIDEO_DIR
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const V = process.argv[2], OVERLAYS_ONLY = process.argv.includes('--overlays');
const scenes = JSON.parse(fs.readFileSync(path.join(__dirname, 'scenes.json')));
const timing = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(V, 'timing.json'))).map(t => [t.id, t]));
const FPS = 30, ANIM = 0.7;
const CSS = fs.readFileSync(path.join(__dirname, 'slides.css'), 'utf8');
const page = body => `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>${CSS}</style></head><body>${body}</body></html>`;

(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  let n = 0;
  for (const sc of scenes) {
    const T = timing[sc.id];
    if (sc.kind === 'slide' && OVERLAYS_ONLY) { n++; continue; }
    if (sc.kind === 'slide') {
      const dir = path.join(V, 'slides', sc.id); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
      const idx = n++;
      await p.setContent(page(`<main class="slide"><div class="bar"></div>${sc.html}<footer><span>Roll-to-Garment</span><span>${String(idx + 1).padStart(2, '0')}</span></footer></main>`), { waitUntil: 'networkidle' });
      await p.evaluate(() => document.fonts.ready);
      // element schedule: appear at sentence start + optional --d delay
      const starts = T.sentences.map(s => s.start);
      const sched = await p.evaluate(starts => [...document.querySelectorAll('[data-at]')].map((el, i) => {
        el.dataset.i = i; const d = parseFloat(getComputedStyle(el).getPropertyValue('--d')) || 0;
        return Math.max(0.15, starts[+el.dataset.at] + d);
      }), starts);
      // frame times: dense during transitions, single held frame otherwise
      const marks = new Set([0]);
      for (const s of sched) for (let t = s; t <= s + ANIM + 1e-6; t += 1 / FPS) marks.add(+t.toFixed(4));
      const times = [...marks].filter(t => t < T.dur).sort((a, b) => a - b);
      const list = [];
      for (let k = 0; k < times.length; k++) {
        const t = times[k];
        await p.evaluate(([t, sched, A]) => {
          document.querySelectorAll('[data-at]').forEach(el => {
            const x = Math.min(1, Math.max(0, (t - sched[+el.dataset.i]) / A)), e = 1 - Math.pow(1 - x, 3);
            el.style.opacity = e; el.style.transform = `translateY(${(1 - e) * 28}px)`;
          });
        }, [t, sched, ANIM]);
        const f = path.join(dir, `${String(k).padStart(5, '0')}.png`);
        await p.screenshot({ path: f });
        const next = k + 1 < times.length ? times[k + 1] : T.dur;
        list.push(`file '${f}'\nduration ${(next - t).toFixed(4)}`);
      }
      list.push(`file '${path.join(dir, String(times.length - 1).padStart(5, '0') + '.png')}'`);
      fs.writeFileSync(path.join(dir, 'list.txt'), list.join('\n') + '\n');
      console.log(sc.id, times.length, 'frames', T.dur.toFixed(1) + 's');
    } else {
      const dir = path.join(V, 'overlays'); fs.mkdirSync(dir, { recursive: true });
      const shots = [];
      if (sc.lower) shots.push([`${sc.id}_lower.png`, `<div class="lower"><i>${sc.lower[0]}</i><b>${sc.lower[1]}</b></div>`]);
      if (sc.id === 's20') shots.push([`${sc.id}_end.png`, `<div class="endcard"><div class="eyebrow">AI-directed roll-to-garment manufacturing</div><h1>Roll-to-Garment</h1><p>Fabric in. T-shirts out.</p></div>`]);
      for (const [name, html] of shots) {
        await p.setContent(page(`<div class="ov">${html}</div>`).replace('<html>', '<html class="clear">').replace('<body>', '<body class="clear">'), { waitUntil: 'networkidle' });
        await p.evaluate(() => document.fonts.ready);
        await p.screenshot({ path: path.join(dir, name), omitBackground: true });
      }
    }
  }
  // persistent watermark for 3D scenes
  await p.setContent(page(`<div class="ov"><div class="mark">Roll-to-Garment <span>concept model · robot motion simulated in MuJoCo</span></div></div>`).replace('<html>', '<html class="clear">').replace('<body>', '<body class="clear">'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(V, 'overlays', 'mark.png'), omitBackground: true });
  await b.close();
})();
