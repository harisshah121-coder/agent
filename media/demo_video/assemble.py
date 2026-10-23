"""Assemble the demo video: per-scene clips (slides or 3D frames + overlays), narration, subtitles.

Usage: assemble.py VIDEO_DIR OUT.mp4
"""
import json, pathlib, subprocess, sys, wave

V = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
FPS, BG = 30, "0xF4F5F2"
scenes = {s["id"]: s for s in json.loads((pathlib.Path(__file__).with_name("scenes.json")).read_text())}
timing = json.loads((V / "timing.json").read_text())
if len(sys.argv) > 3: timing = [t for t in timing if t["id"] in sys.argv[3].split(",")]  # quick partial test
clips = V / "clips"; clips.mkdir(exist_ok=True)

def ff(*a):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *map(str, a)], check=True)

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", FPS]
pcm, srt, t0 = b"", [], 0.0
for T in timing:
    sid, sc = T["id"], scenes[T["id"]]
    n = round(T["dur"] * FPS); dur = n / FPS
    fade = f"fade=in:st=0:d=0.25:color={BG},fade=out:st={dur - 0.25:.3f}:d=0.25:color={BG}"
    out = clips / f"{sid}.mp4"
    if sc["kind"] == "slide":
        ff("-f", "concat", "-safe", 0, "-i", V / "slides" / sid / "list.txt",
           "-vf", f"fps={FPS},scale=1920:1080,{fade}", "-frames:v", n, *ENC, out)
    else:
        ins = ["-framerate", FPS, "-i", V / "frames" / sid / "%05d.jpg"]
        chain, last, k = [], "[0:v]", 1
        if sid != "s20":
            ins += ["-loop", 1, "-framerate", FPS, "-i", V / "overlays" / "mark.png"]
            chain.append(f"{last}[{k}:v]overlay=0:0:shortest=1[v{k}]"); last = f"[v{k}]"; k += 1
        if sc.get("lower"):
            ins += ["-loop", 1, "-framerate", FPS, "-i", V / "overlays" / f"{sid}_lower.png"]
            chain.append(f"[{k}:v]format=rgba,fade=in:st=0.6:d=0.5:alpha=1,fade=out:st={dur - 1.3:.3f}:d=0.5:alpha=1[l{k}]")
            chain.append(f"{last}[l{k}]overlay=0:0:shortest=1[v{k}]"); last = f"[v{k}]"; k += 1
        if sid == "s20":
            st = T["sentences"][-1]["start"] - 0.4
            ins += ["-loop", 1, "-framerate", FPS, "-i", V / "overlays" / "s20_end.png"]
            chain.append(f"[{k}:v]format=rgba,fade=in:st={st:.3f}:d=0.8:alpha=1[l{k}]")
            chain.append(f"{last}[l{k}]overlay=0:0:shortest=1[v{k}]"); last = f"[v{k}]"; k += 1
        fo = fade if sid != "s20" else f"fade=in:st=0:d=0.25:color={BG},fade=out:st={dur - 0.6:.3f}:d=0.6:color=black"
        chain.append(f"{last}{fo}[out]")
        ff(*ins, "-filter_complex", ";".join(chain), "-map", "[out]", "-frames:v", n, *ENC, out)
    # narration, padded or trimmed to the clip's exact frame length
    with wave.open(str(V / f"{sid}.wav")) as w:
        rate = w.getframerate(); data = w.readframes(w.getnframes())
    need = int(round(dur * rate)) * 2
    pcm += data[:need] + b"\x00" * max(0, need - len(data))
    for s in T["sentences"]:
        srt.append((t0 + s["start"], t0 + s["start"] + s["dur"], s["show"]))
    t0 += dur
    print(sid, f"{dur:.2f}s")

with wave.open(str(V / "narration_full.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
srt_path = OUT.with_suffix(".srt")
srt_path.write_text("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(srt, 1)), encoding="utf-8")
(V / "clips.txt").write_text("".join(f"file '{clips / (T['id'] + '.mp4')}'\n" for T in timing))
ff("-f", "concat", "-safe", 0, "-i", V / "clips.txt", "-i", V / "narration_full.wav", "-i", srt_path,
   "-map", "0:v", "-map", "1:a", "-map", "2:s", "-c:v", "copy",
   "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
   "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", "-movflags", "+faststart", "-shortest", OUT)
print("wrote", OUT, f"{t0 / 60:.2f} min")
