
let header__burger = document.querySelector('.header__burger');
let header_menu = document.querySelector('.header__menu');
let header_logo = document.querySelector('.header__logo');
let body = document.getElementById('body');
let header__list = document.querySelector('.header__list');

header__burger.onclick = function(){
    header__burger.classList.toggle('active');
    header_menu.classList.toggle('active');
    header_logo.classList.toggle('active');
    body.classList.toggle('lock');
}

// При клике на кнопку "Получить бесплатную консультацию"
document.getElementById("consultation-btn").addEventListener("click", function() {
    document.getElementById("client-form").style.display = "block";
});


document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('bidsForm2');
    const numberInput = document.querySelector('.tour__info-primary-text input[type="number"]');
    const modal = document.getElementById('client-form');
    const closeModalButton = document.getElementById('closeModal');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        formData.append('number_of_people', numberInput.value);
        
        fetch('/submit-form/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            modal.style.display = 'none';
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    });

    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none';
     });
});