const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Закрыть меню' : 'Открыть меню');
  nav.classList.toggle('is-open', open);
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('is-open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Открыть меню');
}));
const form = document.querySelector('#request-form');
form.addEventListener('submit', event => {
  event.preventDefault();
  const data = new FormData(form);
  const message = `Здравствуйте! Меня зовут ${data.get('name')}.\nТелефон: ${data.get('phone')}\nЗадача: ${data.get('task')}\nПрошу связаться со мной для расчёта стоимости.`;
  document.querySelector('#request-text').value = message;
  document.querySelector('#request-result').hidden = false;
});
document.querySelector('.copy-button').addEventListener('click', async event => {
  try { await navigator.clipboard.writeText(document.querySelector('#request-text').value); event.currentTarget.textContent = 'Скопировано'; }
  catch { document.querySelector('#request-text').select(); event.currentTarget.textContent = 'Выделено — скопируйте текст'; }
});
