# GlassDetailingCR · App del taller

Contexto para seguir trabajando en esta app desde Claude (web o Claude Code).

## Quién la usa

- Taller **GlassDetailingCR** (Costa Rica). Se dedica a la restauración de focos y parabrisas.
- Dueño: Alejandro. **No es programador**: explicale todo en español sencillo y sin jerga. Él solo aprueba resultados.
- Equipo de 3 personas: el dueño y su mamá (iPhone) y un compañero (Android). Entran con su **cuenta de Google**.
- La usan desde el celular, instalada con "Agregar a pantalla de inicio".
- Dueño: Jersan Alejandro Gutiérrez Ocampo (Alejandro). Hablarle de "tú", en español sencillo. A los clientes, de **usted**. La app hacia el equipo, de **vos**.
- Preferencias del dueño: diseños limpios y minimalistas, sin relleno; nada que se vea genérico "hecho por IA" (usar su marca y fotos reales); proponer mejoras con pros y contras; si falta un acceso o herramienta, pedirlo en vez de buscarle la vuelta.

## Vigente hoy (12 nov 2026, noche) · manda sobre todo lo de abajo

Lo que sigue en este archivo es el historial día por día. Si algo de abajo choca con esta sección, vale esta.

**Servicios, precios y garantías**

| Servicio | Precio | Garantía |
| --- | --- | --- |
| Restauración premium de focos con polímero líquido (lo principal, va primero) | ₡20 000 el par | 5 meses (el polímero dura hasta 18 meses) |
| Promo parabrisas + focos | ₡30 000 | focos 5 meses, parabrisas 3 meses |
| Parabrisas SUV o pick-up + cerámico Fireball | ₡25 000 | 3 meses (el cerámico dura hasta 1 año) |
| Parabrisas sedán + cerámico Fireball | ₡20 000 | 3 meses |
| Todos los vidrios SUV o pick-up | ₡40 000 | 3 meses |
| Todos los vidrios sedán | ₡35 000 | 3 meses |
| Techo panorámico (extra) | +₡20 000 | 3 meses |

- Ya **no** se dice "1 año de protección" ni "₡25 000 → ₡20 000 agendando en línea": el precio de focos es ₡20 000 el par. Ya no se ofrece el pulido tradicional.
- Horario: lunes a domingo, 8 a. m. a 4 p. m. (última cita 2 p. m. en `reservar/`). WhatsApp y SINPE Móvil: **7045-8967**. Pago: SINPE Móvil, transferencia o efectivo (no tarjeta). A domicilio gratis en toda la GAM.

**Marca**

- Color: Azul cristal `#0077B6` (guía en `DESIGN.md`).
- **Letras: Questrial en el nombre, títulos y frase del día; Roboto Slab en el resto**, en la app, `reservar/`, `web/`, redes y el Kit de Marca de Canva. Las letras anteriores (Barlow, IBM Plex, Archivo, Manrope, Inter, Michroma, Shrikhand) ya no van en contenido nuevo.
- Lema: "Claridad que se nota". El logo no ha cambiado (la mascota está en pausa).

**App del equipo, como está hoy**

- Barra de abajo: Hoy, Reservas, Clientes, Números y Más. Se agenda **solo** con el botón flotante "Agendar cita".
- Pantalla de entrada azul con el logo y solo "Entrar con Google".
- Fondo con 12 fotos (`img/fondos/`) que cambian con la frase del día; tocar la frase cambia las dos.
- Hoy con filtros del día, un botón principal por cita (Empecé → Marcar hecha → Ya pagó / Cobrar), duración y avisos en "Pendientes" (incluye "Garantía por vencer": focos a los 4 meses, parabrisas a los 2).
- Números, Notas, Metas e Insumos en botones que se abren y cierran. Forma de pago guardada en cada cita ("Cómo pagaron").
- Personalizar: nombre y color de cada miembro, modo claro u oscuro; solo el dueño: frase, datos de pago y mensajes de WhatsApp.
- Animaciones de botones solo en la app del equipo; en `reservar/` sigue la regla de sin animaciones.

**Redes y Meta**

- Respuesta automática, respuesta a comentarios, preguntas frecuentes (Messenger e Instagram) y bio de Instagram ya tienen los precios, la garantía y el horario de arriba. "Responder a preguntas similares" está apagado.
- Reels: plantilla de Remotion (ver "Reels con Remotion"). Último publicado: Porsche Macan, 12 nov, 6:27 p. m. Sin voz (el dueño no quiere usar la suya; si algún día se quiere voz natural, ElevenLabs con cuenta del dueño).
- Canva Pro en prueba por 1 mes desde el 12 nov: antes de que termine, descargar todo lo que use elementos Pro. Las letras de Canva solo sirven dentro de Canva.
- Tarjeta de garantía de imprenta (9 × 5 cm, cartulina mate) lista en PDF.

**Pendientes**

1. Pagar la cuenta de anuncios de Meta (pago sin procesar desde el 7 nov; lo hace el dueño). Después: montar la campaña con `anuncio-parabrisas-A.mp4` y `-B.mp4` (música de la biblioteca de Meta) y corregir la respuesta del anuncio de focos, que todavía dice "1 año de protección" y "₡25 000 → ₡20 000".
2. Perfil de Google: cambiar horario y descripción (sigue L-S 6-6, D 8-3 y "1 año") y verificarlo.
3. Que la mamá y Esteban pongan su nombre en Personalizar.
4. Elegir mascota (A faro o B pulidora); el lienzo de logos está en pausa.
5. Plantilla "Cliente feliz" con creación masiva de Canva (faltan 4-5 fotos de antes y después de clientes).
6. Carrusel de focos con el efecto de letras, cuando haya una foto adecuada (foco de frente, de cerca, encendido, con fondo liso o desmontado).

**Lo que no funcionó (no repetir)**

- Recortar el foco del Mazda pegado a la carrocería: ni Canva ni las herramientas de Claude lo separan limpio.
- Hugging Face: la creación de imágenes está apagada en la cuenta del dueño.
- Las descargas directas de Canva y Unsplash desde el espacio de Claude están bloqueadas: se bajan con el navegador del dueño a su carpeta de Descargas.
- Video de fondo en la app: el dueño prefirió las fotos.

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
| Página web (portada pública) | `/web/` |
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

- **[Viejo, ver Vigente] Promo de reserva en línea (6 nov, noche, decisión del dueño)**: el pulido de focos con polímero líquido "normalmente" cuesta ₡25 000, pero si el cliente agenda en la página de reservas le queda en ₡20 000 (el precio que ya muestra `reservar/`). El pulido tradicional ya no se ofrece. Así se les dice a los clientes por mensaje y así quedó la respuesta automática del anuncio de focos (plantilla "Iniciar conversaciones 26/06/2026" en el Administrador de anuncios).
- **Servicios** [viejo: desde el 12 nov valen los precios y garantías de Vigente] (todos con 1 año de protección): promo parabrisas + focos con polímero líquido y cerámico Fireball ₡30 000, pulido de focos ₡20 000, parabrisas SUV o pick-up ₡25 000, parabrisas sedán ₡20 000, todos los vidrios ₡40 000 y techo panorámico +₡20 000 (confirmado por el dueño).
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
- **ESTILO CRISTAL (9 nov, manda sobre todo lo de abajo, solo en la app del equipo)**: el dueño aprobó el Azul cristal `#0077B6` y la guía `DESIGN.md` (blanco, líneas finas, botones píldora; la letra hoy es Questrial + Roboto Slab, ver Vigente). Está en el bloque "ESTILO CRISTAL" al final del `<style>` de la intro en `index.html`, que pisa las variables viejas. El mismo 9 nov se aplicó también a `reservar/` (bloque "ESTILO CRISTAL" al final de su `<style>`): portada azul cristal, botón blanco, tarjetas con borde fino y sin sombras. También el 9 nov: íconos de la app (`icon-*.png`, `apple-touch-icon.png`, `logo-icon.png`) = dibujo del logo sobre tarjeta blanca en cuadro azul cristal, y `reservar/og.jpg` azul cristal con el logo en tarjeta blanca (scripts en `/home/claude/tools/`). Desde el mismo 9 nov las redes también van en Azul cristal (ver "Paleta de redes AZUL CRISTAL").
- **[Viejo] PALETA NUEVA (6 nov, noche; reemplazada por el Azul cristal)**: grafito `#111315`, verde lima eléctrico `#b8ff00` (claro `#d4ff66`), blanco `#f5f7f2` y azul marino `#15305e` (el dueño lo pidió en vez del celeste de su referencia, que se parecía a GlassStudio). Fondos oscuros `#0b0d0f` / tarjetas `#181b1f`.
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

## Página web `/web/` (9 nov 2026, noche)

- Portada pública oscura con video de fondo (primer plano de foco y capó), franja "Promo del mes" (parabrisas + focos ₡30 000), sello de garantía (hasta el 12 nov decía "1 año de protección"), tira de fotos que se desliza sola (al tocar una se abre con antes/después), comparadores deslizables de antes y después, servicios con precio, "Señales de que sus focos necesitan un pulido", "Así de fácil" y un cotizador (servicio + vehículo) que arma el mensaje de WhatsApp. Botón flotante de WhatsApp.
- HTML + JS puro en `web/index.html`; fotos, logo blanco y video en `web/img/`. El diseño editable está en Claude (artefacto "GlassDetailingCR — Portada web").
- Textos con **usted**. Todos los botones de agendar van a `../reservar/`.
- **9 nov, noche, confirmado por el dueño**: WhatsApp **7045-8967** (el 7142-1488 que se usó un rato fue un error) y horario **lunes a domingo, 8 a. m. a 4 p. m.** Quedó igual en `web/`, `reservar/` (`HOURS` = 8 a 16 todos los días, última cita 2 pm; JSON-LD) y el texto de la app. Las respuestas automáticas de Facebook/Instagram se cambiaron el 12 nov. **Falta el Perfil de Google** (sigue L-S 6-6 y D 8-3).

## Estado al cerrar el 9 nov, 10 pm

- **Web publicada** en `/web/` (ver sección de arriba). Diseño editable en Claude: artefacto "GlassDetailingCR — Portada web".
- **WhatsApp único: 7045-8967. Horario único: lunes a domingo, 8 am a 4 pm** (última cita 2 pm en `reservar/`). Ya está en `web/`, `reservar/` y la app.
- **Pendiente**: cambiar el horario en el Perfil de Google (las respuestas de Facebook/Instagram ya se cambiaron el 12 nov). Preguntar al dueño si la última cita debe ser a las 2 pm o a las 4 pm.
- **Ideas para la web que quedaron pendientes**: reseñas reales de clientes (capturas con permiso), preguntas frecuentes (duración, qué cubre la garantía, formas de pago) y dominio propio.

## Pendiente de confirmar con el dueño

- El horario (`HOURS`): desde el 9 nov, lunes a domingo de 8 am a 4 pm (antes L-S 6-6 y D 8-3). El dueño dice que el trabajo dura unos 45 min (son 2 pulidores), y `DUR` se queda en 2 horas por carro a propósito, para cubrir las presas entre citas (decisión del dueño).
- Enlace de reseñas de Google (`REVURL`).

## Redes (6 nov 2026)

- Metricool (marca 7932743) tiene conectados Facebook (página 884212044785155) e Instagram @glassdetailingcr. Las imágenes que se programan se suben a `redes/<fecha>-<tema>/` para tener una URL pública; Metricool las copia al programar.
- Facebook e Instagram tienen una respuesta automática (Meta Business Suite → Automatizaciones) con precios, horario y el enlace de reservas. También hay una "Respuesta a comentario" (Precios por comentario): si alguien comenta precio, precios, info, cuanto, cuánto, costo, cotizar o agendar, se le contesta en público y se le manda el mismo mensaje por privado. Si cambian los precios o el horario, hay que cambiar las dos (máx. 500 caracteres en la respuesta automática). Desde el 6 nov (noche) las dos usan el texto que eligió el dueño, más humano y sin horario: "¡Hola! Qué gusto que nos escriba 😊 Ya le respondo personalmente. Mientras tanto, le dejo los precios: …". La respuesta pública al comentario es "¡Hola! Le acabo de escribir por privado 😊". Además está activa "Preguntas frecuentes" (botones que salen al abrir el chat), en Messenger e Instagram por separado, con 4 preguntas: ¿Cuánto cuesta?, ¿Llegan hasta mi casa?, ¿Cuánto tardan? (2 pulidores, unos 45 min, y el horario) y ¿Cómo agendo? (enlace de reservas). Si cambian precios u horario, también hay que cambiarlas ahí.
- **Perfil de Instagram (7 nov)**, ordenado según un video de ejemplo del dueño (foto con el dibujo del logo, nombre con palabras que se buscan, bio de 3 líneas, enlace, destacadas y cuadrícula pareja):
  - Nombre: "GlassDetailingCR | Focos y parabrisas". Solo se puede cambiar 2 veces cada 14 días.
  - Bio [vieja; la vigente es la del 12 nov, más abajo]: "💡 Pulido de focos y parabrisas con cerámico Fireball / 🏠 A domicilio gratis en toda la GAM / 🛡️ 1 año de protección · listo en 45 min / 👇 Agende aquí".
  - Enlaces y "Botones de acción" solo se editan desde la app del celular. En Costa Rica el botón "Reservar" solo acepta empresas asociadas, sin enlace propio, así que no se usa.
  - Hashtags: Instagram permite máximo 5 por publicación. Focos: #pulidodefocos #restauraciondefocos #focosamarillos #costarica #glassdetailingcr. Parabrisas: #parabrisas #ceramicoparabrisas #pulidodevidrios #costarica #glassdetailingcr. Además, palabras clave en el texto (ej.: "pulido de focos en San José").
  - Edits no se puede conectar: los reels se suben por Metricool.
- **Reels (7 nov)** [para reels nuevos se usa la plantilla de Remotion del 12 nov]: el dueño escogió el **estilo B (limpio)**: subtítulo blanco con borde negro en la parte media-baja (y ≈ 1210 de 1920), logo chico en tarjeta clara arriba a la derecha, sonido original y cierre de 3 s con logo, precio y "Agende en línea · enlace en la bio" en azul marino. Un reel por día a las 6:37 pm, en Instagram y Facebook, por Metricool.
  - Scripts guardados en `redes/scripts/` (copia de trabajo en `/home/claude/reels/`): `kit.py` (herramientas comunes), `semana.py` (reels 1-7), `build-mercedes.py`, `build-sedan.py` y `covers.py` (portadas y destacadas). Usan ffmpeg + PIL y letras Archivo/Manrope en `/tmp/fonts` (se bajan de fontsource si faltan). Las rutas de los videos apuntan a `/mnt/user-data/uploads/`, que se pierde entre sesiones: si hay que rehacer un reel, pedirle al dueño el video otra vez. Los videos terminados van en `redes/2026-11-reels/`.
  - Material del dueño (7 nov): Cybertruck, Peugeot azul (pulido + polímero), prueba de agua, Mazda antes/después, Mercedes clásico (todos los vidrios), SUV negra. La foto de olx.ua (parabrisas con cinta naranja) es de otro negocio: no usarla. Tapar placas de clientes.
  - **7 nov, 4:36 pm: el dueño pidió pausar los reels.** Los 6 que faltaban (Cybertruck, Peugeot, prueba de agua, antes/después focos, pasta de dientes, promo) quedaron como **borrador** en Metricool (`draft: true`), con su video, portada y texto. No salen hasta que el dueño diga; para reactivar, `updateScheduledPost` con `draft: false` y una fecha futura.
  - Plan original, IG + FB a las 6:37 pm, con portada propia: sáb 7 Cybertruck, dom 8 Peugeot, lun 9 prueba de agua, mar 10 antes/después focos, mié 11 pasta de dientes, jue 12 libre (el sedán gris "El agua ya no se pega", reel 8, se publicó el sáb 7 a las 4:30 pm a pedido del dueño, con hashtags para clientes nuevos: #parabrisas #tratamientoceramico #autoscostarica #sanjosecostarica #costarica; transiciones tipo plantilla: entrada desde negro, fundidos a negro y cortes rápidos al ritmo; `redes/2026-11-reels/build-sedan.py`, audio de la plantilla del dueño; lleva la prueba de agua desde adentro del carro en la parte fuerte de la canción). El Mercedes se adelantó y salió el sáb 7 a las 12:28 pm, pedido del dueño, vie 13 promo parabrisas + focos. Del sáb 14 en adelante hacen falta videos nuevos del dueño.
  - Todos los textos llevan el enlace de reservas escrito (en Facebook se puede tocar; en Instagram dice "enlace en la bio").
  - En Metricool, `media` y `videoThumbnailUrl` se pasan con `raw.githubusercontent.com/.../main/...`: con la URL de github.io la portada da "Failed to normalize media".
- **Paleta de redes AZUL CRISTAL (9 nov, manda sobre la de abajo)**: el dueño pidió las redes en Azul cristal `#0077B6` como la app y las reservas (DESIGN.md). Etiqueta y línea destacada del título en `#0077B6`, cierre de reels con fondo azul cristal, logo en tarjeta blanca y botón blanco con texto `#03466E`, destacadas azul cristal con aro e íconos blancos. Letra: Questrial + Roboto Slab (antes Inter). Los 6 borradores de Metricool ya tienen video y portada nuevos. Scripts: `redes/scripts/covers_cristal.py` (repinta portadas viejas), `endcards.py` (cambia los últimos 3 s del reel), `destacadas.py`. Lo ya publicado (Mercedes, sedán, carrusel de precios, historias) queda como salió.
- **[Viejo] Paleta de redes (7 nov; reemplazada por el Azul cristal)**: grafito `#111315`, azul marino `#15305e`, azul eléctrico `#3b6fd0`, blanco `#f5f7f2` y gris acero `#8a9099`. Igual que la página de reservas, para que todo se vea de la misma marca.
  - Portadas de reels (`redes/2026-11-portadas/covers.py`, `reel_cover`): foto a pantalla completa, etiqueta azul marino arriba a la izquierda (PARABRISAS / FOCOS / PROMO…), logo en tarjeta clara arriba a la derecha, título de 2 líneas en Archivo (línea 1 blanca, línea 2 azul eléctrico) y todo dentro del recorte 3:4 de la cuadrícula.
  - Destacadas: cuadro azul marino con aro azul eléctrico e ícono blanco (Reservar, Tarifas, Parabrisas, Focos, Clientes). Las pone el dueño desde el celular.
  - Las portadas de reels ya publicados solo se cambian desde la app de Instagram (Editar → Editar portada).
  - Hugging Face quedó conectado (7 nov) para portadas, mejorar fotos y voz en off. Nunca usarlo para inventar un "después".
- **Perfil de Negocio de Google (7 nov)**: creado con jersan06500@gmail.com, "GlassDetailingCR", sin local (solo zona de servicio: provincias de San José, Heredia, Alajuela y Cartago), tel. 7045 8967, chat por WhatsApp (wa.me/50670458967), sitio web = página de reservas, horario L-S 6 am-6 pm y D 8 am-3 pm (**viejo: falta cambiarlo a L-D 8 am-4 pm**), descripción de 689 caracteres y 6 servicios con precio.
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

## Estado al cerrar el 9 nov (resumen del dueño)

- **9 nov, tarde: arreglos en `reservar/`**: toda la página trata al cliente de **usted** (antes mezclaba "vos"; mantener "usted" en todo texto nuevo, igual que en redes). La lista de precios ahora incluye "Todos los vidrios ₡40 000" y "Techo panorámico +₡20 000". El precio de la promo ya no se parte en dos renglones. Botón flotante de WhatsApp (`.wafab`, círculo Azul cristal con logo blanco, abajo a la derecha) solo en la portada; abre WhatsApp con "Tengo una consulta". No sale durante los pasos de agendar.

- **Estilo Azul cristal en todo**: `#0077B6` (oscuro `#03466E`, tinte `#E6F4FB`), letra Questrial + Roboto Slab (antes Inter), fondo blanco, bordes finos, botones redondeados, sin sombras. Guía completa en `DESIGN.md`. Ya está en la app del equipo (claro y oscuro), la página de reservas (portada azul, botón blanco), los íconos de la app (dibujo del logo en tarjeta blanca sobre cuadro azul) y la imagen al compartir el enlace de reservas.
- Para ver el ícono nuevo: borrar la app de la pantalla de inicio y volver a agregarla. Para que WhatsApp muestre la imagen nueva del enlace: mandarlo con `?v=2` (`.../reservar/?v=2`).
- **Redes**: los 6 reels en borrador de Metricool tienen portada y cierre nuevos en Azul cristal. **Siguen pausados.** Cybertruck se movió al sáb 14 y Peugeot al dom 15, ambos a las 6:37 pm (siguen como borrador hasta que el dueño diga).
- **Pendiente del dueño en el celular**: poner las 5 portadas nuevas de destacadas y cambiar las portadas de los reels ya publicados del Mercedes y del sedán.
- Porsche: hecho y publicado el 12 nov (ver "Reels con Remotion").

- **`reservar/` a otro nivel, parte 1 (9 nov, noche, hecho)**: (1) "Próxima hora libre" en la portada arriba del botón (`#nxt`, `landFree()`: lee `slots` con las mismas reglas de `slotsOf` para 1 carro, después de leer `pub/cfg`); (2) sección "Su año de protección" (`.gar`); (3) "Preguntas frecuentes" desplegables (`.faq`, `<details>`); (4) barra fija "Agendar" que aparece cuando el botón de la portada sale de la vista (`#stick`, `body.stk`, IntersectionObserver), con el botón de WhatsApp al lado; (5) datos para Google (JSON-LD `AutoRepair` con zona, horario, precios y redes) + `canonical`; (6) logo de 76 KB → 13 KB (320 px) y `preconnect` a fuentes y Firestore. **Textos de la garantía y algunas respuestas ("lo revisamos con usted", "precio cerrado", "si llueve le escribimos") los redactó Claude: confirmar con el dueño.**
- **Parte 2 (necesita material del dueño)**: 4-6 fotos antes/después (barra deslizable), video corto de 5-10 s, capturas de opiniones de clientes, formas de pago (SINPE, tarjeta, efectivo), foto del equipo trabajando, cantidad aproximada de carros atendidos. Después: dominio propio, recordatorio el día antes, cupón de referidos.

- **Uso de Claude (9 nov, noche)**: el dueño quiere gastar menos. Se le recomendó: un chat nuevo por tema (este archivo guarda todo), Sonnet para tareas del día a día y Opus solo para lo grande, pedir todo junto en un mensaje, mandar videos ya recortados, revisar Configuración → Uso y ponerle tope a los créditos de uso, y bajar de plan si casi no llega al límite (eso lo hace él). Desde aquí abre sesiones nuevas en el mismo lugar con el repositorio `glassdetailingcr-app`. OmniRoute (lo preguntó) no aplica: es un proxy para Claude Code con otros modelos, no oficial; se le desaconsejó.

## Mejoras del 9 nov, 11 pm (aprobadas por el dueño)

- `reservar/`: sección "Antes y después" justo debajo de la portada, con 2 comparadores deslizables (fotos de `../web/img/`, `.comp`). Se quitaron repeticiones: chips solo "Varios carros" y "Agende en 1 minuto", la garantía ya no va en cada precio (la explica "Su garantía"). Botón de WhatsApp a 52 px y espacio al final para que no tape contenido.
- App: el inicio muestra "Recordarle a <cliente> su cita de mañana (faltan N)". Al tocarlo (o "Recordar" en la cita) abre WhatsApp con el recordatorio (incluye toma de 110 V y bajo techo) y marca la cita con `rc:1` ("Recordada ✓"). No cambió `firestore.rules`.
- Formas de pago (dueño, 9 nov): SINPE Móvil al 7045-8967 (mismo número del WhatsApp, a nombre de Jersan Alejandro Gutiérrez Ocampo), transferencia o efectivo (no tarjeta). En la app, `PAGO` se agrega al mensaje de confirmación. Ya están en las preguntas frecuentes y el JSON-LD de `reservar/`.
- Pendiente de preguntar al dueño: unir o separar `web/` y `reservar/`.

## Rediseño de la app del equipo (9-10 nov, noche, aprobado: "la app todavía no se usa, se puede rehacer las veces que haga falta")

Comparado con Jobber, Urable y Housecall Pro (apps de citas para detallado móvil). Misma paleta Azul cristal; bloques "REDISEÑO TABLERO" y siguientes al final del `<style>` de la intro.
- **Encabezado** delgado con `logo-icon.png` + nombre; el logo grande (`.brandc`) quedó oculto.
- **Tablero** (`renderHero`): solo la próxima cita (tiempo grande, cliente, "Voy en camino" en blanco). Si pasó hace más de 1 h: "¿Ya se hizo?" con "Sí, marcar como hecha" (`markDone`) o "Cambiar la hora".
- **Avisos** en `#avisos` debajo del tablero (no dentro): recordatorio de mañana, notas para hoy, cancelaciones, reservas web por confirmar y la ruta del día como `<details>` con "Abrir ruta en Maps". `renderHero` limpia `#avisos` y los envoltorios `_rh`, `_rh2`, `_rh3` agregan ahí.
- **Citas**: línea de tiempo con raya de color por estado (`k-Pendiente` naranja, `k-Hecho` azul, `k-Pagado` verde, `k-Porconfirmar` rojo) y etiqueta `.stp`. Botón del siguiente paso (`nextBtn`): Pendiente de hoy o antes → "Marcar hecha"; Hecho → "Ya pagó" + "Cobrar" (`cobrar`, WhatsApp con total y `PAGO`). "Recordar" solo en citas futuras; "En camino" solo hoy. Estado manual, Editar, Calendario y Borrar en "Más opciones".
- **Barra de abajo** [vieja; hoy: Hoy, Reservas, Clientes, Números y Más]: Hoy, Nueva, Clientes, Números y Más. La hoja `#mass` tiene Enlace de reservas (`t-rv`), Notas (`t-not`) e Insumos (`t-ins`); el aviso rojo de notas sale también en Más.
- **Nueva cita en 3 pasos** (`nGo`, `nOk`): 1 Cliente (nombre, WhatsApp, vehículo, cómo nos conoció), 2 Servicio, 3 Día y lugar. Pie fijo con total, Atrás, Siguiente y Agendar. Los campos e ids son los mismos.
- Clientes y Números: tarjetas con borde, buscador redondo.
- Ideas de las apps grandes que faltan: fotos antes/después por cita (Firebase Storage pide plan de pago; alternativa gratis: guardar el enlace), cobro en el sitio, rutas optimizadas.

## Personalizar y forma de pago (12 nov 2026, aprobado por el dueño)

- **Forma de pago**: "Ya pagó" (o pasar a Pagado en Más opciones) abre la hoja `#pgd` ("¿Cómo pagó?": SINPE Móvil, Transferencia, Efectivo) y guarda `pm` en la cita. Números tiene la tarjeta "Cómo pagaron" (`#pgs`); las pagadas sin `pm` salen como "Sin registrar" y las hechas sin pagar como "Por cobrar".
- **Personalizar** (Más → Personalizar, sección `v-per`), guardado en `settings/perso` (las reglas de `settings` ya lo cubren):
  - Cada miembro: nombre y color (`people[correo] = {n, c}`); `whoN()` usa ese nombre primero. Modo Automático/Claro/Oscuro solo en ese celular (`localStorage gdcr_theme`, aplicado en el `<head>` con `data-theme`).
  - Solo el dueño: frase del inicio (`frase`, vacía = cambia sola), datos de pago (`sinpe`, `titular`, arman `PAGO`) y mensajes de WhatsApp (`msg.conf/rec/cam/cob`, vacío = texto original de `msg0()`). Comodines: {cliente} {fecha} {hora} {vehiculo} {total} {cuando}.
- **Quién atiende**: campo `who` (correo) en cada cita, elegido en el paso 3 de Nueva cita (`#atn`; ojo, `#who` es el encabezado). La cita muestra un punto con el color y el nombre (`whoChip`). Filtro "Todas / Mis citas" arriba de la lista del día (`#mine`, `localStorage gdcr_mine`); "Mis citas" también muestra las que no tienen a nadie (reservas web).
- Al editar una cita ahora se conservan los datos que no están en el formulario (`pm`, `rv`, `ck`, `web`…); `rc` se borra si cambia el día.
- **Todos los mensajes a clientes en "usted"** (confirmación, recordatorio, en camino, cobro, atraso, cancelación, retoque, reseña, pedir ubicación). La app hacia el equipo sigue en "vos".
- Pendiente: que la mamá y Esteban pongan su nombre en Personalizar (si no, la app los llama por el inicio del correo).

## Nueva cita rehecha (12 nov 2026, mediodía, pedido del dueño)

- **Servicios y garantías que dio el dueño (12 nov)**: restauración premium de focos ₡20 000 el par (lo principal, va primero; garantía 5 meses, el polímero dura 18 meses); promo parabrisas + focos ₡30 000; parabrisas SUV ₡25 000, pick-up ₡25 000, sedán ₡20 000; todos los vidrios SUV ₡40 000 y sedán ₡35 000 (todo con cerámico). **Garantía del servicio de parabrisas/vidrios: 3 meses**; el cerámico dura 1 año según la ficha técnica. (`reservar/`, `web/`, la bio de Instagram y las respuestas automáticas se cambiaron el mismo 12 nov; ver más abajo.)
- `SERV` nuevo (app): `focos` ("Restauración premium de focos con polímero líquido"), `combo`, `pu`, `ps`, `all` ("Todos los vidrios SUV o pick-up…" ₡40 000), `alls` (nuevo, "Todos los vidrios sedán…" ₡35 000) y `techo` (extra, ya no excluye a los demás). Cada uno con `sec` (título), `d` (garantía) y `t` (tipo). `salias` pasa los nombres viejos o de la web ("Pulido de focos…", "Todos los vidrios + cerámico…") al servicio nuevo. Los nombres de `LN` en `reservar/` ya no son iguales a `SERV` para focos y vidrios.
- **Paso 1**: Marca (lista), Modelo (lista según marca), Año y Tipo Sedán/SUV/Pick-up. El tipo se marca solo con `vtGuess()` (`PICKRX`, `SUVRX`, `SEDRX`, `MARCAS` copiados de `reservar/`), se puede cambiar a mano. `#veh` quedó oculto y se arma solo (marca + modelo + año). La cita guarda `vt` (`sedan`/`suv`/`pickup`). Con el nombre o el WhatsApp de un cliente que ya vino se llena el resto (`cliFill`, `vehLoad`). "¿Cómo nos conoció?" tiene TikTok.
- **Paso 2**: orden Focos (Principal) → Promo → Parabrisas → Todos los vidrios → Extra. Los del otro tipo se apagan (`svcType`) y lo marcado pasa al par (`PAIR`). Focos + parabrisas se cambia solo a la promo (`svcPick`). Otro servicio y descuento van plegados.
- **Paso 3**: resumen arriba (`#nsum`, `renderSum`) con vehículo, servicios, total y garantía.
- **12 nov, 12:20 pm (sí del dueño)**: `reservar/` y `web/` ya no dicen "1 año de protección": dicen "Garantía de 5 meses en focos y 3 meses en parabrisas" (y que el polímero dura hasta 18 meses y el cerámico hasta 1 año). Sección "Su garantía". Focos va primero en la lista de precios, en las opciones de `reservar/` (`GLASS`) y en el cotizador de `web/`. Todos los vidrios: sedán ₡35 000, SUV o pick-up ₡40 000 (`gp()`, `gln()` en `reservar/`; los nombres de línea ya coinciden con `SERV`). **Falta**: Perfil de Google.
- App: si el modelo se reconoce, los otros tipos quedan bloqueados (`.lock`, `disabled`). Animaciones solo en la app del equipo (bloque "ANIMACIONES DE BOTONES"): botones que se hunden al tocar, selección que rebota, pasos que entran suave, total que salta al cambiar; respetan "reducir movimiento". En `reservar/` sigue la regla de sin animaciones.
- **12 nov, 12:30 pm, hecho por Claude en el navegador (sí del dueño)**: Business Suite → Automatizaciones: "Respuesta automática" y "Respuesta a comentario" (mensaje privado) con "restauración de focos ₡20 000 el par… Garantía de 5 meses en focos y 3 meses en parabrisas. A domicilio gratis en la GAM"; "Preguntas frecuentes" en Messenger **y** en Instagram (son pestañas separadas dentro de la misma automatización): ¿Cuánto cuesta? con todos los vidrios ₡35 000/₡40 000 y la garantía, ¿Cuánto tardan? con el horario lunes a domingo 8 am a 4 pm. Bio de Instagram (se puede editar desde instagram.com/accounts/edit, máx. 150): "💡 Restauración de focos y parabrisas / 🏠 A domicilio gratis en la GAM / 🛡️ Garantía: focos 5 meses · parabrisas 3 meses / 👇 Agende aquí · listo en 45min". **Falta**: Perfil de Google (horario y descripción) y el anuncio con error de pago.
- **12 nov, 12:40 pm**: mensajes repetidos en Meta. Caso visto: Asdrubal (7 nov, anuncio 120250980568080371) recibió dos veces la respuesta del anuncio; Ilse (6 nov, comentario) recibió el mensaje automático y después dos respuestas a mano con los mismos precios. Con el sí del dueño se **apagó "Enviar respuestas a preguntas similares"** en Preguntas frecuentes (Messenger; la pestaña de Instagram no tiene esa opción), así las preguntas frecuentes solo responden cuando el cliente toca el botón. Se dejó una nota en la app para el equipo: no repetir los precios que ya mandó el mensaje automático. Pendiente cuando el dueño pague los anuncios: la respuesta del anuncio (plantilla "Iniciar conversaciones 26/06/2026") todavía dice "1 año de protección" y "₡25 000 → ₡20 000".
- **Números en botones (12 nov, 12:50 pm, aprobado tras probarlo en `/prueba/`, ya borrada)**: cada tarjeta de Números se volvió un botón que se abre (`<details class="acc">`, armado por JS con `NACC`, sin cambiar los ids de adentro). Orden: Cómo pagaron, Resumen, Ingresos y gastos, Meta del mes, Comparado con antes, Gastos y materiales; luego "Ajustes": Precios base, Publicidad en Meta, Ajustes de reservas, Equipo, Avisos al celular, Respaldo. Cada botón muestra su cifra (`accSum`, `#av-*`) y se recuerda cuál quedó abierto (`localStorage gdcr_nopen`). "Reservas en línea" pasó a "Ajustes de reservas" sin el enlace (ya está en Más). Efectos: ícono en cuadrito que rebota al abrir, botón que se hunde al tocar, entrada escalonada, cifra que salta. Para probar cambios grandes: copiar `index.html` a `prueba/index.html` con `<base href="../">`, mostrar y borrar al aprobar.
- **Hoy (12 nov, 1 pm, aprobado y publicado)**: (1) chips del día debajo del título (`#dchips`, `renderChips`, filtro `DF` por estado: Todas, Por confirmar, Pendientes, Hechas, Pagadas; se quita al cambiar de día; solo salen con 2+ citas). (2) un botón principal por cita según el momento (`nextBtn`): hoy sin empezar → "▶ Empecé" (guarda `ini`), empezada → "✓ Marcar hecha · empezó 10:15" (`markDone` guarda `fin`), hecha → "Ya pagó" + "Cobrar". Al lado solo lo útil (`helpBtns`: En camino y Cómo llegar hoy, Recordar en futuras, Pedir reseña en pagadas); Llamar, Waze y reseña de hechas van en "Más opciones" (`moreBtns`). Las hechas con `ini` y `fin` muestran "⏱ Duró N min" (`durTag`). (3) todos los avisos de `#avisos` dentro de un botón "🔔 Pendientes N" (`.avs`, envoltorio `_rh4`, abierto/cerrado en `localStorage gdcr_avopen`).
- **[Viejo] Letra (12 nov, 1:40 pm; reemplazada por "Letra 2")**: primero se probó Michroma en todo, pero al dueño le pareció exagerada. Eligió la opción 3 de su imagen de Canva: **Shrikhand** (gratis en Google Fonts, parecida a "Sergio Trendy" de Canva, que es de pago) **solo en el nombre y los títulos** (`h1`, `h2`, número grande del tablero, botones de Números, Pendientes, títulos de servicios y botón flotante) e **Inter en todo lo demás**. Bloque "LETRA" al final del `<style>` en `index.html`, `reservar/` y `web/` (en esas dos, `h1,h2,h3`). Las letras de Canva no se pueden sacar de Canva: si el dueño quiere una, tiene que comprar la licencia web y pasar el archivo. Contenido nuevo de redes: títulos en Shrikhand.
- **Letra 2 (12 nov, 4:50 pm, manda sobre "Letra")**: el dueño probó 10 combinaciones (de una imagen de "Canva font combinations") y eligió la 9: **Questrial** en el nombre, títulos y frase del día, y **Roboto Slab** en todo lo demás (las dos gratis en Google Fonts; parecida a Kollektif + Roboto Slab de Canva). Bloque "LETRA 2" al final del `<style>` de `index.html`, `reservar/` y `web/`. Shrikhand e Inter ya no se cargan desde el enlace de fuentes del `<head>`.
- **Botón flotante "Agendar cita" (12 nov, 1:30 pm)**: `#fab`, abajo a la derecha sobre la barra, abre Nueva (si había una edición abierta, la limpia). Se esconde en Nueva y Personalizar (`.off`) y en la pantalla de entrada (`body.locked`). Efectos: entra con rebote, el + gira al tocar. Las secciones tienen 72 px extra abajo para que no tape nada. **Desde el mismo día se agenda solo con este botón**: `#t-new` quedó oculto en la barra (CSS), así que abajo quedan Hoy, Reservas, Clientes, Números y Más. **Reservas** (`#t-web`, al lado de Hoy, pedido del dueño 12 nov) abre la hoja del enlace de reservas (`rvOpen`, igual que Más → Enlace de reservas).
- **Logos y mascota (12 nov, en pausa por el dueño)**: lienzo de diseño "GlassDetailingCR — Logos y mascota" (https://claude.ai/artifact/FcyPHNtmnZhHpLwYvUopdj), inspirado en su referencia "Moro Burgers" (isologo, mascota, logotipo). Mascota propia: opción A faro de carro con proyectores como ojos y LED como cejas; opción B pulidora rotativa con cara. Azul cristal + azul oscuro + amarillo luz `#FFC83D`, letra Shrikhand en 3D (si se retoma, pasar a Questrial). La primera versión le pareció muy básica; la segunda quedó para revisar después. No se ha cambiado el logo en la app ni en redes.
- **12 nov, 2 pm (aprobado: "de las 3 a la 5")**: (1) **Entrada con la marca**: fondo azul cristal, logo en tarjeta blanca, nombre en Questrial (antes Shrikhand) y "Claridad que se nota" (`#lkbrand`, solo con `body.locked`); solo se ve "Entrar con Google"; correo y contraseña quedan detrás de "Entrar con correo y contraseña" (`#lmail`, clase `.mail`). (2) **Garantía por vencer**: desde 1 mes antes de que venza (parabrisas/vidrios/techo 3 meses → aviso a los 2; focos 5 → a los 4), en Pendientes sale "Garantía por vencer: escribirle a <cliente>" (`porGarantia`, `garEnd`, `garMsg`). Usa la última cita hecha de cada cliente (por teléfono), deja de salir 15 días después de vencida, abre WhatsApp con oferta de revisión o retoque + enlace de reservas y marca la cita con `mt:1`. (3) **Notas, Metas e Insumos en botones** como Números (`mkAcc`, mismo `gdcr_nopen`; estilos `.acc`/`.accb` ya son generales). "+ Agregar insumo" y Editar abren su botón solos.
- **Fondo con fotos + frase del día (12 nov, 4:40 pm, elegido por el dueño en vez del video)**: `#bgv` es un `div` con una de las 12 fotos de `img/fondos/` (8 de Unsplash, licencia libre; 4 `ia-*` creadas con Canva IA), velo `#bgvv` y efecto de profundidad al deslizar. La foto cambia con la frase (`showMot` → `FOND[(MOTI+dayNum())%FOND.length]`); tocar la frase cambia las dos. `MOT` = 20 frases escritas por Claude y aprobadas. `#mot` va grande en Questrial blanco (antes Shrikhand). `web/img/fondo.mp4` ya no se usa en la app (sí en `web/`).
- Garantía en mensajes: comodín `{garantia}` (`garTxt`: parabrisas +3 meses, focos +5 meses desde el día de la cita); el mensaje de cobro por defecto la incluye.

## Reels con Remotion (12 nov 2026, noche)

- Plantilla de reels hecha con **Remotion** (`npx create-video`, plantilla TikTok) en el espacio de trabajo de Claude: `/home/claude/videos/glassdetailing-reels/` (se pierde entre sesiones: si hace falta, reinstalar con `npx create-video@latest --yes --tiktok glassdetailing-reels` y rehacer `src/GDReel.tsx`). `remotion.config.ts` usa `/usr/bin/google-chrome` (la descarga de Chrome de Remotion está bloqueada). Render con `--concurrency=2`.
- `GDReel`: clips verticales 1080x1920 con subtítulos palabra por palabra (Questrial, palabra activa en caja `#0077B6`), logo en tarjeta blanca arriba a la derecha, acercamiento con rebote a una zona (`zoom: {x, y, at, scale}`), canción opcional (`audio`, apaga el sonido de los clips) y cierre azul oscuro con logo, precio, detalle y botón (`cta`). Cortes acomodados a los golpes de la canción (librosa).
- **Publicado en Instagram el 12 nov, 6:27 pm**: reel del Porsche Macan (parabrisas, videos originales 4K del dueño en OneDrive `Documents/porshe macan`, placa recortada, audio que mandó el dueño): https://www.instagram.com/reel/DfqV6j8AM2K/ . Archivos en `redes/2026-11-reels/porsche-macan*`.
- Versiones para anuncio de Meta en Descargas del dueño (`anuncio-parabrisas-A/B.mp4`): gancho A "¿Su parabrisas se ve así?", B "¿Llueve y no ve nada?", prueba de agua real (sedán), cierre "Escríbanos por WhatsApp", **sin música** (elegir de la biblioteca de Meta). Pendiente: que el dueño pague la cuenta de anuncios.
- Tarjeta de garantía de imprenta (logo del dueño, 9 × 5 cm, PDF, cartulina mate) hecha en HTML; la de Canva salió mal. Frente azul con logo y "Claridad que se nota"; reverso "Certificado de garantía" con líneas para cliente, vehículo, servicio, fecha y "válida hasta", recuadros Focos 5 meses / Parabrisas 3 meses, QR a reservas, Instagram y WhatsApp. Kit de Marca de Canva "GlassDetailingCR" (kAHavc9GxCg): títulos Questrial, texto Roboto Slab. Canva Pro en prueba por 1 mes.

## Estado al cerrar el 7 nov, 4:45 pm

- **Publicado hoy en Instagram y Facebook**: reel del Mercedes clásico (12:28 pm, portada "Un clásico que brilla", audio del dueño) y reel del sedán gris "El agua ya no se pega" (4:30 pm, IG `instagram.com/reel/DfdQqkcp-BA`, FB `facebook.com/reel/1445334658660695`). Si Instagram les silencia la música por derechos, el dueño avisa.
- **Pausados (borrador en Metricool)**: Cybertruck, Peugeot, prueba de agua, antes/después focos, pasta de dientes y promo. No hay nada programado.
- Reels viejos (agosto-septiembre, 7) con otro estilo: se le ofreció al dueño sacarlos de la cuadrícula sin borrarlos o hacerles portadas nuevas; no ha respondido.
- **Pendiente del dueño en el celular**: enlace de reservas en la bio de Instagram (Editar perfil → Enlaces; la web lo bloquea), portadas de las 4 destacadas, mensaje de bienvenida de WhatsApp Business.
- Business Suite (7 nov): 21 clientes potenciales nuevos, 2 mensajes y 5 comentarios sin responder. Sigue el aviso de pago pendiente de anuncios.

- **Menú automático de WhatsApp (8 nov, postergado por el dueño)**: vio un anuncio de un menú con botones en WhatsApp y lo quiere a futuro. Se le comparó: (1) gratis con WhatsApp Business (bienvenida con menú numerado + respuestas rápidas); (2) SendPulse, plan gratis con botones reales (10 000 mensajes/mes, 500 contactos; pago desde ~9,60 USD/mes); (3) ManyChat Pro (~15-39 USD/mes). Con API, Meta cobra desde el 1 oct 2026: 1 000 respuestas gratis por número al mes y luego ~0,0113 USD por respuesta (Costa Rica = "Rest of Latin America"). Con "coexistencia" el número sigue en la app del celular. Recomendación: SendPulse gratis (antes verificar que acepte coexistencia). El dueño crea la cuenta y conecta el número; Claude arma el menú con los textos de las respuestas automáticas.

## Para seguir (pendiente al cerrar el 6 nov, 11:45 pm; la lista al día está en Vigente)

- **7 nov, 6:25 am: cuenta de anuncios restringida por un pago que no se procesó.** El anuncio "Nuevo anuncio de Ventas" (id 120250980568080371) está en "Error en el pago" y no sale. Meta no deja editar nada hasta que el dueño pague (botón "Pagar" del aviso rojo; lo hace él). El dueño dijo que paga después.
  - Cuando pague, editar ese anuncio: el mensaje automático de la pregunta "¿Cuánto cuesta el servicio del pulido de focos?" todavía dice "tradicional ₡20 000 / polímero ₡25 000". El anuncio guarda su propia copia de la plantilla, así que cambiar la plantilla no basta.
  - Hay que poner el precio vigente (focos ₡20 000 el par, garantía 5 meses + enlace de reservas), mostrárselo al dueño y publicar con su "sí". Revisar que no quede otra respuesta con el pulido tradicional.

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
