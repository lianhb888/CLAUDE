# Encuesta inicial Equipo HB

Flujo: HTML (Vercel, `encuesta-hb.vercel.app`) -> Apps Script (web app) -> pestaña "Encuesta inicial" del Sheet -> Make (webhook) -> Gmail.
La web `equipohb.com/encuesta-inicial` solo muestra la encuesta en un iframe (`elementor-iframe.html`).

- `src/questions.py`: fuente única de preguntas, orden y pasos. `src/template.html`: HTML/CSS/JS. `src/build.py`: genera `encuesta-inicial.html` y `sheet-encabezados.tsv`.
- `deploy/`: lo que se publica en Vercel (`index.html` = `encuesta-inicial-publicar.html`, con `DEV_NAV = false`). Despliegue: `cd deploy && npx vercel --prod --yes`.
- `apps-script.gs`: copia legible del receptor. El Sheet se mapea por nombre de columna, no por posición.
- Sin credenciales en este repo. El webhook de Make vive en las propiedades del script.
