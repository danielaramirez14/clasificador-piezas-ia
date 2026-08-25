# Clasificador de piezas - Color, Estado, y Tamaño

Proyecto del curso Inteligencia Artificial.

- Alumno: Daniela Elizabeth Ramírez Alvarado
- Código: 220398884
- Dominios: clasificación por color (rojo, verde, azul), estado (lisa, marcada, rayada), y tamaño (pequeña, mediana, grande).


## Descripción

Sistema de clasificación de piezas mediante una banda transportadora y diferentes sensores. El proyecto utiliza tres dominios de clasificación: color, tamaño y estado superficial de las piezas.

Para cada dominio se utilizará un sensor diferente:
* TCS3200: clasificación por color.
* HC-SR04: clasificación por tamaño.
* TCRT5000: clasificación por estado de la superficie.

Los sensores obtienen mediciones mientras las piezas pasan por la banda transportadora. Estos datos se utilizan como entrada para modelos de aprendizaje de máquina, encargados de identificar a qué clase pertenece cada pieza.

Una vez realizada la clasificación, el sistema podrá accionar actuadores para dirigir las piezas hacia diferentes salidas según el resultado obtenido.

El proyecto se desarrollará progresivamente durante el curso, incorporando adquisición de datos, extracción de características, entrenamiento de modelos de clasificación, detección de anomalías y posteriormente la integración con actuadores y PLC.