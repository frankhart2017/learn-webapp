$(document).ready(function() {

  $("#login").click(function() {

      var email = $("#email").val();
      var password = $("#password").val();

      if(email != "" && password != "") {

          $.ajax({
            url: "/login",
            type: "post",
            dataType: "json",
            data: {"email": email, "password": password},
            success: function(result) {
              alert(result.status);
              if(result.code == 1)
                location.href = "/";
            }
          });

      } else {
        alert("Complete the form!");
      }

  });
  
});
