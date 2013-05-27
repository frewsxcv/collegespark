$(function () {
    "use strict";


    var Message = function (obj) {
        this.time = moment(obj.time).format('MMMM Do YYYY, h:mm:ss a');
        this.text = obj.msg;
    };

    Message.prototype.html = function () {
        var html = "<li>" + this.time + ": " + this.text + "</li>";
        return $(html);
    };


    var Chat = function () {
        this._cache();
        this._events();
        this.connect();
    };

    Chat.prototype._cache = function () {
        this.$inputText = $("#chat-input-text");
        this.$inputButton = $("#chat-input-button");
        this.$msgs = $("#chat-msgs");
    };

    Chat.prototype._events = function () {
        var that = this;
        this.$inputText.keypress(function (e) {
            if (e.which === 13) {
                that.send();
            }
        });
        this.$inputButton.click(function() {
            that.send();
        });
    };

    Chat.prototype.connect = function () {
        var that = this;
        this.socket = io.connect('http://localhost:8001');
        this.socket.on('broadcast', function (data) {
            var msg = new Message(data),
                html = msg.html();
            that.$msgs.append(html);
            html.get(0).scrollIntoView();
        });
    };

    Chat.prototype.send = function () {
        var msg = this.$inputText.val();
        if (msg.length > 0) {
            this.socket.emit('send', {'msg': msg});
            this.$inputText.val("");
        } else {
            window.alert("Can not send an empty message");
        }
    };

    new Chat();
});
