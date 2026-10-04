# Equipo HB — Design System

Coaching de composición corporal para profesionales sedentarios (ingenieros, administrativos, ventas). Marca minimalista, firme y selectiva: alto estatus sin lujo ostentoso, no masiva. El estatus se comunica por reducción y disciplina, no por adorno.

**Superficies:** PDFs de entrega, infografías/redes sociales, página web de marketing, app web para clientes.

**Fuentes de este sistema:** brand board adjunto (`uploads/Equipo HB — Brand Board/Brand Board.dc.html`) + logos (`uploads/LOGO-01.png`). No hay codebase ni Figma; el board es la verdad absoluta.

## CONTENT FUNDAMENTALS

- **Idioma:** español. Tuteo directo ("tú"), nunca "usted" ni "vosotros".
- **Tono:** firme, seco, con clase. Frases cortas. Afirmaciones, no promesas infladas. Ej.: "El estándar es alto." · "No es para cualquiera." · "Protocolo antes que motivación." · "Coaching para hombres que trabajan sentados y entrenan en serio. Datos, protocolo y ejecución semanal — sin atajos y sin ruido."
- **Vocabulario:** protocolo, ejecución, datos, método, fase, estándar, disciplina, plazas/cupo limitado. Verbos de acción: Aplicar, Ver método.
- **Casing:** títulos SIEMPRE en MAYÚSCULAS (Archivo 800). Kickers y labels en mayúsculas con tracking amplio. Cuerpo en sentence case.
- **Sin emoji. Nunca.** Sin signos de exclamación salvo excepción muy deliberada.
- **Escasez real:** "12 plazas", "Cupo limitado por trimestre" — selectividad, no urgencia de oferta.
- **Puntos rojos:** un punto final rojo tras un display es un recurso válido ("El estándar es alto<span rojo>.</span>").
- **Números con coma decimal** (92,4 kg · −3,1%) y signo menos real (−, no guion).
- **Evitar:** lenguaje de oferta/promoción, "¡GRATIS!", diminutivos, tono motivacional blando, cualquier cosa que suene masiva o barata.

## VISUAL FOUNDATIONS

- **Colores:** negro base `#080808`, blanco `#ffffff`, gris `#9a9a9a` (tema oscuro, por defecto). Variante clara: papel frío `#F5F5F3`, tinta `#0A0A0A`, gris `#6B6B6B`. Acento rojo `#D62222` (hover `#B81D1D`, activo `#961717`).
- **Regla del 5%:** el rojo ocupa ≤ 5% de la superficie — solo kickers, palabras clave, números y reglas finas. **Nunca como fondo de sección.** Proporción de uso aproximada: 60% negro / 19% papel / 17% grises / 4% rojo.
- **Tipografía:** Archivo 800 para títulos — MAYÚSCULAS, tracking negativo (−0.01 a −0.03em), interlineado ajustado (0.95–1.15). Manrope 400–600 para cuerpo, UI y datos. Escala: Display 76/0.95 · H1 44/1.05 · H2 26/1.15 · H3 21 · Body 16/1.65 · Caption 12 · Kicker 12/+28% · Label 10/+20%.
- **Acentos de sistema:** viñetas de guion rojo (—), nunca puntos ni bullets. Números fantasma gigantes (Archivo 800, ~140px, color #151515 sobre oscuro / #e7e7e4 sobre claro). Kicker de sección: "— Texto" en rojo, Manrope 600 12px, tracking 0.28em, mayúsculas.
- **Layout:** alineación a la izquierda, siempre. Rejilla de 8px, márgenes generosos (88px en piezas grandes). El aire negativo comunica estatus.
- **Bordes y divisores:** hairlines de 1px (`#1e1e1e` oscuro / `#dddedb` claro). Bordes de tarjeta 1px, sin relleno de fondo en oscuro; blanco `#ffffff` con borde en claro.
- **Radios: 0. Sombras: ninguna. Gradientes: ninguno.** Esquinas siempre rectas.
- **Estados:** hover = rojo más oscuro (#B81D1D) o borde que pasa de gris a fg; activo = #961717 o inversión (fondo fg); deshabilitado = grises apagados sin borde de acento.
- **Animación:** mínima o nula. Si existe: fades/opacity cortos y secos (150–200ms, ease-out). Nunca bounces ni springs.
- **Imagen:** alto contraste, desaturada, grano sobrio. Expresión seria, mirada directa, luz dura lateral, fondo neutro oscuro. Nada sonriente ni casual. Sin stock genérico: gimnasio real, oficina real. Filtro de referencia: `grayscale(1) contrast(1.15) brightness(0.92)`.
- **Transparencia/blur:** no se usan. Sobre fotografía, velo oscuro sólido (rgba negro) si hace falta texto encima.
- **Prohibido:** diseños tipo oferta/promo, ilustración cómic, gradientes o sombras cargadas, esquinas redondeadas, emoji, centrado de texto.

## ICONOGRAPHY

- **No hay sistema de iconos.** El board no define iconografía y la marca no la usa: los acentos son tipográficos (guiones rojos —, números fantasma, hairlines, deltas Δ y signos −/+).
- Sin emoji, sin icon fonts. Caracteres unicode permitidos como dato: Δ, −, +, ×.
- **Logos** en `assets/`: `logo-dark.png` (para fondos oscuros: figura roja + texto blanco), `logo-light.png` (para fondos claros: figura roja + texto negro, "HB" rojo), `logo-original.png` (fuente original). Zona de seguridad = altura de la "H". No recolorear, no rotar, no aplicar sobre fondos con ruido sin velo oscuro.
- En tamaños pequeños (nav), el logotipo se compone en texto: `EQUIPO` blanco/negro + `HB` rojo, Archivo 800.

## PLAN BASE — proceso para clientes nuevos

**Disparador:** el usuario pide "quiero un plan para NOMBRE" (o "plan base", "guías para un cliente nuevo"). Sigue siempre este proceso, no lo reinventes por cliente.

**1. Recolectar datos.** Si faltan, pregunta con `ask_user` — no adivines:
- Cliente, entrenador, programa (ej. "Mes 1").
- Rutina de vida: ¿esquema de turnos (ej. 14 días trabajo / 14 descanso) o rutina diaria fija? Si hay turnos: diferencias de alimentación (casino sin pesar vs. comida pesada en casa) y de entrenamiento (gimnasio vs. mancuernas/barra en casa) entre escenarios.
- Alimentación: kcal objetivo y % macros, horarios de las comidas, reglas de hidratación, reglas de casino/contexto de trabajo si aplica, 4 comidas × 2 opciones intercambiables cada una (nombre, ingredientes con cantidades, pasos de preparación), 5 FAQ de nutrición flexible.
- Entrenamiento: división semanal día por día (con columna paralela trabajo/descanso si hay turnos), calentamiento (cardio + movilidad, link de video si existe), ejercicios por bloque con series/reps/descanso/link de video (separados por escenario gym/casa si aplica), reglas de progresión y autorregulación, escala RPE con tramo objetivo, meta de pasos diarios/NEAT (separada por escenario si aplica).

**2. Construir — nunca desde cero.** Copia las plantillas del design system como base:
- `templates/guia-alimentacion/` → `guias-<slug-cliente>/alimentacion/GuiaAlimentacion.dc.html` (+ `ds-base.js`, `image-slot.js`, `support.js`).
- `templates/guia-entrenamiento/` → `guias-<slug-cliente>/entrenamiento/GuiaEntrenamiento.dc.html` (+ mismos soportes).
- Cliente/entrenador/programa como props (`data-props`), nunca hardcodeados en el texto.
- Fotos de comida vía `<image-slot>`; si generas o subes imágenes, comprímelas a JPG ~900px de ancho antes de insertarlas.
- Un único `.dc.html` por guía, estilos inline, sin CSS de clases fuera del bundle del sistema; usa los componentes del bundle (`Kicker`, `DashList`, `GhostNumber`, `DataTable`) en vez de recrearlos a mano.
- Bullets siempre con guion rojo (—), nunca puntos. Kickers "— texto" en rojo, mayúsculas, tracking 0.28em. Español, tuteo, tono seco sin exclamaciones (ver CONTENT FUNDAMENTALS).
- En la lámina de "día de ejemplo" (u otras con varios bloques apilados), distribuye los bloques con `justify-content:space-between` en vez de apilarlos arriba dejando hueco antes del footer.

**3. Cierre.**
- `ready_for_verification` en cada guía.
- Antes de exportar, pregunta: ¿variaciones de contenido? ¿formato final — PNG alta resolución para imprimir/Drive, o HTML autocontenido?
- Si es HTML autocontenido: añade `<template id="__bundler_thumbnail">` y usa `super_inline_html`. Si el bundle supera 30 MiB, comprime las imágenes a JPG calidad ~0.8 antes de re-empaquetar.

## Base de datos de fotos de comidas

`meal-photos.json` (raíz del proyecto) es la base persistente de fotos de comidas, igual en espíritu a `exercise-videos.json` para ejercicios: `[{"name": "Nombre exacto de la comida", "file": "assets/comidas/nombre-archivo.jpg"}]`.

Cuando el usuario suba una foto de una comida:
1. Comprímela/guárdala en `assets/comidas/<slug>.jpg` (JPG, ~900px de ancho).
2. Agrega la entrada `{name, file}` a `meal-photos.json` (nombre igual al que se usará en las guías, case-insensitive al buscar).
3. En las guías (`GuiaAlimentacion.dc.html` de cada cliente), al elegir una comida que ya tiene entrada en `meal-photos.json`, usa esa imagen en el `<image-slot>` en vez de pedir una nueva — mismo patrón que `_ej()` resuelve links de video contra `exercise-videos.json` en la guía de entrenamiento (fetch + Map por nombre normalizado).

Así las fotos se acumulan proyecto a proyecto y los Planes Base futuros las reutilizan automáticamente en vez de generarlas de nuevo.

## INDEX

- `styles.css` → importa `tokens/` (fonts, colors, typography, spacing, base).
- `tokens/` — colores (temas oscuro/claro vía `[data-theme="light"]`), tipografía (clases `.hb-display`…`.hb-label`), espaciado, reset base.
- `assets/` — logos.
- `components/core/` — Nav, Button, SecondaryButton, Input, Card, DataTable, Kicker, GhostNumber, DashList. Todos aceptan los dos temas (heredan tokens del scope `data-theme`).
- `guidelines/` — tarjetas de especímenes (colores, tipo, acentos, logo).
- `ui_kits/web/` — página de marketing (landing).
- `ui_kits/app/` — app web de clientes (panel, protocolo, registro, informe).
- `templates/landing/` — plantilla de landing (Design Component, tema oscuro).
- `templates/informe/` — plantilla de informe de fase / PDF de entrega (variante clara).
- `templates/entrega-plan-base/` — documento de entrega del Plan Base, 16:9, cinco láminas (portada, qué incluye, protocolo semanal, tabla de seguimiento, cierre con CTA a Asesoría / Mentoría 1 a 1).
- `templates/guia-alimentacion/` — guía de alimentación del Plan Base, A4 vertical (1240×1754), siete láminas: portada, dieta personalizada (kcal + macros + distribución), tres comidas con opción alternativa y FAQ de nutrición flexible. Cliente/entrenador/programa como props.
- `templates/guia-entrenamiento/` — guía de entrenamiento del Plan Base, mismo formato A4, seis láminas: portada, rutina semanal, calentamiento, Full Body con escala RPE, NEAT y cierre. Cliente/en. Los nombres de ejercicio se enlazan solo con el nombre — busca el video en `templates/guia-entrenamiento/exercise-videos.json` (copia siempre este archivo junto con el `.dc.html` al duplicar la plantilla); si el ejercicio no está en el JSON, pasa la URL explícita como segundo argumento de `this._ej('Nombre', 'url')`.trenador/programa como props.
- `templates/carrusel-instagram/` — carrusel 1080×1350, tres variantes de slide (portada, dato/tabla, cierre). Huecos `<image-slot>` para foto de marca real.
- `templates/portada-video/` — portada de vídeo 1080×1920, variantes de texto directo y rostro a cámara, más mockup del grid de perfil.
- `SKILL.md` — punto de entrada para agentes.

**Intentional additions:** ninguna — el inventario de componentes es exactamente el del board (nav, botón primario/secundario, campo de formulario, tarjeta, tabla de datos, kicker) más los acentos de sistema del board (GhostNumber, DashList) empaquetados como componentes.

**Nota de fuentes:** Archivo y Manrope se cargan desde Google Fonts (coincidencia exacta, no sustitución). Si prefieres binarios locales, adjúntalos y se convertirán en `@font-face`.
