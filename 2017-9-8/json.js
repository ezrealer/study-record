var express = require('express');
var url = require('url');
var app = express();//express 3.x后这样写
app.listen(3080);
app.get('/json', function (req, res) {
    app.set('json space', 4);
    res.json({
        name: "ezreal",built:'140610', items: '14TX',
        centers:['art', 'astorphysics',  'natural history',
                          'plantary', 'biology', 'space', 'zoo']});
});

app.get('/error', function (req, res) {
    res.json(500, {status:false, message:"Tnternal Server Error"});
});
