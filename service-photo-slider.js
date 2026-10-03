document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-photo-slider]').forEach((slider) => {
    const track = slider.querySelector('.slider-track');
    const previous = slider.querySelector('.prev-btn');
    const next = slider.querySelector('.next-btn');
    const groups = track ? Array.from(track.children) : [];

    if (!track || !previous || !next || groups.length < 2) return;

    let current = 0;
    const viewport = track.parentElement;
    track.style.alignItems = 'flex-start';
    const fitHeight = () => {
      viewport.style.height = `${groups[current].getBoundingClientRect().height}px`;
    };
    const resizeObserver = new ResizeObserver(fitHeight);
    groups.forEach(group => resizeObserver.observe(group));

    const update = () => {
      track.style.transform = `translateX(-${current * 100}%)`;
      previous.disabled = current === 0;
      next.disabled = current === groups.length - 1;
      previous.classList.toggle('disabled', previous.disabled);
      next.classList.toggle('disabled', next.disabled);
      fitHeight();
    };

    previous.addEventListener('click', () => {
      if (current > 0) {
        current -= 1;
        update();
      }
    });

    next.addEventListener('click', () => {
      if (current < groups.length - 1) {
        current += 1;
        update();
      }
    });

    update();
  });
});
