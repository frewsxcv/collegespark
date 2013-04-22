$(document).ready(function () {
    $.validator.addMethod("checkDecimal",
        function() {
             var intRegex = /^\d+(\.\d{0,2})?$/;
             var original = $('#id_price').val();
             if (original < 0)
             {
                 return false;
             }
             if (!original.match(intRegex))
             {
                 return false;
             }
             else
             {
                 return true;
             }
        });
});

$("#id_image").change(function () {
   var input = document.getElementById("id_image");
      if (input.files && input.files[0]) {
         var reader = new FileReader();
         reader.onload = function (e) {
            $('.sum-image')
                  .attr('src', e.target.result)
                  .width(400)
                  .height(300);
         };
         reader.readAsDataURL(input.files[0]);
      }
});

$('.steptwo-btn .pre .btn').click(function() {
   $('#myWizard').wizard('previous');
});

$('.stepthree-btn .pre .btn').click(function() {
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
            number: true,
            checkDecimal: true
        },
        description: {
            required: true
        }
    },
    messages: {
        dpt_name: "department name is required",
        class_name: "class name is required",
        book_name: "book name is required",
        description: "book description is required",
        price: {
            required: "book price is required",
            number: "book price must be a number",
            checkDecimal: "book price must be a non-negative number with only 2 decimal places"
        }
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
            $(".sum-dpt").text($('#id_dpt_name').val());
            $(".sum-class").text($('#id_class_name').val());
            $('#myWizard').wizard('next');
        }
        else if (step == 2) {
            $(".sum-book").text($('#id_book_name').val());
            $(".sum-author").text($('#id_author').val());
            $(".sum-ISBN").text($('#id_ISBN').val());
            var myPrice = parseFloat($('#id_price').val()).toFixed(2);
            $('#id_price').val(myPrice);
            $(".sum-price").text($('#id_price').val());
            $(".sum-description").val($('#id_description').val());

            if ($('#id_condition').val() == 1) {
                $(".sum-condition").text('New');
            }
            else {
                $(".sum-condition").text('Used');
            }
            $('#myWizard').wizard('next');
        }
    }
});
