$(document).ready(function () {

	$('.jumbotron').on("click", '#btnSignUp', function () {
		cont = new contact($('#firstname').val().trim(), $('#lastname').val().trim(), $('#address').val().trim(), $('#email').val().trim(), $('#phone').val().trim())
		cont.fullvalidation()
	});

	$('#upload-file-btn').click(function () {
		var form_data = new FormData($('#upload-file')[0]);
		$.ajax({
			type: 'POST',
			url: '/daniel_minguez/uploader',
			data: form_data,
			contentType: false,
			cache: false,
			processData: false,
			async: false,
			success: function (data) {
				cont2 = new contact(data["contact"]["firstname"], data["contact"]["lastname"], data["contact"]["address"], data["contact"]["email"], data["contact"]["phone"])
				cont2.fullvalidation(data);
				$('#upload-file')[0].reset(); 
			}
		});
	});
});

class contact {
	constructor(firstname, lastname, address, email, phone) {
		this.firstname = firstname
		this.lastname = lastname
		this.address = address
		this.email = email
		this.phone = phone
		this.inp = "firstname=" + this.firstname + "&lastname=" + this.lastname + "&address=" + this.address + "&email=" + this.email +"&phone="+this.phone
	}

	fullvalidation() {
		var $elem = $("#demo");

		var text = "Plase review the following: "

		var val1 = validateEmail(this.email)
		var val2 = validateCompulsory(this.email, this.firstname, this.lastname)

		if (!val1) {
			text = text + " - email is not correct -"
		}
		if (!val2) {
			text = text + " - Some compulsory field is missing (First Name, Last Name and email)"
		}

		if (val2 && val1) {
			text = "Everything ok!"
			$.ajax({
				url: '/daniel_minguez/signUp',
				data: this.inp,
				type: 'POST',
				success: function (response) {
					console.log(response);
					//$elem.html("Accepted");
				},
				error: function (error) {
					console.log(error);
					//$elem.html("Not Accepted");
				}
			});
		}
		$elem.html(text);
	}
}
function validateEmail(email) {
	if (email === "") {
		return false;
	}
	var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
}

function validateCompulsory(email,FirstName,LastName) {
	if (email === "" || FirstName === "" || LastName === "") {
		return false;
	}
	else {
		return true
	}
}