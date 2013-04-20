$(function () {
    $('#textarea').wysihtml5();
    $('#example').popover();

    $('#post-discussion-form').submit(function(e) {
        e.preventDefault();
    });
});