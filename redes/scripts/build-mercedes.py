"""Mercedes reel: cinematic, beat-synced cuts, inspired by the owner's reference reel (no captions until the end)."""
import os
import subprocess
import sys

sys.path.insert(0, "/home/claude/reels")
from PIL import Image, ImageDraw

from kit import W, H, font, logo_card, run, tlen, join

SRC = "/mnt/user-data/uploads/IMG_4221.mov"
AUD = "/mnt/user-data/uploads/ed2d8977-WhatsApp_Audio_2026-11-07_at_11.26.01_AM.mpeg"
D = "/home/claude/merc"
GRADE = "eq=contrast=1.12:saturation=0.86:brightness=-0.025,vignette=PI/5"

# Beat grid from the audio (about 0.8 s per beat; the drop is at 16.30 s).
B = [0.0, 3.51, 6.71, 8.31, 11.52, 14.72, 16.30, 17.09, 17.88, 18.69, 19.48, 20.29, 21.90, 23.50, 25.10, 28.28]
# (source start, speed, zoom from, zoom to, vertical bias 0=top..1=bottom)
SHOTS = [
    (0.0, 0.5, 1.00, 1.10, 0.5),   # grille, slow push-in
    (4.3, 0.5, 1.05, 1.12, 0.5),   # mirror and front door glass
    (7.5, 0.5, 1.05, 1.10, 0.5),   # rear door glass
    (10.0, 0.5, 1.18, 1.24, 0.9),  # back glass (crop out the people at the top)
    (14.5, 0.5, 1.05, 1.12, 0.5),  # other side windows
    (2.4, 0.5, 1.45, 1.60, 0.25),  # star and grille detail, build-up
    (4.6, 1.0, 1.10, 1.15, 0.5),   # drop: fast cuts on every beat
    (8.6, 1.0, 1.10, 1.15, 0.5),
    (12.4, 1.0, 1.20, 1.25, 0.9),
    (17.0, 1.0, 1.10, 1.15, 0.5),
    (0.5, 1.0, 1.30, 1.38, 0.3),
    (15.0, 0.6, 1.05, 1.12, 0.5),
    (9.0, 0.6, 1.08, 1.14, 0.5),
    (18.0, 0.6, 1.05, 1.12, 0.5),
    (1.0, 0.5, 1.00, 1.08, 0.5),   # back to the grille for a seamless loop, with the end text
]


def endcard_overlay(path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = logo_card()
    im.alpha_composite(c, ((W - c.width) // 2, 820))
    f = font("Archivo-900.ttf", 64)
    fs = font("Manrope-800.ttf", 44)
    for txt, ff, y, col in [("Todos los vidrios · ₡40 000", f, 975, (255, 255, 255)),
                            ("A domicilio gratis en la GAM · agende en la bio", fs, 1065, (220, 224, 218))]:
        x = (W - tlen(ff, txt)) / 2
        for ch in txt:
            g = ff if ord(ch) in ff.cmap or ch == " " else ff.fb
            d.text((x, y), ch, font=g, fill=col, stroke_width=4, stroke_fill=(0, 0, 0))
            x += g.getlength(ch)
    im.save(path)


def shot(i, src_t, speed, z0, z1, bias, dur, overlay=None):
    out = f"{D}/m{i:02d}.mp4"
    n = round(dur * 30)
    zs = 1.25  # oversize so the zoom stays sharp
    z = f"({z0}+({z1}-{z0})*on/{max(n - 1, 1)})"
    vf = (f"setpts=(PTS-STARTPTS)/{speed},fps=30,"
          f"scale={int(W * zs)}:{int(H * zs)}:force_original_aspect_ratio=increase,crop={int(W * zs)}:{int(H * zs)},"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*{bias}':d=1:s={W}x{H}:fps=30,"
          f"{GRADE},setsar=1,trim=end_frame={n}")
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(src_t), "-t", str(dur * speed + 0.2), "-i", SRC]
    if overlay:
        cmd += ["-loop", "1", "-t", str(dur), "-i", overlay,
                "-filter_complex", f"[0:v]{vf}[b];[1:v]format=rgba,fade=t=in:st=0.4:d=0.5:alpha=1[o];[b][o]overlay=0:0:shortest=1,format=yuv420p[v]",
                "-map", "[v]"]
    else:
        cmd += ["-vf", vf + ",format=yuv420p"]
    cmd += ["-an", "-frames:v", str(n), "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30"]
    run(cmd, out)
    return out


if __name__ == "__main__":
    endcard_overlay(f"{D}/end.png")
    parts = []
    for i, (s, sp, z0, z1, bias) in enumerate(SHOTS):
        dur = B[i + 1] - B[i]
        parts.append(shot(i, s, sp, z0, z1, bias, dur, f"{D}/end.png" if i == len(SHOTS) - 1 else None))
        print("shot", i, round(dur, 2), flush=True)
    join(parts, f"{D}/video.mp4")
    total = B[-1]
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/video.mp4", "-i", AUD,
         "-filter_complex", f"[1:a]atrim=0:{total},afade=t=out:st={total - 0.9}:d=0.9,aresample=48000[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart"],
        "/home/claude/reels/reel6-mercedes-cinematico.mp4")
    print("done")
