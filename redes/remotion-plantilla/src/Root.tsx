import { Composition, staticFile } from "remotion";
import { GDReel, reelFrames, GDReelProps } from "./GDReel";
import {
  CaptionedVideo,
  calculateCaptionedVideoMetadata,
  captionedVideoSchema,
} from "./CaptionedVideo";

// Each <Composition> is an entry in the sidebar!

export const RemotionRoot: React.FC = () => {
  const porsche: GDReelProps = {
    clips: [
      { src: "gd/c1.mp4", seconds: 2.72, text: "Un Porsche Macan en nuestras manos" },
      { src: "gd/c2.mp4", seconds: 2.5, text: "Parabrisas con manchas", zoom: { x: 0.45, y: 0.45, at: 1.0, scale: 1.7 } },
      { src: "gd/c3.mp4", seconds: 1.86, text: "Pulido profesional", zoom: { x: 0.3, y: 0.5, at: 0.5, scale: 1.6 } },
      { src: "gd/c4.mp4", seconds: 2.51, text: "Sin salir de su casa" },
      { src: "gd/c5.mp4", seconds: 2.48, text: "Sellado con cerámico Fireball", zoom: { x: 0.5, y: 0.6, at: 0.6, scale: 1.5 } },
      { src: "gd/c6.mp4", seconds: 2.61, text: "Claridad que se nota" },
    ],
    precio: "₡25 000",
    detalle: "Parabrisas SUV + cerámico Fireball\nGarantía 3 meses · A domicilio en la GAM",
    cierre: 2.53,
    audio: "gd/song.mp3",
    golpe: 0.69,
  };
  const anuncio = (gancho: string): GDReelProps => ({
    clips: [
      { src: "gd/c2.mp4", seconds: 2.6, text: gancho, zoom: { x: 0.45, y: 0.5, at: 1.1, scale: 1.7 } },
      { src: "gd/c3.mp4", seconds: 2.0, text: "Lo pulimos a máquina", zoom: { x: 0.3, y: 0.5, at: 0.5, scale: 1.6 } },
      { src: "gd/c4.mp4", seconds: 2.0, text: "A domicilio en la GAM", zoom: { x: 0.35, y: 0.42, at: 0.6, scale: 1.45 } },
      { src: "gd/c5.mp4", seconds: 2.5, text: "Sellado con cerámico Fireball", zoom: { x: 0.5, y: 0.6, at: 0.7, scale: 1.5 } },
      { src: "gd/agua.mp4", seconds: 4.2, text: "Prueba de agua real: resbala sola", zoom: { x: 0.55, y: 0.35, at: 1.6, scale: 1.6 } },
    ],
    precio: "Desde ₡20 000",
    detalle: "Parabrisas con cerámico Fireball\nGarantía 3 meses · A domicilio en la GAM",
    cierre: 3.2,
    cta: "Escríbanos por WhatsApp",
    vol: 0.5,
  });
  return (
    <>
    <Composition id="AnuncioA" component={GDReel} durationInFrames={reelFrames(anuncio("¿Su parabrisas se ve así?"), 30)} fps={30} width={1080} height={1920} defaultProps={anuncio("¿Su parabrisas se ve así?")} />
    <Composition id="AnuncioB" component={GDReel} durationInFrames={reelFrames(anuncio("¿Llueve y no ve nada?"), 30)} fps={30} width={1080} height={1920} defaultProps={anuncio("¿Llueve y no ve nada?")} />
    <Composition
      id="GDReel"
      component={GDReel}
      durationInFrames={reelFrames(porsche, 30)}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={porsche}
    />
    <Composition
      id="CaptionedVideo"
      component={CaptionedVideo}
      calculateMetadata={calculateCaptionedVideoMetadata}
      schema={captionedVideoSchema}
      width={1080}
      height={1920}
      defaultProps={{
        src: staticFile("sample-video.mp4"),
      }}
    />
    </>
  );
};
