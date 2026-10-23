"""Synthesize narration per sentence with Piper (neural, offline) and write timings + SRT.

Usage: tts.py OUT_DIR   (needs ~/.venvs/tts with piper-tts and the en_US-ryan-high voice)
"""
import json, pathlib, subprocess, sys, wave

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1]); (OUT / "wav").mkdir(parents=True, exist_ok=True)
VENV = pathlib.Path(sys.executable).parent.parent   # run with the tts venv python
PIPER = VENV / "bin/piper"
VOICE = VENV / "voices/en_US-ryan-high.onnx"
GAP, LEAD, TAIL = 0.35, 0.5, 0.9      # pause between sentences, before first, after last (s)
RATE = 22050

def dur(p):
    with wave.open(str(p)) as w: return w.getnframes() / w.getframerate()

def silence(sec):
    return b"\x00\x00" * int(sec * RATE)

scenes = json.loads((HERE / "scenes.json").read_text())
timing, srt, t_global = [], [], 0.0
for sc in scenes:
    placed, t = [], LEAD                       # (start, pcm bytes, show)
    for i, s in enumerate(sc["sentences"]):
        if isinstance(s, dict): say, show, at = s["say"], s["show"], s["at"]
        elif isinstance(s, str): say, show, at = s, s, None
        else: (say, show), at = s, None
        f = OUT / "wav" / f"{sc['id']}_{i}.wav"
        if not f.exists():
            subprocess.run([str(PIPER), "-m", str(VOICE), "--length-scale", "1.06", "-f", str(f)], input=say.encode(), check=True, capture_output=True)
        with wave.open(str(f)) as w:
            assert w.getframerate() == RATE and w.getsampwidth() == 2 and w.getnchannels() == 1
            data = w.readframes(w.getnframes())
        start = t if at is None else max(at, t if i else 0.0)
        if at is not None and start - at > 0.6:
            print(f"  warn {sc['id']} line {i} starts {start - at:.1f}s after its cue")
        placed.append((start, data, show)); t = start + len(data) / 2 / RATE + GAP
    end = t - GAP + TAIL
    if sc.get("fixed_frames"):
        fixed = sc["fixed_frames"] / 30
        assert end - TAIL + 0.2 <= fixed, f"{sc['id']}: narration runs {end - TAIL - fixed:.1f}s past the shot"
        end = fixed
    buf = bytearray(int(end * RATE) * 2)
    sents = []
    for start, data, show in placed:
        o = int(start * RATE) * 2; buf[o:o + len(data)] = data[:len(buf) - o]
        d = len(data) / 2 / RATE
        sents.append(dict(start=round(start, 3), dur=round(d, 3), show=show)); srt.append((0, t_global + start, t_global + start + d, show))
    with wave.open(str(OUT / f"{sc['id']}.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(buf))
    timing.append(dict(id=sc["id"], kind=sc["kind"], dur=round(end, 3), sentences=sents))
    t_global += end
srt = [(i + 1, a, b, txt) for i, (_, a, b, txt) in enumerate(srt)]

def ts(x):
    h, r = divmod(x, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"

(OUT / "timing.json").write_text(json.dumps(timing, indent=1))
(OUT / "narration.srt").write_text("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{txt}\n" for i, a, b, txt in srt))
print(f"{len(timing)} scenes, {t_global/60:.2f} min; 3D {sum(x['dur'] for x in timing if x['kind']=='3d'):.0f} s, slides {sum(x['dur'] for x in timing if x['kind']=='slide'):.0f} s")
