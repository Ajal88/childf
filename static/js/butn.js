$(document).ready(function () {
    $('#ext').on('click', function (e) {
        window.location = 'http://127.0.0.1:8000/';
    });
    $('#sgup').on('click', function (e) {
        window.location = 'signup.html';
    });

    $('#help').on('click', function (e) {
       window.location = 'login.html';
    });
});
