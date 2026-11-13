# Plantilla de reels (Remotion)

Respaldo de la plantilla con la que se hicieron los reels del 12 nov 2026 (Porsche Macan y anuncios de parabrisas).

Para volver a usarla en una sesión nueva:

1. `npx create-video@latest --yes --tiktok glassdetailing-reels`
2. Copiar `src/GDReel.tsx`, `src/Root.tsx`, `remotion.config.ts` y la carpeta `public/gd/` de aquí al proyecto nuevo.
3. `npm i @remotion/fonts@<misma versión de remotion>`
4. Poner los clips (1080x1920, H.264, 30 fps) en `public/gd/` y editar los textos, tiempos y acercamientos en `Root.tsx`.
5. `npx remotion render GDReel salida.mp4 --concurrency=2`

Los videos originales no se suben aquí (pesan mucho): están en `Documentos/GlassDetailingCR/04-Videos/material-original` en la compu del dueño.
