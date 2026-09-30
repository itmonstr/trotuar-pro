document.querySelectorAll('.project-gallery').forEach(gallery => {
  const track = gallery.querySelector('.project-track');
  const count = track.children.length;
  const counter = gallery.querySelector('.project-counter');
  const progress = gallery.querySelector('.project-progress span');
  let targetIndex = 0;
  let settleTimer;

  const currentIndex = () => Math.max(0, Math.min(count - 1,
    Math.round(track.scrollLeft / Math.max(track.clientWidth, 1))));
  const update = () => {
    const index = currentIndex();
    counter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(count).padStart(2, '0')}`;
    progress.style.width = `${((index + 1) / count) * 100}%`;
  };
  const move = direction => {
    targetIndex = (targetIndex + direction + count) % count;
    track.scrollTo({
      left: targetIndex * track.clientWidth,
      behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'
    });
  };
  gallery.querySelector('.project-prev').addEventListener('click', () => move(-1));
  gallery.querySelector('.project-next').addEventListener('click', () => move(1));
  track.addEventListener('keydown', event => {
    if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
    event.preventDefault();
    move(event.key === 'ArrowLeft' ? -1 : 1);
  });
  track.addEventListener('scroll', () => {
    update();
    clearTimeout(settleTimer);
    settleTimer = setTimeout(() => { targetIndex = currentIndex(); }, 150);
  }, { passive: true });
  track.addEventListener('scrollend', () => { targetIndex = currentIndex(); });
  new ResizeObserver(() => {
    track.scrollTo({ left: targetIndex * track.clientWidth, behavior: 'instant' });
    update();
  }).observe(track);
  update();
});
