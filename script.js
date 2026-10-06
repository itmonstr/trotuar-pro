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
if (form) {
form.addEventListener('submit', async event => {
  event.preventDefault();
  const data = new FormData(form);
  const message = `Здравствуйте! Меня зовут ${data.get('name')}.\nТелефон: ${data.get('phone')}\nЗадача: ${data.get('task')}\nПрошу связаться со мной для расчёта стоимости.`;
  const result = document.querySelector('#request-result');
  const resultMessage = document.querySelector('#request-result-message');
  const text = document.querySelector('#request-text');
  const button = form.querySelector('button[type="submit"]');
  button.disabled = true;
  button.classList.add('is-loading');
  try {
    const response = await fetch(form.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
    const payload = await response.json();
    if (!response.ok || !payload.ok) throw new Error(payload.error || 'Не удалось отправить заявку');
    resultMessage.textContent = 'Заявка отправлена. Мы свяжемся с вами в ближайшее время.';
    text.hidden = true;
    result.hidden = false;
    form.reset();
  } catch (error) {
    resultMessage.textContent = 'Сайт пока работает в тестовом режиме. Скопируйте заявку и отправьте её нам.';
    text.value = message;
    text.hidden = false;
    result.hidden = false;
  } finally {
    button.disabled = false;
    button.classList.remove('is-loading');
  }
});
document.querySelector('.copy-button').addEventListener('click', async event => {
  try { await navigator.clipboard.writeText(document.querySelector('#request-text').value); event.currentTarget.textContent = 'Скопировано'; }
  catch { document.querySelector('#request-text').select(); event.currentTarget.textContent = 'Выделено — скопируйте текст'; }
});
}
