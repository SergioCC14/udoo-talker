import requests
import serial
import json
from time import sleep

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