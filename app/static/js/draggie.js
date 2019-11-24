$(document).ready(function() {
	$(".draggie").draggable({
		containment: "parent",
		cursor: "move",
		revert: true,
		revertDuration: 100
	});
	var targetName;
	$(".draggie").mousedown(function(){
		targetName = $(this).attr("src");
	});
	$("#textCompose").droppable({
		accept: ".draggie",
		drop: function(event) {
			$('#textCompose').val($('#textCompose').val() + '<img src="' + targetName + ' />');
		}
	});
});