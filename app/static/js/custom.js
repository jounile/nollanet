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
        Show story_type selection depending when media_type is 5 (Stories)
    */
    $("#story_type_form_group").hide();
    $("#media_type_selector").change(function() {
        var selectedMediaType = $("#media_type_selector option:selected").val();
        if(selectedMediaType == 5){
            $("#story_type_form_group").show();
        } else {
            $("#story_type_form_group").hide();
        }
    });

    /*
        Modal window for image selections
    */
    $("#btnShowModal").click(function () {
        $("#myModal").modal("show");
    });

});
