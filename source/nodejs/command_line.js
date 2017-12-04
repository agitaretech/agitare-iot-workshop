var dht = require('dht-sensor');
var current = dht.read(11, 4); // 11 -> DHT11, 4 -> GPIO  

console.log('Humidity: ' + current.humidity +'%');
console.log('Temperature: ' + current.temperature + 'C');