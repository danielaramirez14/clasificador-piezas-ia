# adquirir.py - captura ventanas etiquetadas de los tres dominios
#
# sensor.ino manda una linea con cinco valores:
#     rojo,verde,azul,distancia_cm,superficie
#
# Este script sigue el protocolo: rondas alternadas de las
# nueve clases, y guarda cada ventana en el archivo de su dominio:
#     datos/datos_color.csv   -> ventana,t,rojo,verde,azul,etiqueta
#     datos/datos_tamano.csv  -> ventana,t,distancia_cm,etiqueta
#     datos/datos_estado.csv  -> ventana,t,reflectancia,etiqueta
#
# Se corre desde la raiz del repositorio:
#     python codigo/adquirir.py

import serial
import time
import csv
import os
import pandas as pd

PUERTO = 'COM3'          # el tuyo puede ser otro: COM4, COM5...
BAUDIOS = 115200
N_MUESTRAS = 80           # largo de cada ventana (~4 s de recorrido a ~60 ms)

# Para cada dominio: archivo, nombres de columnas, que posiciones de la
# linea del Arduino le tocan, y sus tres etiquetas en el orden del protocolo
DOMINIOS = {
    'color': {
        'archivo': 'datos/datos_color.csv',
        'columnas': ['rojo', 'verde', 'azul'],
        'indices': [0, 1, 2],
        'etiquetas': ['color_rojo', 'color_verde', 'color_azul'],
    },
    'tamano': {
        'archivo': 'datos/datos_tamano.csv',
        'columnas': ['distancia_cm'],
        'indices': [3],
        'etiquetas': ['tamano_chica', 'tamano_mediana', 'tamano_grande'],
    },
    'estado': {
        'archivo': 'datos/datos_estado.csv',
        'columnas': ['reflectancia'],
        'indices': [4],
        'etiquetas': ['estado_lisa', 'estado_marcada', 'estado_rayada'],
    },
}

# Orden de una ronda: rojo, verde, azul, chica, mediana, grande, lisa, marcada, rayada
ORDEN = [(dom, et) for dom in DOMINIOS for et in DOMINIOS[dom]['etiquetas']]


def siguiente_ventana(archivo):
    """Numero de ventana donde te quedaste la vez pasada (0 si no hay datos)."""
    if not os.path.exists(archivo) or os.path.getsize(archivo) == 0:
        return 0
    datos = pd.read_csv(archivo)
    if len(datos) == 0:
        return 0
    return int(datos['ventana'].max()) + 1


def leer_linea(ser):
    """Lee una linea completa del Arduino. Devuelve 5 numeros o None."""
    linea = ser.readline().decode('utf-8', errors='ignore').strip()
    partes = linea.split(',')
    if len(partes) != 5:
        return None                      # linea incompleta o basura
    try:
        return [float(p) for p in partes]
    except ValueError:
        return None


# Preparar un archivo, un escritor y un contador de ventana por dominio
os.makedirs('datos', exist_ok=True)
archivos, escritores, ventanas = {}, {}, {}
for dom, cfg in DOMINIOS.items():
    ventanas[dom] = siguiente_ventana(cfg['archivo'])
    nuevo = not os.path.exists(cfg['archivo']) or os.path.getsize(cfg['archivo']) == 0
    archivos[dom] = open(cfg['archivo'], 'a', newline='')   # 'a' = no borra lo anterior
    escritores[dom] = csv.writer(archivos[dom])
    if nuevo:
        escritores[dom].writerow(['ventana', 't'] + cfg['columnas'] + ['etiqueta'])

n_rondas = int(input("Cuantas rondas vas a capturar (cada ronda = una ventana de las 9 clases): "))

ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)             # el Arduino se reinicia al abrir el puerto

try:
    for ronda in range(n_rondas):
        print(f"\n===== Ronda {ronda + 1} de {n_rondas} =====")
        for dom, etiqueta in ORDEN:
            cfg = DOMINIOS[dom]
            ventana = ventanas[dom]
            input(f"\n[{dom}] ventana {ventana} -> pieza {etiqueta}. Enter y pasa la pieza...")
            ser.reset_input_buffer()     # tira lo que se acumulo mientras esperabas

            t = 0
            while t < N_MUESTRAS:
                valores = leer_linea(ser)
                if valores is None:
                    continue
                fila = [valores[i] for i in cfg['indices']]
                escritores[dom].writerow([ventana, t] + fila + [etiqueta])
                t += 1

            archivos[dom].flush()        # si cortas con Ctrl+C, lo capturado no se pierde
            print(f"  {N_MUESTRAS} muestras guardadas en {cfg['archivo']}")
            ventanas[dom] += 1
except KeyboardInterrupt:
    print("\nCaptura interrumpida. Lo que ya se guardo se queda en los archivos.")
finally:
    for f in archivos.values():
        f.close()
    ser.close()

print("\nListo. Ventanas totales por dominio:")
for dom in DOMINIOS:
    print(f"  {dom}: {ventanas[dom]}")
