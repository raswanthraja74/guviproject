function validate() {
    $.ajax({
        url: '/register.html',
        method: 'POST',
        data: {
            'username': $("#username"),
            'number': $("#number"),
            'email': $("#email"),
            'password': $("#password")
        },
        success: function (response) {
            window.location = response.text;
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}