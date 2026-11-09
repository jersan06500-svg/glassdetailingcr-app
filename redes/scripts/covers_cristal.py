"""Pasa las portadas de reels al Azul cristal: repinta etiqueta, línea destacada del título y barrita."""
import numpy as np,sys
from PIL import Image,ImageDraw
R='/home/claude/glassdetailingcr-app/redes/2026-11-portadas/'
OUT=sys.argv[1]
NAVY=np.array([21,48,94.]);ELEC=np.array([59,111,208.]);CRIS=np.array([0,119,182.])
def swap(a,box,old,new):
    x0,y0,x1,y1=box;r=a[y0:y1,x0:x1]
    # píxel = t*old + (1-t)*fondo gris: se estima t con la diferencia azul-rojo (el fondo es neutro)
    t=np.clip((r[...,2]-r[...,0])/(old[2]-old[0]),0,1)
    t=np.where((r[...,2]-r[...,0])>12,t,0)
    for i in range(3):r[...,i]=np.clip(r[...,i]+t*(new[i]-old[i]),0,255)
for k in ['r1','r2','r3','r4','r5','r7']:
    a=np.asarray(Image.open(R+f'portada-{k}.jpg').convert('RGB'),float).copy()
    swap(a,(60,1350,1080,1500),ELEC,CRIS)   # línea 2 del título
    swap(a,(60,1600,260,1630),ELEC,CRIS)    # barrita
    # etiqueta: el fondo es azul marino casi puro, se reemplaza el color de los píxeles marinos
    x0,y0,x1,y1=60,310,760,410;r=a[y0:y1,x0:x1]
    d=np.linalg.norm(r-NAVY,axis=2);m=np.clip(1-d/90,0,1)
    for i in range(3):r[...,i]=r[...,i]+m*(CRIS[i]-NAVY[i])
    Image.fromarray(np.clip(a,0,255).astype('uint8')).save(OUT+f'/portada-{k}.jpg',quality=93)
print('ok')
