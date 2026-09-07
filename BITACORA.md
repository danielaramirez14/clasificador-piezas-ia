# Bitácora del proyecto

## Semana 1 - Encuadre y configuración del entorno

### Antes de la clase

#### BLOQUE 1

Creé mi repositorio, agregué la BITACORA.md y el README.md, seguidos de las carpetas "codigo", "datos", y "figuras".

#### BLOQUE 2

1. ¿Cuál es la diferencia entre programar la regla y aprender la regla?

Programar la regla es darle indicaciones a un programa para que tome una decisión. Por ejemplo, establecer los valores para determinar el tamaño de un objeto.
Aprender la regla significa darle muchos datos al programa, por ejemplo mediciones de un objeto, e indicar a qué categoría pertenecen para que después el modelo aprenda por si mismo los patrones para poder identificar la solución sin ayuda del programador.

2. ¿Cuáles son tus dominios y cuáles son tus tres tipos de pieza?

*Dominio 1: Color*

Se utilizará un sensor **TCS3200**.

Los tres tipos de pieza serán:

* Pieza roja
* Pieza verde
* Pieza azul

Las piezas tendrán características similares y la principal diferencia entre ellas será el color.

*Dominio 2: Tamaño*

Se utilizará un sensor **HC-SR04**.

Los tres tipos de pieza serán:

* Pieza pequeña
* Pieza mediana
* Pieza grande

Las piezas tendrán el mismo material y una forma similar, pero tendrán diferentes alturas.

*Dominio 3: Estado de la superficie*

Se utilizará un sensor **TCRT5000**.

Los tres tipos de pieza serán:

* Pieza lisa/normal: superficie limpia y uniforme.
* Pieza marcada: superficie con una marca o franja negra.
* Pieza defectuosa: superficie con varias marcas o rayas.

Las piezas serán del mismo material para que el sistema se enfoque principalmente en identificar el estado de su superficie.

3. Describe el bucle de control de tu sistema

El proyecto utilizará una banda transportadora por la cual pasarán las piezas. Cada dominio contará con un sensor encargado de obtener diferentes características de la pieza.

- Dominio de color

El sensor **TCS3200** mide la intensidad de los componentes de color de la superficie de la pieza. Las mediciones se envían al modelo de aprendizaje automático, que debe decidir si la pieza es roja, verde o azul.

Dependiendo del resultado:

* Si es roja, el actuador la dirige hacia la salida correspondiente a piezas rojas.
* Si es verde, el actuador la dirige hacia la salida de piezas verdes.
* Si es azul, el actuador la dirige hacia la salida de piezas azules.

El flujo sería:

**TCS3200 -> mediciones de color -> modelo de IA -> rojo/verde/azul -> actuador**

- Dominio de tamaño

El sensor **HC-SR04** mide la distancia entre el sensor y la parte superior de la pieza. Como el sensor estará colocado a una altura fija, esta medición permitirá obtener información relacionada con la altura de la pieza. El modelo utilizará estas mediciones para decidir si la pieza es pequeña, mediana o grande.

Dependiendo del resultado:

* Si es pequeña, el actuador la dirige hacia la salida de piezas pequeñas.
* Si es mediana, el actuador la dirige hacia la salida de piezas medianas.
* Si es grande, el actuador la dirige hacia la salida de piezas grandes.

El flujo sería:

**HC-SR04 -> medición de distancia -> modelo de IA -> pequeña/mediana/grande -> actuador**

- Dominio de estado

El sensor **TCRT5000** emite luz infrarroja hacia la superficie y mide la cantidad de luz reflejada. Mientras la pieza se desplaza sobre la banda transportadora, se tomarán varias mediciones. Una pieza lisa debería generar una señal relativamente uniforme, una pieza marcada presentará un cambio importante cuando la marca pase frente al sensor y una pieza defectuosa podrá presentar varias variaciones debido a las diferentes marcas o rayas.

El modelo deberá decidir si la pieza es lisa, marcada o defectuosa.

Dependiendo del resultado:

* Si es lisa, la pieza continúa normalmente por la banda.
* Si está marcada, un actuador puede desviarla hacia una zona de revisión.
* Si está defectuosa, un actuador puede enviarla hacia una zona de rechazo.

El flujo sería:

**TCRT5000 -> mediciones de reflexión -> modelo de IA -> lisa/marcada/defectuosa -> actuador**

*Bucle general del sistema*

En los tres dominios se sigue el mismo principio:

**Sensor -> adquisición de datos -> modelo de aprendizaje automático -> clasificación -> actuador -> separación de la pieza.**

#### BLOQUE EXTRA

##### Sensor de color: TCS3200

| Dato | TCS3200 |
| --- | --- |
| Tipo de salida | Digital por frecuencia |
| Rango de medición | Canales rojo, verde, azul y claro; respuesta espectral aproximada de 300 a 1100 nm |
| Tiempo de respuesta | Un periodo de la nueva frecuencia + 1 µs |
| Voltaje de alimentación | 2.7 a 5.5 V |

##### Sensor de tamaño: HC-SR04

| Dato | HC-SR04 |
| --- | --- |
| Tipo de salida | Digital por pulso |
| Rango de medición | 2 a 400 cm |
| Tiempo de respuesta | Se recomienda un intervalo mayor a 60 ms entre mediciones |
| Voltaje de alimentación | 5 V DC |

##### Sensor de estado: TCRT5000

| Dato | TCRT5000 |
| --- | --- |
| Tipo de salida | Analógica mediante fototransistor; algunos módulos también ofrecen salida digital |
| Rango de medición | 0.2 a 15 mm; distancia óptima aproximada de 2.5 mm |
| Tiempo de respuesta | No especificado en el datasheet oficial; módulos comerciales suelen indicar menos de 1 ms |
| Voltaje de alimentación | El módulo para Arduino normalmente trabaja con 3.3 a 5 V |

## Semana 2 - La primera señal del sensor

### Antes de la clase

#### BLOQUE 1

1. Qué sensor vas a usar y qué tipo de salida tiene.

Debido a que realizaré individualmente los tres dominios del clasificador,
utilizaré tres sensores:
* El TCS3200 para el dominio de color, con las clases roja, verde y azul.
* El HC-SR04 para el dominio de tamaño, con las clases chica, mediana y grande.
* El TCRT5000 para el dominio de estado superficial, con las clases lisa, marcada y rayada.
El TCS3200 tiene una salida en forma de pulsos. Para obtener información del
color se miden por separado los canales rojo, verde y azul mediante la
función "pulseIn()".

El HC-SR04 también funciona mediante pulsos. El Arduino envía un pulso por
el pin TRIG y mide mediante el pin ECHO cuánto tarda el sonido en regresar.
Con esa duración se calcula la distancia en centímetros.

El TCRT5000 se utilizará con salida analógica. Su señal se leerá en el pin
A0 mediante "analogRead()", obteniendo un valor entre 0 y 1023 relacionado
con la cantidad de luz infrarroja reflejada por la superficie.

Como los tres sensores se integrarán en el mismo sistema, cada línea
contendrá cinco valores separados por comas, con el siguiente formato:

rojo,verde,azul,distancia_cm,superficie

2. Tres líneas de ejemplo tal como se van a ver saliendo de tu Arduino, con valores plausibles para tu caso.

24,73,81,8.40,762

58,27,69,12.75,515

70,65,22,18.30,301


3. Por qué el Arduino no puede mandar Serial.println("Leyendo...").
No se deben enviar mensajes como “Leyendo...” porque todo lo que el Arduino escribe en el puerto serial también lo recibe el programa de Python. Como el programa estará preparado para interpretar números de los sensores, recibir una palabra podría provocar un error y detener la lectura de los datos. Por eso, el Arduino solamente enviará los valores obtenidos por los sensores, separados por comas.

#### BLOQUE 2

1. ¿Cuánto tarda tu pieza en cruzar frente al sensor? Es una estimación, mídelo a ojo o con el cronómetro del celular.

Se estimó que cada pieza tardará aproximadamente 1.5 segundos en pasar frente a los sensores.
Para obtener por lo menos 20 muestras durante el evento se realizó el siguiente cálculo:

delay máximo = 1500 ms / 20 muestras = 75 ms

2. Con ese tiempo, ¿qué delay() eliges para tener al menos 20 muestras del evento?

Se eligió un delay de 60 ms debido a que permite obtener más de 20 muestras y respeta aproximadamente el tiempo requerido por el sensor ultrasónico HC-SR04.

3. ¿Cuántas muestras te da eso mientras la pieza pasa?

Aproximadamente 25 muestras.

## Semana 3 - Recolección de datos etiquetados (U2)

### Antes de la clase

#### BLOQUE 1: diseño del dataset etiquetado

1. Las columnas exactas de `datos.csv`, con el nombre de cada una y qué guarda

Como el proyecto trabaja con tres dominios de clasificación y utiliza un sensor diferente para cada uno, se diseñará un archivo de datos para color, otro para tamaño y otro para estado superficial.

Para el dominio de color, el archivo `datos/datos_color.csv` tendrá las siguientes columnas:

* `ventana`: guarda el número que identifica cada pasada completa de una pieza frente al sensor.
* `t`: guarda el número de la muestra dentro de la ventana, comenzando desde cero.
* `rojo`: guarda la lectura obtenida con el filtro rojo del sensor TCS3200.
* `verde`: guarda la lectura obtenida con el filtro verde del sensor TCS3200.
* `azul`: guarda la lectura obtenida con el filtro azul del sensor TCS3200.
* `etiqueta`: guarda el color conocido de la pieza que fue presentada al sensor.

Para el dominio de tamaño, el archivo `datos/datos_tamano.csv` tendrá las siguientes columnas:

* `ventana`: guarda el número que identifica cada pasada completa de una pieza frente al sensor.
* `t`: guarda el número de la muestra dentro de la ventana, comenzando desde cero.
* `distancia_cm`: guarda la distancia en centímetros medida por el sensor ultrasónico HC-SR04.
* `etiqueta`: guarda el tamaño conocido de la pieza que fue presentada al sensor.

Para el dominio de estado superficial, el archivo `datos/datos_estado.csv` tendrá las siguientes columnas:

* `ventana`: guarda el número que identifica cada pasada completa de una pieza frente al sensor.
* `t`: guarda el número de la muestra dentro de la ventana, comenzando desde cero.
* `reflectancia`: guarda la lectura analógica obtenida con el sensor infrarrojo TCRT5000.
* `etiqueta`: guarda el estado conocido de la superficie de la pieza.

2. Las tres etiquetas, escritas tal como aparecerán en el archivo

Para evitar que las etiquetas de los tres módulos se repitan o se confundan, se utilizará un prefijo que permita identificar el dominio al que pertenece cada una.

Las tres etiquetas correspondientes al dominio de color serán:

* `color_rojo`
* `color_verde`
* `color_azul`

Las tres etiquetas correspondientes al dominio de tamaño serán:

* `tamano_chica`
* `tamano_mediana`
* `tamano_grande`

Las tres etiquetas correspondientes al dominio de estado superficial serán:

* `estado_lisa`
* `estado_marcada`
* `estado_rayada`

Todas las etiquetas están escritas en minúsculas, sin espacios y sin acentos.

3. Cinco filas de ejemplo de cada tabla, con valores plausibles para el sensor

Las siguientes son cinco filas de ejemplo para el archivo `datos/datos_color.csv`:

```csv
ventana,t,rojo,verde,azul,etiqueta
0,0,42,118,105,color_rojo
0,1,40,121,108,color_rojo
0,2,43,117,104,color_rojo
0,3,41,119,107,color_rojo
0,4,39,120,106,color_rojo
```

En este ejemplo, todas las filas pertenecen a la ventana número 0 y representan muestras consecutivas de una misma pieza roja. Las columnas `rojo`, `verde` y `azul` contienen las lecturas de los tres filtros del sensor TCS3200.

Las siguientes son cinco filas de ejemplo para el archivo `datos/datos_tamano.csv`:

```csv
ventana,t,distancia_cm,etiqueta
0,0,18.4,tamano_chica
0,1,18.2,tamano_chica
0,2,17.9,tamano_chica
0,3,18.1,tamano_chica
0,4,18.3,tamano_chica
```

En este ejemplo, todas las filas pertenecen a la ventana número 0 y representan muestras consecutivas de una misma pieza chica. La columna `distancia_cm` contiene la distancia medida por el sensor HC-SR04.

Las siguientes son cinco filas de ejemplo para el archivo `datos/datos_estado.csv`:

```csv
ventana,t,reflectancia,etiqueta
0,0,724,estado_lisa
0,1,719,estado_lisa
0,2,727,estado_lisa
0,3,722,estado_lisa
0,4,725,estado_lisa
```

En este ejemplo, todas las filas pertenecen a la ventana número 0 y representan muestras consecutivas de una misma pieza con superficie lisa. La columna `reflectancia` contiene la lectura analógica obtenida con el sensor TCRT5000.

Estos valores se utilizaron únicamente como ejemplos plausibles para diseñar la estructura de los archivos. Durante la recolección se sustituirán por las lecturas obtenidas directamente de cada sensor.


### Avance del proyecto

Preparé mi entorno de Python con las bibliotecas del curso y creé este
repositorio. Elegí clasificar por color, tamaño, y estado, por mi conocimiento previo de estos sensores y variedad de opciones.
Comencé a realizar simulaciones con las lecturas de datos utilizando los sensores para mi pproyecto. Calculé el delay que necesitaré y cuántas muestras me da.



Logré hacer push

Procedimiento para hacer push

- Para hacer un push primero edito mi archivo
- luego hago git add 
- luego git commit
- luego git push
