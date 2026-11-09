"""Cambia el cierre de 3 s de los reels en borrador por la versión en Azul cristal."""
import subprocess,sys,os
from PIL import Image,ImageDraw,ImageFont
REP='/home/claude/glassdetailingcr-app/'
V=REP+'redes/2026-11-reels/';OUT=sys.argv[1]
W,H=1080,1920;CRIS=(0,119,182);DEEP=(3,70,110);TINT=(230,244,251)
I='/usr/share/fonts/opentype/inter/Inter-'
GAM='A domicilio gratis en toda la GAM';FOC='Precio agendando en línea · domicilio gratis en la GAM'
REELS={'reel1-cybertruck':('Parabrisas desde ₡20 000',GAM),'reel2-peugeot-focos':('Pulido de focos ₡20 000',FOC),
 'reel3-prueba-agua':('Parabrisas desde ₡20 000',GAM),'reel4-antes-despues-focos':('Pulido de focos ₡20 000',FOC),
 'reel5-pasta-de-dientes':('Pulido de focos ₡20 000',FOC),'reel7-promo-suv':('Promo parabrisas + focos ₡30 000',GAM)}
def wrap(d,t,f,mw):
    out,cur=[],''
    for w in t.split():
        n=(cur+' '+w).strip()
        if d.textlength(n,font=f)<=mw:cur=n
        else:out.append(cur);cur=w
    return out+[cur]
def card(path,l1,l2,l3='Agende en línea · enlace en la bio'):
    im=Image.new('RGB',(W,H),CRIS);d=ImageDraw.Draw(im)
    c=(120,430,W-120,990);d.rounded_rectangle(c,48,fill=(255,255,255))
    lg=Image.open(REP+'logo-full.png').convert('RGBA');s=min((c[2]-c[0]-100)/lg.width,(c[3]-c[1]-100)/lg.height)
    lg=lg.resize((int(lg.width*s),int(lg.height*s)),Image.LANCZOS);im.paste(lg,((W-lg.width)//2,c[1]+(560-lg.height)//2),lg)
    ft=ImageFont.truetype(I+'ExtraBold.otf',64);fs=ImageFont.truetype(I+'Medium.otf',42);fg=ImageFont.truetype(I+'Bold.otf',42)
    y=1100
    for ln in wrap(d,l1,ft,W-160):d.text((W/2,y),ln,font=ft,fill='white',anchor='ma');y+=82
    y+=18
    for ln in wrap(d,l2,fs,W-180):d.text((W/2,y),ln,font=fs,fill=TINT,anchor='ma');y+=58
    y+=44;tw=d.textlength(l3,font=fg)
    d.rounded_rectangle((W/2-tw/2-44,y,W/2+tw/2+44,y+104),52,fill='white');d.text((W/2,y+52),l3,font=fg,fill=DEEP,anchor='mm')
    im.save(path,quality=95)
def run(c):subprocess.run(['ffmpeg','-v','error','-y']+c,check=True)
ENC=['-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','128k','-ar','48000','-ac','2']
for name,(l1,l2) in REELS.items():
    src=V+name+'.mp4';d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]))
    cut=round(d-3.0,3);jpg=f'{OUT}/end-{name}.jpg';card(jpg,l1,l2)
    run(['-i',src,'-t',str(cut)]+ENC+[f'{OUT}/body.mp4'])
    run(['-loop','1','-i',jpg,'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','3','-vf','fps=30,fade=t=in:st=0:d=0.3,format=yuv420p']+ENC+[f'{OUT}/end.mp4'])
    with open(f'{OUT}/l.txt','w') as fh:fh.write(f"file '{OUT}/body.mp4'\nfile '{OUT}/end.mp4'\n")
    run(['-f','concat','-safe','0','-i',f'{OUT}/l.txt','-c','copy','-movflags','+faststart',f'{OUT}/{name}.mp4'])
    print(name,round(d,2),'->',subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{OUT}/{name}.mp4']).decode().strip(),flush=True)
for f in ['body.mp4','end.mp4','l.txt']:os.remove(f'{OUT}/{f}')
