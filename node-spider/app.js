var express = require('express');
var app = module.exports = express.createServer();
var request = require('request');

app.get('/', function (req, res) {
  request('http://www.jikexueyuan.com/', function (error, response, body) {
    if (!error && response.statusCode == 200) {
      console.log(body);
      res.send('hello world');
    }
  });
});
app.listen(3000);