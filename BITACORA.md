# Bitácora del proyecto

## Semana 1 - Encuadre y configuración del entorno

### Antes de la clase

*BLOQUE 1*

Creé mi repositorio, agregué la BITACORA.md y el README.md, seguidos de las carpetas "codigo", "datos", y "figuras".

*BLOQUE 2*

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



### Avance del proyecto

Proyecto sin definir por el momento.


Logré hacer push

Procedimiento para hacer push

- Para hacer un push primero edito mi archivo
- luego hago git add 
- luego git commit
- luego git push