# Fuente única: preguntas -> HTML + encabezados del Sheet. (v2 concisa; la v1 de 72 está en questions_v1_72.py)
# t: s=texto corto, l=párrafo, r=opción única, c=casillas, n=escala 1-10, e=email gmail, p=teléfono, a=número, i=solo instrucción
Q = [
 # Sobre ti
 (1,"Nombre completo","s","Nombre completo",""),
 (2,"Sexo","r","Sexo","",["Hombre","Mujer"]),
 (3,"Instagram","s","Instagram","Si no tienes, escribe NO TENGO."),
 (4,"Correo Gmail","e","Correo Gmail",""),
 (5,"WhatsApp","p","WhatsApp","Con código de país."),
 (6,"Edad","a","Edad",""),
 (7,"País y ciudad","s","País y ciudad",""),
 (8,"Ocupación","s","Ocupación","Profesión o emprendimiento."),
 # Cómo nos conociste (datos del lead)
 (101,"Cómo descubriste a Lian","l","Cómo nos conociste","Sé específico: qué viste y qué te llevó a entrar."),
 (102,"Acciones antes de ingresar","c","Acciones previas al ingreso","Marca todas las que apliquen.",["Anuncio publicitario","Perfil de Instagram","Perfil de TikTok","Canal de YouTube","Pocos posts (primeros días)","Varios posts (semanas o meses)","Muchos posts (meses o años)","Testimonios de la web","Recomendación de un conocido"]),
 (107,"Comentario adicional","o","Algo más","Cómo nos conociste y qué nos diferencia para ti. Opcional."),
 (103,"Tiempo en decidir","r","Tiempo de decisión","",["Primer día o primeros días","Semanas","Meses","Años"]),
 (104,"Por qué ingresaste","l","Motivo de ingreso","Qué te convenció y por qué confiaste."),
 (105,"Contenido que más impactó","l","Contenido que te impactó","Videos o posts que influyeron en tu decisión."),
 (106,"Miedos y creencias previas","l","Frenos previos","Miedos y creencias, y qué te hizo superarlos."),
 # Tu objetivo
 (9,"Metas","l","Metas físicas y mentales","Solo metas de tu estado físico y mental, no de tu vida en general. A semanas, a meses y a años."),
 (10,"Cuerpo deseado","l","Cuerpo objetivo","Descríbelo: definido, atlético, tonificado, abdomen marcado."),
 (11,"Motivación","l","Motivación","Salud, autoestima, relaciones, superación u otra. Sé específico."),
 (12,"Cuerpo actual","l","Estado físico actual","Cómo está tu cuerpo y cómo te sientes con él. Sé concreto: «no me queda la ropa», no «me siento mal»."),
 (13,"Intentos previos","l","Intentos previos","Qué funcionó, qué no y por qué."),
 (14,"Malos hábitos y autosabotaje","l","Malos hábitos","Aquello que sabes que debes mejorar."),
 (15,"Cómo guiarte","l","Preferencias de seguimiento","Cómo te exigimos y te apoyamos para que ejecutes."),
 # Tu cuerpo
 (16,"Altura","s","Altura",""),
 (17,"Peso","s","Peso corporal",""),
 (18,"Mediciones corporales","l","Mediciones corporales","Escribe cada número con su medida en centímetros. Si no puedes medirte ahora, escribe NT y envíalas luego por WhatsApp.",{"img":"q71","lista":["1. Pecho: contorno a la altura del pecho.","2. Brazo relajado: contorno en la mitad del brazo.","2*. Brazo contraído: contorno en el punto más alto del bíceps.","3. Cintura: contorno a la altura del ombligo.","4. Cadera: contorno en la parte más ancha.","5. Muslo: contorno en la parte alta del muslo."]}),
 (19,"Lesiones u hormonales","l","Lesiones o problemas hormonales","Cuál y desde cuándo. Si no tienes, escribe NT."),
 (20,"Alergias e intolerancias","s","Alergias o intolerancias","Si no tienes, escribe NT."),
 # Alimentación
 (21,"Comidas del día","l","Comidas diarias","Si tu rutina cambia según días o semanas (por ejemplo, turnos 7x7 en minería), detalla cada esquema por separado en la misma respuesta.\nCantidad, alimentos, porciones y horarios. Si no tienes orden, indica los horarios en que podrías comer.",{"mal":"3 o 4 comidas diarias, comida casera.\nSin horarios, alimentos ni cantidades.","bien":"08:30 desayuno: 3 huevos revueltos, 1 taza de leche con 4 cucharadas de avena.\n11:00 colación: yogur sin azúcar con proteína y 1 fruta.\n13:00 almuerzo: 1 taza de arroz, pollo a la plancha, ensalada surtida.\n16:00: 1 scoop de proteína, creatina y un puñado de almendras.\n20:30 cena: 1 taza de arroz, pollo a la plancha y ensalada.\nSi tu alimentación es desordenada, descríbela tal cual: horarios y alimentos reales."}),
 (22,"Comidas que disfrutas","l","Alimentos que disfrutas",""),
 (23,"Comidas que desagradan","l","Alimentos que rechazas",""),
 (24,"Dulces y chatarra","s","Dulces y chatarra","Cada cuánto los comes y en qué cantidad. Por ejemplo: dos veces por semana, un postre o una porción de pizza."),
 (25,"Tabaco, alcohol o drogas","l","Tabaco, alcohol o drogas","Frecuencia y cantidad. Si no, escribe NO."),
 (26,"Agua al día","s","Agua diaria",""),
 # Entrenamiento
 (27,"Actividad diaria","l","Rutina diaria","Si tu rutina cambia según días o semanas (por ejemplo, turnos 7x7 en minería), detalla cada esquema por separado en la misma respuesta.\nHorarios y actividades. Indica si eres sedentario o activo.",{"mal":"Sedentario.\nTrabajo de escritorio y conducir.","bien":"06:00 me levanto. Voy caminando al trabajo, 15 minutos.\n07:30 a 16:30 trabajo sentado. Al mediodía salgo a caminar 30 minutos.\n16:30 salgo, llego a casa y voy al gimnasio 3 o 4 días por semana.\n19:00 vuelvo a casa y como.\n22:00 o 23:00 me duermo."}),
 (28,"Antecedentes deportivos","l","Antecedentes deportivos","Qué entrenas o entrenabas, y cómo."),
 (29,"Dónde entrenar","s","Lugar de entrenamiento","Gimnasio, casa o aire libre."),
 (30,"Implementación disponible","l","Implementación disponible","En casa, en tu gimnasio o en el parque. Luego envía foto o video por WhatsApp."),
 (31,"Días y horas para entrenar","s","Disponibilidad semanal","Días y horas por semana. Sé honesto: no lo que quisieras, sino lo que realmente puedes sostener. Descuenta viajes y semanas cargadas."),
 # Descanso
 (32,"Nivel de energía","r","Nivel de energía","",["Muy baja: quiero estar acostado todo el día y me canso rápido","Baja: cumplo mis actividades, pero me cuesta mucho esfuerzo","Suficiente: rindo bien en todas mis actividades","Muy alta: quiero estar en movimiento todo el día"]),
 (33,"Horas de sueño","r","Horas de sueño","",["Menos de 5 horas","Entre 5 y 6 horas","Entre 7 y 8 horas","Más de 8 horas"]),
 (34,"Calidad de sueño","r","Calidad de sueño","",["Mala: despierto fácil y sin energía","Regular: a veces despierto, no es frecuente","Buena: sueño profundo y descanso completo"]),
 (35,"Estrés (1-10)","n","Nivel de estrés","De 1 a 10.",["Relajado","Estresado, me irrito fácil"]),
 # Último paso
 (36,None,"i","Fotos de tu estado físico","Envíame por WhatsApp 6 fotos en total. Son obligatorias.\n— 3 fotos (frontal, lateral y trasera) en ropa interior o deportiva. Mujer: ropa deportiva o ropa interior. Hombre: short o ropa interior.\n— 3 fotos (frontal, lateral y trasera) con una prenda que te guste pero no te quede como quieres: camisa, vestido, short u otra. También medimos el progreso con la ropa.\nSi no tienes quién te las tome, graba un video girando sobre tu eje y saca capturas de pantalla de cada vista.","q72"),
]
STEPS = [
 ("Sobre ti",[[1,2],[3],[4,5],[6,7],[8]]),
 ("Tu cuerpo",[[16,17],[18]]),
 ("Tu objetivo",[[12],[13],[14],[9],[10],[11],[15]]),
 ("Alimentación",[[21],[22,23],[24,25],[26,20]]),
 ("Entrenamiento",[[27],[28],[29,30],[31]]),
 ("Salud y descanso",[[19],[32],[33,34],[35]]),
 ("Cómo nos conociste",[[101],[102,107],[103],[104],[105],[106]]),
 ("Último paso",[[36]]),
]
# Orden de las preguntas = orden de aparición en los pasos
_by = {q[0]: q for q in Q}
Q = [_by[n] for _, sts in STEPS for st in sts for n in st]
assert len(Q) == len(_by)

# Renumerar secuencialmente según el orden de la lista
_map = {q[0]: i + 1 for i, q in enumerate(Q)}
Q = [(_map[q[0]],) + tuple(q[1:]) for q in Q]
STEPS = [(sec, [[_map[n] for n in st] for st in sts]) for sec, sts in STEPS]
