// Node modules
var request = require('request');
var neo = require('./udooneo');
var URL = 'http://ec2-52-17-73-59.eu-west-1.compute.amazonaws.com:3000/sensors/';

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
  }];
}

/// Main loop
(function loop() {
  console.log(getSensorData());
  //      put(getSensorData());
  setTimeout(loop, 1000);
}());
