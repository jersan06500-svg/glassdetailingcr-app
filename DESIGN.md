# GlassDetailingCR — Guía de diseño

Estilo limpio y ordenado: fondo blanco, líneas grises finas y **un solo color fuerte**, el Azul cristal, reservado para lo importante. Debe sentirse profesional, preciso y brillante, como un carro recién pulido.

---

## 1. Principios

1. **Un solo protagonista.** El Azul cristal aparece pocas veces por pantalla: en el bloque principal, el botón para agendar y el paquete destacado. Si todo es azul, nada destaca.
2. **Blanco y aire.** Mucho espacio en blanco. Menos elementos, más grandes y claros.
3. **Bordes, no sombras.** Las tarjetas se separan con líneas finas, sin sombras ni degradados.
4. **Fácil en el celular.** Casi todos los clientes llegan por WhatsApp o Instagram, así que se diseña primero para la pantalla del celular.

---

## 2. Color

| Nombre | Hex | Uso |
|---|---|---|
| Azul cristal | `#0077B6` | Color de marca: bloque principal, botón principal, pestaña activa, paquete destacado |
| Azul profundo | `#03466E` | Texto sobre el tinte azul, hover del botón, títulos de acento |
| Tinte cristal | `#E6F4FB` | Fondos suaves: paquete destacado, avisos, etiquetas |
| Blanco | `#FFFFFF` | Fondo general y tarjetas |
| Gris niebla | `#F5F7F9` | Fondo de secciones alternas |
| Línea | `#E3E6EA` | Bordes de tarjetas, divisores y tablas |
| Gris texto | `#5B6470` | Texto secundario, descripciones y fechas |
| Carbón | `#1F2328` | Texto principal y títulos |

**Estados (solo en la app):**

| Estado | Hex | Fondo suave |
|---|---|---|
| Confirmado / pagado | `#1A7F4B` | `#E7F5EC` |
| Pendiente | `#B26A00` | `#FFF4E0` |
| Cancelado | `#C0352B` | `#FDECEA` |

**Reglas**
- El texto sobre Azul cristal siempre va en blanco.
- El texto sobre el Tinte cristal va en Azul profundo, nunca en negro.
- No se usa el Azul cristal para textos largos; solo para títulos cortos, botones y enlaces.

---

## 3. Tipografía

- **Títulos:** Questrial (nombre, títulos, frase del día). **Texto:** Roboto Slab (todo lo demás). Las dos son gratis en Google Fonts. Elegidas por el dueño el 12 nov 2026 (opción 9 de su imagen de Canva); son las mismas del Kit de Marca de Canva "GlassDetailingCR".
- Las letras de pago de Canva solo se usan dentro de Canva.
- **Pesos:** 400 (normal) y 500 (medio) en el texto. Nada de negritas pesadas.
- **Títulos grandes** con letras un poco más juntas (`letter-spacing: -0.02em`).
- Mayúscula solo al inicio de la frase: "Agendar cita", no "Agendar Cita" ni "AGENDAR CITA".

| Estilo | Tamaño celular | Tamaño compu | Peso |
|---|---|---|---|
| Título principal | 32 px | 48 px | 500 |
| Título de sección | 24 px | 32 px | 500 |
| Subtítulo | 18 px | 20 px | 500 |
| Texto | 16 px | 16 px | 400 |
| Pequeño / etiquetas | 13 px | 13 px | 400 |
| Precio | 20 px | 24 px | 500 |

---

## 4. Espaciado y formas

- **Base de espaciado:** múltiplos de 8 px (8, 16, 24, 32, 48, 64).
- **Ancho máximo del contenido:** 1100 px, centrado.
- **Botones:** forma de píldora (`border-radius: 999px`), alto mínimo de 44 px.
- **Tarjetas:** esquinas de 12 px y borde de 1 px en `#E3E6EA`, sin sombra.
- **Bloque principal (hero):** esquinas de 20 px, fondo Azul cristal.
- **Campos de formulario:** esquinas de 10 px, borde `#E3E6EA`, borde Azul cristal al tocarlos.

---

## 5. Componentes

### Botones
- **Principal:** fondo `#0077B6`, texto blanco y hover `#03466E`. Máximo uno por pantalla (normalmente "Agendar cita").
- **Secundario:** fondo blanco, borde `#E3E6EA` y texto Carbón.
- **Sobre azul:** fondo blanco y texto Azul profundo, para usar dentro del bloque principal.
- **WhatsApp:** botón secundario con el ícono de WhatsApp. No usar el verde de WhatsApp como fondo.

### Barra superior
Fondo blanco, logo a la izquierda, menú corto (Servicios · Precios · Galería · Contacto) y botón principal "Agendar" a la derecha, con línea inferior gris.

### Bloque principal (hero)
Bloque Azul cristal con esquinas redondeadas, título corto en blanco, una línea de descripción en Tinte cristal y botón blanco "Agendar cita". Opcional: foto del carro a la derecha.

### Servicios
Cuadrícula de tarjetas blancas con borde fino, ícono de línea delgada, nombre del servicio, descripción de una línea y "desde ₡___". Se ven en 3 columnas en compu y 1 columna en celular.

### Paquetes y precios
Hasta 4 tarjetas en fila. El paquete recomendado lleva el fondo Tinte cristal, un borde de 2 px Azul cristal y la etiqueta "Más pedido". Cada tarjeta lleva el nombre, el precio, una lista de lo que incluye con ✓ y un botón.

### Antes y después
Pares de fotos lado a lado con la etiqueta "Antes" en gris y "Después" en Azul cristal, con esquinas de 12 px.

### Testimonios
Tarjeta blanca con la frase del cliente, el nombre y el tipo de carro. Solo testimonios reales.

### Franja final
Bloque Azul cristal de ancho completo con "¿Listo para que su carro brille?" y botones "Agendar cita" y "Escribir por WhatsApp".

### Pie de página
Fondo Gris niebla en 4 columnas: Servicios, Zona de cobertura, Horario y Redes.

---

## 6. App (agenda y clientes)

- **Fondo:** Gris niebla. Las tarjetas son blancas con borde fino.
- **Agenda:** cada cita es una fila con hora, cliente, carro, servicio y etiqueta de estado (con los colores de estado de arriba).
- **Pestañas activas y navegación:** el ícono y el texto en Azul cristal y el resto en Gris texto.
- **Números y totales del día:** tarjetas con una etiqueta pequeña gris y la cifra grande en Carbón.
- **Botón flotante "Agendar cita":** el único elemento Azul cristal relleno en pantalla y la única forma de crear citas.
- **Fondo de la app:** una de las 12 fotos de `img/fondos/` con un velo, que cambia con la frase del día.
- **Animaciones:** solo en la app del equipo (botones que se hunden, selección que rebota). En la página de reservas, nada de animaciones.

---

## 7. Redes sociales

- **Formato:** 1080×1080 (post) y 1080×1920 (historia).
- **Fondo:** blanco o foto real del trabajo, nunca fondos de colores saturados.
- **Color:** el Azul cristal solo en el precio, la oferta o una franja inferior con el logo.
- **Texto:** títulos en Questrial y texto en Roboto Slab, máximo 2 líneas grandes y 1 línea pequeña.
- **Reels:** plantilla de Remotion con subtítulos palabra por palabra (la palabra activa en Azul cristal), logo arriba a la derecha y cierre azul con logo, precio y llamado a la acción. Sin voz.
- **Logo:** siempre en la misma esquina: abajo a la derecha en publicaciones, arriba a la derecha en reels.
- **Fotos:** reales, bien iluminadas, mostrando reflejos y acabado. Nada de fotos de banco.

---

## 8. Íconos e imágenes

- Íconos de línea delgada (por ejemplo, Tabler o Lucide), en Carbón o Azul cristal.
- Sin emojis en la web ni en la app. En las publicaciones de redes se permiten con moderación.
- Las fotos llevan esquinas de 12 px y sin filtros exagerados.

---

## 9. Tono de voz

- **Cercano y claro, de usted:** al cliente siempre se le habla de usted ("Su carro", "Agende aquí"), en la web, las reservas, las redes y los mensajes de WhatsApp. La app del equipo, hacia el equipo, va de vos.
- **Frases cortas** que van al grano: "Restauración de focos, ₡20 000 el par. Vamos a domicilio."
- **Garantía:** "5 meses en focos y 3 meses en parabrisas". Ya no se dice "1 año de protección".
- Sin exceso de signos de exclamación ni mayúsculas.
- **Botones** que empiezan con verbo: "Agendar cita", "Ver precios", "Escribir por WhatsApp".

---

## 10. Variables CSS

```css
:root {
  --azul-cristal: #0077B6;
  --azul-profundo: #03466E;
  --tinte-cristal: #E6F4FB;
  --blanco: #FFFFFF;
  --gris-niebla: #F5F7F9;
  --linea: #E3E6EA;
  --gris-texto: #5B6470;
  --carbon: #1F2328;

  --ok: #1A7F4B;       --ok-fondo: #E7F5EC;
  --pendiente: #B26A00; --pendiente-fondo: #FFF4E0;
  --cancelado: #C0352B; --cancelado-fondo: #FDECEA;

  --fuente-titulos: "Questrial", system-ui, sans-serif;
  --fuente: "Roboto Slab", Georgia, serif;
  --radio-tarjeta: 12px;
  --radio-hero: 20px;
  --radio-boton: 999px;
}
```
