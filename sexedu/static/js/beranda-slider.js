$(document).ready(function() {
    var swiper = new Swiper('.js-review-slider', {
        slidesPerView: 1,
        spaceBetween: 30,
        pagination: {
            el: '.js-review-pagination',
            clickable: true,
        },
        breakpoints: {
            767: {
                slidesPerView: 2,
            }
        }
    });
});
