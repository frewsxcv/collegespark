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

    $('#login-form').submit(function(e) {
        e.preventDefault();
        console.log($(this).serialize());
        $.post('/login/validation', $(this).serialize(), function(data){
            if (data['error']) {
                alert(data['error']);
            } else if (data['redirect_url']) {
                window.location = data['redirect_url'];
            }
        });
    });

    $('.signup-form').validate({
        errorPlacement: function(error, element) {
            element.parent().prepend(error);
        },
        rules: {
            email_signup: {
                required: true,
                email: true,
                remote: {
                    url: "/email/validation",
                    type: "POST"
                }
            },
            school_signup: {
                minlength: 3,
                required: true
            },
            password_signup: {
              minlength: 6,
              required: true
            },
            re_enter_password_signup: {
              equalTo: "#id_password_signup",
              minlength: 6,
              required: true
            }
        },
        messages: {
            re_enter_password_signup: "Your password does not match"
        },
        highlight: function(element) {
            $(element).closest('.control-group').removeClass('success').addClass('error');
        },
        success: function(element) {
            $(element).text('OK!').addClass('valid');
            $(element).closest('.control-group').removeClass('error').addClass('success');
        },
        submitHandler: function(form) {
            $.post('/login/validation', form.serialize(), function(data){
                alert(data);
            });
        }
    });

    $('.signup-form').submit(function(e) {
        console.log(e);
    });
});
