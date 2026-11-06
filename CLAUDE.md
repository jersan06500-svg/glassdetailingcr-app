# GlassDetailingCR · App del taller

Contexto para seguir trabajando en esta app desde Claude Code. Se armó en una conversación de Claude el 5 de noviembre de 2026.

## Quién la usa

- Taller **GlassDetailingCR** (Costa Rica). Se dedica sobre todo a la restauración de focos y también a parabrisas.
- Dueño: Alejandro. **No es programador**: explicale todo en español sencillo y sin jerga. Él solo aprueba resultados.
- Equipo de 3 personas, cada una con su usuario de Firebase: el dueño y su mamá (iPhone) y un compañero (Android).
- Los correos del equipo **no van en este repositorio** porque es público. Están solo en Firebase Console (Authentication → Usuarios y Firestore → Reglas).
- La usan desde el celular, instalada como app (PWA) con "Agregar a pantalla de inicio".

## Dónde vive

| Qué | Dónde |
| --- | --- |
| App publicada | https://jersan06500-svg.github.io/glassdetailingcr-app/ |
| Repositorio | https://github.com/jersan06500-svg/glassdetailingcr-app (público, rama `main`) |
| Publicación | GitHub Pages, "Deploy from a branch" → `main` / `(root)` |
| Firebase | Proyecto `glassdetailingcr`, plan gratis Spark. Auth con correo y contraseña. Firestore Standard en `nam5`, modo producción |
| Dominios autorizados en Auth | `localhost`, `glassdetailingcr.firebaseapp.com`, `glassdetailingcr.web.app`, `jersan06500-svg.github.io` |

## Archivos

- `index.html`: toda la app (HTML + CSS + JS, sin frameworks ni build). Aquí pasa casi todo.
- `config.js`: `window.FIREBASE_CONFIG` del proyecto `glassdetailingcr`. La apiKey web es pública por diseño; lo que protege los datos son las reglas.
- `firestore.rules`: plantilla de referencia con correos de ejemplo. Solo los 3 correos del equipo leen y escriben (`request.auth.token.email in [...]`). **Las reglas vigentes, con los correos reales, viven en Firebase Console → Firestore → Reglas.** No pongas los correos reales en el repo.
- `sw.js`: service worker. Primero busca en la red y, si no hay, usa el caché. Constante `CACHE` (va en `gdcr-v8` al 5 nov 2026).
- `manifest.json`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`: para instalarla como app. El ícono es la pulidora del logo de la marca.
- `LEEME.md`: explicación corta para el dueño.

## Cómo funciona `index.html`

- **Estado**: `S` guarda una lista por colección. `COLS = clientes, citas, productos, servicios, movimientos, consultas, gastos, config`. `UI` guarda el estado de la pantalla (filtros, textos a medio escribir, periodo de Números…).
- **Datos**: `subscribeAll()` abre un `onSnapshot` por colección y llama a `render()` en cada cambio. Para escribir se usan `addDoc`, `updDoc`, `setDoc` y `delDoc`, que pasan por `window.FB.adapter`.
  - El adaptador está en el `<script type="module">` del final. Carga Firebase JS SDK 10.12.2 desde gstatic, con caché local persistente.
  - Si `config.js` todavía tiene `PEGA_AQUI`, la app entra en modo local (localStorage) y muestra un aviso.
- **Sesión**: `window.onAuth(user)` muestra u oculta `#login`. `AUTHERR` traduce los errores de Firebase Auth al español.
- **Navegación**: por hash (`#inicio`, `#agenda`, `#clientes`, `#redes`, `#productos`, `#numeros`, `#ajustes`). `render()` reconstruye `#main` con `vInicio`, `vAgenda`, `vClientes`, `vRedes`, `vProductos`, `vNumeros` y `vAjustes`.
  - Como `render()` reemplaza todo `#main`, cualquier texto que el usuario esté escribiendo dentro de `#main` tiene que vivir en `UI`. Se hace con el atributo `data-ui="clave"`. Si no, se pierde cuando llega un snapshot.
- **Ventanas emergentes**: `openModal(titulo, html, onSave, botonesExtra)` crea un `<form>` en `#modal-root`. Si `onSave` devuelve `false`, la ventana no se cierra. Están `modalCita`, `modalCompletar` (cobrar y descontar producto), `modalCliente`, `verCliente`, `modalProducto`, `modalMov` (compra o uso), `modalServicio`, `modalConsulta` y `modalConfig` (datos del negocio).
- **Eventos**: un solo listener de `click` en `document` reparte según `data-act`. Los `input` y `change` actualizan `UI` mediante `data-ui`.
- **Utilidades**: `esc`, `money` (₡, es-CR), `fdate`, `ymd`, `parse`, `addDays`, `monday`, `cap`, `num`, `fmtQty`, `byId`, `toast`, `waLink` (agrega 506 si el número tiene 8 dígitos).
- **Redes**: fuera de Claude no hay `sample`, así que `claudeOff` es siempre true. Los botones copian el pedido (`promptReply` / `promptPost`) para pegarlo en la app de Claude. Las plantillas de respuesta rápida salen de `plantillas()`. `espaciosLibres()` calcula los horarios libres según `config/redes` (apertura, cierre, domingo).
- **Mantenimiento**: `paraMantenimiento()` arma la tarjeta "Para mantenimiento" de Hoy, con los clientes que cumplen unos 6 meses desde su restauración de focos y un botón de WhatsApp con el mensaje listo.
- **Gastos y carro eléctrico**: los gastos del negocio usan las categorías de `TIPOS_GASTO`. Números los resta para dar la ganancia real (`gastosCard`).
  - La categoría "Carga del carro" (`CARGA`) calcula kWh, km y costo a partir del % de batería al salir y al llegar. Usa `carro()`: Geely EX5, 18,5 kWh/100 km de consumo real, batería de 60,22 kWh y ₡86 el kWh, editables en Ajustes. Los km del tablero son opcionales.
  - Un gasto se puede ligar a una cita (`citaId`), y `costoViaje(citaId)` lo muestra en el historial del cliente.
- **Ajustes**: datos del carro, logo (se reduce a 256 px y se guarda como data URL en `config/marca`), lista de servicios, copiar respaldo (JSON de `S`), importar respaldo (`importar()` hace `setDoc` por id y no duplica) y cerrar sesión.

## Modelo de datos (Firestore, colecciones en la raíz)

| Colección | Campos |
| --- | --- |
| `clientes` | nombre, telefono, vehiculo, placa, direccion, origen (Instagram/Facebook/WhatsApp/Referido/Google/Pasó por el taller/Otro), notas, creado (ms) |
| `citas` | clienteId, servicioId, servicioNombre, fecha `YYYY-MM-DD`, hora `HH:MM`, precio, estado (pendiente/confirmada/completada/cancelada), metodoPago, costoProductos, notas, creado, completada |
| `productos` | nombre, unidad, stock, minimo, costo (por unidad) |
| `servicios` | nombre, precio, duracion (min) |
| `movimientos` | tipo (compra/uso), productoId, productoNombre, cantidad, costoUnit, total, fecha, citaId?, creado |
| `consultas` | nombre, red (Instagram/Facebook), contacto, interes, estado (nueva/cotizada/agendada/perdida), fecha, notas, creado |
| `config/redes` | instagram, facebook, whatsapp, ubicacion, apertura, cierre, domingo (bool), extra |
| `gastos` | categoria (ver `TIPOS_GASTO`), monto, fecha, metodoPago, notas, citaId?, y para cargas del carro: bateria al salir/llegar, kmCarro?, km, kwh; creado |
| `config/marca` | logo (data URL PNG) |
| `config/carro` | nombre, consumo (kWh/100 km), bateria (kWh), precioKwh (₡) |

Firestore no acepta `undefined`, así que todo campo que se guarde tiene que tener valor.

## Reglas de la casa (vienen de la skill glassdetailingcr-app)

1. **Cambios pequeños y enfocados**: tocar solo lo que se pidió y no reescribir lo que funciona.
2. Un solo `index.html`, sin React, npm ni bundlers.
3. Nombres en español claro, como el resto del código. Funciones cortas.
4. Todo texto que escribe un usuario pasa por `esc()` antes de ir a `innerHTML`.
5. Sin código muerto, sin `console.log` olvidados y sin comentarios obvios.
6. Reutilizar lo que ya existe (helpers, clases `.card`, `.btn`, `.kpi`, `.pill`, `.chip`, `.list`, `.empty`).
7. Fechas y dinero en formato Costa Rica: `es-CR` y colones (₡).
8. **No borrar ni migrar datos de Firestore sin preguntar antes.**
9. Diseño: solo las variables CSS existentes (`--bg`, `--surface`, `--ink`, `--muted`, `--line`, `--accent`, `--cyan`, `--ok`, `--warn`, `--bad`, `--soft`, `--shine`).
   - Tipografías: `--display` (Barlow Condensed) y `--body` (IBM Plex Sans).
   - Paleta sobria grafito, con modo claro y oscuro.
   - Primero celular: botones de 44 px o más, textos cortos en español tico.
   - El título "GlassDetailingCR" lleva un brillo animado (`@keyframes shine`).

## Antes de entregar un cambio

- [ ] Probar en ancho de celular, en modo claro y en modo oscuro. Para probar en local: `python3 -m http.server 8000` y abrir `http://localhost:8000` (localhost ya está autorizado en Firebase Auth).
- [ ] Revisar que la consola no tenga errores.
- [ ] **Subir la versión de `CACHE` en `sw.js`** (gdcr-v1 → gdcr-v2 → …) para que los celulares reciban la versión nueva.
- [ ] Si cambió algo de los datos, revisar `firestore.rules` y recordarle al dueño que las pegue en la consola.
- [ ] Explicarle al dueño en 2 a 4 frases qué cambió y cómo probarlo desde el celular.

## Cómo publicar

Cada push a `main` vuelve a publicar en GitHub Pages en 1 o 2 minutos. Desde Claude Code, en la compu del dueño, se hace con `git commit` y `git push`, que ya funciona. Desde Claude en la web, el dueño sube los archivos a mano (Add file → Upload files → Commit changes). No subas un `config.js` distinto al actual.

## Estado actual (5 nov 2026, noche)

Ya está hecho:

- App publicada y funcionando, con las reglas y los 3 usuarios configurados.
- Desde Claude Code se agregaron: la tarjeta de mantenimiento a 6 meses, el ajuste de diseño para celular (controles de 44 px, sin zoom en iPhone, Clientes en lista), los gastos del negocio con la ganancia real y la carga del carro eléctrico ligada a citas.

Por confirmar con el dueño: si ya importó el respaldo desde la versión anterior (el artefacto de Claude) y si los 3 celulares ya tienen la app instalada.

## Mejoras pendientes

1. **Fotos de antes y después** en cada cita. Firebase Storage pide plan Blaze, así que conviene comprimir y guardar como data URL pequeño, o evaluar con el dueño.
2. **Cotizaciones y recibos** con el logo, para compartir por WhatsApp.

## Cosas a tener en cuenta

- Las escrituras a Firestore sin señal no resuelven hasta reconectar. El botón Guardar queda deshabilitado mientras tanto.
- En iPhone, para instalarla hay que abrirla en Safari, no dentro de WhatsApp.
- La skill `redes-glassdetailingcr` existe para escribir publicaciones y respuestas de redes del taller.
