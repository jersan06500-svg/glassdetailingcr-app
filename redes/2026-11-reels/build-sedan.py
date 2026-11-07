"""Reel sedán gris: transiciones como la plantilla del dueño (entrada desde negro, fundidos a negro, cortes rápidos al ritmo)."""
import subprocess, sys
sys.path.insert(0, "/home/claude/reels")
from PIL import Image, ImageDraw
from kit import W, H, font, logo_card, run, tlen, join

U = "/mnt/user-data/uploads/"
C1 = U + "873afe91-videocarro.mp4"
C2 = U + "ec1f2509-videocarro2_atras.mp4"
AUD = U + "bb62ab6e-WhatsApp_Video_2026-11-07_at_3.59.14_PM.mp4"
D = "/home/claude/sedan"
GRADE = ("eq=contrast=1.16:saturation=0.82:brightness=-0.06:gamma=0.94,"
         "curves=all='0/0 0.5/0.44 0.85/0.74 1/0.86',colorbalance=bs=0.05:bm=0.03:rh=0.02,"
         "unsharp=5:5:0.7,vignette=PI/4.5")
B = [0, 1.81, 3.58, 5.36, 7.15, 7.59, 8.03, 8.45, 8.94, 9.38, 9.82, 10.26, 10.68, 11.59, 13.9]
# (fuente, inicio, velocidad, zoom desde, zoom hasta, sesgo vertical, transición)
S = [
    (C1, 0.0, 0.6, 1.00, 1.09, 0.5, "open"),
    (C2, 0.2, 0.6, 1.04, 1.12, 0.5, "dip"),
    (C1, 4.5, 0.8, 1.04, 1.10, 0.6, "dip"),
    (C1, 6.0, 0.8, 1.04, 1.10, 0.6, "dipout"),
    (C1, 7.6, 1.0, 1.20, 1.08, 0.5, "punch"),
    (C2, 1.6, 1.0, 1.20, 1.08, 0.5, "punch"),
    (C1, 2.0, 1.0, 1.32, 1.20, 0.4, "punch"),
    (C2, 3.0, 1.0, 1.20, 1.08, 0.5, "punch"),
    (C1, 9.0, 1.0, 1.20, 1.08, 0.5, "punch"),
    (C1, 4.9, 1.0, 1.45, 1.32, 0.7, "punch"),
    (C2, 2.3, 1.0, 1.25, 1.12, 0.5, "punch"),
    (C1, 10.2, 1.0, 1.20, 1.08, 0.5, "punch"),
    (C2, 0.6, 0.7, 1.06, 1.12, 0.5, "dipout"),
    (C1, 9.4, 0.5, 1.00, 1.08, 0.5, "end"),
]

def endcard(path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = logo_card(); im.alpha_composite(c, ((W - c.width) // 2, 820))
    f = font("Archivo-900.ttf", 64); fs = font("Manrope-800.ttf", 44)
    for txt, ff, y, col in [("Parabrisas sedán · ₡20 000", f, 975, (255, 255, 255)),
                            ("A domicilio gratis en la GAM · agende en la bio", fs, 1065, (220, 224, 218))]:
        x = (W - tlen(ff, txt)) / 2
        for ch in txt:
            g = ff if ord(ch) in ff.cmap or ch == " " else ff.fb
            d.text((x, y), ch, font=g, fill=col, stroke_width=4, stroke_fill=(0, 0, 0)); x += g.getlength(ch)
    im.save(path)

def shot(i, src, t, sp, z0, z1, bias, tr, dur, overlay=None):
    out = f"{D}/s{i:02d}.mp4"; n = round(dur * 30); zs = 1.25
    z = f"({z0}+({z1}-{z0})*on/{max(n-1,1)})"
    fx = {"open": f",fade=t=in:st=0:d=0.55", "dip": f",fade=t=in:st=0:d=0.18,fade=t=out:st={dur-0.22}:d=0.22",
          "dipout": f",fade=t=in:st=0:d=0.18,fade=t=out:st={dur-0.22}:d=0.22", "punch": "", "end": ",fade=t=in:st=0:d=0.25"}[tr]
    if i == 0: fx += f",fade=t=out:st={dur-0.22}:d=0.22"
    vf = (f"setpts=(PTS-STARTPTS)/{sp},fps=30,deshake=rx=32:ry=32,"
          f"scale={int(W*zs)}:{int(H*zs)}:force_original_aspect_ratio=increase:flags=lanczos,crop={int(W*zs)}:{int(H*zs)},"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*{bias}':d=1:s={W}x{H}:fps=30,{GRADE},setsar=1,trim=end_frame={n}{fx}")
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-t", str(dur*sp+0.3), "-i", src]
    if overlay:
        cmd += ["-loop", "1", "-t", str(dur), "-i", overlay, "-filter_complex",
                f"[0:v]{vf}[b];[1:v]format=rgba,fade=t=in:st=0.5:d=0.5:alpha=1[o];[b][o]overlay=0:0:shortest=1,format=yuv420p[v]", "-map", "[v]"]
    else:
        cmd += ["-vf", vf + ",format=yuv420p"]
    cmd += ["-an", "-frames:v", str(n), "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30"]
    run(cmd, out); return out

if __name__ == "__main__":
    endcard(f"{D}/end.png"); parts = []
    for i, s in enumerate(S):
        parts.append(shot(i, *s, B[i+1]-B[i], f"{D}/end.png" if i == len(S)-1 else None)); print("shot", i, flush=True)
    join(parts, f"{D}/video.mp4"); T = B[-1]
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/video.mp4", "-i", AUD, "-filter_complex",
         f"[1:a]atrim=0:{T},afade=t=out:st=12.6:d=1.1,aresample=48000[a]", "-map", "0:v", "-map", "[a]",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart"],
        "/home/claude/reels/reel8-sedan-parabrisas.mp4")
    print("done")
