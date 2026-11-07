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
- `manifest.json`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`: la app instalable. `logo-full.png` es el logo completo; `logo-icon.png` es el dibujo sobre un cuadro olivo.
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
- **Formulario de cada carro** (simplificado el 6 nov para clientes mayores): tipo, marca, modelo y año (opcional). La marca y el año se escriben con sugerencias (`mkl`, `yrl`); `mkName()` corrige la marca a como está en `MARCAS` sin importar mayúsculas ni tildes. `veh` = marca + modelo + año. Ya no se piden color ni placa.
- **Paso 2**: una sola opción por carro, en tarjetas grandes: Parabrisas + focos (promo), Solo parabrisas (muestra sedán ₡20 000 y SUV ₡25 000) y Solo focos (₡20 000). Arriba dice para qué carro son los precios.
- **Ubicación**: si el cliente no da permiso, sale una hoja (`#locdlg`, `locAlert`) con los pasos para activarla en iPhone o Android, el botón "Intentar de nuevo" y la opción de escribir la dirección.
- **Cancelar cita**: al reservar se guarda en cada cita una clave `ck` de 16 caracteres. El cliente recibe el enlace `reservar/?cancelar=<ids>&k=<ck>&d=<fecha>&h=<hora>&t=<tel>` en tres lugares: la pantalla final, el mensaje de WhatsApp que manda y el mensaje de confirmación del equipo (`cxLink`).
  - Las reglas (`webCancel`) solo dejan pasar la cita a `Cancelada` si la clave coincide, y luego el cliente libera sus `slots` y `holds` (`jobCancelled`).
  - En la app, las citas `Cancelada` salen de `S.jobs` y quedan en `S.cx`. Se muestran como aviso en el inicio (Escribirle / Entendido = `cxSeen`) y le llegan al dueño por ntfy (`cxNtf`).
- **Diseño**, para que no se parezca a GlassStudio. Colores elegidos por el dueño: **negro y amarillo olivo**.
  - Negro cálido `#0d0d0b` y amarillo olivo `#c8c13a`; en modo claro se usa el olivo más oscuro `#a39c14` para que el texto se lea.
  - Letras: Archivo (ancha, 112 %) y Manrope.
  - En modo claro el botón principal es negro; en modo oscuro, amarillo olivo.
  - El momento protagonista es el haz de luz que se enciende una sola vez en la portada de reservas. No sumes animaciones decorativas en cada tarjeta.
  - **Regla del dueño: de ahora en adelante todo lo de la página va en negro y amarillo olivo.** Los íconos van en amarillo, no en negro: la barra de abajo tiene íconos olivo y la pestaña activa con fondo olivo (`--olv`, `--olvink`).
- **App del equipo (6 nov, noche)**:
  - El inicio lleva el logo centrado con el lema "Claridad que se nota" (`.brandc`). La barra de arriba ya no repite el nombre: solo muestra la cuenta y Salir.
  - Botón **Reservas** en la barra de abajo, al lado de Clientes (`#t-rv`). Abre una hoja (`#rvs`) con el enlace de reservas para mandarlo por WhatsApp, copiarlo, compartirlo o abrir la página.
  - Agenda pensada para una mano: cada cita es su propia tarjeta con borde olivo (rojo si falta confirmar), botones de 44 px y flechas redondas para cambiar de semana. Se quitaron las animaciones de entrada de la plantilla.
- **Logo (6 nov, noche)**: el del dueño, con la pulidora en negro, "GLASS DETAILING CR" en amarillo olivo y el vidrio en gris como venía.
  - `logo-full.png` (en la raíz y en `reservar/`) es el logo completo con fondo transparente. Como la pulidora es negra, sobre fondo oscuro siempre va sobre una tarjeta clara `#f4f4ef`.
  - `logo-icon.png` es solo el dibujo, sobre un cuadro olivo con esquinas redondeadas. Los íconos de la app son el dibujo sobre fondo olivo.
  - El nombre ya no se escribe con letras al lado del logo (así se veía igual que GlassStudio): las letras animadas de la entrada (`.lgt`) están ocultas y el pie de la página de reservas ya no repite el nombre.
  - Los botones que eran verdes (WhatsApp, GPS, confirmar) ahora son amarillo olivo con texto negro.

## Pendiente de confirmar con el dueño

- El horario (`HOURS`) lo confirmó el dueño el 6 nov: lunes a sábado de 6 am a 6 pm, domingo de 8 am a 3 pm. El dueño dice que el trabajo dura unos 45 min (son 2 pulidores), y `DUR` se queda en 2 horas por carro a propósito, para cubrir las presas entre citas (decisión del dueño).
- Enlace de reseñas de Google (`REVURL`) y, si lo quiere, un píxel de Meta propio.

## Redes (6 nov 2026)

- Metricool (marca 7932743) tiene conectados Facebook (página 884212044785155) e Instagram @glassdetailingcr. Las imágenes que se programan se suben a `redes/<fecha>-<tema>/` para tener una URL pública; Metricool las copia al programar.
- Facebook e Instagram tienen una respuesta automática (Meta Business Suite → Automatizaciones) con precios, horario y el enlace de reservas. También hay una "Respuesta a comentario" (Precios por comentario): si alguien comenta precio, precios, info, cuanto, cuánto, costo, cotizar o agendar, se le contesta en público y se le manda el mismo mensaje por privado. Si cambian los precios o el horario, hay que cambiar las dos (máx. 500 caracteres en la respuesta automática). Desde el 6 nov (noche) las dos usan el texto que eligió el dueño, más humano y sin horario: "¡Hola! Qué gusto que nos escriba 😊 Ya le respondo personalmente. Mientras tanto, le dejo los precios: …". La respuesta pública al comentario es "¡Hola! Le acabo de escribir por privado 😊".
- Opiniones de la página de Facebook apagadas por decisión del dueño. El enlace de reservas está en Información → Enlaces de la página.
- **Anuncios (Meta, cuenta 5156973244430777)**: el 6 nov se prendió "Nueva campaña de Ventas" (la de agosto, video de focos, manda a WhatsApp) a ₡4 200 al día. Segmentación corregida: San José +20 km, Heredia +17 km, Alajuela +20 km, Cartago +17 km, 20 a 65 años, Advantage+ abierto, sin intereses ni exclusiones (se quitaron "trabaja en lavacar/detallado" y la exclusión de San Carlos). Las otras 3 campañas siguen en pausa. El conector Adspirer solo da 15 usos al mes (se reinician el 7 dic); si se acaban, se hace desde el Administrador de anuncios en el navegador.
- **Publicado el 6 nov**: carrusel de precios (5 imágenes, `redes/2026-11-precios/`) en Instagram y Facebook, e historias de Tarifas y Reservar (`redes/2026-11-historias/`).
- **Destacadas de Instagram**: estilo propio, distinto a GlassStudio (que usa círculos negros con íconos de línea celeste): fondo amarillo olivo lleno con íconos negros rellenos. Nombres: Tarifas, Focos, Parabrisas, Reservar, Clientes. Ya están creadas Tarifas y Reservar; faltan Focos, Parabrisas y Clientes (cuando el dueño mande videos o fotos). Las portadas personalizadas solo se pueden poner desde la app del celular; el dueño tiene los archivos. Los scripts que dibujan portadas, historias y carrusel no están en el repo: se rehacen con Archivo/Manrope (fontsource) y PIL.
- **Plan de contenido**: doc "Plan de redes · semana del 9 al 14 de noviembre" (Claude Docs). Meta: un reel por día. El dueño manda los videos por la app de Claude del celular; Claude los edita en negro y amarillo olivo, se los muestra y los programa en Metricool. Antes de publicar algo siempre se le muestra y se espera su "sí".
- **Pendiente del dueño, en el celular**: enlace de reservas en la bio de Instagram (la web no deja editar enlaces), mensaje de bienvenida en WhatsApp Business con el mismo texto de la respuesta automática, y portadas de las destacadas.

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
