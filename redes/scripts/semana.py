"""Build the week's 7 reels in style B. Usage: python3 semana.py [draw|N ...]"""
import os
import sys

sys.path.insert(0, "/home/claude/reels")
from PIL import Image, ImageDraw

from kit import GRAF, NAVY, U, W, H, cap_b, clip, cover_photo, ctext, endcard, font, join, still, tlen

R = "/home/claude/reels"
CY = U + "fb59454b-CCBC2E84-28FC-4069-8438-0BFFD6A74585.mov"
M5769 = U + "5769f505-4b2c26aa245b4406af1b18872c15c3f0.mov"
GAM = "A domicilio gratis en toda la GAM"


def split(dst):
    """Mazda before/after as a top/bottom split with labels below Instagram's top bar."""
    c = Image.new("RGB", (W, H), GRAF)
    src = Image.open(U + "1a8bab9f-image.jpg").convert("RGB")
    for i, box in enumerate([(128, 108, 802, 1000), (830, 108, 1496, 1000)]):
        im = src.crop(box)
        im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
        top = (im.height - 900) // 2
        c.paste(im.crop((0, top, W, top + 900)), (0, 50 + i * 960))
    d = ImageDraw.Draw(c)
    f = font("Archivo-900.ttf", 60)
    for i, t in enumerate(["ANTES", "DESPUÉS"]):
        w = tlen(f, t)
        y = 330 + i * 960 if i == 0 else 1040
        d.rounded_rectangle((50, y, 50 + w + 64, y + 90), 45, fill=(255, 255, 255) if i == 0 else NAVY)
        ctext(d, 50 + (w + 64) / 2, y + 45, t, f, GRAF if i == 0 else (255, 255, 255), "mm")
    c.save(dst, quality=95)


# Each reel: list of scenes ("v", src, start, dur, text) or ("p", photo_key, dur, text), then end card lines.
REELS = {
    1: ("reel1-cybertruck", [
        ("p", "cyber", 2.4, "nos tocó una Cybertruck"),
        ("v", CY, 0.0, 3.4, "pulido profundo del parabrisas"),
        ("v", CY, 3.4, 3.2, "+ cerámico Fireball"),
        ("v", U + "IMG_6338.mov", 1.8, 4.2, "así quedó: como espejo"),
        ("v", U + "1803b0b7-IMG_6339.mov", 0.0, 2.0, ""),
    ], ("Parabrisas desde ₡20 000", GAM)),
    2: ("reel2-peugeot-focos", [
        ("p", "peugeot", 2.2, "así llegó este Peugeot"),
        ("v", U + "IMG_5943_1.mov", 13.5, 3.5, "primero, pulido profundo"),
        ("v", U + "IMG_5943_1.mov", 20.0, 2.5, ""),
        ("v", U + "IMG_5945.mov", 2.0, 3.5, "después, polímero líquido"),
        ("v", U + "IMG_5945.mov", 18.0, 4.0, "mire cómo se aclara"),
        ("v", U + "IMG_5945.mov", 44.0, 3.5, "de opaco a nuevo en 45 min"),
    ], ("Pulido de focos ₡20 000", "Precio agendando en línea · domicilio gratis en la GAM")),
    3: ("reel3-prueba-agua", [
        ("v", U + "IMG_6358.mov", 0.0, 4.5, "prueba de agua con cerámico Fireball"),
        ("v", U + "fdc46f38-IMG_6357.mov", 0.0, 3.0, "el agua resbala sola"),
        ("v", U + "IMG_6358.mov", 5.0, 4.5, "y se ve mejor cuando llueve"),
        ("p", "agua", 2.5, "1 año de protección"),
    ], ("Parabrisas desde ₡20 000", GAM)),
    4: ("reel4-antes-despues-focos", [
        ("p", "split", 3.5, ""),
        ("v", M5769, 0.0, 3.3, "antes"),
        ("v", M5769, 4.0, 3.0, "después"),
        ("v", U + "IMG_5435_3.mov", 2.0, 4.0, "polímero líquido: 1 año de protección"),
        ("v", U + "IMG_5438.mov", 6.0, 3.5, ""),
    ], ("Pulido de focos ₡20 000", "Precio agendando en línea · domicilio gratis en la GAM")),
    5: ("reel5-pasta-de-dientes", [
        ("v", U + "IMG_5943_1.mov", 0.0, 3.0, "¿pasta de dientes en los focos?"),
        ("v", U + "IMG_5943_1.mov", 4.0, 3.5, "dura poco: no lleva protección UV y se vuelve a opacar"),
        ("v", U + "IMG_5945.mov", 6.0, 3.5, "lo que sí funciona: pulido + polímero líquido"),
        ("v", U + "IMG_5945.mov", 22.0, 3.5, "1 año de protección"),
        ("v", U + "IMG_5435_3.mov", 10.0, 3.0, "así quedan"),
    ], ("Pulido de focos ₡20 000", "Precio agendando en línea · domicilio gratis en la GAM")),
    6: ("reel6-mercedes-vidrios", [
        ("v", U + "IMG_4221.mov", 0.0, 3.0, "un clásico que merecía brillar"),
        ("v", U + "IMG_4221.mov", 4.0, 4.0, "todos los vidrios pulidos"),
        ("v", U + "IMG_4221.mov", 10.0, 4.0, "+ cerámico Fireball"),
        ("v", U + "IMG_4221.mov", 15.0, 4.0, ""),
    ], ("Todos los vidrios ₡40 000", GAM)),
    7: ("reel7-promo-suv", [
        ("v", U + "IMG_5796.mov", 4.0, 3.5, "promo: parabrisas + focos"),
        ("v", U + "IMG_5796.mov", 11.0, 4.0, "parabrisas con cerámico Fireball"),
        ("v", U + "IMG_5796.mov", 6.0, 3.0, "focos con polímero líquido"),
        ("v", U + "IMG_5796.mov", 18.0, 3.0, ""),
    ], ("Promo parabrisas + focos ₡30 000", GAM)),
}


def photos(D):
    cover_photo(U + "00d5ad31-image.jpg", f"{D}/cyber.jpg", blur_box=(170, 1135, 300, 1265))
    cover_photo(U + "d9f5a6d2-image.jpg", f"{D}/peugeot.jpg")
    cover_photo(U + "ac14099f-image.jpg", f"{D}/agua.jpg")
    split(f"{D}/split.jpg")


def build(n, draw_only=False):
    name, scenes, (l1, l2) = REELS[n]
    D = f"{R}/b{n}"
    os.makedirs(D, exist_ok=True)
    photos(D)
    endcard(f"{D}/end.jpg", l1, l2)
    for i, s in enumerate(scenes):
        cap_b(f"{D}/o{i}.png", s[-1])
    if draw_only:
        return
    parts = []
    for i, s in enumerate(scenes):
        out = f"{D}/s{i}.mp4"
        last = i == len(scenes) - 1
        if s[0] == "p":
            still(out, f"{D}/{s[1]}.jpg", s[2], f"{D}/o{i}.png", fade_out=last)
        else:
            clip(out, s[1], s[2], s[3], f"{D}/o{i}.png", vol=0.7, fade_out=last)
        parts.append(out)
    still(f"{D}/end.mp4", f"{D}/end.jpg", 3.0, zoom=False, fade_in=True)
    parts.append(f"{D}/end.mp4")
    join(parts, f"{R}/{name}.mp4")


if __name__ == "__main__":
    args = sys.argv[1:]
    draw = "draw" in args
    ns = [int(a) for a in args if a.isdigit()] or list(REELS)
    for n in ns:
        build(n, draw)
        print("ok", n, flush=True)
