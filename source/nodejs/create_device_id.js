'use strict';

var iothub = require('azure-iothub');
var connectionString = '{iothub connection string}';
var registry = iothub.Registry.fromConnectionString(connectionString);

var device = {
    deviceId: 'AgitareTechIoTWorkshopDevice'
}

registry.create(device, function(err, deviceInfo, res) {
    if (err) {
        registry.get(device.deviceId, printDeviceInfo);
    }
    if (deviceInfo) {
        printDeviceInfo(err, deviceInfo, res)
    }
});
  
function printDeviceInfo(err, deviceInfo, res) {
    if (deviceInfo) {

        console.log("IoT Hub Device:")
        console.log("  deviceId                    = " + deviceInfo.deviceId)
        console.log("  primaryKey                  = " + deviceInfo.authentication.symmetricKey.primaryKey)
        console.log("  secondaryKey                = " + deviceInfo.authentication.symmetricKey.secondaryKey)
        console.log("  status                      = " + deviceInfo.status)
        console.log("  lastActivityTime            = " + deviceInfo.lastActivityTime)
        console.log("  cloudToDeviceMessageCount   = " + deviceInfo.cloudToDeviceMessageCount)
        console.log("")
    }
}