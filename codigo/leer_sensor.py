# leer_sensor.py
# Lee una ventana de datos enviada por Arduino y crea una gráfica.

import serial
import time
import matplotlib.pyplot as plt
from pathlib import Path

# CONFIGURACIÓN
PUERTO = "COM3"        # Puede cambiar: COM4, COM5, etc.
BAUDIOS = 115200
N_MUESTRAS = 100

# Carpeta donde se guardará la gráfica
CARPETA_FIGURAS = Path(__file__).parent.parent / "figuras"
CARPETA_FIGURAS.mkdir(exist_ok=True)

# Conexión con Arduino
ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)

# Esperar mientras Arduino se reinicia
time.sleep(2)

valores = []

print("Leyendo datos...")
print("Pasa la pieza frente al sensor.")

while len(valores) < N_MUESTRAS:
    linea = ser.readline().decode("utf-8").strip()

    try:
        valor = float(linea)
    except ValueError:
        continue

    valores.append(valor)
    print(valor)

ser.close()

print(f"Se obtuvieron {len(valores)} muestras.")

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(valores, color="blue")

plt.xlabel("Número de muestra")
plt.ylabel("Valor del sensor")
plt.title("Señal durante el paso de la pieza")
plt.grid(True)
plt.tight_layout()

# Guardar la gráfica
ruta_figura = CARPETA_FIGURAS / "senal.png"
plt.savefig(ruta_figura, dpi=300)

print(f"Gráfica guardada en: {ruta_figura}")

plt.show()