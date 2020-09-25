 $(function () {

                'use strict';

                var winH = $(window).height();

                $('header').height(winH);

                $('header .container > div').css('top', (winH / 2) - ( $('header .container > div').height() / 2));

                $('.navbar ul li a.search').on('click', function (e) {
                    e.preventDefault();
                });
                $('.navbar a.search').on('click', function () {
                    $('.navbar form').fadeToggle();
                });

                $('.navbar ul.navbar-nav li a').on('click', function (e) {

                    var getAttr = $(this).attr('href');

                    e.preventDefault();
                    $('html').animate({scrollTop: $(getAttr).offset().top}, 1000);
                });
            })