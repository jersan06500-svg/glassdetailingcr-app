import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Html5Video,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/fonts";

// Plantilla de reels de GlassDetailingCR: clips con subtítulos palabra por palabra y cierre de marca.
const AZUL = "#0077B6";
const AZUL_OSC = "#03466E";
const CLARO = "#BFE3F7";

loadFont({ family: "Questrial", url: staticFile("gd/questrial.woff2") });
loadFont({ family: "Roboto Slab", url: staticFile("gd/robotoslab400.woff2"), weight: "400" });
loadFont({ family: "Roboto Slab", url: staticFile("gd/robotoslab700.woff2"), weight: "700" });

// zoom: acercamiento a una zona (x, y de 0 a 1) que entra con rebote en el segundo `at`
export type Clip = { src: string; seconds: number; text: string; zoom?: { x: number; y: number; at: number; scale: number } };
export type GDReelProps = {
  clips: Clip[];
  precio: string;
  detalle: string;
  cierre: number;
  audio?: string;
  // Segundos dentro del cierre en que el logo "golpea" (para caer en el golpe de la canción)
  golpe?: number;
  cta?: string;
  // Volumen del sonido original de los clips cuando no hay canción
  vol?: number;
  // Cortes directos: sin fundidos ni acercamientos con rebote
  cortes?: boolean;
  // Solo la capa (textos, logo y cierre) sin los videos: los clips se ponen debajo con FFmpeg
  capa?: boolean;
};

const FADE = 6;

export const reelFrames = (p: GDReelProps, fps: number) =>
  Math.round((p.clips.reduce((a, c) => a + c.seconds, 0) + p.cierre) * fps);

const Caption: React.FC<{ text: string; frames: number; top?: number }> = ({ text, frames, top = 1180 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(" ");
  const per = Math.min(fps * 0.32, (frames - 8) / words.length);
  const cur = Math.min(words.length - 1, Math.floor(Math.max(0, frame - 4) / per));
  return (
    <div style={{ position: "absolute", top, left: 70, right: 70, display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "8px 18px" }}>
      {words.map((w, i) => {
        if (i > cur) return null;
        const pop = spring({ frame: frame - 4 - i * per, fps, config: { damping: 12, stiffness: 220 } });
        const on = i === cur;
        return (
          <span
            key={i}
            style={{
              fontFamily: "Questrial",
              fontSize: 92,
              lineHeight: 1.05,
              textTransform: "uppercase",
              color: "white",
              padding: "4px 18px 8px",
              borderRadius: 18,
              background: on ? AZUL : "transparent",
              WebkitTextStroke: on ? "0px" : "3px #000",
              paintOrder: "stroke fill",
              textShadow: on ? "none" : "0 4px 18px rgba(0,0,0,.55)",
              transform: `scale(${0.6 + 0.4 * pop})`,
            }}
          >
            {w}
          </span>
        );
      })}
    </div>
  );
};

const ClipScene: React.FC<{ clip: Clip; frames: number; hook: boolean; vol: number; cortes: boolean; capa: boolean }> = ({ clip, frames, hook, vol, cortes, capa }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const z = cortes ? undefined : clip.zoom;
  const punch = z ? spring({ frame: frame - Math.round(z.at * fps), fps, config: { damping: 15, stiffness: 120 } }) : 0;
  const zoom = interpolate(frame, [0, frames], [1, 1.06]) * (1 + (z ? z.scale - 1 : 0) * punch);
  const origin = z ? `${z.x * 100}% ${z.y * 100}%` : "50% 50%";
  const op = interpolate(frame, [0, FADE], [hook || cortes ? 1 : 0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: op, backgroundColor: capa ? undefined : "black" }}>
      {capa ? null : (
        <AbsoluteFill style={{ transform: `scale(${zoom})`, transformOrigin: origin }}>
          <Html5Video src={staticFile(clip.src)} volume={vol} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        </AbsoluteFill>
      )}
      <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 55%,rgba(0,0,0,.45) 100%)" }} />
      <div style={{ position: "absolute", top: 70, right: 60, background: "white", borderRadius: 22, padding: "10px 14px" }}>
        <Img src={staticFile("gd/logo.png")} style={{ height: 70, filter: "invert(1) brightness(.25)" }} />
      </div>
      <Caption text={clip.text} frames={frames} top={hook ? 330 : 1180} />
    </AbsoluteFill>
  );
};

const EndCard: React.FC<{ precio: string; detalle: string; golpe: number; cta: string; cortes: boolean }> = ({ precio, detalle, golpe, cta, cortes }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - Math.round(golpe * fps), fps, config: { damping: 9, stiffness: 260 } });
  return (
    <AbsoluteFill style={{ backgroundColor: AZUL_OSC, alignItems: "center", justifyContent: "center", opacity: cortes ? 1 : interpolate(frame, [0, 8], [0, 1]) }}>
      <Img src={staticFile("gd/logo.png")} style={{ width: 620, transform: `scale(${0.8 + 0.2 * s})` }} />
      <div style={{ fontFamily: "Roboto Slab", fontWeight: 700, fontSize: 104, color: "white", marginTop: 60 }}>{precio}</div>
      <div style={{ fontFamily: "Roboto Slab", fontSize: 40, lineHeight: 1.4, color: CLARO, marginTop: 14, textAlign: "center", padding: "0 90px", whiteSpace: "pre-line" }}>{detalle}</div>
      <div style={{ marginTop: 70, background: "white", color: AZUL_OSC, borderRadius: 999, padding: "26px 54px", fontFamily: "Questrial", fontSize: 50 }}>
        {cta}
      </div>
    </AbsoluteFill>
  );
};

export const GDReel: React.FC<GDReelProps> = (p) => {
  const { fps } = useVideoConfig();
  let from = 0;
  return (
    <AbsoluteFill style={{ backgroundColor: p.capa ? undefined : "black" }}>
      {p.audio ? <Audio src={staticFile(p.audio)} /> : null}
      {p.clips.map((c, i) => {
        const frames = Math.round(c.seconds * fps);
        const el = (
          <Sequence key={i} from={from} durationInFrames={frames + (i < p.clips.length - 1 && !p.cortes ? FADE : 0)}>
            <ClipScene clip={c} frames={frames} hook={i === 0} vol={p.audio ? 0 : (p.vol ?? 0.35)} cortes={!!p.cortes} capa={!!p.capa} />
          </Sequence>
        );
        from += frames;
        return el;
      })}
      <Sequence from={from}>
        <EndCard precio={p.precio} detalle={p.detalle} golpe={p.golpe ?? 0} cta={p.cta ?? "Agende: enlace en la bio"} cortes={!!p.cortes} />
      </Sequence>
    </AbsoluteFill>
  );
};
