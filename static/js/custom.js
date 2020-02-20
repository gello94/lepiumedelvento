//EmailJs 
function sendMail(contactForm) {
    emailjs.send("gmail", "buyit", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "order": contactForm.order.value,
            "enquiry": contactForm.enquiry.value
        })
        .then(
            function (response) {
                var alert = '<div class="alert alert-success" role="alert"> Your message has been sent.You will receive an answer as soon as possible.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            },
            function (error) {
                var alert = '<div class="alert alert-danger" role="alert">Your message was not sent. Please check that all the details are correct.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            }
        );
    return false; // To block from loading a new page
}


//NavBar scroll
var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    if (window.pageYOffset >= 60) {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.getElementById("navbar").style.top = "";
        } else {
            document.getElementById("navbar").style.top = "-60px";
        }
        prevScrollpos = currentScrollPos;
    }
};



// Gallery Script
popup = {
    init: function () {
        $('figure').click(function () {
            popup.open($(this));
            $('.navbar').hide()
            $('figure').removeClass('gallerySizeImg')
        });

        $(document).on('click', '.popup img', function () {
            return false;
        }).on('click', '.popup', function () {
            popup.close();
            $('figure').addClass('gallerySizeImg')
            $('.navbar').show()
        })
    },
    open: function ($figure) {
        $('.gallery').addClass('pop');
        $popup = $('<div class="popup" />').appendTo($('body'));
        $fig = $figure.clone().appendTo($('.popup'));
        $bg = $('<div class="bg" />').appendTo($('.popup'));
        $close = $('<div class="close"><svg><use xlink:href="#close"></use></svg></div>')
            .appendTo($fig);
        $shadow = $('<div class="shadow" />').appendTo($fig);
        src = $('img', $fig).attr('src');
        $shadow.css({
            backgroundImage: 'url(' + src + ')'
        });
        $bg.css({
            backgroundImage: 'url(' + src + ')'
        });
        setTimeout(function () {
            $('.popup').addClass('pop');
        }, 10);
    },
    close: function () {
        $('.gallery, .popup').removeClass('pop');
        setTimeout(function () {
            $('.popup').remove()
        }, 100);
    }
}

popup.init()