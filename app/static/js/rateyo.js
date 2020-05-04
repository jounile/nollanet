
$(document).ready(function() {

    /* Read rating from page meta field and provide it to RateYo */
    var rating_data = $('#rating').data("rating");

    $("#rateYo").rateYo({
        rating: rating_data,
        fullStar: true
    });

    /* Read spot_id from meta field and provide it to Ajax call */
    var spotid_data = $('#spotid').data("spotid");

    $("#rateYo").rateYo().on("rateyo.set", function (e, data) {
        saverating(data, spotid_data);
    });

});

function saverating(data, spotid_data) {
    spotid_rating_data = { 'spotid': spotid_data, 'rating': data.rating }
    $.ajax({
        url: "/spots/saverating",
        data: spotid_rating_data,
        type: "POST",
        success: function(response) {
            $('#rating_feedback').html(response);
        },
        error: function(error) {
            $('#rating_feedback').text(error);
        }
    });
}
