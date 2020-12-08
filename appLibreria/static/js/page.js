var slideIndex;
var slides;

$(document).ready(function () {
    getPagina();
});

function getPagina() {
    slideIndex = parseInt($('#content .img-gl').attr('alt'));
    slides = parseInt($('#slide').text());
    if (slideIndex == 0){
        $('.prev').css('pointer-events', 'none');
    }if (slideIndex == slides) {
        $('.next').css('pointer-events', 'none');
    }
}

function plusSlides(n) {
  slideIndex += n;
  showSlides(slideIndex);
}
function showSlides(n) {
    slides = parseInt($('#slide').text());
    if (n == slides) {
        $('.next').css('pointer-events', 'none');
    } else if (n < 0) {
        $('.prev').css('pointer-events', 'none');
    } else {
        changeURL(n);
        $('.prev').css('pointer-events', 'auto');
        $('.next').css('pointer-events', 'auto');
    }
    
}
function changeURL(n) {
    var theURL = window.location.pathname.split('/');
    window.location.replace("http://127.0.0.1:8000/appLibreria/comic/" + theURL[3] + "/" + n + "/" );
}

