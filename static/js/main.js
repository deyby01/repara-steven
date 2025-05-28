// static/js/main.js
const navToggle = document.querySelector('.nav-toggle');
const mainNav = document.querySelector('.main-navigation');
const body = document.body; // Para la clase .nav-open en body

if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => {
        // Alterna la clase en el body para los estilos de X y mostrar/ocultar nav
        body.classList.toggle('nav-open');

        // También podrías alternar una clase directamente en mainNav si prefieres
        // mainNav.classList.toggle('active');
    });
}