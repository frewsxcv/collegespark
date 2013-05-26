$(function () {
    "use strict";

    var prettyUnixDate = function (unix) {
        return moment(unix).format('MMMM Do YYYY, h:mm:ss a');
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
            var html = "<li>" + prettyUnixDate(data.time) + ": " + data.msg + "</li>";
            that.$msgs.append(html);
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
