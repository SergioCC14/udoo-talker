import requests
from time import sleep

fakte_data = [
  {'sensor_id': 1, 'measure': '20'},
  {'sensor_id': 2, 'measure': '-528'},
  {'sensor_id': 3, 'measure': '-16404'},
  {'sensor_id': 4, 'measure': '30'},
  {'sensor_id': 5, 'measure': '5'},
  {'sensor_id': 6, 'measure': '-3'},
  {'sensor_id': 7, 'measure': '-465,534,267\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '112'},
  {'sensor_id': 2, 'measure': '-564'},
  {'sensor_id': 3, 'measure': '-16332'},
  {'sensor_id': 4, 'measure': '24'},
  {'sensor_id': 5, 'measure': '18'},
  {'sensor_id': 6, 'measure': '-9'},
  {'sensor_id': 7, 'measure': '-473,536,274\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '68'},
  {'sensor_id': 2, 'measure': '-640'},
  {'sensor_id': 3, 'measure': '-16388'},
  {'sensor_id': 4, 'measure': '27'},
  {'sensor_id': 5, 'measure': '15'},
  {'sensor_id': 6, 'measure': '-5'},
  {'sensor_id': 7, 'measure': '-518,540,263\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '104'},
  {'sensor_id': 2, 'measure': '-620'},
  {'sensor_id': 3, 'measure': '-16396'},
  {'sensor_id': 4, 'measure': '20'},
  {'sensor_id': 5, 'measure': '14'},
  {'sensor_id': 6, 'measure': '-12'},
  {'sensor_id': 7, 'measure': '-483,524,271\n'},
  {'sensor_id': 9, 'measure': 726.0},
  {'sensor_id': 1, 'measure': '188'},
  {'sensor_id': 2, 'measure': '-576'},
  {'sensor_id': 3, 'measure': '-16384'},
  {'sensor_id': 4, 'measure': '26'},
  {'sensor_id': 5, 'measure': '18'},
  {'sensor_id': 6, 'measure': '-7'},
  {'sensor_id': 7, 'measure': '-509,550,273\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '112'},
  {'sensor_id': 2, 'measure': '-588'},
  {'sensor_id': 3, 'measure': '-16396'},
  {'sensor_id': 4, 'measure': '25'},
  {'sensor_id': 5, 'measure': '16'},
  {'sensor_id': 6, 'measure': '-7'},
  {'sensor_id': 7, 'measure': '-519,537,283\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '68'},
  {'sensor_id': 2, 'measure': '-464'},
  {'sensor_id': 3, 'measure': '-16284'},
  {'sensor_id': 4, 'measure': '28'},
  {'sensor_id': 5, 'measure': '14'},
  {'sensor_id': 6, 'measure': '1'},
  {'sensor_id': 7, 'measure': '-500,543,270\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '28'},
  {'sensor_id': 2, 'measure': '-512'},
  {'sensor_id': 3, 'measure': '-16368'},
  {'sensor_id': 4, 'measure': '21'},
  {'sensor_id': 5, 'measure': '13'},
  {'sensor_id': 6, 'measure': '-3'},
  {'sensor_id': 7, 'measure': '-503,544,267\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '56'},
  {'sensor_id': 2, 'measure': '-480'},
  {'sensor_id': 3, 'measure': '-16384'},
  {'sensor_id': 4, 'measure': '23'},
  {'sensor_id': 5, 'measure': '14'},
  {'sensor_id': 6, 'measure': '-5'},
  {'sensor_id': 7, 'measure': '-511,543,259\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '68'},
  {'sensor_id': 2, 'measure': '-512'},
  {'sensor_id': 3, 'measure': '-16428'},
  {'sensor_id': 4, 'measure': '29'},
  {'sensor_id': 5, 'measure': '5'},
  {'sensor_id': 6, 'measure': '-6'},
  {'sensor_id': 7, 'measure': '-484,542,280\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '44'},
  {'sensor_id': 2, 'measure': '-560'},
  {'sensor_id': 3, 'measure': '-16440'},
  {'sensor_id': 4, 'measure': '21'},
  {'sensor_id': 5, 'measure': '16'},
  {'sensor_id': 6, 'measure': '-8'},
  {'sensor_id': 7, 'measure': '-502,548,271\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '68'},
  {'sensor_id': 2, 'measure': '-536'},
  {'sensor_id': 3, 'measure': '-16400'},
  {'sensor_id': 4, 'measure': '27'},
  {'sensor_id': 5, 'measure': '12'},
  {'sensor_id': 6, 'measure': '-5'},
  {'sensor_id': 7, 'measure': '-493,536,292\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '60'},
  {'sensor_id': 2, 'measure': '-504'},
  {'sensor_id': 3, 'measure': '-16432'},
  {'sensor_id': 4, 'measure': '24'},
  {'sensor_id': 5, 'measure': '8'},
  {'sensor_id': 6, 'measure': '-7'},
  {'sensor_id': 7, 'measure': '-510,547,281\n'},
  {'sensor_id': 9, 'measure': 726.0},
  {'sensor_id': 1, 'measure': '44'},
  {'sensor_id': 2, 'measure': '-584'},
  {'sensor_id': 3, 'measure': '-16484'},
  {'sensor_id': 4, 'measure': '27'},
  {'sensor_id': 5, 'measure': '13'},
  {'sensor_id': 6, 'measure': '-6'},
  {'sensor_id': 7, 'measure': '-501,547,272\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '124'},
  {'sensor_id': 2, 'measure': '-560'},
  {'sensor_id': 3, 'measure': '-16472'},
  {'sensor_id': 4, 'measure': '30'},
  {'sensor_id': 5, 'measure': '12'},
  {'sensor_id': 6, 'measure': '-3'},
  {'sensor_id': 7, 'measure': '-478,531,277\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '76'},
  {'sensor_id': 2, 'measure': '-568'},
  {'sensor_id': 3, 'measure': '-16400'},
  {'sensor_id': 4, 'measure': '24'},
  {'sensor_id': 5, 'measure': '5'},
  {'sensor_id': 6, 'measure': '-6'},
  {'sensor_id': 7, 'measure': '-517,545,287\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '64'},
  {'sensor_id': 2, 'measure': '-496'},
  {'sensor_id': 3, 'measure': '-16432'},
  {'sensor_id': 4, 'measure': '29'},
  {'sensor_id': 5, 'measure': '19'},
  {'sensor_id': 6, 'measure': '-5'},
  {'sensor_id': 7, 'measure': '-513,552,278\n'},
  {'sensor_id': 9, 'measure': 725.0},
  {'sensor_id': 1, 'measure': '116'},
  {'sensor_id': 2, 'measure': '-600'},
  {'sensor_id': 3, 'measure': '-16124'},
  {'sensor_id': 4, 'measure': '14'},
  {'sensor_id': 5, 'measure': '12'},
  {'sensor_id': 6, 'measure': '-6'}
]

for i in fakte_data:
  r = requests.put("http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/"+ str(i['sensor_id'])+ "/data", data=i)
  sleep(0.125)
  print i