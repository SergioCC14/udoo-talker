import requests
import json
from time import sleep

accelerometter_path = '/sys/class/misc/FreescaleAccelerometer/data' 
magnetometer_path   = '/sys/class/misc/FreescaleMagnetometer/data' 
gyroscope_path      = '/sys/class/misc/FreescaleGyroscope/data' 

def read_file(path):
  file = open(path)
  data = file.read()
  file.close()

  return data

def split_data(data):
  dr = data.replace("\n", "").split(',')
  data_formatted = [dr[0], dr[1], dr[2]]
  
  return data_formatted


# main
with serial.Serial('/dev/ttyMCC', 115200, timeout=0) as ser:
  while True:
    payload = {}

    measure_accelerometter = read_file(accelerometter_path)
    measure_magnetometer = read_file(magnetometer_path)
    measure_gyroscope  = read_file(gyroscope_path)
    
    payload_a = {
      'sensor_id': 1,
      'measure': split_data(measure_accelerometter)[0]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/1/data", data=payload_a)
    sleep(0.125)
    print payload_a

    payload_b = {
      'sensor_id': 2,
      'measure': split_data(measure_accelerometter)[1]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/2/data", data=payload_b)
    sleep(0.125)
    print payload_b

    payload_c = {
      'sensor_id': 3,
      'measure': split_data(measure_accelerometter)[2]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/3/data", data=payload_c)
    sleep(0.125)
    print payload_c

    payload_d = {
      'sensor_id': 4,
      'measure': split_data(measure_gyroscope)[0]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/4/data", data=payload_d)
    sleep(0.125)
    print payload_d

    payload_e = {
      'sensor_id': 5,
      'measure': split_data(measure_gyroscope)[1]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/5/data", data=payload_e)
    sleep(0.125)
    print payload_e

    payload_f = {
      'sensor_id': 6,
      'measure': split_data(measure_gyroscope)[2]
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/6/data", data=payload_f)
    sleep(0.125)
    print payload_f


    payload_g = {
      'sensor_id': 7,
      'measure': measure_magnetometer
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/7/data", data=payload_g)
    sleep(0.125)
    print payload_g
    
    line = ser.readline()
    if not line:
            continue
    measure = line.splitlines()[0]
    if not measure:
            continue
    measure = float(measure)
    payload_h = {
            'sensor_id': 9,
            'measure': measure
    }
    r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/7/data", data=payload_h)
    sleep(0.125)
    print payload_h