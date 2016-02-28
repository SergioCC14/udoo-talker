import requests
import serial
import json
from time import sleep

def obtain_distance():
  with serial.Serial('/dev/ttyMCC', 115200, timeout=0) as ser:
    while True:
      line = ser.readline()
      if not line:
              continue
      measure = line.splitlines()[0]
      if not measure:
              continue
      measure = float(measure)
      payload = {
              'sensor_id': 4,
              'measure': measure
      }
      #r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/4/data", data=payload)
      print payload
      sleep(0.5)


def read_file(path):
  file = open(path)
  data = file.read()
  file.close()

  return data


def split_data(data, name):
  dr = data.replace("\n", "").split(',')
  
  return data_formatted : {
    (name + '-x'): dr[0]
    (name + '-y'): dr[1]
    (name + '-z'): dr[2]
  }


def send_data(udoo_id):
  if (udoo_id == 1):
  elif (udoo_id == 2):
    
  elif (udoo_id == 3):
  elif (udoo_id == 4):
  elif (udoo_id == 5):
  elif (udoo_id == 6):
  elif (udoo_id == 7):

  



