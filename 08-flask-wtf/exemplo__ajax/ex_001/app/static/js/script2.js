$(document).ready(function(){
	$('#form_send2').on('submit', function(event) {
		$.ajax({
			url: $SCRIPT_ROOT + '/process2',
			data: { info: $('input[name="info2"]').val() },
			type:'POST'
		}).done(function (data){
			if(data.error){
				alert(data.error);
			}
			else {
				alert('correct:' + data.result);
			}
		});
		
		event.preventDefault();
	});
});