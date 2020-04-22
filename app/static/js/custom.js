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

$(document).ready(function() {

    /* 
        Show file preview when a file is selected
    */
    $("#image").change(function () {
        filePreview(this);
    });

});
