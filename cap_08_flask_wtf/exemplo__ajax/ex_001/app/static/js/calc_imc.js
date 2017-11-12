$(document).ready(function(){
	/*  .submit ou on('submit' 
		I do not try sth like that: $("#submitBtn").click(function() {
	*/
	$('#form_imc').submit(function(event) {
		console.log('Ajax working!')
		$.ajax({
			url: $SCRIPT_ROOT + '/calc_imc',
			data: { 
				/* dados enviados para a função flask */
				weight: $('input[name="weight"]').val(),
				height: $('input[name="height"]').val()
			},
			type:'POST',
			success: function(data) {
				alert('just a success alert');
			},
			failure: function(response){
				alert('just a failure alert');
			}
		}).done(function (data){
			/*
				Para especificar o que ocorre após a chamada Ajax ter se completado
			*/
			/* O resultado do processamento é exibido ao usuário */
			if(data.error){
				var msg = data.error + '\n' + data.msg;
				$('#div_success').hide();
				$('#div_error').text(msg).show();
				alert(msg);
			}
			else {
				var msg = 'your imc is:' + data.imc;
				$('#div_error').hide();
				$('#div_success').text(msg).show();
				alert(msg);
			}
		});
		/*	A ação default do evento não será encadeada 
			(Para evitar submeta os dados duas vezes)
		*/
		event.preventDefault();
	});
});