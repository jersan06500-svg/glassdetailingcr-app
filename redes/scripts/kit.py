"""Shared helpers for GlassDetailingCR reels: text overlays, end card, scene encoding."""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
F = "/tmp/fonts/"
U = "/mnt/user-data/uploads/"
LOGO = "/home/claude/glassdetailingcr-app/logo-full.png"
GRAF = (17, 19, 21)
WHITE = (245, 247, 242)
NAVY = (43, 90, 168)
ENC = ["-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]


_CMAP = {}


def font(name, size):
    f = ImageFont.truetype(F + name, size)
    if name not in _CMAP:
        from fontTools.ttLib import TTFont
        _CMAP[name] = set(TTFont(F + name).getBestCmap())
    f.cmap = _CMAP[name]
    f.fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * 0.92))
    return f


def _pick(f, c):
    return f if ord(c) in f.cmap or c == " " else f.fb


def tlen(f, s):
    return sum(_pick(f, c).getlength(c) for c in s)


def ctext(d, x, y, s, f, fill, anchor="ma"):
    """Centered text with per-character fallback (₡). anchor 'ma' = top, 'mm' = middle."""
    w = tlen(f, s)
    x -= w / 2
    if anchor == "mm":
        y -= f.size * 0.62
    for c in s:
        ff = _pick(f, c)
        d.text((x, y), c, font=ff, fill=fill)
        x += ff.getlength(c)


def wrap(d, text, f, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if tlen(f, t) <= maxw:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def caption(path, title, sub=None, y=330, tag=None):
    """Transparent PNG: title in white on a graphite box, optional subtitle and navy tag."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    ft = font("Archivo-900.ttf", 66)
    fs = font("Manrope-800.ttf", 44)
    lines = wrap(d, title, ft, W - 200)
    lh = 80
    bh = lh * len(lines) + 56
    sl = wrap(d, sub, fs, W - 220) if sub else []
    bh += 58 * len(sl) + (14 if sl else 0)
    d.rounded_rectangle((70, y, W - 70, y + bh), 34, fill=GRAF + (235,))
    yy = y + 30
    for ln in lines:
        ctext(d, W / 2, yy, ln, ft, WHITE, "ma")
        yy += lh
    yy += 14
    for ln in sl:
        ctext(d, W / 2, yy, ln, fs, (200, 205, 198), "ma")
        yy += 58
    if tag:
        fg = font("Archivo-900.ttf", 50)
        tw = tlen(fg, tag)
        ty = y + bh + 24
        d.rounded_rectangle((W / 2 - tw / 2 - 34, ty, W / 2 + tw / 2 + 34, ty + 92), 46, fill=NAVY + (255,))
        ctext(d, W / 2, ty + 46, tag, fg, (255, 255, 255), "mm")
    im.save(path)


def endcard(path, line1, line2, line3="Agende en línea · enlace en la bio"):
    im = Image.new("RGB", (W, H), GRAF)
    d = ImageDraw.Draw(im)
    card = (120, 430, W - 120, 430 + 560)
    d.rounded_rectangle(card, 48, fill=WHITE)
    lg = Image.open(LOGO)
    s = min((card[2] - card[0] - 100) / lg.width, (card[3] - card[1] - 100) / lg.height)
    lg = lg.resize((int(lg.width * s), int(lg.height * s)), Image.LANCZOS)
    im.paste(lg, ((W - lg.width) // 2, card[1] + (560 - lg.height) // 2), lg)
    ft = font("Archivo-900.ttf", 62)
    fs = font("Manrope-800.ttf", 46)
    y = 1100
    for ln in wrap(d, line1, ft, W - 160):
        ctext(d, W / 2, y, ln, ft, WHITE, "ma")
        y += 80
    y += 20
    for ln in wrap(d, line2, fs, W - 160):
        ctext(d, W / 2, y, ln, fs, (200, 205, 198), "ma")
        y += 60
    fg = font("Archivo-900.ttf", 44)
    tw = tlen(fg, line3)
    y += 40
    d.rounded_rectangle((W / 2 - tw / 2 - 40, y, W / 2 + tw / 2 + 40, y + 100), 50, fill=NAVY)
    ctext(d, W / 2, y + 50, line3, fg, (255, 255, 255), "mm")
    im.save(path, quality=95)


def cover_photo(src, dst, blur_box=None, rotate=0):
    """Scale/crop a photo to 1080x1920 (cover), optionally blur a box (in source pixels)."""
    im = Image.open(src).convert("RGB")
    if rotate:
        im = im.rotate(rotate, expand=True)
    if blur_box:
        r = im.crop(blur_box).filter(ImageFilter.GaussianBlur(28))
        im.paste(r, blur_box[:2])
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    im.crop((x, y, x + W, y + H)).save(dst, quality=95)


def run(cmd, out):
    tmp = out[:-4] + ".tmp.mp4"
    subprocess.run(cmd + [tmp], check=True)
    os.replace(tmp, out)


def clip(out, src, ss, dur, overlay=None, vf_extra="", vol=1.0, fade_in=False, fade_out=False):
    """One scene from a video: cover-crop to 1080x1920, optional overlay PNG (fades in), with audio."""
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}"
    if vf_extra:
        vf += "," + vf_extra
    if fade_in:
        vf += ",fade=t=in:st=0:d=0.3"
    if fade_out:
        vf += f",fade=t=out:st={dur - 0.3}:d=0.3"
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(dur), "-i", src]
    if overlay:
        cmd += ["-loop", "1", "-t", str(dur), "-i", overlay]
        fc = f"[0:v]{vf}[b];[1:v]format=rgba,fade=t=in:st=0:d=0.12:alpha=1[o];[b][o]overlay=0:0:shortest=1,format=yuv420p[v]"
    else:
        fc = f"[0:v]{vf},format=yuv420p[v]"
    fc += f";[0:a]volume={vol},aresample=48000,apad,atrim=0:{dur}[a]"
    cmd += ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", str(dur)] + ENC + ["-c:a", "aac", "-b:a", "128k", "-ac", "2", "-ar", "48000"]
    run(cmd, out)


def still(out, img, dur, overlay=None, zoom=True, fade_in=False, fade_out=False):
    """Scene from a 1080x1920 still with slow push-in, optional overlay, silent audio."""
    n = int(dur * FPS)
    vf = f"scale={W * 2}:{H * 2},zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}" if zoom else f"loop=-1:1,fps={FPS},trim=duration={dur}"
    if fade_in:
        vf += ",fade=t=in:st=0:d=0.3"
    if fade_out:
        vf += f",fade=t=out:st={dur - 0.4}:d=0.4"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", img]
    if overlay:
        cmd += ["-loop", "1", "-t", str(dur), "-i", overlay]
        fc = f"[0:v]{vf}[b];[1:v]format=rgba,fade=t=in:st=0:d=0.12:alpha=1[o];[b][o]overlay=0:0:shortest=1,format=yuv420p[v]"
    else:
        fc = f"[0:v]{vf},format=yuv420p[v]"
    cmd += ["-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo"]
    ai = 2 if overlay else 1
    cmd += ["-filter_complex", fc, "-map", "[v]", "-map", f"{ai}:a", "-t", str(dur)] + ENC + ["-c:a", "aac", "-b:a", "128k"]
    run(cmd, out)


def join(parts, out):
    lst = out + ".txt"
    with open(lst, "w") as fh:
        for p in parts:
            fh.write(f"file '{p}'\n")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart"], out)
    os.remove(lst)


def logo_card():
    lg = Image.open(LOGO).convert("RGBA")
    lg.thumbnail((190, 120), Image.LANCZOS)
    card = Image.new("RGBA", (lg.width + 28, lg.height + 18), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle((0, 0, card.width - 1, card.height - 1), 16, fill=(245, 247, 242, 235))
    card.alpha_composite(lg, (14, 9))
    return card


def cap_b(path, text=""):
    """Style B: clean subtitle (white, black outline) in the lower middle + small logo top-right."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    c = logo_card()
    im.alpha_composite(c, (W - c.width - 44, 190))
    if text:
        d = ImageDraw.Draw(im)
        f = font("Manrope-800.ttf", 60)
        lines = wrap(d, text, f, W - 180)
        y = 1210 - (len(lines) - 1) * 76
        for ln in lines:
            w = tlen(f, ln)
            x = (W - w) / 2
            for ch in ln:
                ff = f if ord(ch) in f.cmap or ch == " " else f.fb
                d.text((x, y), ch, font=ff, fill=(255, 255, 255), stroke_width=6, stroke_fill=(0, 0, 0))
                x += ff.getlength(ch)
            y += 76
    im.save(path)
