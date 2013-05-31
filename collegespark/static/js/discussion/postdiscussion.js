$(function () {
    $.validator.addMethod(
        "check_class_name",
        function(value) {
            console.log(value);
            var regexp = /[a-zA-Z]+\d+\w*/;
            var re = new RegExp(regexp);

            return re.test(value);
        },
        "Class name should start with character and contains number!"
    );

    $('#id_post_body').wysihtml5();

    $('.help-text').popover();


    $('#post-discussion-form').submit(function(e) {
        console.log("asdasdasd");
        console.log($(this).serialize());
        e.preventDefault();
        url = window.location.pathname;
        $.post(url, $(this).serialize(), function(data){
            window.location.href = data["redirect_url"];
        });

    });

    $('#post-discussion-form').validate({
        errorPlacement: function(error, element) {
            element.parent().parent().append(error);
        },
        rules: {
            department: {
                minlength: 3,
                required: true
            },
            class_name: {
              minlength: 3,
              required: true,
              check_class_name: true
            },
            post_topic: {
              minlength: 6,
              required: true
            },
            post_body: {
              minlength: 10,
              required: true
            }
        },
        highlight: function(element) {
            $(element).closest('.control-group').removeClass('success').addClass('error');
        },
        success: function(element) {

            $(element).closest('.control-group').removeClass('error').addClass('success');
            $(element).text('OK!').addClass('valid');
        }
    });


});