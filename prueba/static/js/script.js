// LOGIN CLICK
document.getElementById('loginBtn').addEventListener('click', function(e){
	var data = $('#loginForm').serialize();
	var url = 'http://localhost:8000/accounts/login/';
	// console.log(data);

	$.ajax({
		type: 'POST',
		url: url,
		data: data,

		success:function(res, data){
			$('#login').modal('hide');
			$('#logoutLi').removeClass('hidden');
			$('#loginLi').addClass('hidden');
			console.log(res);
			console.log(data);
			// console.log("MUY BIEN");
		},
		error:function(res, data){
			// console.log("MUY MAL");
		}
	});
})

document.getElementById('logoutLi').addEventListener('click', function(e){
	var url = 'http://localhost:8000/accounts/logout/';
	var data = $('#loginForm').serialize();
	// console.log("Data");
	// console.log(data);
	
	$.ajax({
		type: 'POST',
		url: url,
		data: data,

		success:function(res, data){
			console.log("LOGOUT EXITOSO");
		},
		error:function(res, data){
			console.log("FALLO LOGOUT");
		}
	});
})
