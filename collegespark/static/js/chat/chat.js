$(function () {
    "use strict";


    var Message = function (obj) {
        this.time = moment(obj.time).format('h:mm');
        this.text = obj.msg;
        this.user = obj.user;
    };

    Message.prototype.html = function () {
        var html = "<li class='chat-msg'>" +
            "<span class='label label-inverse'>" + this.time + "</span>&nbsp;" +
            "<span class='label label-info'>" + this.user + "</span>: " + 
            this.text + "</li>";
        return $(html);
    };


    var Chat = function () {
        this.room = defaultRoom;
        this.user = user;
        this._cache();
        this._events();
        this.connect();

        var that = this;
        $(".chat-tab").click(function (elem) {
            that.switchTab(elem);
        });

        $("#chat-tab-add").click(function () {
            var newTab = prompt("Enter the new tab name"),
                $elem = $("<li class='chat-tab'>" +
                    "<a href='#'>" + newTab + "</a></li>");
            if (newTab) {
                $elem.click(function (elem) {
                    that.switchTab(elem);
                }); 
                $("#chat-tab-add").before($elem);
            }
        });
    };

    Chat.prototype.switchTab = function (elem) {
        var $elem = $(elem.target);
        $(".chat-tab").removeClass("active");
        $elem.parent().addClass("active");
        this.clear();
        this.room = $elem.text();
        this.socket.emit('history', {'room': this.room});
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

    Chat.prototype.clear = function () {
        this.$msgs.empty();
    };

    Chat.prototype.connect = function () {
        var that = this;
        this.socket = io.connect('http://' + window.location.hostname + ':8001');
        this.socket.on('history', function (data) {
            data.history.forEach(function (m) {
                var msg = new Message(m),
                    html = msg.html();
                that.$msgs.append(html);
            });
        });
        this.socket.on('broadcast', function (data) {
            var msg = new Message(data),
                html = msg.html();
            if (data.room === that.room) {
                that.$msgs.append(html);
                html.get(0).scrollIntoView();
            }
        });
        this.socket.emit('history', {'room': this.room});
    };

    Chat.prototype.send = function () {
        var msg = this.$inputText.val();
        if (msg.length > 0) {
            this.socket.emit('send', {
                'room': this.room,
                'msg': msg,
                'user': this.user
            });
            this.$inputText.val("");
        } else {
            window.alert("Can not send an empty message");
        }
    };

    new Chat();
});
