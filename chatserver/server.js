(function () {
    "use strict";

    /* Load modules */
    var express = require('express');
    var http = require('http');
    var socketio = require('socket.io');
    // var _ = require('underscore');
    
    var getTime = function () {
        return (new Date()).getTime();
    };

    var config = {
        "port": 8001,
    };

    var app = express();
    var server = http.createServer(app);
    var io = socketio.listen(server);

    server.listen(config.port);

    app.get('/', function (req, res) {
        res.send('hello world');
    });

    io.sockets.on('connection', function (client) {
        client.on('send', function (data) {
            io.sockets.emit('broadcast', {
                "msg": data.msg,
                "time": getTime()
            });
        });
    });
}());
