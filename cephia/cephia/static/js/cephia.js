$(document).ready(function() {
    //remove alerts after certain amount of time
    $('.alert').fadeOut(10000);
    $( ".datepicker" ).datepicker();
    //initially disable upload file button
    //$('.upload-btn').attr('disabled', 'disabled');

    //enable and disable the upload file button
    $('#id_data_file').on('change', function() {
        if ($('#id_file_type').val() != "") {
            $('.upload-btn').removeAttr('disabled');
        }
    });

    $('#id_file_type').on('change', function() {
        if ($('#id_data_file').val() != "") {
            $('.upload-btn').removeAttr('disabled');
        }
    });
    //

    $('.btn-comment-modal').on('click', function(event) {
        event.preventDefault();
        var rowId = $(this).parent().data('row-id');
        var fileId = $(this).parent().data('file-id');
        var fileType = $(this).parent().data('file-type');
        var url = "/row_comment/" + fileType + '/' + String(fileId) + '/' + String(rowId);

        $.get(url, function(data, status) {
            var response = JSON.parse(data);
            if (status == "success") {
                $(".comment-modal").html(response.response);
                $( ".datepicker" ).datepicker();
                $("#myModal").modal();
            }
        })
    });
    //

    $('.navtab').on('click', function(event) {
        $(this).addClass('active');
    });

    $('input[name="visit"]').on('click', function(event) {
        var artificialButton = $(this).parents().eq(9).find('input[name="artificial"]');
        var confirmButton = $(this).parents().eq(9).find('input[name="confirm"]');
        var provisionalButton = $(this).parents().eq(9).find('input[name="provisional"]');
        var selectedSpecimen = $('input[name="specimen"].selected');

        $('input[name="visit"].selected').removeClass('selected');
        $(this).addClass('selected');

        if (selectedSpecimen.length > 0) {
            provisionalButton.show();
        }
    });

    $('input[name="specimen"]').on('click', function(event) {
        var artificialButton = $(this).parents().eq(9).find('input[name="artificial"]');
        var confirmButton = $(this).parents().eq(9).find('input[name="confirm"]');
        var provisionalButton = $(this).parents().eq(9).find('input[name="provisional"]');
        var selectedVisit = $('input[name="visit"].selected');
        
        $('input[name="specimen"].selected').removeClass('selected');
        $(this).addClass('selected');
        artificialButton.show();

        if (selectedVisit.length > 0) {
            provisionalButton.show();
        }
    });

    $('a.show-specimen').on('click', function(event) {
        event.preventDefault();
        
        var url = "/reports/visit_specimen_report/";
        var post_data = $('#specimen-form').serializeArray();

        $.post(url, post_data, function(data, status) {
            var response = JSON.parse(data);
            if (status == "success") {
                $(".specimen-modal").html(response.response);
                $("#specimenModal").modal();
            }
        });
    });
});


