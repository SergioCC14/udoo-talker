// Node modules
var udoo = require('udoo');
var request = require('request');
var neo = require("./udooneo");

var URL = '172.16.3.201/sensors/';

gyroscopic = neo.sensors.Gyroscope;
magnetometer = neo.sensors.Magnetometer;
accelerometer = sensors.Accelerometer;
real_path = "/sys/class/gpio/gpio174"

function put(data, callback) {
  request({
    url: URL + 'update_bulk/',
    method: 'PUT',
    json: data,
  }, callback);
}

function getSensorData() {
  var data = [];

  // Get data from a sensor
  gyroscopic_data = gyroscopic.data();
  magnetometer = magnetometer.data();
  accelerometer = accelerometer.data();
  // var sensor_proximity = udoo.get("")

  // Duplicar por cada sensor --------------------------
  var sensorData = {
    'gyroscopic': gyroscopic_data, // Fill this with real data
    'magnetometer': magnetometer, // Fill this with real data
    'accelerometer': accelerometer

  };
  data.push(sensorData);
  //  --------------------------

  return data;

}

// Main loop
(function loop() {
  put(getSensorData());
  setTimeout(loop, 1000);
}());