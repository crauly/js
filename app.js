var express = require('express');

var app = express();


app.get('/', function (req, res) {
  res.sendFile("index.html")
})

app.listen(3000, function (req, res) {
  console.log("OK")
})