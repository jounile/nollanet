$(document).ready(function() {
	$(".draggie").draggable({
		containment: "parent",
		cursor: "move",
		revert: true,
		revertDuration: 100
	});
	var targetName;
	$(".draggie").mousedown(function(){
		targetName = $(this).attr("href");
	});
	$(".draggie").hover(function(){
		targetName = $(this).attr("href");
		$("#image_preview").append("<p id='screenshot'><img src='"+ targetName +"' alt='url preview' /></p>");
	}, function() {
		$("#screenshot").remove();
	});
	$("#textCompose").droppable({
		accept: ".draggie",
		drop: function(event) {
			$('#textCompose').val($('#textCompose').val() + '<img src="' + targetName + '" />');
		}
	});
});