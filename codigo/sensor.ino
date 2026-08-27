// sensor.ino
// Lee los sensores TCS3200, HC-SR04 y TCRT5000.
// Envía únicamente datos numéricos separados por comas.
//
// Formato:
// rojo,verde,azul,distancia_cm,superficie

// =====================================================
// Pines del sensor de color TCS3200
// =====================================================

const int PIN_TCS_S0  = 4;
const int PIN_TCS_S1  = 5;
const int PIN_TCS_S2  = 6;
const int PIN_TCS_S3  = 7;
const int PIN_TCS_OUT = 8;

// =====================================================
// Pines del sensor ultrasónico HC-SR04
// =====================================================

const int PIN_HC_TRIG = 9;
const int PIN_HC_ECHO = 10;

// =====================================================
// Pin del sensor reflectivo TCRT5000
// =====================================================

const int PIN_TCRT = A0;


// =====================================================
// Configuración inicial
// =====================================================

void setup() {
  // Comunicación serial con Python
  Serial.begin(115200);

  // Configuración del TCS3200
  pinMode(PIN_TCS_S0, OUTPUT);
  pinMode(PIN_TCS_S1, OUTPUT);
  pinMode(PIN_TCS_S2, OUTPUT);
  pinMode(PIN_TCS_S3, OUTPUT);
  pinMode(PIN_TCS_OUT, INPUT);

  // Escala de frecuencia del TCS3200 al 20 %
  digitalWrite(PIN_TCS_S0, HIGH);
  digitalWrite(PIN_TCS_S1, LOW);

  // Configuración del HC-SR04
  pinMode(PIN_HC_TRIG, OUTPUT);
  pinMode(PIN_HC_ECHO, INPUT);

  digitalWrite(PIN_HC_TRIG, LOW);
}


// =====================================================
// Función para medir el canal rojo del TCS3200
// =====================================================

unsigned long leerRojo() {
  digitalWrite(PIN_TCS_S2, LOW);
  digitalWrite(PIN_TCS_S3, LOW);

  delayMicroseconds(200);

  return pulseIn(PIN_TCS_OUT, LOW, 30000);
}


// =====================================================
// Función para medir el canal verde del TCS3200
// =====================================================

unsigned long leerVerde() {
  digitalWrite(PIN_TCS_S2, HIGH);
  digitalWrite(PIN_TCS_S3, HIGH);

  delayMicroseconds(200);

  return pulseIn(PIN_TCS_OUT, LOW, 30000);
}


// =====================================================
// Función para medir el canal azul del TCS3200
// =====================================================

unsigned long leerAzul() {
  digitalWrite(PIN_TCS_S2, LOW);
  digitalWrite(PIN_TCS_S3, HIGH);

  delayMicroseconds(200);

  return pulseIn(PIN_TCS_OUT, LOW, 30000);
}


// =====================================================
// Función para medir distancia con el HC-SR04
// =====================================================

float leerDistancia() {
  // Envía un pulso de 10 microsegundos
  digitalWrite(PIN_HC_TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(PIN_HC_TRIG, HIGH);
  delayMicroseconds(10);

  digitalWrite(PIN_HC_TRIG, LOW);

  // Mide cuánto tarda en regresar el sonido
  unsigned long duracion =
      pulseIn(PIN_HC_ECHO, HIGH, 30000);

  // Si no recibió eco, devuelve -1
  if (duracion == 0) {
    return -1.0;
  }

  // Convierte la duración a centímetros
  float distancia = duracion * 0.0343 / 2.0;

  return distancia;
}


// =====================================================
// Ciclo principal
// =====================================================

void loop() {
  // TCS3200: tres canales de color
  unsigned long rojo = leerRojo();
  unsigned long verde = leerVerde();
  unsigned long azul = leerAzul();

  // HC-SR04: distancia en centímetros
  float distancia = leerDistancia();

  // TCRT5000: valor analógico entre 0 y 1023
  int superficie = analogRead(PIN_TCRT);

  // Envía los cinco valores separados por comas
  Serial.print(rojo);
  Serial.print(",");

  Serial.print(verde);
  Serial.print(",");

  Serial.print(azul);
  Serial.print(",");

  Serial.print(distancia, 2);
  Serial.print(",");

  Serial.println(superficie);

  // Valor provisional solicitado en el Bloque 1
  delay(10);
}