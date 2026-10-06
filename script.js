const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
if (menuButton && nav) {
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
}

const form = document.querySelector('#request-form');
if (form) {
  const phone = form.elements.phone;
  const status = document.querySelector('#request-status');
  const submitButton = form.querySelector('button[type="submit"]');
  const contactOptions = form.querySelectorAll('input[name="contact_method"]');

  const validatePhone = () => {
    const digits = phone.value.replace(/\D/g, '');
    const valid = digits.length === 11 && /^[78]/.test(digits);
    phone.setCustomValidity(valid || !phone.value ? '' : 'Введите российский номер из 11 цифр, например +7 999 123-45-67');
    return valid;
  };

  const updateContactFields = () => {
    const selected = form.querySelector('input[name="contact_method"]:checked').value;
    form.querySelectorAll('.contact-extra').forEach(label => {
      const active = label.dataset.method === selected;
      const input = label.querySelector('input');
      label.hidden = !active;
      input.disabled = !active;
      input.required = active;
    });
    status.hidden = true;
  };

  phone.addEventListener('input', () => {
    phone.setCustomValidity('');
    if (phone.value.replace(/\D/g, '').length >= 11) validatePhone();
  });
  phone.addEventListener('blur', validatePhone);
  contactOptions.forEach(option => option.addEventListener('change', updateContactFields));
  updateContactFields();

  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (!validatePhone() || !form.reportValidity()) {
      form.reportValidity();
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = 'Отправляем…';
    status.hidden = true;

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      });
      const result = await response.json();
      if (!response.ok || !result.ok) throw new Error(result.error || 'Не удалось отправить заявку. Попробуйте ещё раз.');
      form.reset();
      updateContactFields();
      phone.setCustomValidity('');
      status.textContent = 'Заявка отправлена. Скоро свяжемся с вами.';
      status.dataset.state = 'success';
    } catch (error) {
      status.textContent = error.message || 'Не удалось отправить заявку. Попробуйте ещё раз.';
      status.dataset.state = 'error';
    } finally {
      status.hidden = false;
      submitButton.disabled = false;
      submitButton.textContent = 'Отправить';
    }
  });
}
