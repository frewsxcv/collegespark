(function () {
    "use strict";

    /* Load modules */
    var express = require('express');
    var http = require('http');
    var socketio = require('socket.io');
    // var _ = require('underscore');
    
    var history = {};
    
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

    io.sockets.on('connection', function (client) {
        client.on('send', function (data) {
            var time = getTime();

            if (history[data.room] === undefined) {
                history[data.room] = [];
            }

            history[data.room].push({
                "msg": data.msg,
                "time": time
            });

            console.log(history[data.room]);

            io.sockets.emit('broadcast', {
                "msg": data.msg,
                "time": time,
                "room": data.room
            });
        });
    });
}());
