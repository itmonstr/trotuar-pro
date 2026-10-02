(() => {
  const card = document.querySelector('[aria-labelledby="project-pavers-120"]');
  if (!card) return;
  const gallery = card.querySelector('.project-gallery');
  const track = gallery.querySelector('.project-track');
  // Pair the prepared area with its finished view, then end on the wide shot.
  const frames = [
    ['photo_02.webp', 'Основание вокруг бассейна'],
    ['photo_01.webp', 'Подготовленная площадка'],
    ['photo_06.webp', 'Площадка после мощения'],
    ['photo_05.webp', 'Готовая дорожка у бассейна'],
    ['photo_03.webp', 'Покрытие у дома'],
    ['photo_04.webp', 'Результат · 120 м² за 4 дня']
  ].map(([file, title]) => ({
    src: [...track.querySelectorAll('img')].find(img => img.getAttribute('src').endsWith(file)).getAttribute('src'),
    title
  }));
  const layer = document.createElement('div');
  layer.className = 'process-player';
  layer.hidden = true;
  layer.innerHTML = '<img class="process-frame" alt=""><img class="process-frame" alt=""><div class="process-player-caption"><span class="process-stage"></span><div class="process-timeline" aria-hidden="true">' + frames.map(() => '<i></i>').join('') + '</div></div>';
  gallery.append(layer);
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'process-play';
  toggle.innerHTML = '<span class="process-play-icon" aria-hidden="true">▶</span><span class="process-play-label">Как это было</span>';
  toggle.setAttribute('aria-label', 'Посмотреть процесс мощения у бассейна');
  toggle.setAttribute('aria-pressed', 'false');
  gallery.append(toggle);
  gallery.classList.add('has-process');
  const icon = toggle.querySelector('.process-play-icon');
  const label = toggle.querySelector('.process-play-label');
  const pictures = [...layer.querySelectorAll('img')];
  const caption = layer.querySelector('.process-stage');
  const steps = [...layer.querySelectorAll('.process-timeline i')];
  let frame = 0;
  let activePicture = 0;
  let playing = false;
  let started = false;
  let finished = false;
  let timer;
  let requestId = 0;

  function buttonState() {
    gallery.classList.toggle('process-is-playing', playing);
    toggle.setAttribute('aria-pressed', String(playing));
    icon.textContent = playing ? 'Ⅱ' : finished ? '↻' : '▶';
    label.textContent = playing ? 'Пауза' : finished ? 'Посмотреть ещё раз' : started ? 'Продолжить' : 'Как это было';
    toggle.setAttribute('aria-label', playing ? 'Приостановить показ процесса' : finished ? 'Повторить показ процесса' : started ? 'Продолжить показ процесса' : 'Посмотреть процесс мощения у бассейна');
  }
  function pause() {
    playing = false;
    clearTimeout(timer);
    buttonState();
  }
  async function show(index) {
    const id = ++requestId;
    const nextPicture = pictures[1 - activePicture];
    nextPicture.src = frames[index].src;
    nextPicture.alt = frames[index].title + ' — Брусчатка у бассейна';
    try { await nextPicture.decode(); } catch {
      if (id === requestId) { close(); label.textContent = 'Повторить показ'; }
      return;
    }
    if (id !== requestId) return;
    pictures[activePicture].classList.remove('is-visible');
    pictures[activePicture].setAttribute('aria-hidden', 'true');
    nextPicture.classList.add('is-visible');
    nextPicture.removeAttribute('aria-hidden');
    activePicture = 1 - activePicture;
    frame = index;
    caption.textContent = `${String(index + 1).padStart(2, '0')} / 06 — ${frames[index].title}`;
    steps.forEach((step, i) => step.classList.toggle('is-complete', i <= index));
    if (playing) schedule();
  }
  function schedule() {
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (frame === frames.length - 1) {
        finished = true;
        pause();
      } else show(frame + 1);
    }, 2600);
  }
  function close() {
    ++requestId;
    pause();
    started = false;
    finished = false;
    layer.hidden = true;
    gallery.classList.remove('process-is-active');
    buttonState();
  }
  toggle.addEventListener('click', () => {
    if (playing) return pause();
    playing = true;
    layer.hidden = false;
    gallery.classList.add('process-is-active');
    if (!started || finished) {
      started = true;
      finished = false;
      show(0);
    } else schedule();
    buttonState();
  });
  gallery.querySelectorAll('.project-prev, .project-next').forEach(button => button.addEventListener('click', close));
  track.addEventListener('pointerdown', close);
  track.addEventListener('keydown', event => {
    if (['ArrowLeft', 'ArrowRight', 'Escape'].includes(event.key)) close();
  });
  gallery.addEventListener('keydown', event => {
    if (event.key === 'Escape') close();
  });
  document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });
  new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting && playing) pause();
  }).observe(gallery);
})();
