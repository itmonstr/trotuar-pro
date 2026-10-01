"""Keep the selected finished-project photos in both test galleries."""
from pathlib import Path
import re
from bs4 import BeautifulSoup

SELECTION = {
    'kultura': [1, 7, 9, 6, 3],
    'safari': [6, 8, 5, 3, 9],
    'large-format': [7, 6, 10, 1],
    'old-town': [6, 7],
    'pavers-80': [9, 8, 1, 7],
    'pavers-120': [4, 5],
}

def curate(match):
    card = BeautifulSoup(match.group(0), 'html.parser')
    article = card.find('article')
    slug = article['aria-labelledby'].removeprefix('project-')
    track = card.select_one('.project-track')
    slides = {Path(s.img['src']).name: s for s in track.select('.project-slide')}
    selected = SELECTION[slug]
    track.clear()
    for index, number in enumerate(selected, 1):
        slide = slides[f'photo_{number:02d}.webp']
        slide['aria-label'] = f'Фото {index} из {len(selected)}'
        slide.img['alt'] = card.h3.get_text() + f' — готовое покрытие, фото {index}'
        track.append(slide)
    card.select_one('.project-photo-label').string = f'{len(selected)} фото объекта'
    card.select_one('.project-counter').string = f'01 / {len(selected):02d}'
    return str(card)

root = Path(__file__).parent / 'test'
for filename in ['index.html', 'projects.html']:
    path = root / filename
    html = path.read_text(encoding='utf-8')
    html = re.sub(r'<article\b(?=[^>]*class="project-card")[^>]*>.*?</article>', curate, html, flags=re.S)
    html = html.replace('Реальные объекты, фотографии процесса и готового покрытия.', 'Реальные объекты и фотографии готового покрытия.')
    html = re.sub(r'\s*<script src="project-process\.js"></script>', '', html)
    path.write_text(html, encoding='utf-8')
print('Updated project galleries with 22 selected finished photos.')
