// LOGIN CLICK
// document.getElementById('loginBtn').addEventListener('click', function(e){
// 	var data = $('#loginForm').serialize();
// 	var url = 'http://localhost:8000/accounts/login/';
// 	// console.log(data);

// 	$.ajax({
// 		type: 'POST',
// 		url: url,
// 		data: data,

// 		success:function(res, data){
// 			$('#login').modal('hide');
// 			$('#logoutLi').removeClass('hidden');
// 			$('#loginLi').addClass('hidden');
// 			console.log(res);
// 			console.log(data);
// 			// console.log("MUY BIEN");
// 		},
// 		error:function(res, data){
// 			console.log("MUY MAL");
// 		}
// 	});
// })

document.getElementById('logout').addEventListener('click', function(e){
	var url = 'http://localhost:8000/accounts/logout/';
	var data = $('#loginForm').serialize();
	// console.log("Data");
	// console.log(data);
	
	$.ajax({
		type: 'POST',
		url: url,
		data: data,

		success:function(res, data){
			$('#logoutLi').addClass('hidden');
			$('#loginLi').removeClass('hidden');
			console.log("LOGOUT EXITOSO");
		},
		error:function(res, data){
			console.log("FALLO LOGOUT");
		}
	});
})

$('#enviarBtn > button').on('click', function(e){
	var origen = $('#origenSelect option:selected').text().trim();
	var destino = $('#destinoSelect option:selected').text().trim();
	var url = 'http://localhost:8000/buses/empresas/consulta/'+ origen +'/'+ destino +'/'

	window.location = url;
});

$('button.verParadas').on('click', function(e){
	e.preventDefault();
	var element = $(this);
	var url = 'http://localhost:8000/buses/empresas/consulta/'
	var btnVars = element.attr('value').split('|')
	var data = {
		csrfmiddlewaretoken : document.getElementsByName('csrfmiddlewaretoken')[0].value,
		id : btnVars[0],
		origen : btnVars[1],
		destino : btnVars[2]
	}

	$.ajax({
		type : 'POST',
		url : url,
		data : data

	}).done(function(data, status, jqXHR){
		console.log("A");
		element.parent().html(data.res)

	}).fail(function(jqXHR, status, err){
		console.log("ERROR");

	});
});
