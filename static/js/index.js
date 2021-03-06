$(document).ready(function () {
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();

        var target = this.hash;
        var $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            window.location.hash = target;
        });
        $(".navbar-collapse").collapse('hide');
    });

    $('#support').on('click', function (e) {
        e.preventDefault();

        var target = '#list-holder';
        var $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            window.location = '#list-holder';
        });
        $(".navbar-collapse").collapse('hide');
    });

    $('#sgup').on('click', function (e) {
        window.location = 'http://127.0.0.1:8000/hamyar/signup/';
    });

    $('#help').on('click', function (e) {
        window.location = 'http://127.0.0.1:8000/auth/login/';
    });

    $('#search').on('click', function (e) {
        window.location = 'http://127.0.0.1:8000/search/';
    });

});

