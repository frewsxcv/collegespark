$('#info-tabs a').click(function(e) {
    e.preventDefault();
    $(this).tab('show');
});

$('#info-tabs a:last').tab('show');

$(function() {
    // Setup drop down menu
    $('.dropdown-toggle').dropdown();

    // Fix input element click problem
    $('.dropdown input, .dropdown label').click(function(e) {
        e.stopPropagation();
    });
});
