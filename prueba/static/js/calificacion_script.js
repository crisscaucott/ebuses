$('#calificaciones_container').on('click', 'form > ul > a ', function(e){
	e.preventDefault();
	var element = $(this);
	var id = element.attr('href');
	var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

	$.ajax({
		type: 'POST',
		url: 'http://localhost:8000/buses/usuario/calificaciones/',
		data: {csrfmiddlewaretoken: token, id: id},
		// dataType: "json",
		beforeSend: function(xhr){
			$('#calificaciones_container > form > ul > a').removeClass('active');
		}
	}).done(function(data, status, jqXHR){
		element.addClass('active');
		$('#detalles_container').html(data);

		// AGREGAR EVENT LISTENER
		document.getElementById('editarBtn').addEventListener('click', function(e){e.preventDefault(); editarBtn(e);}, false);
		document.getElementById('borrarBtn').addEventListener('click', function(e){e.preventDefault(); borrarBtn(e);}, false);


	}).fail(function(jqXHR, status, err){
		console.log("ERROR");

	});
});

function borrarBtn(element)
{
	var data = {
		csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[1].value,
		id : document.getElementById('idHidden').value,
	}

	console.log(data);

	$.ajax({
		type: 'POST',
		url: 'http://localhost:8000/buses/usuario/calificaciones/borrar/',
		data: data,
		beforeSend: function(xhr){
			$('#dangerMsg').addClass('hidden');
		}
	}).done(function(data, status, jqXHR){
		console.log(data)
		$('#dangerMsg').removeClass('hidden');
		$('#calificaciones_container').html(data.cal);
		$('#detalles_container').empty();
		$('#mensajesNotif').html(data.msg);

	}).fail(function(jqXHR, status, err){
		console.log("ERROR");

	});
}


function editarBtn(element)
{
	element.preventDefault();
	var data = {
		id : document.getElementById('idHidden').value,
		csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[1].value,
		estrellas : $('#estrellas option:selected').val(),
		comentario : document.getElementById('comentario').value.trim()
	};
	if (data.comentario.length != 0)
	{
		console.log(data);

		$.ajax({
			type: 'POST',
			url: 'http://localhost:8000/buses/usuario/calificaciones/editar/',
			data: data,
			// dataType: "json",
			beforeSend: function(xhr){
				
			}
		}).done(function(data, status, jqXHR){
			$('#mensajesNotif').html(data);
			console.log("PASSS");

			// element.addClass('active');
			// $('#detalles_container').html(data);
			// document.getElementById('editarBtn').addEventListener('click', function(e){e.preventDefault(); editarBtn(e);}, false);

		}).fail(function(jqXHR, status, err){
			console.log("ERROR");

		});
	}
}