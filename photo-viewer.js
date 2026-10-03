(() => {
  const dialog = document.createElement('dialog');
  dialog.className = 'photo-dialog';
  dialog.setAttribute('aria-label', 'Фотография проекта');
  const close = document.createElement('button');
  close.className = 'photo-dialog-close';
  close.type = 'button';
  close.textContent = 'Закрыть ×';
  const content = document.createElement('div');
  dialog.append(close, content);
  document.body.append(dialog);
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  document.querySelectorAll('button.photo-window').forEach(button => {
    button.addEventListener('click', () => {
      const frame = document.createElement('div');
      frame.className = 'photo-window';
      frame.style.cssText = button.style.cssText;
      const img = button.querySelector('img').cloneNode();
      img.loading = 'eager';
      frame.append(img);
      const caption = document.createElement('p');
      caption.className = 'photo-dialog-caption';
      caption.textContent = img.alt;
      content.replaceChildren(frame, caption);
      dialog.showModal();
    });
  });
})();
