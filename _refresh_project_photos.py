"""Refresh photo markup from original files without changing case descriptions.
Embedded black borders are hidden in CSS; original files stay untouched.
Run after the service generator when rebuilding the paving page.
"""
from pathlib import Path
import re, shutil, json
from PIL import Image, ImageStat
from bs4 import BeautifulSoup
ROOT = Path(__file__).parent
SOURCE = ROOT.parent / 'проекты'
SELECTION = {
 'kultura': ('01', [1,7,9,6]), 'safari': ('02', [6,5,3,9]),
 'large-format': ('03', [7,6,10,1]), 'old-town': ('04', [6,7]),
 'pavers-120': ('05', [4,5,3]), 'pavers-80': ('06', [9,8,1,7,11]),
 'private-yard': ('10', [5,1,6,2]), 'parquet': ('11', [1,2,3,4,5]),
 'gas-station': ('12', [7,6,8,2]),
}
EDITED = {
 ('safari', 6): 'safari-cleaned.webp',
 ('safari', 5): 'safari-cleaned-05.webp',
 ('safari', 3): 'safari-cleaned-03.webp',
 ('safari', 9): 'safari-cleaned-09.webp',
 ('large-format', 7): 'large-format-cleaned-07.webp',
 ('large-format', 6): 'large-format-cleaned-06.webp',
 ('large-format', 10): 'large-format-cleaned-10.webp',
 ('large-format', 1): 'large-format-cleaned-01.webp',
 ('old-town', 7): 'old-town-cleaned-07.webp',
 ('pavers-120', 4): 'pavers-120-cleaned-04.webp',
 ('pavers-120', 5): 'pavers-120-cleaned-05.webp',
 ('pavers-120', 3): 'pavers-120-cleaned-03.webp',
 ('pavers-80', 9): 'pavers-80-cleaned-09.webp',
 ('pavers-80', 8): 'pavers-80-cleaned-08.webp',
 ('pavers-80', 1): 'pavers-80-cleaned-01.webp',
 ('pavers-80', 7): 'pavers-80-cleaned-07.webp',
 ('pavers-80', 11): 'pavers-80-cleaned-11.webp',
 ('gas-station', 7): 'gas-station-cleaned-07.webp',
 ('gas-station', 6): 'gas-station-cleaned-06.webp',
 ('gas-station', 8): 'gas-station-cleaned-08.webp',
 ('gas-station', 2): 'gas-station-cleaned-02.webp',
 ('private-yard', 5): 'private-yard-cleaned-05.webp',
 ('private-yard', 1): 'private-yard-cleaned-01.webp',
 ('private-yard', 6): 'private-yard-cleaned-06.webp',
 ('private-yard', 2): 'private-yard-cleaned-02.webp',
 ('parquet', 1): 'parquet-cleaned-01.webp',
 ('parquet', 2): 'parquet-cleaned-02.webp',
 ('parquet', 3): 'parquet-cleaned-03.webp',
 ('parquet', 4): 'parquet-cleaned-04.webp',
 ('parquet', 5): 'parquet-cleaned-05.webp',
}
META = {}
for slug,(prefix,numbers) in SELECTION.items():
    folder = next(SOURCE.glob(prefix+'_*'))
    dest = ROOT/'test/assets/projects'/slug
    dest.mkdir(parents=True,exist_ok=True)
    for n in numbers:
        src = folder/f'photo_{n:02}.jpg'
        shutil.copyfile(src,dest/f'original_{n:02}.jpg')
        with Image.open(src) as im:
            w,h=im.size
            small=im.convert('RGB').resize((96,h))
            rows=[y for y in range(h) if max(ImageStat.Stat(small.crop((0,y,96,y+1))).mean)>6]
            top,bottom=rows[0],rows[-1]+1
            if top<8: top=0
            if h-bottom<8: bottom=h
        META[slug,n]=dict(width=w,height=h,top=top,visible=bottom-top,source=str(src.relative_to(SOURCE)))

def photo(soup,slug,n,alt,prefix=''):
    m=META[slug,n]
    edited_name = EDITED.get((slug,n))
    edited = bool(edited_name and (ROOT/'test/assets/projects'/slug/edited_name).exists())
    filename = edited_name if edited else f'original_{n:02}.jpg'
    if edited:
        with Image.open(ROOT/'test/assets/projects'/slug/filename) as im:
            width,height=im.size
        ratio=width/height; top=0; visible=height
    else:
        width,height=m['width'],m['height']; ratio=width/m['visible']; top=m['top']; visible=m['visible']
    frame=soup.new_tag('button',type='button')
    frame['class']='photo-window'
    frame['aria-label']='Увеличить: '+alt
    frame['style']=(f'--photo-ratio:{ratio:.7f};--photo-max-width:{width}px;'
                    f'--photo-top:{-top/visible*100:.7f}%;'
                    f'--photo-height:{height/visible*100:.7f}%')
    frame.append(soup.new_tag('img',src=f'{prefix}assets/projects/{slug}/{filename}',
        alt=alt,width=str(width),height=str(height),loading='lazy',decoding='async'))
    return frame

def curate(match):
    soup=BeautifulSoup(match.group(0),'html.parser')
    slug=soup.article['aria-labelledby'].removeprefix('project-')
    numbers=SELECTION[slug][1]
    track=soup.select_one('.project-track'); track.clear()
    for i,n in enumerate(numbers,1):
        slide=soup.new_tag('div',role='group')
        slide['class']='project-slide'; slide['aria-label']=f'Фото {i} из {len(numbers)}'
        edited_name = EDITED.get((slug,n))
        preview = edited_name if edited_name and (ROOT/'test/assets/projects'/slug/edited_name).exists() else f'original_{n:02}.jpg'
        slide['style']=f'--photo-preview:url("assets/projects/{slug}/{preview}")'
        slide.append(photo(soup,slug,n,soup.h3.get_text()+f' — фото {i}'))
        track.append(slide)
    first_edited = EDITED.get((slug,numbers[0]))
    if first_edited and (ROOT/'test/assets/projects'/slug/first_edited).exists():
        with Image.open(ROOT/'test/assets/projects'/slug/first_edited) as im:
            gallery_ratio=im.width/im.height
    else:
        m=META[slug,numbers[0]]; gallery_ratio=m['width']/m['visible']
    soup.select_one('.project-gallery')['style']=f'--gallery-ratio:{gallery_ratio:.7f}'
    soup.select_one('.project-photo-label').string=f'{len(numbers)} фото · нажмите для увеличения'
    soup.select_one('.project-counter').string=f'01 / {len(numbers):02}'
    return str(soup)

def assets(html,prefix=''):
    html=re.sub(r'\s*<link[^>]+href="[^\"]*photo-presentation.css[^\"]*"[^>]*>','',html)
    html=re.sub(r'\s*<script[^>]+src="[^\"]*photo-viewer.js[^\"]*"[^>]*></script>','',html)
    html=html.replace('</head>',f'  <link rel="stylesheet" href="{prefix}photo-presentation.css?v=1">\n</head>')
    return html.replace('</body>',f'  <script src="{prefix}photo-viewer.js?v=1" defer></script>\n</body>')

for name in ['index.html','projects.html']:
    p=ROOT/'test'/name; html=p.read_text(encoding='utf-8')
    html=re.sub(r'<article\b(?=[^>]*class="project-card")[^>]*>.*?</article>',curate,html,flags=re.S)
    html=html.replace('assets/projects/kultura/photo_07.webp','assets/projects/kultura/original_07.jpg')
    p.write_text(assets(html),encoding='utf-8')

p=ROOT/'test/services/ukladka-plitki.html'
html=p.read_text(encoding='utf-8')
def panel(match):
    soup=BeautifulSoup(match.group(0),'html.parser'); img=soup.find('img')
    slug=img['src'].split('/')[-2]
    n=int(re.search(r'(?:photo|original)_(\d+)',img['src'])[1])
    replacement=photo(soup,slug,n,img.get('alt','Готовое мощение'),'../')
    (soup.select_one('.photo-window') or img).replace_with(replacement)
    return str(soup)
html=re.sub(r'<div class="paver-panel".*?</div></div>',panel,html,flags=re.S)
html=html.replace('В каталоге — шесть проектов','В каталоге — девять проектов')
p.write_text(assets(html,'../'),encoding='utf-8')
report={f'{slug}/original_{n:02}.jpg':m for (slug,n),m in META.items()}
(ROOT/'test/assets/projects/photo-sources.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Curated {len(META)} original photographs across {len(SELECTION)} projects.')
