function change_status(id){
		var before = $('a[id=a' + id + ']').find('span').html();
		$.getJSON(
			$SCRIPT_ROOT + '/change_status', 
			{ id_record: id }, 
			function(data) {
				$('a[id=a' + id + ']').find('span').html(data.result);
				//alert('the status of record with id ' + id + ' was changed from ' + before + ' to ' + data.result);
		});
	}