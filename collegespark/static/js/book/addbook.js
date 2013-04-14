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

      $("#addBook-StepOne").change(function() {
         if ($.trim($("#id_school_name").val()) == "" ||
            $.trim($("#id_dpt_name").val()) == "" ||
            $.trim($("#id_class_name").val()) == "") {
               $('#stepone-next').hide(300);
         }
         else {
            $('#stepone-next').show(300);
         }
      })

     $('#stepone-next').click(function() { 
        $('#myWizard').wizard('next');
        $("#sum-school").text($('#id_school_name').val());
        $("#sum-dpt").text($('#id_dpt_name').val());
        $("#sum-class").text($('#id_class_name').val());
     });

     $("#addBook-StepTwo").change(function() {
         if ($.trim($("#id_book_name").val()) == "" ||
            $.trim($("#id_author").val()) == "" ||
            $.trim($("#id_ISBN").val()) == "" ||
            $.trim($("#id_price").val()) == "" ||
            $("#id_image").val() == "") {
               $('#steptwo-next').hide(300);
         }
         else {
            $('#steptwo-next').show(300);
         }
      })

    $('#steptwo-next').click(function() { 
       $('#myWizard').wizard('next');
       $("#sum-book").text($('#id_book_name').val());
       $("#sum-author").text($('#id_author').val());
       $("#sum-ISBN").text($('#id_ISBN').val());
       $("#sum-price").text($('#id_price').val());

       if ($('#id_condition').val() == 1) {
          $("#sum-condition").text('New');
       }
       else {
         $("#sum-condition").text('Used');
       }
    });

    $('#steptwo-pre').click(function() { 
       $('#myWizard').wizard('previous');
    });

    $('#stepthree-pre').click(function() { 
       $('#myWizard').wizard('previous');
    });