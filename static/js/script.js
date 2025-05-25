document.addEventListener('DOMContentLoaded', function () {
  const trigger = document.querySelector('.select-trigger');
  const options = document.querySelector('.custom-options');
  const hiddenInput = document.getElementById('order-input');

  trigger.addEventListener('click', function (e) {
    e.stopPropagation();
    options.classList.toggle('show');
  });

  document.querySelectorAll('.custom-options span').forEach(option => {
    option.addEventListener('click', function () {
      trigger.textContent = this.textContent;
      hiddenInput.value = this.dataset.value;
      options.classList.remove('show');
    });
  });

  document.addEventListener('click', function (e) {
    if (!document.getElementById('custom-select').contains(e.target)) {
      options.classList.remove('show');
    }
  });
});
const stars = document.querySelectorAll('.star');

function loadRating() {
  const saved = localStorage.getItem('rating');
  if (saved) {
    stars.forEach((s, i) => {
      s.classList.toggle('glow', i < parseInt(saved));
    });
  }
}

stars.forEach(star => {
  star.addEventListener('click', () => {
    const rating = parseInt(star.getAttribute('data-value'));
    localStorage.setItem('rating', rating);
    stars.forEach((s, i) => {
      s.classList.toggle('glow', i < rating);
    });
  });
});

loadRating();

const input = document.getElementById('smartInput');

input.addEventListener('input', () => {
  let val = input.value;
  val = val.replace(/(^\w{1}|\.\s*\w{1})/g, match => match.toUpperCase());
  input.value = val;
});
const onput = document.getElementById('smartInput');




