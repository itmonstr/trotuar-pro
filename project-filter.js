const filterButtons = [...document.querySelectorAll('.project-filters [data-filter]')];
const filterCards = [...document.querySelectorAll('.projects-grid .project-card')];

function setProjectFilter(category) {
  const selected = filterButtons.some(button => button.dataset.filter === category) ? category : 'all';
  filterButtons.forEach(button => {
    const active = button.dataset.filter === selected;
    button.classList.toggle('is-active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  filterCards.forEach(card => { card.hidden = selected !== 'all' && card.dataset.category !== selected; });
  const url = new URL(window.location.href);
  if (selected === 'all') url.searchParams.delete('category');
  else url.searchParams.set('category', selected);
  history.replaceState(null, '', url);
}

filterButtons.forEach(button => button.addEventListener('click', () => setProjectFilter(button.dataset.filter)));
if (filterButtons.length) setProjectFilter(new URLSearchParams(window.location.search).get('category') || 'all');
