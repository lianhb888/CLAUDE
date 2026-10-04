/**
 * Equipo HB - Encuesta inicial: receptor (Google Apps Script, proyecto independiente).
 * Despliegue: Aplicación web, ejecutar como "Yo", acceso "Cualquiera".
 * Propiedad requerida del script: MAKE_WEBHOOK_URL (URL del webhook de Make).
 * Esta es la versión legible de lo desplegado; el código real está en script.google.com.
 */
var ID = '1ejgWhy5XCAyEd-AbtLjrZ0ytYdQZzFJry9E0XR6STLc';
var NAME = 'Encuesta inicial';
var TZ = 'America/Bogota';

// Escribe los encabezados de la pestaña (se ejecuta a mano una vez).
function setup() {
  var s = SpreadsheetApp.openById(ID).getSheetByName(NAME);
  var h = ['Fecha y hora','Nombre completo','Sexo','Instagram','Correo Gmail','WhatsApp','Edad','País y ciudad','Ocupación','Cómo descubriste a Lian','Acciones antes de ingresar','Comentario adicional','Tiempo en decidir','Por qué ingresaste','Contenido que más impactó','Miedos y creencias previas','Metas','Cuerpo deseado','Motivación','Cuerpo actual','Intentos previos','Malos hábitos y autosabotaje','Cómo guiarte','Altura','Peso','Mediciones corporales','Lesiones u hormonales','Alergias e intolerancias','Comidas del día','Comidas que disfrutas','Comidas que desagradan','Dulces y chatarra','Tabaco, alcohol o drogas','Agua al día','Actividad diaria','Antecedentes deportivos','Dónde entrenar','Implementación disponible','Días y horas para entrenar','Nivel de energía','Horas de sueño','Calidad de sueño','Estrés (1-10)'];
  s.getRange(1, 1, 1, h.length).setValues([h]);
  s.setFrozenRows(1);
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(30000);
    var d = JSON.parse(e.postData.contents);
    var s = SpreadsheetApp.openById(ID).getSheetByName(NAME);
    var hs = s.getRange(1, 1, 1, s.getLastColumn()).getValues()[0];
    var w = d.enviadoEn ? new Date(d.enviadoEn) : new Date();
    if (isNaN(w.getTime())) w = new Date();
    var fh = Utilities.formatDate(w, TZ, 'yyyy-MM-dd HH:mm:ss');
    // Mapea por nombre de encabezado, no por posición.
    var row = hs.map(function (k) {
      if (k === 'Fecha y hora') return fh;
      var v = d[k];
      return v === undefined || v === null ? '' : san(String(v));
    });
    s.appendRow(row);
    lock.releaseLock();
    notify({ nombre: d['Nombre completo'] || '', fechaHora: fh, telefono: d['WhatsApp'] || '', correo: d['Correo Gmail'] || '' });
    return out({ ok: true });
  } catch (err) {
    try { lock.releaseLock(); } catch (x) {}
    console.error('doPost error: ' + err.message); // sin datos personales
    return out({ ok: false, error: 'error' });
  }
}

// Evita que Sheets interprete texto del usuario como fórmula.
function san(s) { return /^[=+\-@]/.test(s) ? String.fromCharCode(39) + s : s; }

function notify(p) {
  try {
    var u = PropertiesService.getScriptProperties().getProperty('MAKE_WEBHOOK_URL');
    if (!u) { console.error('Falta MAKE_WEBHOOK_URL'); return; }
    UrlFetchApp.fetch(u, { method: 'post', contentType: 'application/json', payload: JSON.stringify(p), muteHttpExceptions: true });
  } catch (err) { console.error('notify error: ' + err.message); }
}

function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
