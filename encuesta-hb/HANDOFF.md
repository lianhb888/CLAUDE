# Handoff: Encuesta inicial Equipo HB (contexto completo)

Pega este archivo como primer mensaje en la sesión local. Responde siempre en **español**. Preferencias de Lian: respuestas concisas, no asumir (preguntar), no contradecir de frente (acotaciones al final).

## Objetivo
Reemplazar el Google Form de Lian (Equipo HB) por un **HTML con su branding** que guarde respuestas en **Google Sheets** y **avise por correo** (vía Make) en cada envío.

## Insumos (Lian los tiene en su equipo; aquí hay copias de apoyo)
- PDF impreso del Form (fuente de verdad): `Copia de ENCUESTA INICIAL EHB - claude - Formularios de Google.pdf` (23 págs). Texto extraído: `ref/pdf-texto.txt` (`pdftotext -layout`).
- Zip de Claude Design `Encuesta inicial Equipo HB.zip` y `Encuesta Inicial - standalone.html` (bundle de 4 MB). Copias útiles en `ref/design/` (fuente `.dc.html`, tokens CSS, readme del design system, logo).
- 4 imágenes de ejemplo extraídas del PDF (740x740, ya en `img/`): `q50-comidas.jpg` (Mal/Buen ejemplo de respuesta), `q58-actividad-diaria.jpg`, `q71-mediciones.jpg`, `q72-fotos-posicion.jpg` (Fotos corporales frontal/lateral/trasera, mujer y hombre).
- Google Sheet destino: https://docs.google.com/spreadsheets/d/1ejgWhy5XCAyEd-AbtLjrZ0ytYdQZzFJry9E0XR6STLc/edit (hay una "Hoja 1" que NO se toca).
- Form original (solo referencia): https://forms.gle/Fm7ePQSJN9JFCsc16

## Hallazgo de la auditoría
El diseño de Claude Design es solo un **prototipo base de 19 campos en 5 pasos** (nombre, WhatsApp, correo, sexo Hombre/Mujer, peso, objetivo...). NO contiene las 72 preguntas del PDF, ni sus textos de portada/cierre, ni las imágenes. Lian confirmó que el diseño es solo la **base visual**: hay que **construir la encuesta de 72 preguntas con ese mismo diseño**.

## Decisiones tomadas con Lian
- **Flujo**: pasos muy cortos, estilo "una pregunta y siguiente" con barra de progreso fluida. **1–2 preguntas por paso**; máximo 3 solo si están estrictamente correlacionadas.
- **Tiempo estimado en portada**: 20–30 minutos (texto del PDF).
- **Cierre**: texto del PDF ("Eso es todo maquina! Gracias por responder y detallar todo. Ahora tomaré 24-48 horas para tener lista la planificación." + recordatorio WhatsApp con 3 viñetas) **y se mantiene el botón "Acceder a App Equipo HB"** (https://app.equipohb.com) como en el diseño. Se quita el texto "Te contactamos por WhatsApp...".
- **Aviso por correo**: datos = nombre completo (P1), teléfono/WhatsApp (P5), correo (P4) + fecha y hora. Destinatario: **lian.hbgang@gmail.com**. Conexión de correo en Make: **Gmail**.
- **Publicación**: Lian pega el HTML en una página de **equipohb.com** (el HTML debe ser autocontenido, pegable; fuentes por Google Fonts OK).
- **Apps Script**: lo hace Claude. En la sesión nube NO se pudo (sin navegador ni conector de Sheets/Script, solo Drive). Por eso Lian pasa a sesión local para que Claude inicie sesión/use navegador.
- Fotos y videos NO se suben en el form: se piden por WhatsApp, igual que el original.

## Pendiente de Lian (pedírselo)
1. **Token de API de Make** (Profile → API → Add token; scopes: scenarios:read/write/run, hooks:read/write, connections:read) + **zona** de la cuenta (eu1/us1/eu2...make.com) + ID de organización/equipo. Revocar el token al final. Nunca ponerlo en el HTML ni en el repo.
2. Que la conexión Gmail exista/autorizada en Make.

## Diseño visual (NO cambiar estilos)
Tokens y componentes en `ref/design/`. Resumen: tema oscuro `--bg #080808`, `--fg #fff`, `--accent #D62222` (hover #B81D1D, activo #961717), texto muted #9a9a9a, faint #6b6b6b, hairline #1e1e1e, border-input #3d3d3d, disabled bg #262626 / fg #5c5c5c. Fuentes Google Fonts: **Archivo 800** (títulos MAYÚSCULAS, tracking negativo) y **Manrope 400–600**. Radios 0, sin sombras ni gradientes. Contenedor max-width 560px, padding 28px 24px 40px. Kicker "— Texto" rojo 12px/600/tracking .28em mayúsculas. Punto final rojo en h1. Botón primario: fondo accent, texto blanco 12px/600/.12em mayúsculas, padding 13px 22px, ancho completo. Botón secundario ("Atrás"): borde 1px #3d3d3d, hover borde fg, padding 12px 21px. Input: label 10px/600/.18em mayúsculas muted; campo borde 1px (error=accent, focus=fg), padding 13px 14px, 14px; error "— mensaje" 12px accent. Opciones tipo botón (sexo/objetivo): seleccionado = fondo y borde accent, texto blanco. Barra de progreso: línea 1px hairline con relleno accent (width = paso/total), cabecera "PASO X DE N" 11px + etiqueta de sección. Animación fade 200ms. Sin emoji (regla de marca; el título de P1 en el PDF lleva 👇: se omite, avisar a Lian). Logo: `ref/design/logo-dark.png` en la pantalla final con "equipohb.com".
La construcción del diseño original usa un framework propio (`<x-dc>`, `support.js`); para publicar, **reimplementar en HTML/CSS/JS vanilla autocontenido** con exactamente los mismos estilos (ya revisados: Button, SecondaryButton, Input).

## Las 72 preguntas (PDF = fuente de verdad)
Texto exacto en `ref/pdf-texto.txt`. Secciones: "Preguntas sobre ti" (1–34), "Por qué ingresaste a el Equipo HB" (35–47), "Para la planificación" (48–72). **Todas obligatorias excepto la 72** (es solo instrucción + imagen, sin campo).
Tipos no texto libre:
- P2 opción única: Hombre / Mujer / **Otros:** (con campo de texto).
- P27 opción única (4): "Muy poca energía, quiero quedarme acostado/a todo el día y me canso muy rápido" / "Poca energía, hago todas mis actividades pero me toma mucho esfuerzo" / "Suficiente energía como para rendir bien en todas mis actividades" / "Muchísima energía, quiero estar todo el día en movimiento".
- P36 **casillas múltiples** ("Selecciona todas las opciones que correspondan."), 9 opciones: Vi un anuncio de Lian y el Equipo HB / Vi el perfil de instagram de Lian y el Equipo HB / Vi un par de videos o posts de Lian y el Equipo HB / Vi bastantes de videos o posts de Lian y el Equipo HB / Entré a su página web y vi su propuesta / Vi su masterclass gratuita / Conversé directamente con el por Instagram o Whatsapp / Me lo recomendó un conocido / Revisé los testimonios de los demás miembros.
- P39 opción única (5): El mismo día que lo conocí / Dentro de los primeros días que lo conocí / En un par de semanas luego de haberlo conocido / Meses después de haberlo conocido / Años desde que lo conocí.
- P63 escala 1–10 (productividad). P68 escala 1–10 con extremos "Muy relajado" (1) y "Muy estresado, me irrito fácil" (10).
- P66 opción única (4): Menos de 5 horas al día / Entre 5 - 6 horas al día / Entre 7 - 8 horas al día / Más de 8 horas por día.
- P67 opción única (3): Duermo muy mal, despierto fácil y no me siento con energía / Duermo relativamente bien, a veces despierto pero no es seguido / Duermo muy bien, descanso buenas horas con un sueño profundo.
- P4: validar formato y que sea Gmail ("Debe ser correo de google Gmail"). P5: tipo tel.
- P60 en el PDF es texto libre (no opciones).
Imágenes: P50 (`q50-comidas`), P58 (`q58-actividad-diaria`), P71 (`q71-mediciones`), P72 (`q72-fotos-posicion`, dentro de la pantalla de la 72).
Texto largo vs corto: el PDF impreso no distingue; propuesta: corto en P1,3,4,5,6,7,15,48,49,57,65; el resto párrafo (confirmar con Lian si lo desea).
Portada (texto exacto PDF): "Maquinaria te haré unas preguntas para saber de ti, de tu situación, de tus objetivos y de todo lo que haga falta para hacer la planificación que te llevará a tu estado físico ideal." / "Sé sincero, no voy a juzgar tus respuestas. Ten en cuenta que entre más sincero y detallado seas en cada pregunta, más personalizado será todo y por consecuencia más resultados tendrás." / "Reserva unos 20-30 minutos para responder la encuesta con calma y concentración."
Nota: una extracción automática previa mezcló preguntas consecutivas (5, 12, 16, 20, 24, 28, 32, 35, 38, 42, 46, 50, 51, 55, 58, 59, 63, 67, 71, 72); **re-extraer o copiar a mano desde `ref/pdf-texto.txt`**, no confiar en un parseo automático sin revisar las 72.

### Agrupación en pasos propuesta (≤2 por paso)
Sobre ti: 1,2 | 3 | 4,5 | 6,7 | 8 | 9 | 10,11 | 12 | 13 | 14,15 | 16 | 17 | 18 | 19,20 | 21 | 22,23 | 24 | 25,26 | 27 | 28 | 29 | 30 | 31 | 32,33 | 34
Por qué ingresaste: 35 | 36 | 37 | 38,39 | 40 | 41 | 42 | 43 | 44 | 45,46 | 47
Planificación: 48,49 | 50 | 51,52 | 53 | 54 | 55,56 | 57 | 58 | 59 | 60,61 | 62 | 63,64 | 65 | 66,67 | 68,69 | 70 | 71 | 72 (final, botón Enviar).
Mostrar la pregunta como texto Manrope ~20px/600 (no h2 en mayúsculas, por longitud) con ayuda en gris; sección en la cabecera de progreso.

## Tarea 2: envío desde el HTML
- `const ENDPOINT_URL = '';` al inicio del script (Lian la rellena tras desplegar el Apps Script).
- `fetch(ENDPOINT_URL, { method:'POST', mode:'no-cors', headers:{'Content-Type':'text/plain;charset=utf-8'}, body: JSON.stringify(datos) })`.
- Con no-cors no se lee la respuesta: tras enviar → pantalla de confirmación; error de red → mensaje y permitir reintentar.
- Mantener: validación de obligatorios, estado de carga en el botón ("Enviando…"), flujo por pasos + barra de progreso, campo oculto con fecha/hora ISO del envío (`enviadoEn`), anti doble envío (deshabilitar tras primer clic; re-habilitar solo si hay error de red).
- Casillas múltiples se envían unidas con ", ". Las claves del JSON = **encabezados exactos de la hoja**.
- Sugerencias a ofrecer (no asumir): guardar borrador en localStorage por si recargan (dato sensible, ojo).

## Tarea 3: pestaña "Encuesta inicial" (no tocar "Hoja 1")
Columna A "Fecha y hora" (zona America/Bogota) y una columna por pregunta (P72 no tiene columna). Encabezados propuestos, en orden P1..P71:
Nombre completo | Sexo | Instagram | Correo Gmail | WhatsApp | Edad | País y ciudad | Profesión o emprendimiento | Situación laboral | Hobbies | Redes sociales | Familia cercana | Estado físico actual | Descripción del cuerpo | Tiempo con el problema | Problemas en el proceso | Qué necesita para resolverlo | Intentos que no funcionaron | Preocupaciones | Miedos físicos y mentales | Enojos | Top 3 frustraciones | Malos hábitos | Autosabotaje | Estado emocional actual | Estado emocional deseado | Nivel de energía | Metas | Mayor motivación | Cuerpo deseado | Intentos que sí funcionaron | Buenos hábitos | Referentes fitness | Cómo coachearte | Cómo descubriste a Lian | Acciones antes de ingresar | Conversación con tu entorno | Otras investigaciones | Tiempo en decidir | Miedos y creencias previas | Creencias sobre perder grasa | Por qué ingresaste | Contenido que más impactó | Por qué confiaste | Qué incluir en el programa | Qué no incluir | Diferencia frente a competidores | Altura | Peso | Comidas del día | Comidas que disfrutas | Comidas que desagradan | Momento de más hambre | Relación con la comida | Frecuencia de dulces y chatarra | Tabaco, alcohol o drogas | Agua al día | Actividad diaria | Antecedentes deportivos | Dónde entrenar | Implementación disponible | Horarios diarios | Productividad (1-10) | Estrategias y apps | Días y horas para entrenar | Horas de sueño | Calidad de sueño | Estrés (1-10) | Manejo del estrés | Lesiones u hormonales | Mediciones corporales
Si no se puede escribir en el Sheet: entregar los encabezados en TSV para pegar. (Conector Google Drive de la sesión nube solo ve archivos; en sesión local intentar navegador/Sheets.)

## Tarea 4: Apps Script (vinculado al Sheet)
- `doPost(e)`: parsear JSON del body (`e.postData.contents`), escribir fila **mapeando por nombre de encabezado** (leer fila 1 de la pestaña "Encuesta inicial"), no por posición; "Fecha y hora" = hora de `enviadoEn` formateada en America/Bogota (fallback: ahora).
- `LockService.getScriptLock()` (waitLock) para evitar filas pisadas.
- Devolver JSON `{ok:true}` o `{ok:false,error}` con `ContentService`.
- Tras guardar la fila: `UrlFetchApp.fetch(webhook, {method:'post', contentType:'application/json', payload: JSON.stringify({nombre, fechaHora, telefono, correo})})` dentro de try/catch; si falla, la fila igual queda guardada y se registra el error (sin datos personales en logs).
- URL del webhook en `PropertiesService.getScriptProperties()` (clave p. ej. `MAKE_WEBHOOK_URL`), nunca en el HTML ni en el código.
- Entregar código completo listo para pegar.

## Tarea 5: Make
Escenario: Webhook personalizado → Gmail "Enviar correo". Para: lian.hbgang@gmail.com. Asunto: `Nueva encuesta inicial: {nombre}`. Cuerpo: nombre, fecha y hora (hora Bogotá), teléfono, correo. Intentar crear por API de Make (con token de Lian); si no se puede, dar pasos manuales y ejecutar lo posible. Entregar la URL del webhook para guardarla en las propiedades del script.

## Tarea 6: publicación y pruebas
Pasos para Lian: Apps Script → Implementar → Nueva implementación → Aplicación web → ejecutar como "Yo" → acceso "Cualquier persona" → autorizar (incluye la advertencia "app no verificada": Configuración avanzada → Ir a... (no seguro) → Permitir). Con la URL, ponerla en `ENDPOINT_URL`. Prueba end-to-end con curl/Node al endpoint (ahí sí se ve la respuesta): fila en la pestaña correcta con columnas bien mapeadas + correo recibido con los 4 datos. **Borrar los datos de prueba del Sheet al terminar.**

## Reglas
- Sin credenciales/tokens en front-end ni en repositorios.
- Sin datos personales en logs.
- Datos sensibles (correo, teléfono, peso, medidas, lesiones): el Sheet NO se hace público.
- Dejar el HTML listo para pegar en equipohb.com.
- Hay un repo `lianhb888/claude` y la rama de trabajo era `claude/ecstatic-brahmagupta-3lnfm9` (en esta rama está esta carpeta `encuesta-hb/`). No crear PR salvo que Lian lo pida.

## Estado al momento del handoff
Hecho: lectura de insumos, auditoría (hallazgo clave), extracción de las 4 imágenes, decisiones con Lian, análisis de estilos de los componentes. **Aún no creado**: el HTML final, el Apps Script, la pestaña del Sheet, el escenario de Make, pruebas.

## Entrega final esperada
HTML actualizado, código del Apps Script, encabezados del Sheet, URL del webhook configurada, resultado de la prueba y pasos manuales restantes. Resumen corto de discrepancias de la auditoría.
