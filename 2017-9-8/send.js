var express = require('express');
var url = require('url');
var app = express();
app.listen(3000);
app.get('/', function (req, res) {
	var response = '<html><head><title>Simple send</title></head>' + 
	                              '<body><h1>Hello from Express</h1></body></html>';
	res.status(200);
	res.send({
		'Content-Type': 'text/html',
		'Content-Length': response.length
	});
	res.send(response);
	console.log('response finishhed?' + res.finishhed);
	console.log('\nHeaders sent:');
	console.log(res.headerSent);
});

app.get('/error', function (res, req) {
	res.status(400);
	res.send("This is a bad request");
});