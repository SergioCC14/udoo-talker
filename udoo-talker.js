// Node modules
var request = require('request');
var neo = require('./udooneo');
var SerialPort = require('serialport').SerialPort;
var lastDistance;

var serialPort = new SerialPort('/dev/ttyMCC', {
  baudrate: 115200,
});

serialPort.on('open', function() {
  serialPort.on('data', function(data) {
    console.log('data received: ' + data);
    lastDistance = data;
  });
});



var URL = '172.16.3.201/sensors/';

var gyroscopic = neo.sensors.Gyroscope;
var magnetometer = neo.sensors.Magnetometer;
var accelerometer = neo.sensors.Accelerometer;
var real_path = '/sys/class/gpio/gpio174';

function put(data, callback) {
  request({
    url: URL + 'update_bulk/',
    method: 'PUT',
    json: data,
  }, callback);
}

function getSensorData() {
  return [{
    udoo_id: 1,
    measure: gyroscopic.data(),
  }, {
    udoo_id: 2,
    measure: magnetometer.data(),
  }, {
    udoo_id: 3,
    measure: accelerometer.data(),
  }, {
    udoo_id: 4,
    measure: lastDistance,
  }];
}

// Main loop
(function loop() {
  console.log(getSensorData());
  //      put(getSensorData());
  setTimeout(loop, 300);
}());
