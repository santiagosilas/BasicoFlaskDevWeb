$(document).ready(function(){
	$('#form_send').on('submit', function(event) {
		/*
			getJSON: Get JSON data using AJAX HTTP GET Request
			getJSON (url, data, success)
				url: url to send the request to
				data: data to be sent to the server
				success (optional)
					data: data returned from the server
					status: request status - success, error, timeout, ..
					xhr: ..

			Equivalente a: 4.ajax({
				datatype: "json"
				url: ...
				data:...
				success: ...
			});
		*/
		$.getJSON(
			$SCRIPT_ROOT + '/process', 
			{ info: $('input[name="info"]').val() }, 
			function(data) {
				alert(data.result);
		});
		event.preventDefault();
	});
});