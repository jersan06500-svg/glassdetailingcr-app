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
  // Porsche Cayenne, todos los vidrios (13 nov 2026). Sin sonido: la música se pone en Instagram.
  const porsche1311: GDReelProps = {
    clips: [
      { src: "gd/p1.mp4", seconds: 3.0, text: "¿Sus vidrios se ven así?", zoom: { x: 0.45, y: 0.45, at: 1.2, scale: 1.5 } },
      { src: "gd/p2.mp4", seconds: 2.2, text: "Así quedaron", zoom: { x: 0.5, y: 0.4, at: 0.8, scale: 1.3 } },
      { src: "gd/p3.mp4", seconds: 2.6, text: "Todos los vidrios" },
      { src: "gd/p4.mp4", seconds: 2.6, text: "Sellados con cerámico Fireball" },
      { src: "gd/p5.mp4", seconds: 3.0, text: "Claridad que se nota" },
    ],
    precio: "₡40 000",
    detalle: "Todos los vidrios SUV o pick-up\nGarantía 3 meses · A domicilio gratis en la GAM",
    cierre: 3.2,
    golpe: 0.3,
    vol: 0,
    cortes: true,
  };
  return (
    <>
    <Composition id="Porsche1311" component={GDReel} durationInFrames={reelFrames(porsche1311, 30)} fps={30} width={1080} height={1920} defaultProps={porsche1311} />
    <Composition id="Porsche1311Capa" component={GDReel} durationInFrames={reelFrames(porsche1311, 30)} fps={30} width={1080} height={1920} defaultProps={{ ...porsche1311, capa: true }} />
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
