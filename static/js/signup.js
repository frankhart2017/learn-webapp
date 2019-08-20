$(document).ready(function() {

  $("#signup").click(function() {
      var name = $("#name").val();
      var email = $("#email").val();
      var phone = $("#phone").val()
      var password = $("#password").val();
      var cpassword = $("#cpassword").val();

      if(name != "" && email != "" && phone != "" && password != "" && cpassword != "") {

        if(password == cpassword) {
          $.ajax({
            url: "/signup",
            method: "post",
            dataType: "json",
            data: {"name": name, "email": email, "phone": phone, "password": password},
            success: function(result) {
                alert(result.status);
                if(result.code == 1)
                  location.href = "/login";
            }
          });
        } else {
          alert("Passwords do not match!");
        }

      } else {
        alert("Complete the form!");
      }
  })

});
