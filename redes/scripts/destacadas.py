"""Portadas de destacadas de Instagram en Azul cristal (mismos dibujos que antes)."""
import math,sys
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1];S=1080
CRIS=(0,119,182);DEEP=(3,70,110);WHITE=(255,255,255);TINT=(191,227,247)
def base():
    im=Image.new('RGB',(S,S),CRIS);d=ImageDraw.Draw(im);d.ellipse((90,90,S-90,S-90),outline=WHITE,width=10);return im,d
def ic_calendar(d):
    x0,y0,x1,y1=330,360,750,740
    d.rounded_rectangle((x0,y0,x1,y1),40,fill=WHITE);d.rounded_rectangle((x0,y0,x1,y0+110),40,fill=DEEP);d.rectangle((x0,y0+70,x1,y0+110),fill=DEEP)
    for cx in (430,650):d.rounded_rectangle((cx-18,y0-50,cx+18,y0+40),18,fill=WHITE)
    d.line((440,590,520,670,660,500),fill=CRIS,width=44,joint='curve')
def ic_price(d):
    f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Black.otf',440);d.text((S/2,S/2+10),'₡',font=f,fill=WHITE,anchor='mm')
def ic_windshield(d):
    d.polygon([(300,700),(360,400),(720,400),(780,700)],fill=WHITE);d.polygon([(330,680),(380,430),(700,430),(750,680)],fill=TINT)
    d.line((470,690,560,610),fill=DEEP,width=26);d.line((620,690,700,620),fill=DEEP,width=26)
    for x,y in [(420,480),(520,520),(610,470)]:d.ellipse((x,y,x+34,y+34),fill=WHITE)
def ic_headlight(d):
    d.pieslice((300,380,640,720),90,270,fill=WHITE);d.rectangle((470,380,520,720),fill=WHITE)
    for i,y in enumerate([430,520,610,700]):d.rounded_rectangle((590,y-18,800,y+18),18,fill=TINT if i%2 else WHITE)
def ic_star(d):
    pts=[(540+(230 if i%2==0 else 95)*math.cos(-math.pi/2+i*math.pi/5),560+(230 if i%2==0 else 95)*math.sin(-math.pi/2+i*math.pi/5)) for i in range(10)];d.polygon(pts,fill=WHITE)
for n,f in [('reservar',ic_calendar),('tarifas',ic_price),('parabrisas',ic_windshield),('focos',ic_headlight),('clientes',ic_star)]:
    im,d=base();f(d);im.save(f'{OUT}/destacada-{n}.jpg',quality=95)
# hoja de paleta para redes
im=Image.new('RGB',(1600,900),WHITE);d=ImageDraw.Draw(im);I='/usr/share/fonts/opentype/inter/Inter-'
fh=ImageFont.truetype(I+'ExtraBold.otf',64);fb=ImageFont.truetype(I+'Medium.otf',32);fn=ImageFont.truetype(I+'Bold.otf',36)
d.text((80,70),'Paleta de redes · GlassDetailingCR',font=fh,fill=(31,35,40));d.text((80,160),'La misma de la app y la página de reservas (DESIGN.md).',font=fb,fill=(91,100,112))
for i,(n,hx,c,u) in enumerate([('Azul cristal','#0077B6',CRIS,'Etiquetas, palabra destacada'),('Azul profundo','#03466E',DEEP,'Texto sobre blanco'),('Tinte cristal','#E6F4FB',(230,244,251),'Fondos suaves'),('Blanco','#FFFFFF',WHITE,'Títulos, tarjeta del logo'),('Carbón','#1F2328',(31,35,40),'Sombra sobre fotos')]):
    x=80+i*296;d.rounded_rectangle((x,250,x+260,520),28,fill=c,outline=(227,230,234),width=3)
    d.text((x,545),n,font=fn,fill=(31,35,40));d.text((x,595),hx,font=fb,fill=(91,100,112));d.text((x,640),u,font=ImageFont.truetype(I+'Medium.otf',24),fill=(91,100,112))
d.text((80,760),'Letra: Inter · Portadas: foto real + etiqueta azul cristal + título blanco con una línea azul cristal',font=ImageFont.truetype(I+'Medium.otf',28),fill=(31,35,40))
im.save(f'{OUT}/paleta.jpg',quality=94)
