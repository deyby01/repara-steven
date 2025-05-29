// static/js/carousel.js
document.addEventListener('DOMContentLoaded', function () {
    var heroSplide = document.querySelector('.hero-section.splide');
    if (heroSplide) {
        new Splide(heroSplide, {
            type       : 'loop', // 'slide', 'loop', or 'fade'
            perPage    : 1,
            autoplay   : true,   // true para que se mueva solo
            interval   : 5000,   // Tiempo en milisegundos entre slides (5 segundos)
            pauseOnHover: true,   // Pausa el autoplay al pasar el mouse
            arrows     : true,   // Muestra flechas de navegación
            pagination : true,   // Muestra los puntos de paginación
            keyboard   : 'global', // Permite navegar con el teclado
            // drag       : true,    // Permite arrastrar con el mouse/dedo
            // gap        : '1rem', // Espacio entre slides si muestras más de uno
        }).mount();
    }
});