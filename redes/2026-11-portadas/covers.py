"""GlassDetailingCR social brand: palette, reel covers (1080x1920, safe in the 3:4 grid crop), highlight covers."""
import sys

sys.path.insert(0, "/home/claude/reels")
from PIL import Image, ImageDraw, ImageFilter

from kit import LOGO, font, tlen, wrap

W, H = 1080, 1920
GRAF = (17, 19, 21)
NAVY = (21, 48, 94)       # #15305e
ELEC = (59, 111, 208)     # #3b6fd0
WHITE = (245, 247, 242)   # #f5f7f2
STEEL = (138, 144, 153)   # #8a9099
U = "/mnt/user-data/uploads/"
C = "/home/claude/covers/"
# 3:4 grid crop of a 9:16 cover: 1080x1440 centered → y 240..1680. Keep everything inside with margin.
TOP, BOT = 300, 1620


def cover_fit(src, blur_box=None, ybias=0.5):
    im = Image.open(src).convert("RGB")
    if blur_box:
        r = im.crop(blur_box).filter(ImageFilter.GaussianBlur(28))
        im.paste(r, blur_box[:2])
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - W) // 2
    y = int((im.height - H) * ybias)
    return im.crop((x, y, x + W, y + H))


def text_run(d, x, y, parts, f):
    """Draw [(text, color)] left-aligned on one line with per-char fallback (₡, ¿)."""
    for txt, col in parts:
        for ch in txt:
            g = f if ord(ch) in f.cmap or ch == " " else f.fb
            d.text((x, y), ch, font=g, fill=col)
            x += g.getlength(ch)
    return x


def reel_cover(out, photo, tag, line1, line2, accent_line=2, sub=None, blur_box=None, ybias=0.5):
    im = cover_fit(photo, blur_box, ybias).convert("RGBA")
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    # Darken bottom half for the title, and a light veil on top for the tag/logo.
    for y in range(H):
        a = 0
        if y > 820:
            a = int(225 * min(1, (y - 820) / 520))
        elif y < 520:
            a = int(110 * (1 - y / 520))
        sd.line((0, y, W, y), fill=(17, 19, 21, a))
    im.alpha_composite(shade)
    d = ImageDraw.Draw(im)
    # Tag pill (top-left inside safe area)
    ft = font("Archivo-900.ttf", 40)
    tw = tlen(ft, tag)
    d.rounded_rectangle((70, TOP + 20, 70 + tw + 56, TOP + 20 + 74), 37, fill=NAVY + (255,))
    text_run(d, 98, TOP + 34, [(tag, WHITE)], ft)
    # Logo card (top-right inside safe area)
    lg = Image.open(LOGO).convert("RGBA")
    lg.thumbnail((170, 108), Image.LANCZOS)
    card = Image.new("RGBA", (lg.width + 26, lg.height + 16), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle((0, 0, card.width - 1, card.height - 1), 14, fill=WHITE + (240,))
    card.alpha_composite(lg, (13, 8))
    im.alpha_composite(card, (W - 70 - card.width, TOP + 10))
    # Title: two big lines, one in electric blue; then a small subline.
    f = font("Archivo-900.ttf", 112)
    y = 1235
    for i, ln in enumerate([line1, line2]):
        col = ELEC if i + 1 == accent_line else WHITE
        text_run(d, 70, y, [(ln, col)], f)
        y += 122
    if sub:
        fs = font("Manrope-800.ttf", 40)
        text_run(d, 74, y + 14, [(sub, (205, 210, 215))], fs)
    # Thin brand bar
    d.rectangle((70, BOT - 6, 70 + 120, BOT), fill=ELEC)
    im.convert("RGB").save(out, quality=92)


def highlight(out, label, icon):
    """Highlight cover: navy circle-friendly square with white glyph."""
    S = 1080
    im = Image.new("RGB", (S, S), NAVY)
    d = ImageDraw.Draw(im)
    d.ellipse((90, 90, S - 90, S - 90), outline=ELEC, width=14)
    icon(d, S)
    im.save(out, quality=95)


def ic_calendar(d, S):
    x0, y0, x1, y1 = 330, 360, 750, 740
    d.rounded_rectangle((x0, y0, x1, y1), 40, fill=WHITE)
    d.rectangle((x0, y0 + 40, x1, y0 + 110), fill=WHITE)
    d.rounded_rectangle((x0, y0, x1, y0 + 110), 40, fill=ELEC)
    for cx in (430, 650):
        d.rounded_rectangle((cx - 18, y0 - 50, cx + 18, y0 + 40), 18, fill=WHITE)
    d.line((440, 590, 520, 670, 660, 500), fill=NAVY, width=44, joint="curve")


def ic_price(d, S):
    f = font("Archivo-900.ttf", 420)
    g = f.fb
    ch = "₡"
    w = g.getlength(ch)
    d.text(((S - w) / 2, 270), ch, font=g, fill=WHITE)


def ic_windshield(d, S):
    d.polygon([(300, 700), (360, 400), (720, 400), (780, 700)], fill=WHITE)
    d.polygon([(330, 680), (380, 430), (700, 430), (750, 680)], fill=ELEC)
    d.line((470, 690, 560, 610), fill=WHITE, width=26)
    d.line((620, 690, 700, 620), fill=WHITE, width=26)
    for i, (x, y) in enumerate([(420, 480), (520, 520), (610, 470)]):
        d.ellipse((x, y, x + 34, y + 34), fill=WHITE)


def ic_headlight(d, S):
    d.pieslice((300, 380, 640, 720), 90, 270, fill=WHITE)
    d.rectangle((470, 380, 520, 720), fill=WHITE)
    for i, y in enumerate([430, 520, 610, 700]):
        d.rounded_rectangle((590, y - 18, 800, y + 18), 18, fill=ELEC if i % 2 else WHITE)


def ic_star(d, S):
    import math
    cx, cy, r1, r2 = 540, 560, 230, 95
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = r1 if i % 2 == 0 else r2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=WHITE)


def brand_sheet(out):
    im = Image.new("RGB", (1600, 900), WHITE)
    d = ImageDraw.Draw(im)
    fh = font("Archivo-900.ttf", 64)
    fb = font("Manrope-800.ttf", 34)
    text_run(d, 80, 70, [("Paleta GlassDetailingCR", GRAF)], fh)
    text_run(d, 80, 160, [("Igual a la página de reservas. Sin verde lima, sin degradados de color.", STEEL)], fb)
    sw = [("Grafito", "#111315", GRAF, "Fondos"), ("Azul marino", "#15305e", NAVY, "Marca, etiquetas"),
          ("Azul eléctrico", "#3b6fd0", ELEC, "Palabra destacada"), ("Blanco", "#f5f7f2", WHITE, "Títulos"),
          ("Gris acero", "#8a9099", STEEL, "Texto chico")]
    for i, (n, hx, col, use) in enumerate(sw):
        x = 80 + i * 296
        d.rounded_rectangle((x, 250, x + 260, 520), 28, fill=col, outline=(210, 214, 218), width=3)
        text_run(d, x, 545, [(n, GRAF)], font("Archivo-900.ttf", 36))
        text_run(d, x, 595, [(hx, STEEL)], fb)
        text_run(d, x, 640, [(use, STEEL)], font("Manrope-700.ttf", 28))
    text_run(d, 80, 740, [("Letras: ", GRAF), ("Archivo Black", NAVY), (" para títulos · ", GRAF), ("Manrope", NAVY), (" para textos", GRAF)], fb)
    text_run(d, 80, 800, [("Portadas: foto real + etiqueta azul marino + título blanco con una palabra en azul eléctrico", GRAF)], font("Manrope-700.ttf", 30))
    im.save(out, quality=94)


REELS = [
    ("r1", U + "cf670693-image.jpg", "PARABRISAS", "Le tocó a una", "Cybertruck", "Pulido + cerámico Fireball", None, 0.3),
    ("r2", C + "f_peugeot.jpg", "FOCOS", "De opaco", "a nuevo", "En 45 min, en su casa", None, 0.5),
    ("r3", U + "ac14099f-image.jpg", "PARABRISAS", "La lluvia", "resbala sola", "Cerámico Fireball · 1 año", None, 0.5),
    ("r4", U + "1a8bab9f-image.jpg", "FOCOS", "Antes y", "después", "Focos amarillos → como nuevos", None, 0.5),
    ("r5", C + "f_pasta.jpg", "FOCOS", "¿Pasta de", "dientes?", "Lo que sí funciona", None, 0.5),
    ("r6", C + "f_merc.jpg", "TODOS LOS VIDRIOS", "Un clásico", "que brilla", "Todos los vidrios ₡40 000", None, 0.45),
    ("r7", C + "f_suv.jpg", "PROMO", "Parabrisas", "+ focos", "₡30 000 · 1 año de protección", None, 0.5),
]

if __name__ == "__main__":
    brand_sheet(C + "paleta.jpg")
    for key, ph, tag, l1, l2, sub, bb, yb in REELS:
        reel_cover(C + f"portada-{key}.jpg", ph, tag, l1, l2, 2, sub, bb, yb)
    for name, label, ic in [("reservar", "Reservar", ic_calendar), ("tarifas", "Tarifas", ic_price),
                            ("parabrisas", "Parabrisas", ic_windshield), ("focos", "Focos", ic_headlight),
                            ("clientes", "Clientes", ic_star)]:
        highlight(C + f"destacada-{name}.jpg", label, ic)
    print("ok")
