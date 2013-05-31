var csrftoken = $.cookie('csrftoken');

function get_school_name(){
    var url = window.location.pathname;
    var urlsplit = url.split("/");
    var school_name = urlsplit[1];

    return school_name;
}