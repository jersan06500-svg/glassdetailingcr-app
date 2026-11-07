# GlassDetailingCR · App del taller

Contexto para seguir trabajando en esta app desde Claude (web o Claude Code).

## Quién la usa

- Taller **GlassDetailingCR** (Costa Rica). Se dedica a la restauración de focos y parabrisas.
- Dueño: Alejandro. **No es programador**: explicale todo en español sencillo y sin jerga. Él solo aprueba resultados.
- Equipo de 3 personas: el dueño y su mamá (iPhone) y un compañero (Android). Entran con su **cuenta de Google**.
- La usan desde el celular, instalada con "Agregar a pantalla de inicio".

## Historia corta

- 5 nov 2026: primera versión propia (agenda, clientes, productos, números, redes, carro eléctrico).
- **6 nov 2026: se reemplazó por la plantilla de GlassStudioCR**, adaptada a GlassDetailing. Es del mismo equipo: GlassStudioCR es el otro negocio de Esteban, el compañero. El dueño eligió **empezar en blanco**, así que los datos de la versión vieja (colecciones `clientes`, `citas`, `productos`, `servicios`, `movimientos`, `consultas`, `gastos`, `config`) quedaron guardados en Firestore. Las reglas nuevas ya no los dejan leer. **No los borres.**
- El dueño dijo que después decide si se vuelve a agregar algo de la versión vieja: la carga del carro eléctrico (Geely EX5, 18,5 kWh/100 km), el aviso de mantenimiento a 6 meses y la sección Redes.

## Dónde vive

| Qué | Dónde |
| --- | --- |
| App del equipo | https://jersan06500-svg.github.io/glassdetailingcr-app/ |
| Reservas para clientes | `/reservar/` |
| Página para mandar ubicación | `/ubicacion/` |
| Repositorio | https://github.com/jersan06500-svg/glassdetailingcr-app (público, rama `main`, GitHub Pages desde `main` / root, **sin dominio propio**: no agregues `CNAME` sin que el dueño compre y configure un dominio) |
| Firebase | Proyecto `glassdetailingcr`, plan gratis Spark. Auth con Google (y correo/contraseña, que la app no usa). Firestore Standard en `nam5` |

## Archivos

- `index.html`: la app interna, que es HTML + JS puro con Firebase **compat** SDK 10.12.2. Trae agenda, nueva cita, clientes, notas y metas, insumos, números (finanzas y anuncios de Meta), ruta del día, avisos de viaje entre citas, pedir reseña de Google y la animación de entrada con el logo.
- `reservar/index.html`: página pública donde el cliente agenda solo. Permite varios carros, servicios con precio por carro, ubicación por GPS, zonas con recargo y horas libres según las otras citas.
- `ubicacion/index.html`: el cliente manda su ubicación por WhatsApp. El enlace que vuelve (`/?loc=lat,lng&t=tel`) se guarda solo en su cita.
- `firestore.rules`: copia de las reglas vigentes. También están dentro de `index.html` como `var RULES`. Las vigentes de verdad se publican a mano en Firebase Console → Firestore → Reglas.
- `manifest.json`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`: la app instalable. `logo-icon.png` y `reservar/logo-icon.png` son la pulidora en PNG transparente.
- `reservar/og.jpg`: la imagen que aparece cuando se comparte el enlace de reservas.
- `sw.js`: solo limpia el caché de la versión vieja en los celulares y se da de baja. La app nueva no lo registra.

## Datos (Firestore)

`jobs` (citas), `settings` (precios, notas, metas, movimientos, meta de ventas, configuración de Meta y avisos `settings/notify`), `exp` (gastos), `team` (correos autorizados, uno por documento; solo el dueño los escribe), `slots` (horas ocupadas, de lectura pública), `holds` y `pub/cfg` (configuración pública de reservas).

- El dueño está fijo en el código: `OWNER` en `index.html` e `isOwner()` en las reglas, con su correo de Gmail. Los demás miembros se agregan desde la app (colección `team`).
- Las reglas exigen `email_verified`, por eso se entra con Google.
- No subas a este repositorio público los correos de la mamá ni del compañero.

## Lo que se adaptó de la plantilla (6 nov 2026)

- Marca GlassStudio → GlassDetailing en todos los textos. WhatsApp del negocio: `50670458967`. Enlaces a `citas.glassstudiocr.com` → la URL de GitHub Pages.
- Firebase `glassstudiocr-13cf7` → `glassdetailingcr`.
- Se quitó el píxel de Meta de GlassStudio en `reservar/`. Falta crear uno propio si el dueño lo quiere.
- `REVURL` (reseñas de Google) quedó vacío. El mensaje de agradecimiento sale sin enlace hasta que el dueño dé el enlace de reseñas de su Perfil de Empresa.
- El canal de avisos de ntfy se crea con el prefijo `glassdetailingcr-`.

## Ajustes del 6 nov 2026 (tarde)

- **Servicios** (todos con 1 año de protección): promo parabrisas + focos con polímero líquido y cerámico Fireball ₡30 000, pulido de focos ₡20 000, parabrisas SUV o pick-up ₡25 000 y parabrisas sedán ₡20 000 (confirmado por el dueño).
  - En `reservar/` están en `GLASS`, `FOCOS` y `LN`; en la app, en `SERV`. Los nombres de `LN` y `SERV` tienen que ser iguales. Si se elige la promo, los focos ya vienen incluidos.
  - La promo vieja de GlassStudio (`PROMO`, regalo de vidrio trasero) quedó apagada.
- **Zona**: toda la GAM (San José, Heredia, Alajuela y Cartago) es gratis. Fuera de la GAM no se agenda por la web: se le pide al cliente que escriba por WhatsApp.
- **Formulario de cada carro**: tipo, marca (lista `MARCAS`), modelo (con sugerencias), año, color y placa opcionales. `veh` = marca + modelo + año. El color y la placa van en la nota de la cita.
- **Cancelar cita**: al reservar se guarda en cada cita una clave `ck` de 16 caracteres. El cliente recibe el enlace `reservar/?cancelar=<ids>&k=<ck>&d=<fecha>&h=<hora>&t=<tel>` en tres lugares: la pantalla final, el mensaje de WhatsApp que manda y el mensaje de confirmación del equipo (`cxLink`).
  - Las reglas (`webCancel`) solo dejan pasar la cita a `Cancelada` si la clave coincide, y luego el cliente libera sus `slots` y `holds` (`jobCancelled`).
  - En la app, las citas `Cancelada` salen de `S.jobs` y quedan en `S.cx`. Se muestran como aviso en el inicio (Escribirle / Entendido = `cxSeen`) y le llegan al dueño por ntfy (`cxNtf`).
- **Diseño**, para que no se parezca a GlassStudio. Colores elegidos por el dueño: **negro y amarillo olivo**.
  - Negro cálido `#0d0d0b` y amarillo olivo `#c8c13a`; en modo claro se usa el olivo más oscuro `#a39c14` para que el texto se lea.
  - Letras: Archivo (ancha, 112 %) y Manrope.
  - En modo claro el botón principal es negro; en modo oscuro, amarillo olivo.
  - El momento protagonista es el haz de luz que se enciende una sola vez en la portada de reservas. No sumes animaciones decorativas en cada tarjeta.

## Pendiente de confirmar con el dueño

- El horario (`HOURS`, `DUR`) sigue siendo el de GlassStudio: lunes a sábado de 6 am a 6 pm, domingo de 8 am a 3 pm, 2 horas por carro.
- Enlace de reseñas de Google (`REVURL`) y, si lo quiere, un píxel de Meta propio.

## Reglas de la casa

1. **Cambios pequeños y enfocados**: tocar solo lo que se pidió. Antes de cambiar algo, leé cómo lo resuelve el código; la lógica de la plantilla funciona.
2. HTML + JS puro, sin frameworks, npm ni build.
3. Todo texto de usuarios o clientes que vaya a `innerHTML` se escapa.
4. Sin código muerto ni `console.log` olvidados.
5. Fechas y dinero en formato Costa Rica: `es-CR` y colones (₡).
6. **No borrar ni migrar datos de Firestore sin preguntar.**
7. Cada `<script>` tiene que pasar `node -e "new Function(src)"`. Probá en 390 px de ancho, sin scroll horizontal.
8. Si un cambio toca qué datos se leen o escriben, actualizá `firestore.rules` y `var RULES`, y recordale al dueño que publique las reglas en la consola. Publicarlas lo tiene que confirmar él.

## Cómo publicar

Cada push a `main` publica en GitHub Pages en 1 o 2 minutos. Claude en la web tiene GitHub conectado y puede hacer push directo. Explicale al dueño en 2 a 4 frases qué cambió y cómo probarlo desde el celular.
