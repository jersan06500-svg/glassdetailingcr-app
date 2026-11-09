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
- Se quitó el píxel de Meta de GlassStudio en `reservar/`. **7 nov: píxel propio creado** en el portfolio "Glassdetailingcr" (business 1217773779879043): conjunto de datos "Pixel GlassDetailingCR reservas", id `2161726007758577`. En `reservar/` manda PageView, InitiateCheckout (botón de empezar), AddToCart (al pasar del paso de servicios, con valor en CRC) y Schedule + Lead (al confirmar, con valor). Helper `px()`. No manda datos personales. El mismo 7 nov, con el sí del dueño, la cuenta publicitaria 5156973244430777 se agregó (para siempre) al portfolio "Glassdetailingcr" y el píxel quedó conectado a ella. Ya recibe eventos.
- `REVURL` (reseñas de Google) quedó vacío. El mensaje de agradecimiento sale sin enlace hasta que el dueño dé el enlace de reseñas de su Perfil de Empresa.
- El canal de avisos de ntfy se crea con el prefijo `glassdetailingcr-`.

## Ajustes del 6 nov 2026 (tarde)

- **Promo de reserva en línea (6 nov, noche, decisión del dueño)**: el pulido de focos con polímero líquido "normalmente" cuesta ₡25 000, pero si el cliente agenda en la página de reservas le queda en ₡20 000 (el precio que ya muestra `reservar/`). El pulido tradicional ya no se ofrece. Así se les dice a los clientes por mensaje y así quedó la respuesta automática del anuncio de focos (plantilla "Iniciar conversaciones 26/06/2026" en el Administrador de anuncios).
- **Servicios** (todos con 1 año de protección): promo parabrisas + focos con polímero líquido y cerámico Fireball ₡30 000, pulido de focos ₡20 000, parabrisas SUV o pick-up ₡25 000, parabrisas sedán ₡20 000, todos los vidrios ₡40 000 y techo panorámico +₡20 000 (confirmado por el dueño).
  - En `reservar/` están en `GLASS`, `FOCOS` y `LN`; en la app, en `SERV`. Los nombres de `LN` y `SERV` tienen que ser iguales. Si se elige la promo, los focos ya vienen incluidos.
  - La promo vieja de GlassStudio (`PROMO`, regalo de vidrio trasero) quedó apagada.
- **Zona**: toda la GAM (San José, Heredia, Alajuela y Cartago) es gratis. Fuera de la GAM no se agenda por la web: se le pide al cliente que escriba por WhatsApp.
- **Formulario de cada carro** (simplificado el 6 nov para clientes mayores): tipo, marca, modelo y año (opcional). La marca y el año se escriben con sugerencias (`mkl`, `yrl`); `mkName()` corrige la marca a como está en `MARCAS` sin importar mayúsculas ni tildes. `veh` = marca + modelo + año. Ya no se piden color ni placa.
- **Varios carros (arreglo 6 nov, noche)**: un solo manejador de clics por delegación (`addCar`, `rmCar`, `useCar`). La ✕ de cada carro es su propio botón de 44 px (en iPhone el toque sobre un `span` dentro de un `button` no llegaba). "Agregar otro carro" ignora toques hasta 0,7 s después de elegir un servicio (toque fantasma) y es un botón secundario, no negro. Al pasar del paso 2, los carros que quedaron en blanco se quitan solos (`dropEmpty`). `syncVeh` ya no reconstruye el paso 2.
- **Paso 1 (6 nov, noche)**: primero marca y modelo, después el tipo. Si `guess()` reconoce el modelo (listas `SUVRX`/`SEDRX`), marca el tipo solo (`setVt`), atenúa el otro (`.lock`) y no deja escogerlo (ej.: un Vitara no se puede poner como sedán). Si no lo reconoce, el cliente elige.
- **Paso 2 (6 nov, noche)**: en este orden: Parabrisas + focos (promo ₡30 000), Parabrisas SUV o pick-up ₡25 000, Parabrisas sedán ₡20 000 (el del otro tipo queda bloqueado), Todos los vidrios ₡40 000, Pulido de focos ₡20 000, y un extra "+ Techo panorámico" +₡20 000 (`S.tp`, `TECHO`) que se suma a cualquier opción. Íconos SVG propios (`ICO`: parabrisas, focos, techo). Debajo, recuadro "Servicio a domicilio totalmente gratis en toda la GAM" con "Ocupamos un toma de 110 V" y "De preferencia, el carro bajo techo"; lo mismo sale en el resumen. `SERV` en la app tiene "Todos los vidrios + cerámico Fireball" y "Techo panorámico + cerámico Fireball" con los mismos nombres que `LN`/`TECHO`.
- **Ubicación**: si el cliente no da permiso, sale una hoja (`#locdlg`, `locAlert`) con los pasos para activarla en iPhone o Android, el botón "Intentar de nuevo" y la opción de escribir la dirección.
- **Cancelar cita**: al reservar se guarda en cada cita una clave `ck` de 16 caracteres. El cliente recibe el enlace `reservar/?cancelar=<ids>&k=<ck>&d=<fecha>&h=<hora>&t=<tel>` en tres lugares: la pantalla final, el mensaje de WhatsApp que manda y el mensaje de confirmación del equipo (`cxLink`).
  - Las reglas (`webCancel`) solo dejan pasar la cita a `Cancelada` si la clave coincide, y luego el cliente libera sus `slots` y `holds` (`jobCancelled`).
  - En la app, las citas `Cancelada` salen de `S.jobs` y quedan en `S.cx`. Se muestran como aviso en el inicio (Escribirle / Entendido = `cxSeen`) y le llegan al dueño por ntfy (`cxNtf`).
- **PALETA NUEVA (6 nov, noche, manda sobre lo de abajo)**: grafito `#111315`, verde lima eléctrico `#b8ff00` (claro `#d4ff66`), blanco `#f5f7f2` y azul marino `#15305e` (el dueño lo pidió en vez del celeste de su referencia, que se parecía a GlassStudio). Fondos oscuros `#0b0d0f` / tarjetas `#181b1f`.
  - Modo oscuro: acentos, íconos y botones en lima con texto grafito. Modo claro: el lima no se lee sobre blanco, así que íconos, bordes de selección y texto de acento van en azul marino (`--glow`, `--olv` claro); el botón principal es grafito con letras lima.
  - Íconos de la app y `logo-icon.png`: dibujo sobre cuadro lima. En `logo-full.png` el nombre "GLASS DETAILING CR" quedó en azul marino (en lima no se leía sobre la tarjeta clara).
  - **Página de reservas (`reservar/`), decisión del dueño 6 nov noche: sin verde lima, todo en azul marino.** Claro: `#15305e`; oscuro: `#2b5aa8` (botones) y `#3b6fd0` (selección), con letras blancas. La app del equipo sigue con lima.
  - Las variables siguen llamándose `--olv`/`--olvink` aunque ya no sean olivo. `reservar/og.jpg` y lo ya publicado en redes siguen en olivo; lo nuevo va con la paleta nueva.
- **Diseño**, para que no se parezca a GlassStudio. Colores elegidos por el dueño: **negro y amarillo olivo** (paleta anterior).
  - Negro cálido `#0d0d0b` y amarillo olivo `#c8c13a`; en modo claro se usa el olivo más oscuro `#a39c14` para que el texto se lea.
  - Letras: Archivo (ancha, 112 %) y Manrope.
  - En modo claro el botón principal es negro; en modo oscuro, amarillo olivo.
  - **Sin efectos (decisión del dueño, 6 nov noche):** en `reservar/` se quitaron el resplandor de la portada, el confeti y todas las animaciones (`@keyframes`). Colores planos, de un solo tono. No volver a agregar brillos, degradados ni animaciones.
  - **Regla del dueño: todo lo de la página va con la paleta vigente** (hoy: grafito, lima y azul marino). Los íconos van en amarillo, no en negro: la barra de abajo tiene íconos olivo y la pestaña activa con fondo olivo (`--olv`, `--olvink`).
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
- Enlace de reseñas de Google (`REVURL`).

## Redes (6 nov 2026)

- Metricool (marca 7932743) tiene conectados Facebook (página 884212044785155) e Instagram @glassdetailingcr. Las imágenes que se programan se suben a `redes/<fecha>-<tema>/` para tener una URL pública; Metricool las copia al programar.
- Facebook e Instagram tienen una respuesta automática (Meta Business Suite → Automatizaciones) con precios, horario y el enlace de reservas. También hay una "Respuesta a comentario" (Precios por comentario): si alguien comenta precio, precios, info, cuanto, cuánto, costo, cotizar o agendar, se le contesta en público y se le manda el mismo mensaje por privado. Si cambian los precios o el horario, hay que cambiar las dos (máx. 500 caracteres en la respuesta automática). Desde el 6 nov (noche) las dos usan el texto que eligió el dueño, más humano y sin horario: "¡Hola! Qué gusto que nos escriba 😊 Ya le respondo personalmente. Mientras tanto, le dejo los precios: …". La respuesta pública al comentario es "¡Hola! Le acabo de escribir por privado 😊". Además está activa "Preguntas frecuentes" (botones que salen al abrir el chat), en Messenger e Instagram por separado, con 4 preguntas: ¿Cuánto cuesta?, ¿Llegan hasta mi casa?, ¿Cuánto tardan? (2 pulidores, unos 45 min, y el horario) y ¿Cómo agendo? (enlace de reservas). Si cambian precios u horario, también hay que cambiarlas ahí.
- **Perfil de Instagram (7 nov)**, ordenado según un video de ejemplo del dueño (foto con el dibujo del logo, nombre con palabras que se buscan, bio de 3 líneas, enlace, destacadas y cuadrícula pareja):
  - Nombre: "GlassDetailingCR | Focos y parabrisas". Solo se puede cambiar 2 veces cada 14 días.
  - Bio: "💡 Pulido de focos y parabrisas con cerámico Fireball / 🏠 A domicilio gratis en toda la GAM / 🛡️ 1 año de protección · listo en 45 min / 👇 Agende aquí".
  - Enlaces y "Botones de acción" solo se editan desde la app del celular. En Costa Rica el botón "Reservar" solo acepta empresas asociadas, sin enlace propio, así que no se usa.
  - Hashtags: Instagram permite máximo 5 por publicación. Focos: #pulidodefocos #restauraciondefocos #focosamarillos #costarica #glassdetailingcr. Parabrisas: #parabrisas #ceramicoparabrisas #pulidodevidrios #costarica #glassdetailingcr. Además, palabras clave en el texto (ej.: "pulido de focos en San José").
  - Edits no se puede conectar: los reels se suben por Metricool.
- **Reels (7 nov)**: el dueño escogió el **estilo B (limpio)**: subtítulo blanco con borde negro en la parte media-baja (y ≈ 1210 de 1920), logo chico en tarjeta clara arriba a la derecha, sonido original y cierre de 3 s con logo, precio y "Agende en línea · enlace en la bio" en azul marino. Un reel por día a las 6:37 pm, en Instagram y Facebook, por Metricool.
  - Scripts guardados en `redes/scripts/` (copia de trabajo en `/home/claude/reels/`): `kit.py` (herramientas comunes), `semana.py` (reels 1-7), `build-mercedes.py`, `build-sedan.py` y `covers.py` (portadas y destacadas). Usan ffmpeg + PIL y letras Archivo/Manrope en `/tmp/fonts` (se bajan de fontsource si faltan). Las rutas de los videos apuntan a `/mnt/user-data/uploads/`, que se pierde entre sesiones: si hay que rehacer un reel, pedirle al dueño el video otra vez. Los videos terminados van en `redes/2026-11-reels/`.
  - Material del dueño (7 nov): Cybertruck, Peugeot azul (pulido + polímero), prueba de agua, Mazda antes/después, Mercedes clásico (todos los vidrios), SUV negra. La foto de olx.ua (parabrisas con cinta naranja) es de otro negocio: no usarla. Tapar placas de clientes.
  - **7 nov, 4:36 pm: el dueño pidió pausar los reels.** Los 6 que faltaban (Cybertruck, Peugeot, prueba de agua, antes/después focos, pasta de dientes, promo) quedaron como **borrador** en Metricool (`draft: true`), con su video, portada y texto. No salen hasta que el dueño diga; para reactivar, `updateScheduledPost` con `draft: false` y una fecha futura.
  - Plan original, IG + FB a las 6:37 pm, con portada propia: sáb 7 Cybertruck, dom 8 Peugeot, lun 9 prueba de agua, mar 10 antes/después focos, mié 11 pasta de dientes, jue 12 libre (el sedán gris "El agua ya no se pega", reel 8, se publicó el sáb 7 a las 4:30 pm a pedido del dueño, con hashtags para clientes nuevos: #parabrisas #tratamientoceramico #autoscostarica #sanjosecostarica #costarica; transiciones tipo plantilla: entrada desde negro, fundidos a negro y cortes rápidos al ritmo; `redes/2026-11-reels/build-sedan.py`, audio de la plantilla del dueño; lleva la prueba de agua desde adentro del carro en la parte fuerte de la canción). El Mercedes se adelantó y salió el sáb 7 a las 12:28 pm, pedido del dueño, vie 13 promo parabrisas + focos. Del sáb 14 en adelante hacen falta videos nuevos del dueño.
  - Todos los textos llevan el enlace de reservas escrito (en Facebook se puede tocar; en Instagram dice "enlace en la bio").
  - En Metricool, `media` y `videoThumbnailUrl` se pasan con `raw.githubusercontent.com/.../main/...`: con la URL de github.io la portada da "Failed to normalize media".
- **Paleta de redes (7 nov, manda sobre olivo y lima en redes)**: grafito `#111315`, azul marino `#15305e`, azul eléctrico `#3b6fd0`, blanco `#f5f7f2` y gris acero `#8a9099`. Igual que la página de reservas, para que todo se vea de la misma marca.
  - Portadas de reels (`redes/2026-11-portadas/covers.py`, `reel_cover`): foto a pantalla completa, etiqueta azul marino arriba a la izquierda (PARABRISAS / FOCOS / PROMO…), logo en tarjeta clara arriba a la derecha, título de 2 líneas en Archivo (línea 1 blanca, línea 2 azul eléctrico) y todo dentro del recorte 3:4 de la cuadrícula.
  - Destacadas: cuadro azul marino con aro azul eléctrico e ícono blanco (Reservar, Tarifas, Parabrisas, Focos, Clientes). Las pone el dueño desde el celular.
  - Las portadas de reels ya publicados solo se cambian desde la app de Instagram (Editar → Editar portada).
  - Hugging Face quedó conectado (7 nov) para portadas, mejorar fotos y voz en off. Nunca usarlo para inventar un "después".
- **Perfil de Negocio de Google (7 nov)**: creado con jersan06500@gmail.com, "GlassDetailingCR", sin local (solo zona de servicio: provincias de San José, Heredia, Alajuela y Cartago), tel. 7045 8967, chat por WhatsApp (wa.me/50670458967), sitio web = página de reservas, horario L-S 6 am-6 pm y D 8 am-3 pm, descripción de 689 caracteres y 6 servicios con precio.
  - Categoría principal: "Auto glass repair service" (en español sale como servicio de reparación de vidrios de autos). En español no aparece "detallado de autos". "Servicio de reparación de cristales" en español era de pantallas de celular: no usarla. "Tienda de cristales para autos" y "Windshield Repair Service" piden local abierto. Para editar categorías conviene la vista en inglés (`google.com/search?q=mi+negocio&hl=en`).
  - **Falta que el dueño lo verifique** (dirección privada + video). Sin eso no sale en Google, y el botón de reservas de Google también lo pide. Fotos listas en `/home/claude/gbp/` (logo, portada, antes/después): las sube el dueño o Claude cuando esté verificado.
- Opiniones de la página de Facebook apagadas por decisión del dueño. El enlace de reservas está en Información → Enlaces de la página.
- **Anuncios (Meta, cuenta 5156973244430777)**: el 6 nov se prendió "Nueva campaña de Ventas" (la de agosto, video de focos, manda a WhatsApp) a ₡4 200 al día. Segmentación corregida: San José +20 km, Heredia +17 km, Alajuela +20 km, Cartago +17 km, 20 a 65 años, Advantage+ abierto, sin intereses ni exclusiones (se quitaron "trabaja en lavacar/detallado" y la exclusión de San Carlos). Las otras 3 campañas siguen en pausa. El conector Adspirer solo da 15 usos al mes (se reinician el 7 dic); si se acaban, se hace desde el Administrador de anuncios en el navegador.
- **Publicado el 6 nov**: carrusel de precios (5 imágenes, `redes/2026-11-precios/`) en Instagram y Facebook, e historias de Tarifas y Reservar (`redes/2026-11-historias/`).
- **Destacadas de Instagram (7 nov)**: ya existen 4: Reservar, Tarifas, Parabrisas y Focos (falta Clientes, se crea al subir una historia de clientes). Las portadas nuevas con la paleta de redes están en `redes/2026-11-portadas/destacada-*.jpg` y se las mandé al dueño: las pone él desde el celular (en la compu Instagram solo deja escoger la portada entre las historias de la destacada, no subir una imagen; se probó el 7 nov). El estilo viejo (olivo con íconos negros) quedó reemplazado.
- **Forma de trabajar con el contenido (7 nov)**: el dueño delegó el manejo de redes ("usted mismo lo suba y me maneje todo"). Manda videos por la app de Claude; Claude los edita con la paleta de redes, les hace portada, se los muestra y los publica o programa por Metricool. Muchas veces pide publicar enseguida: se hace adelantando la fecha del post a 2-3 min y revisando con `getScheduledPosts` que quede `PUBLISHED`. Le gustan los videos tipo cine (oscuros, cortes al ritmo, sin subtítulos, cierre con logo y precio). Hashtags para atraer clientes nuevos: servicio + Costa Rica/San José (ej. #parabrisas #tratamientoceramico #autoscostarica #sanjosecostarica #costarica), no la marca. El doc "Plan de redes · semana del 9 al 14 de noviembre" (Claude Docs) quedó viejo.
- **Pendiente del dueño en Business Suite**: verificar la cuenta de anuncios (Meta lo pide; si no, pausan los anuncios). Hay 2 borradores "Nuevo anuncio de interacción" sin publicar en el Administrador de anuncios: no publicarlos salvo que el dueño lo pida.
- La bandeja de Business Suite solo muestra la caja para responder si el navegador de Claude está visible y en vista ancha (emular 1280 px).
- **Pendiente del dueño, en el celular**: enlace de reservas en la bio de Instagram (la web no deja editar enlaces), mensaje de bienvenida en WhatsApp Business con el mismo texto de la respuesta automática, y portadas de las destacadas.

## Estado al cerrar el 7 nov, 4:45 pm

- **Publicado hoy en Instagram y Facebook**: reel del Mercedes clásico (12:28 pm, portada "Un clásico que brilla", audio del dueño) y reel del sedán gris "El agua ya no se pega" (4:30 pm, IG `instagram.com/reel/DfdQqkcp-BA`, FB `facebook.com/reel/1445334658660695`). Si Instagram les silencia la música por derechos, el dueño avisa.
- **Pausados (borrador en Metricool)**: Cybertruck, Peugeot, prueba de agua, antes/después focos, pasta de dientes y promo. No hay nada programado.
- Reels viejos (agosto-septiembre, 7) con otro estilo: se le ofreció al dueño sacarlos de la cuadrícula sin borrarlos o hacerles portadas nuevas; no ha respondido.
- **Pendiente del dueño en el celular**: enlace de reservas en la bio de Instagram (Editar perfil → Enlaces; la web lo bloquea), portadas de las 4 destacadas, mensaje de bienvenida de WhatsApp Business.
- Business Suite (7 nov): 21 clientes potenciales nuevos, 2 mensajes y 5 comentarios sin responder. Sigue el aviso de pago pendiente de anuncios.

- **Menú automático de WhatsApp (8 nov, postergado por el dueño)**: vio un anuncio de un menú con botones en WhatsApp y lo quiere a futuro. Se le comparó: (1) gratis con WhatsApp Business (bienvenida con menú numerado + respuestas rápidas); (2) SendPulse, plan gratis con botones reales (10 000 mensajes/mes, 500 contactos; pago desde ~9,60 USD/mes); (3) ManyChat Pro (~15-39 USD/mes). Con API, Meta cobra desde el 1 oct 2026: 1 000 respuestas gratis por número al mes y luego ~0,0113 USD por respuesta (Costa Rica = "Rest of Latin America"). Con "coexistencia" el número sigue en la app del celular. Recomendación: SendPulse gratis (antes verificar que acepte coexistencia). El dueño crea la cuenta y conecta el número; Claude arma el menú con los textos de las respuestas automáticas.

## Para seguir (pendiente al cerrar el 6 nov, 11:45 pm)

- **7 nov, 6:25 am: cuenta de anuncios restringida por un pago que no se procesó.** El anuncio "Nuevo anuncio de Ventas" (id 120250980568080371) está en "Error en el pago" y no sale. Meta no deja editar nada hasta que el dueño pague (botón "Pagar" del aviso rojo; lo hace él). El dueño dijo que paga después.
  - Cuando pague, editar ese anuncio: el mensaje automático de la pregunta "¿Cuánto cuesta el servicio del pulido de focos?" todavía dice "tradicional ₡20 000 / polímero ₡25 000". El anuncio guarda su propia copia de la plantilla, así que cambiar la plantilla no basta.
  - Hay que poner la promo (₡25 000 → ₡20 000 agendando en la página + enlace de reservas), mostrársela al dueño y publicar con su "sí". Revisar que no quede otra respuesta con el pulido tradicional.

- Preguntar si actualiza las respuestas automáticas de Facebook/Instagram con "todos los vidrios" (₡40 000) y "techo panorámico" (+₡20 000).
- Preguntar si la app del equipo también pasa a azul marino sin verde lima (la página de reservas ya está así).
- Rehacer con la paleta nueva lo de redes (carrusel, historias, portadas de destacadas) y `reservar/og.jpg`, si el dueño quiere.
- Si el celular muestra una versión vieja: agregar `?v=<número>` al final del enlace (GitHub Pages guarda ~10 min).

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
