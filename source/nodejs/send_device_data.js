'use strict';

var clientFromConnectionString = require('azure-iot-device-mqtt').clientFromConnectionString;
var Message = require('azure-iot-device').Message;
var dht = require('dht-sensor');

var connectionString = 'HostName={youriothostname};DeviceId=AgitareTechIoTWorkshopDevice;SharedAccessKey={yourdevicekey}';

var client = clientFromConnectionString(connectionString);

function printResultFor(op) {
    return function printResult(err, res) {
        if (err) console.log(op + ' error: ' + err.toString());
        if (res) console.log(op + ' status: ' + res.constructor.name);
    };
}

var connectCallback = function (err) {
    if (err) {
        console.log('Could not connect: ' + err);
    } else {
        console.log('Client connected');
  
        // Create a message and send it to the IoT Hub every second
        setInterval(function(){
            var currentMeasure = null;
            try {
                currentMeasure = dht.read(11, 4); // 11 -> DHT11, 4 -> GPIO
                var data = JSON.stringify({ deviceId: 'AgitareTechIoTWorkshopDevice', temperature: currentMeasure.temperature, humidity: currentMeasure.humidity });
                var message = new Message(data);
                console.log("Sending message: " + message.getData());
                client.sendEvent(message, printResultFor('send'));
            } catch (err) {
                console.log("Error: An error occured while reading or transmitting sensor data.")
            }
        }, 10000);
    }
};

client.open(connectCallback);