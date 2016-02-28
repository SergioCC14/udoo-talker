Parte con Arduino
-
Lanzamos con Arduino un código que nos escupe en un log los datos del sensor de proximidad

1. Debemos configurar la parte Arduino de UDOO. Para ello nos conectamos por VNC (https://www.realvnc.com/download/viewer/) y arrancamos en modo desktop.
2. Con el IDE de Arduino lanzamos el siguiente programa:
  int ir_sensor0 = A0;
   
  void setup()
  {
    Serial.begin(9600);
  }
   
  void loop()
  {
    int lectura, cm;
   
    lectura = analogRead(ir_sensor0);
    cm = pow(3027.4 / lectura, 1.2134);
    Serial.print("Sensor 0: ");
    Serial.print(cm);
    delay(1000);

Este programa lanzará el log en un fichero definido por el tipo de placa. En nuestro caso, la configuración es ttyMCC (y la ruta entonces es /dev/ttyMCC).

Si queremos leerlo desde consola buscamos ese fichero y lo leemos con minicon, con un buffer de 96000. (Lanzar con sudo)



Opción 1: Parte con NodeJS (Coming Soon)
--
Lanzamos un programa en NodeJS para leer los datos nativos de UDOO

La localización de los valores del Acelerometro, el Magnometro y el giroscipio son los ficheros:
 '/sys/class/misc/FreescaleAccelerometer/data' 
 '/sys/class/misc/FreescaleMagnetometer/data' 
 '/sys/class/misc/FreescaleGyroscope/data'

La conversión es real y contiene valores no enteros (diferente al caso de las señales digitales)

Utilizamos una libreria que se llama udooneo (https://raw.githubusercontent.com/bouiboui/udooneo/). Que abstrae la lectura de esos ficheros en tiempo real. El código que utilizamos se enecuentra en udoo-talker.js.

Si pudieramos obtener señales analógicas leyendo ficheros lo haríamos, pero la lectura de los valores en "/sys/class/gpio/gpio174" solo da valores 1 o 0 (señales digitales). Por eso utilizamos la parte Arduino.


Opción 2: Parte con Python
--
Lanzamos un programa en Python para leer los datos nativos de UDOO.

En este caso, cada placa tiene un rol definido, en el cual manda únicamente datos de unos sensores determinados
La localización de los valores del Acelerometro, el Magnometro y el giroscipio son los ficheros:
 '/sys/class/misc/FreescaleAccelerometer/data' 
 '/sys/class/misc/FreescaleMagnetometer/data' 
 '/sys/class/misc/FreescaleGyroscope/data'

Además, obtenemos del log de Arduino (explicado antes) la información de las señales analogicas (en este caso el fichero está en /dev/ttyMCC). Lo lee como un buffer a 9600.

Todos estos datos se mandan con una petición PUT con la forma:
    payload_a = {
      'sensor_id': 1,
      'measure': split_data(measure_accelerometter)[0]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/1/data", data=payload_a)
    sleep(0.125)

Para esta parte existe un fichero faker.py, que simula peticiones.

Conexión con la API
--
Cada X tiempo lanzamos una petición a la API con la información obtenida. Node se encarga de juntarlo todo.


Contr: IagoLast, SergioCC14
