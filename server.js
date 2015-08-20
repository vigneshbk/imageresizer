var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.json());

var readings=[{'Temperature':0,'Humidity':0}]

console.log('Current Date'+new Date())

app.get('/', function (req, res) {
  res.send('Hello World!');
});



app.get('/data/log', function (req, res) {

		console.log('temp : '+req.query.temp + ' humidity ' + req.query.humidity);
	if(req.query.temp == undefined ||  req.query.humidity ==undefined)
	{
		res.statusCode = 400;
		return res.send('Error 400:  syntax incorrect.');
	}
	else
	{

		var newReading = {
		Temperature : req.query.temp,
		Humidity :req.query.humidity,
		logged:new Date()
	  };

	readings.push(newReading);
	  res.json(true);
		res.end();
	return	res.status(200).end();
	}

});

app.get('/data', function (req, res) {
	res.json(readings);
	res.end();
});



app.post('/data', function (req, res) {

	console.log(req.body);
	  if(!req.body.hasOwnProperty('Temperature') ||  !req.body.hasOwnProperty('Humidity')) {
		res.statusCode = 400;
		return res.send('Error 400: Post syntax incorrect.');
	}

	var newReading = {
		Temperature : req.body.Temperature,
		Humidity : req.body.Humidity,
		logged:new Date()
	  };

	readings.push(newReading);
	  res.json(true);
		res.end();
})

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});