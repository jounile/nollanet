function confirmDelete(form) {
    if (confirm("Are you sure you want to delete?")) {
        form.submit();
    }
}

function filePreview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#uploadPreview > img').remove();
            $('#uploadPreview').append('<img src="'+e.target.result+'" />');
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function addImageTagToTextarea(param){
    var imgSrc = $(param).attr("src");
    var imgAlt = $(param).attr("alt");
    var imgTag = '<img src="'+imgSrc+'" alt="'+imgAlt+'" />'; 
    $('#textArea').empty();
    $('#textArea').html(imgTag);
    $('#myModal').modal('hide');
}

$(document).ready(function() {

    /* 
        Show file preview when a file is selected
    */
    $("#file").change(function () {
        filePreview(this);
    });

    /* 
        Show storytype_id selection depending when mediatype_id is 5 (Stories)
    */
    $("#storytype_id_form_group").hide();
    $("#mediatype_id_selector").change(function() {
        var selectedMediaType = $("#mediatype_id_selector option:selected").val();
        if(selectedMediaType == 5){
            $("#storytype_id_form_group").show();
        } else {
            $("#storytype_id_form_group").hide();
        }
    });

    /*
        Modal window for image selections
    */
    $("#btnShowModal").click(function () {
        $("#myModal").modal("show");
    });

});
