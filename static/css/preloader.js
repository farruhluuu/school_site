window.addEventListener('load', function() {
    var preloader = document.querySelector('.preloader');
    preloader.classList.add('hide');
  });
  window.addEventListener('load', () => {
    const preloader = document.querySelector('#preloader');
    preloader.classList.add('fadeout');
    setTimeout(() => preloader.remove("fadeout"), 20000);
})