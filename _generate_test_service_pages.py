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
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Дренаж и отвод воды', 'drenazh.html')],
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
        'slug': 'drenazh',
        'title': 'Дренаж и отвод воды с участка',
        'lead': 'Устройство дренажной системы для отвода воды с участка. Подходящее решение зависит от рельефа и условий на месте.',
        'section_title': 'С чего начинаем',
        'section_lead': 'Перед выбором решения нужно понять, где скапливается вода и куда её можно отвести.',
        'items': [
            ('Обсуждение задачи', 'Уточняем, на каких участках возникает проблема с водой.'),
            ('Осмотр территории', 'Смотрим рельеф и расположение дорожек, площадок и построек.'),
            ('Подбор решения', 'Согласуем систему отвода воды для конкретного участка.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Бетонирование дворов', 'betonirovanie-dvorov.html')],
    },
    {
        'slug': 'landshaftnoe-osveshchenie',
        'title': 'Ландшафтное освещение',
        'lead': 'Световая система для участка под ключ. Размещение света обсуждаем с учётом дорожек, зон отдыха и задач владельца.',
        'section_title': 'Как формируем решение',
        'section_lead': 'Состав системы и расположение света определяем для конкретной территории.',
        'items': [
            ('Задачи освещения', 'Определяем, какие зоны должны быть освещены.'),
            ('План размещения', 'Согласуем расположение элементов световой системы.'),
            ('Реализация', 'Выполняем световую систему под ключ по согласованному решению.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Автоматический полив', 'avtopoliv.html')],
    },
    {
        'slug': 'avtopoliv',
        'title': 'Система автоматического полива',
        'lead': 'Автоматический полив для озеленения участка. Подбираем размещение системы под план территории и посадок.',
        'section_title': 'Что учитываем',
        'section_lead': 'Для расчёта потребуется схема участка и понимание, какие зоны нужно поливать.',
        'items': [
            ('Площадь и зоны', 'Уточняем, какие участки будут поливаться.'),
            ('План системы', 'Согласуем расположение элементов системы полива.'),
            ('Выполнение работ', 'Реализуем систему по согласованному плану.'),
        ],
        'related': [('Укладка газона', 'ukladka-gazona.html'), ('Ландшафтное освещение', 'landshaftnoe-osveshchenie.html')],
    },
    {
        'slug': 'ukladka-gazona',
        'title': 'Подготовка основания и укладка газона',
        'lead': 'Подготавливаем участок под газон и выполняем его укладку. Объём подготовки зависит от состояния территории.',
        'section_title': 'Этапы работы',
        'section_lead': 'Начинаем с участка и согласуем объём работ до укладки.',
        'items': [
            ('Осмотр участка', 'Оцениваем площадь и состояние территории.'),
            ('Подготовка основания', 'Подготавливаем основание под газон.'),
            ('Укладка газона', 'Укладываем газон на подготовленном участке.'),
        ],
        'related': [('Автоматический полив', 'avtopoliv.html'), ('Ландшафтное освещение', 'landshaftnoe-osveshchenie.html')],
    },
]

def e(text):
    return escape(text, quote=True)

def render(service):
    title = e(service['title'])
    cards = ''.join(f'<article class="detail-card"><span>{i:02d}</span><h3>{e(name)}</h3><p>{e(body)}</p></article>' for i, (name, body) in enumerate(service['items'], 1))
    related = ''.join(f'<a href="{e(href)}">{e(name)} ↗</a>' for name, href in service['related'])
    special = ''
    if service['slug'] == 'ukladka-plitki':
        special = '''
    <section class="detail-section" id="coverings"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Варианты покрытия</div><h2>Виды плитки и брусчатки</h2><p>Выбор зависит от задачи и пожеланий заказчика. На фотографиях — материалы из выполненных проектов.</p></div><div class="detail-image-grid">
      <article class="detail-image-card"><img src="../assets/projects/pavers-120/photo_06.webp" alt="Брусчатка 100 на 200 мм у бассейна" loading="lazy"><div><h3>Брусчатка 100 × 200</h3><p>Использована в проектах у бассейна и у дома.</p></div></article>
      <article class="detail-image-card"><img src="../assets/projects/large-format/photo_11.webp" alt="Укладка широкоформатной плитки" loading="lazy"><div><h3>Широкоформатная плитка</h3><p>В каталоге есть объект с форматом 600 × 300 мм.</p></div></article>
      <article class="detail-image-card"><img src="../assets/projects/old-town/photo_07.webp" alt="Плитка Старый город" loading="lazy"><div><h3>«Старый город»</h3><p>Пример покрытия площадью 200 м².</p></div></article>
    </div><p class="detail-note">Также можно обсудить уличный керамогранит и клинкерную брусчатку. Подбор покрытия зависит от запроса и условий участка.</p></div></section>
    <section class="detail-section" id="examples"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Реальные объекты</div><h2>Посмотрите результат</h2><p>В каталоге — шесть проектов с фотографиями, площадью и сроками работ.</p></div><a class="button button-lime" href="../projects.html">Смотреть проекты <span aria-hidden="true">↗</span></a></div></section>'''
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
</head>
<body>
  <header class="site-header" id="top"><div class="container header-inner"><a class="brand" href="../index.html" aria-label="Тротуар Про — на главную"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span>Тротуар<span class="brand-accent">_</span>Про</span></a><nav class="main-nav" id="navigation" aria-label="Основная навигация"><a href="../services.html">Услуги</a><a href="../index.html#technology">Технология</a><a href="../index.html#process">Как работаем</a><a href="../projects.html">Проекты</a></nav><a class="header-cta" href="../index.html#request">Рассчитать стоимость <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-label="Открыть меню" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button></div></header>
  <main>
    <section class="inner-hero service-detail-hero"><div class="container"><a class="service-back" href="../services.html">← Все услуги</a><div class="eyebrow lime"><span class="eyebrow-line"></span> Тротуар_Про</div><h1>{title}</h1><p>{e(service['lead'])}</p></div></section>
    <section class="detail-section"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Состав работ</div><h2>{e(service['section_title'])}</h2><p>{e(service['section_lead'])}</p></div><div class="detail-cards">{cards}</div></div></section>
{special}
    <section class="detail-section"><div class="container"><div class="detail-section-head"><h2>Другие направления</h2><p>Соседние работы можно обсудить вместе с основной задачей.</p></div><div class="detail-links">{related}<a href="../services.html">Все услуги ↗</a></div></div></section>
    <section class="inner-cta"><div class="container"><h2>Обсудим ваш участок?</h2><a class="button button-lime" href="../index.html#request">Перейти к заявке <span aria-hidden="true">↗</span></a></div></section>
  </main>
  <footer class="site-footer"><div class="container"><span>© 2026 Тротуар_Про</span><span>Мощение и благоустройство территорий</span><a href="#top">Наверх ↑</a></div></footer>
  <script src="../script.js"></script>
</body>
</html>
'''

for service in SERVICES:
    (OUT / (service['slug'] + '.html')).write_text(render(service), encoding='utf-8')
