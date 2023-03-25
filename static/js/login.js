function validate(){
    $.ajax({
        url: '/login.html',
        method: 'POST',
        data: {
            'username': $("#username"),
            'password': $("#password")
        },
        success: function(response) {
            window.location = response.text;
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
    return false;
}