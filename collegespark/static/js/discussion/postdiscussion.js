$(function () {
    $('#id_post_body').wysihtml5();

    $('.help-text').popover();

    console.log();
    $('#post-discussion-form').submit(function(e) {
        console.log("asdasdasd");
        console.log($(this).serialize());
        e.preventDefault();
        url = window.location.pathname;
        $.post(url, $(this).serialize(), function(data){
            console.log(data);
        });

    });
});