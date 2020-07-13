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



lazyload();


// Gallery Script -- BUG slideIndex CHANGE ONLY ON SECOND CLICK ?? why??

function openModal() {
    document.getElementById("myModal").style.display = "block";
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1


function getIndex() {
    $(".galleryImg").click(function (e) {
        if (e.originalEvent) {
            console.log('user clicked')
        }
        // `this` is the DOM element that was clicked
        var index = $(".galleryImg").index(this);
        slideIndex = index + 1
        return slideIndex
    });
}


function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide() {
    showSlides(slideIndex);
}

getIndex()

function showSlides(n) {
    console.log('current slide is : ' + slideIndex)

    var i;
    var slides = document.getElementsByClassName("mySlides");

    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";

}
showSlides(slideIndex);