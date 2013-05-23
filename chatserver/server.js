/* Load modules */
var express = require('express');
var http = require('http');
var socketio = require('socket.io');
var _ = require('underscore');

var config = {
    "port": 8001,
}


var app = express();
var server = http.createServer(app);
var io = socketio.listen(server);

server.listen(config.port);

app.get('/', function (req, res) {
    res.send('hello world');
});

io.sockets.on('connection', function (socket) {
    socket.emit('news', { hello: 'world' });
    socket.on('my other event', function (data) {
        console.log(data);
    });
});
