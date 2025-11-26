

//  No toquen esto!! Importa la librería e inicia la función!
(function loadScrollReveal() {
  const script = document.createElement("script");
  script.src = "https://unpkg.com/scrollreveal";
  script.onload = iniciarAnimaciones;
  document.head.appendChild(script);
})();



/*
Adentro de la función pueden ir agregando más ScrollReveal().reveal(clase,{...});
Dejé las mismas que en el ejemplo que les pasé (y un par más ) para que sea más evidente
y puedan jugar con las variables tranquilamente.
*/

function iniciarAnimaciones() {

    //clase ".card"
    ScrollReveal().reveal('.card', {
        origin: 'bottom',
        distance: '40px',
        duration: 700,
        interval: 120,
        reset: false
    });

ScrollReveal().reveal('.button1', {
    origin: 'bottom',
    distance: '15px',
    duration: 1200,
    opacity: 0,
    easing: 'ease-out',
    interval: 120,
    reset: false
});




    /*

    //clase ".box"
    ScrollReveal().reveal('.box', {
        origin: 'left',
        distance: '80px',
        duration: 500,
        delay: 100,
        opacity: 0,
        scale: 0.5,
        easing: 'cubic-bezier(0.5, 0, 0, 1)',
        interval: 120,
        reset: true
    });

    //clase ".item"
    ScrollReveal().reveal('.item', {
        origin: 'right',
        distance: '60px',
        duration: 800,
        rotate: { x: 0, y: 45, z: 0 },
        viewFactor: 0.3,
        mobile: true,
        desktop: true
    });
    
    //clase ".texto"
    ScrollReveal().reveal('.texto', {
        opacity: 0,
        scale: 0.9,
        duration: 500,
        easing: 'ease-in-out',
        delay: 200
    });
     */
}