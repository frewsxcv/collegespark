$("#id_image").change(function () {
   var input = document.getElementById("id_image");
      if (input.files && input.files[0]) {
         var reader = new FileReader();
         reader.onload = function (e) {
            $('#sum-image')
                  .attr('src', e.target.result)
                  .width(400)
                  .height(300);
         };
         reader.readAsDataURL(input.files[0]);
      }
});

$('#steptwo-pre').click(function() {
   $('#myWizard').wizard('previous');
});

$('#stepthree-pre').click(function() {
   $('#myWizard').wizard('previous');
});

$('#addbook-form').validate({
    errorPlacement: function(error, element) {
        element.parent().prepend(error);
    },
    rules: {
        dpt_name: {
            required: true
        },
        class_name: {
            required: true
        },
        book_name: {
            required: true
        },
        price: {
            required: true,
            number: true
        },
        description: {
            required: true
        }
    },
    messages: {
        dpt_name: "department name is required",
        class_name: "class name is required",
        book_name: "book name is required",
        price: "book price is required and must be number",
        description: "book description is required"
    },
    highlight: function(element) {
        $(element).closest('.control-group').removeClass('success').addClass('error');
    },
    success: function(element) {
        $(element).text('OK!').addClass('valid');
        $(element).closest('.control-group').removeClass('error').addClass('success');
    },
    submitHandler: function(form) {
        var step = $('#myWizard').wizard('selectedItem').step;
        if (step == 1) {
            $("#sum-dpt").text($('#id_dpt_name').val());
            $("#sum-class").text($('#id_class_name').val());
            $('#myWizard').wizard('next');
        }
        else if (step == 2) {
            $("#sum-book").text($('#id_book_name').val());
            $("#sum-author").text($('#id_author').val());
            $("#sum-ISBN").text($('#id_ISBN').val());
            $("#sum-price").text($('#id_price').val());
            $("#sum-description").text($('#id_description').val());

            if ($('#id_condition').val() == 1) {
                $("#sum-condition").text('New');
            }
            else {
                $("#sum-condition").text('Used');
            }
            $('#myWizard').wizard('next');
        }
    }
});
