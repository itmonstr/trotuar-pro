from html import escape
from pathlib import Path

OUT = Path(__file__).parent / 'test' / 'services'
OUT.mkdir(exist_ok=True)

SERVICES = [
    {
        'slug': 'ukladka-plitki',
        'title': 'Укладка тротуарной плитки и брусчатки',
        'lead': 'Мощение дворов, дорожек и площадок. Подготовка основания — часть работы по укладке, а вид покрытия выбираем под запрос и особенности участка.',
        'section_title': 'Что входит в работу',
        'section_lead': 'Точный состав определяем после осмотра участка и согласования покрытия.',
        'items': [
            ('Осмотр участка', 'Оцениваем площадь, состояние грунта, перепады и будущую нагрузку.'),
            ('Подготовка основания', 'Подготавливаем участок и основание перед укладкой покрытия.'),
            ('Укладка покрытия', 'Укладываем выбранную плитку или брусчатку с учётом рисунка и примыканий.'),
            ('Сдача результата', 'Проверяем готовое покрытие вместе с заказчиком.'),
        ],
        'related': [('Бетонирование дворов', 'betonirovanie-dvorov.html'), ('Уход за плиткой', 'uhod-za-plitkoy.html')],
    },
    {
        'slug': 'betonirovanie-dvorov',
        'title': 'Бетонирование дворов',
        'lead': 'Устройство бетонного покрытия во дворе и на площадках. Решение подбираем по условиям участка и назначению будущей поверхности.',
        'section_title': 'Как подходим к задаче',
        'section_lead': 'Объём подготовки и устройство покрытия определяем для конкретного объекта.',
        'items': [
            ('Осмотр и замер', 'Уточняем площадь, состояние участка и назначение площадки.'),
            ('Подготовка', 'Согласуем необходимую подготовку перед бетонными работами.'),
            ('Бетонирование', 'Выполняем работы по согласованному решению и объёму.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Благоустройство участка', 'blagoustroystvo-uchastka.html')],
    },
    {
        'slug': 'uhod-za-plitkoy',
        'title': 'Уход за тротуарной плиткой',
        'lead': 'Помогаем поддерживать мощёное покрытие в порядке между сезонами. Состав работ зависит от состояния плитки и швов.',
        'section_title': 'Что можем сделать',
        'section_lead': 'Состав работ подбираем по состоянию покрытия и ваших задач.',
        'items': [
            ('Мойка плитки', 'Очищаем поверхность покрытия.'),
            ('Гидрофобная пропитка', 'Наносим гидрофобный состав на плитку.'),
            ('Обновление швов', 'Засыпаем швы кварцевым или модифицированным песком.'),
            ('Удаление травы', 'Убираем растительность в швах покрытия.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Все услуги', '../services.html')],
    },
    {
        'slug': 'blagoustroystvo-uchastka',
        'title': 'Благоустройство участка',
        'lead': 'Дренаж, ландшафтное освещение, автоматический полив и укладка газона. Выбирайте нужные работы для вашего участка.',
        'section_title': 'Направления благоустройства',
        'section_lead': 'Каждую задачу обсуждаем с учётом участка и того, какие работы вам нужны.',
        'items': [
            ('Дренаж и отвод воды', 'Система отвода воды с участка. Решение зависит от рельефа и условий на месте.'),
            ('Ландшафтное освещение', 'Световая система для участка под ключ. Размещение света согласуем под задачи территории.'),
            ('Автоматический полив', 'Система полива для озеленения участка. Расположение зависит от плана территории и посадок.'),
            ('Подготовка и укладка газона', 'Подготавливаем основание и укладываем газон. Объём работ зависит от состояния участка.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Бетонирование дворов', 'betonirovanie-dvorov.html')],
    },
]

DETAILS = {
    'ukladka-plitki': {
        'about': 'Работа начинается с осмотра участка и выбора покрытия. Подготовка основания входит в укладку, а брусчатка, широкоформатная плитка и другие варианты подбираются под запрос. После согласования решения можно определить состав работ и стоимость.',
        'photos': ['Готовое покрытие на объекте', 'Процесс укладки'],
        'prices': ['Укладка на готовое основание', 'Укладка с подготовкой основания'],
    },
    'betonirovanie-dvorov': {
        'about': 'Бетонирование подходит для дворов и площадок, где нужно бетонное покрытие. Перед расчётом осматриваем участок, уточняем площадь, назначение поверхности и объём подготовки.',
        'photos': ['Готовый бетонный двор', 'Этап бетонных работ'],
        'prices': ['Подготовка под бетонирование', 'Бетонирование двора'],
    },
    'uhod-za-plitkoy': {
        'about': 'Уход помогает поддерживать готовое мощение в порядке. Выполняем мойку плитки, гидрофобную пропитку, засыпку швов кварцевым или модифицированным песком и удаление травы. Нужные работы выбираем по состоянию покрытия.',
        'photos': ['Покрытие до ухода', 'Покрытие после ухода'],
        'prices': ['Мойка плитки', 'Гидрофобная пропитка', 'Обновление швов', 'Удаление травы'],
    },
    'blagoustroystvo-uchastka': {
        'about': 'В это направление входят четыре задачи: отвод воды с участка, ландшафтное освещение, автоматический полив и подготовка основания с укладкой газона. Их можно обсудить вместе или выбрать отдельные работы.',
        'photos': ['Дренаж и отвод воды', 'Ландшафтное освещение', 'Автоматический полив', 'Уложенный газон'],
        'prices': ['Дренаж и отвод воды', 'Ландшафтное освещение', 'Автоматический полив', 'Подготовка и укладка газона'],
    },
}

PHOTO_DATA = {
    'ukladka-plitki': [
        ('../assets/projects/pavers-120/photo_06.webp', 'Брусчатка у бассейна'),
        ('../assets/projects/large-format/photo_11.webp', 'Широкоформатная плитка'),
        ('../assets/projects/old-town/photo_07.webp', 'Плитка «Старый город»'),
        ('../assets/projects/pavers-80/photo_11.webp', 'Мощение двора'),
    ],
    'betonirovanie-dvorov': [
        (f'../assets/service-demos/concrete-{n}.webp', label)
        for n, label in enumerate(('Подготовка и армирование', 'Заливка бетона', 'Выравнивание поверхности', 'Готовый бетонный двор'), 1)
    ],
    'uhod-za-plitkoy': [
        (f'../assets/service-demos/care-{n}.webp', label)
        for n, label in enumerate(('Мойка плитки', 'Нанесение защитного состава', 'Обновление швов', 'Удаление травы из швов'), 1)
    ],
    'blagoustroystvo-uchastka': [
        (f'../assets/service-demos/landscape-{n}.webp', label)
        for n, label in enumerate(('Устройство дренажа', 'Ландшафтное освещение', 'Автоматический полив', 'Укладка рулонного газона'), 1)
    ],
}

PRICE_DATA = {
    'ukladka-plitki': [
        ('Укладка плитки на готовое основание', 'от 900 ₽/м²'),
        ('Укладка брусчатки на готовое основание', 'от 1 100 ₽/м²'),
        ('Подготовка основания и укладка плитки', 'от 2 200 ₽/м²'),
    ],
    'betonirovanie-dvorov': [
        ('Подготовка основания под бетонирование', 'от 650 ₽/м²'),
        ('Армирование площадки', 'от 450 ₽/м²'),
        ('Бетонирование двора', 'от 1 800 ₽/м²'),
    ],
    'uhod-za-plitkoy': [
        ('Мойка тротуарной плитки', 'от 250 ₽/м²'),
        ('Гидрофобная пропитка', 'от 350 ₽/м²'),
        ('Засыпка и обновление швов', 'от 180 ₽/м²'),
        ('Удаление травы из швов', 'от 150 ₽/м²'),
    ],
    'blagoustroystvo-uchastka': [
        ('Дренаж и отвод воды', 'от 1 500 ₽/пог. м'),
        ('Ландшафтный свет', 'от 3 500 ₽/точка'),
        ('Автоматический полив', 'от 12 000 ₽/зона'),
        ('Подготовка и укладка газона', 'от 750 ₽/м²'),
    ],
}

PAVER_TYPES = [
    ('Брусчатка 100 × 200', '../assets/projects/pavers-120/photo_06.webp', 'Прямоугольный формат для двора, дорожек и зоны у бассейна. Рисунок укладки подбираем под планировку участка.'),
    ('Широкоформатная плитка', '../assets/projects/large-format/photo_11.webp', 'Крупные плиты создают спокойный рисунок покрытия. На одном из наших объектов использован формат 600 × 300 мм.'),
    ('«Старый город»', '../assets/projects/old-town/photo_07.webp', 'Набор элементов разного размера даёт выразительный рисунок мощения. Это покрытие использовано на объекте площадью 200 м².'),
]

def render_paving_special():
    buttons = ''.join(
        f'<button class="paver-choice{" is-active" if i == 0 else ""}" type="button" role="tab" id="paver-tab-{i}" aria-controls="paver-panel-{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span>0{i + 1}</span>{e(name)}<b aria-hidden="true">↗</b></button>'
        for i, (name, _, _) in enumerate(PAVER_TYPES)
    )
    panels = ''.join(
        f'<div class="paver-panel" id="paver-panel-{i}" role="tabpanel" aria-labelledby="paver-tab-{i}"{" hidden" if i else ""}><img src="{e(image)}" alt="Покрытие: {e(name)}" loading="lazy"><div class="paver-panel-copy"><span>Тип покрытия</span><h3>{e(name)}</h3><p>{e(description)}</p></div></div>'
        for i, (name, image, description) in enumerate(PAVER_TYPES)
    )
    return f'''<section class="detail-section" id="coverings"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Варианты покрытия</div><h2>Виды плитки и брусчатки</h2><p>Выберите покрытие слева, чтобы увидеть фотографию и описание. На снимках — материалы из выполненных проектов.</p></div><div class="paver-browser"><div class="paver-choices" role="tablist" aria-label="Виды плитки">{buttons}</div><div class="paver-panels">{panels}</div></div><p class="detail-note">Также можно обсудить уличный керамогранит и клинкерную брусчатку. Покрытие подберём под нагрузку и особенности участка.</p></div></section>
    <section class="detail-section" id="examples"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Реальные объекты</div><h2>Посмотрите результат</h2><p>В каталоге — шесть проектов с фотографиями, площадью и сроками работ.</p></div><a class="button button-lime" href="../projects.html">Смотреть проекты <span aria-hidden="true">↗</span></a></div></section>'''

def e(text):
    return escape(text, quote=True)

def render(service):
    title = e(service['title'])
    detail = DETAILS[service['slug']]
    photo_intro = ('Показываем покрытия на выполненных объектах.' if service['slug'] == 'ukladka-plitki'
                   else 'Посмотрите основные этапы и возможный результат работ.')
    extra_ids = ['drenazh', 'osveshchenie', 'avtopoliv', 'gazon'] if service['slug'] == 'blagoustroystvo-uchastka' else []
    cards = ''
    for i, (name, body) in enumerate(service['items'], 1):
        id_attr = f' id="{extra_ids[i - 1]}"' if extra_ids else ''
        cards += f'<article class="detail-card"{id_attr}><span>{i:02d}</span><h3>{e(name)}</h3><p>{e(body)}</p></article>'
    related = ''.join(f'<a href="{e(href)}">{e(name)} ↗</a>' for name, href in service['related'])
    photos = ''.join(
        f'<figure class="service-photo"><img src="{e(src)}" alt="{e(label)}" loading="lazy"><figcaption><strong>{e(label)}</strong></figcaption></figure>'
        for src, label in PHOTO_DATA[service['slug']]
    )
    prices = ''.join(
        f'<div class="price-row"><span>{e(label)}</span><strong>{e(amount)}</strong></div>'
        for label, amount in PRICE_DATA[service['slug']]
    )
    special = render_paving_special() if service['slug'] == 'ukladka-plitki' else ''
    card_class = 'detail-cards detail-cards-four' if service['slug'] == 'blagoustroystvo-uchastka' else 'detail-cards'
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex, nofollow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#14241f">
  <meta name="description" content="{e(service['lead'])}">
  <title>{title} — Тротуар_Про</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
  <link rel="stylesheet" href="../pages.css">
  <link rel="stylesheet" href="../responsive.css?v=20261001-mobile3">
</head>
<body>
  <header class="site-header" id="top"><div class="container header-inner"><a class="brand" href="../index.html" aria-label="Тротуар Про — на главную"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span>Тротуар<span class="brand-accent">_</span>Про</span></a><nav class="main-nav" id="navigation" aria-label="Основная навигация"><a href="../services.html">Услуги</a><a href="../index.html#technology">Технология</a><a href="../index.html#process">Как работаем</a><a href="../projects.html">Проекты</a></nav><a class="header-cta" href="../index.html#request">Рассчитать стоимость <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-label="Открыть меню" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button></div></header>
  <main>
    <section class="inner-hero service-detail-hero"><div class="container"><a class="service-back" href="../services.html">← Все услуги</a><div class="eyebrow lime"><span class="eyebrow-line"></span> Тротуар_Про</div><h1>{title}</h1><p>{e(service['lead'])}</p></div></section>
    <section class="detail-intro"><div class="container detail-intro-grid"><div><div class="eyebrow"><span class="eyebrow-line"></span> Об услуге</div><h2>Что важно знать</h2></div><p>{e(detail['about'])}</p></div></section>
    <section class="detail-section"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Состав работ</div><h2>{e(service['section_title'])}</h2><p>{e(service['section_lead'])}</p></div><div class="{card_class}">{cards}</div></div></section>
{special}
    <section class="detail-section photo-section"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Фотографии</div><h2>Фотографии и этапы работ</h2><p>{e(photo_intro)}</p></div><div class="service-photo-grid">{photos}</div></div></section>
    <section class="detail-section price-section"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Стоимость</div><h2>Стоимость работ</h2><p>Указаны цены «от». Точную смету составим после осмотра участка и уточнения объёма работ.</p></div><div class="price-list">{prices}</div></div></section>
    <section class="detail-section"><div class="container"><div class="detail-section-head"><h2>Другие направления</h2><p>Соседние работы можно обсудить вместе с основной задачей.</p></div><div class="detail-links">{related}<a href="../services.html">Все услуги ↗</a></div></div></section>
    <section class="inner-cta"><div class="container"><h2>Обсудим ваш участок?</h2><a class="button button-lime" href="../index.html#request">Перейти к заявке <span aria-hidden="true">↗</span></a></div></section>
  </main>
  <footer class="site-footer"><div class="container"><span>© 2026 Тротуар_Про</span><span>Мощение и благоустройство территорий</span><a href="#top">Наверх ↑</a></div></footer>
  <script src="../script.js"></script>
  <script src="../paver-types.js" defer></script>
</body>
</html>
'''

for service in SERVICES:
    (OUT / (service['slug'] + '.html')).write_text(render(service), encoding='utf-8')

# Preserve links to the four earlier test pages while keeping one current page.
LEGACY = {
    'dopolnitelnye-raboty': '',
    'drenazh': 'drenazh',
    'landshaftnoe-osveshchenie': 'osveshchenie',
    'avtopoliv': 'avtopoliv',
    'ukladka-gazona': 'gazon',
}
for slug, anchor in LEGACY.items():
    target = 'blagoustroystvo-uchastka.html' + (f'#{anchor}' if anchor else '')
    (OUT / f'{slug}.html').write_text(
        f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow"><meta http-equiv="refresh" content="0; url={target}"><title>Благоустройство участка — Тротуар_Про</title></head><body><p><a href="{target}">Открыть благоустройство участка</a></p></body></html>\n',
        encoding='utf-8',
    )
