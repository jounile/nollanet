$('#summernote').summernote({
    placeholder: 'Write here',
    tabsize: 2,
    height: 200,
    toolbar: [
        ['style', ['style']],
        ['font', ['bold', 'underline', 'clear']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['table', ['table']],
        ['insert', ['link', 'picture']],
        ['view', ['fullscreen', 'codeview', 'help']]
    ],
    callbacks: {
        onImageUpload: function(image) {
            console.log("onImageUploadCallback")
            uploadImage(image[0]);
        }
    }
});

function uploadImage(image) {
    var data = new FormData();
    console.log("data", data)
    data.append("file", image);
    $.ajax({
        url: "/media/savefile",
        cache: false,
        contentType: false,
        processData: false,
        data: data,
        type: "POST",
        success: function(filename) {
            console.log("filename", filename)
            var image = $('<img>').attr('src', '/media/images/' + filename).addClass("img-fluid");
            $('#summernote').summernote("insertNode", image[0]);
        },
        error: function(data) {
            console.log(data);
        }
    });
}