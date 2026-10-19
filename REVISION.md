# Retroalimentacion

Esto lo llena tu asesor despues de cada revision de avances (semanas 9, 14 y
17). Lo ves haciendo un `git pull` normal de tu repositorio. No lo edites:
crece con una seccion nueva en cada revision, las anteriores no se borran.

Los niveles son los de la rubrica de `evaluacion/individual`: **Excelente**,
**Bueno**, **Suficiente**, **Insuficiente**.

Evidencias, en este curso, es tu codigo en `codigo/`, tus datos en `datos/`,
tus figuras en `figuras/` y la demo del bucle de control.

---

### Nota rápida (2026-09-14)
Elegiste tres dominios (color, tamaño y estado), cada uno con su propio sensor, pero la semana 1 pide un solo dominio individual con tres tipos de pieza: combinar varios dominios es la estructura del proyecto integrador en equipo, no la del proyecto individual. Conviene platicarlo antes de la semana 3 para que no termines triplicando la recolección de datos.

### Nota rápida (2026-09-14) - s03
Tu diseño del bloque 1 y 2 está muy completo, pero cubre tres dominios a la vez (color, tamaño y estado superficial), con nueve etiquetas y 270 ventanas planeadas en total. El proyecto individual es un solo dominio de clasificación con tres clases (como los demás compañeros: madera/metal/plástico, chica/mediana/grande, etc.), no tres dominios en paralelo. Entiendo que es por el interés en varios sensores, pero mantener tres pipelines completos (captura, limpieza, features, modelo) para uno solo ya es bastante trabajo semana a semana; vale la pena platicarlo antes de que el triple esfuerzo te vaya atrasando frente al resto del curso. Si quieres explorar los tres sensores, puede quedar como algo aparte del entregable semanal.

### Nota rápida (2026-09-14) - s04
No veo commits de la semana 04 (`s04 bloque 1`/`s04 bloque 2`). Si tuviste un problema, cuéntamelo para que quede en la bitácora.

### Nota rápida (2026-09-21) - s05
No veo commits de la semana 05 (`s05 bloque 1`/`s05 bloque 2`). Si tuviste un problema, cuéntamelo para que quede en la bitácora.

### Nota rápida (2026-10-19) - s06
Tu bloque 1 quedó a medias: respondiste frecuencia de muestreo y Nyquist, pero los puntos 3 (resolución) y 4 (predicción) están vacíos, y no hay nada del bloque 2 (ni FFT, ni features espectrales, ni `figuras/espectro.png`). Por el texto de "Avance del proyecto" todavía estás en la etapa de captura con tus tres sensores, lo cual tiene sentido dado que vas tripicando ese trabajo (color, tamaño y estado superficial) frente al resto del grupo que lleva un solo sensor. Dicho eso, completar la bitácora no depende de cuántos sensores lleves: termina los puntos 3 y 4 del bloque 1 con lo que ya sabes de tu `sensor.ino`, y en cuanto tengas aunque sea un `datos_limpios.csv` de un dominio, corre el bloque 2 sobre ese para no seguir acumulando semanas pendientes.
