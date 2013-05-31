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
        client.on('history', function (data) {
            client.emit('history', {
                "history": history[data.room] || []
            });
        });
        client.on('send', function (data) {
            var time = getTime();

            if (history[data.room] === undefined) {
                history[data.room] = [];
            }

            history[data.room].push({
                "msg": data.msg,
                "user": data.user,
                "time": time
            });

            io.sockets.emit('broadcast', {
                "msg": data.msg,
                "time": time,
                "user": data.user,
                "room": data.room
            });
        });
    });
}());
