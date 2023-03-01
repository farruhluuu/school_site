function openModal(img) {
    // Получаем элементы модального окна
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
  
    // Отображаем модальное окно
    modal.style.display = "block";
    
    // Устанавливаем изображение в модальном окне
    modalImg.src = img.src;
  }
  
  function closeModal() {
    // Получаем элемент модального окна и скрываем его
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
  }
  