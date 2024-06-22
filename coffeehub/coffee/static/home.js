$(document).ready(function() {
    $("#buyButton").click(function() {
        console.log("Button clicked");
        $.ajax({
            url: "{% url 'check_authentication' %}",
            type: "GET",
            success: function(response) {
                if (response.authenticated) {
                    window.location.href = "{% url 'Buy' %}";
                } else {
                    alert("Please sign in to proceed with the purchase.");
                    // You can also redirect the user to the sign-in page instead of showing an alert
                    // window.location.href = "{% url 'SignIn' %}";
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});
