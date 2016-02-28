// Node modules
var request = require('request');
var neo = require('./udooneo');
var SerialPort = require('serialport').SerialPort;
var lastDistance;

var serialPort = new SerialPort('/dev/ttyMCC', {
  baudrate: 115200,
});



serialPort.on('open', function() {
  console.log('Open port');
  process.on('SIGINT', exitHandler.bind(null, { exit: true }));

  function exitHandler() {
    serialPort.close();
  }
  serialPort.on('error', function(err) {
    console.error('Error opening serial', err);
  });
  serialPort.on('data', function(data) {
    if (data) {
      lastDistance = data.toString();
    }
  });
});



var URL = '172.16.3.201/sensors/';

var gyroscopic = neo.sensors.Gyroscope;
var magnetometer = neo.sensors.Magnetometer;
var accelerometer = neo.sensors.Accelerometer;

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

/// Main loop
(function loop() {
  console.log(getSensorData());
  //      put(getSensorData());
  setTimeout(loop, 1000);
}());
