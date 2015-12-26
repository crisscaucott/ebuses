// TRAER RECORRIDOS POR EMPRESA
$('#empresas_list > a').on('click', function(e){
	e.preventDefault();
	var element = $(this);
	var id = element.attr('href');
	var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

	$.ajax({
		type: 'POST',
		url: 'http://localhost:8000/buses/empresas/recorridos/',
		data: {csrfmiddlewaretoken: token, id: id},
		// dataType: "json",
		beforeSend: function(xhr){
			$('#empresas_list > a').removeClass('active')
		}
	}).done(function(data, status, jqXHR){
		element.addClass("active");
		$('#recorridos_container').html(data);

	}).fail(function(jqXHR, status, err){
		console.log("ERROR");

	});
})

// CALIFICAR RECORRIDO
$('#calificarBtn').on('click', function(e){
	var id = document.getElementById('calificarModalBtn').value;
	var comentario = document.getElementById('comentario').value.trim();

	if(comentario.length != 0)
	{
		var data = {
			csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[0].value,
			id_recorrido: id,
			estrellas : $('#estrellas option:selected').val(),
			comentario: comentario
		};

		$.ajax({
			type: "POST",
			url: 'http://localhost:8000/buses/empresas/calificar/',
			data: data,

			beforeSend: function(xhr){

			}
		}).done(function(data, status, jqXHR){
			$('#calificar').modal('hide');
			$('#mensajesNotif').html(data)

		}).fail(function(jqXHR, status, err){
			if(jqXHR.status == 400)
			{
				$('#modalMessages').html(jqXHR.responseText);
			}

		});	
	}
})
