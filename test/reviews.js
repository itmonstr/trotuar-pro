document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('.reviews-track');
  
  if (track) {
    // Drag-to-scroll logic
    let isDown = false;
    let startX;
    let scrollLeft;
    let dragged = false;

    track.addEventListener('mousedown', (e) => {
      isDown = true;
      dragged = false;
      track.classList.add('active');
      startX = e.pageX - track.offsetLeft;
      scrollLeft = track.scrollLeft;
      // Отключаем плавную прокрутку при перетаскивании для мгновенного отклика
      track.style.scrollBehavior = 'auto';
    });

    track.addEventListener('mouseleave', () => {
      isDown = false;
      track.classList.remove('active');
      track.style.scrollBehavior = 'smooth';
    });

    track.addEventListener('mouseup', () => {
      isDown = false;
      track.classList.remove('active');
      track.style.scrollBehavior = 'smooth';
    });

    track.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - track.offsetLeft;
      const walk = (x - startX) * 2; // Множитель скорости прокрутки
      
      if (Math.abs(walk) > 5) {
        dragged = true; // Если мышь сдвинулась, значит это драг, а не клик
      }
      
      track.scrollLeft = scrollLeft - walk;
    });

    // Lightbox
    const reviewCards = document.querySelectorAll('.review-card');
    if (reviewCards.length > 0) {
      // Create lightbox HTML
      const lightboxHtml = `
        <div class="lightbox-modal">
          <button class="lightbox-close">&times;</button>
          <img src="" alt="Увеличенный отзыв">
        </div>
      `;
      document.body.insertAdjacentHTML('beforeend', lightboxHtml);
      
      const lightbox = document.querySelector('.lightbox-modal');
      const lightboxImg = lightbox.querySelector('img');
      const closeBtn = lightbox.querySelector('.lightbox-close');

      reviewCards.forEach(card => {
        card.addEventListener('click', (e) => {
          // Если мы только что перетаскивали ленту, не открываем лайтбокс
          if (dragged) {
            e.preventDefault();
            return;
          }
          
          const img = card.querySelector('img');
          if (img) {
            lightboxImg.src = img.src;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
          }
        });
      });

      const closeModal = () => {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
      };

      closeBtn.addEventListener('click', closeModal);
      lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeModal();
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) closeModal();
      });
    }
  }
});
