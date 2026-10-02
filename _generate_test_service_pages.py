from html import escape
from pathlib import Path

OUT = Path(__file__).parent / 'test' / 'services'
OUT.mkdir(exist_ok=True)

SERVICES = [
    {
        'slug': 'ukladka-plitki',
        'title': 'Укладка тротуарной плитки и брусчатки',
        'lead': 'Устройство мощения для дворов, дорожек и площадок — от подготовки основания и отвода воды до укладки плитки и заполнения швов.',
        'section_title': 'Что входит в работу',
        'section_lead': 'Конструкцию основания и способ укладки подбираем под грунт, рельеф и будущую нагрузку.',
        'items': [
            ('Осмотр и нивелирование', 'Замеряем участок, определяем перепады высот, направление уклонов и места отвода воды.'),
            ('Подготовка основания', 'При необходимости демонтируем старое покрытие, вынимаем грунт и послойно уплотняем песчано-щебёночное основание.'),
            ('Бордюры и водоотведение', 'Фиксируем края мощения, формируем уклоны и при необходимости устанавливаем лотки и дождеприёмники.'),
            ('Укладка покрытия', 'Укладываем плитку по выбранному рисунку, выполняем подрезку и примыкания, заполняем швы и очищаем покрытие.'),
        ],
        'related': [('Бетонирование дворов', 'betonirovanie-dvorov.html'), ('Уход за плиткой', 'uhod-za-plitkoy.html')],
    },
    {
        'slug': 'betonirovanie-dvorov',
        'title': 'Бетонирование дворов',
        'lead': 'Устройство бетонного покрытия во дворе и на площадках. Решение подбираем по условиям участка и назначению будущей поверхности.',
        'section_title': 'Как подходим к задаче',
        'section_lead': 'Толщину основания, армирование и марку бетона определяем с учётом грунта и нагрузки на площадку.',
        'items': [
            ('Осмотр и отметки', 'Замеряем участок, оцениваем грунт, перепады и направление отвода воды.'),
            ('Подготовка основания', 'Выполняем выемку грунта, устраиваем и послойно уплотняем основание под будущую нагрузку.'),
            ('Опалубка и армирование', 'Формируем границы площадки, предусматриваем уклоны и собираем согласованное армирование.'),
            ('Заливка и выравнивание', 'Укладываем бетон, выравниваем поверхность и контролируем качество готового покрытия.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Благоустройство участка', 'blagoustroystvo-uchastka.html')],
    },
    {
        'slug': 'uhod-za-plitkoy',
        'title': 'Уход за тротуарной плиткой',
        'lead': 'Помогаем поддерживать мощёное покрытие в порядке между сезонами. Состав работ зависит от состояния плитки и швов.',
        'section_title': 'Что можем сделать',
        'section_lead': 'Сначала оцениваем состояние плитки и швов, затем предлагаем необходимый набор работ.',
        'items': [
            ('Мойка плитки', 'Удаляем уличные загрязнения и налёт с поверхности, подбирая способ очистки под состояние покрытия.'),
            ('Гидрофобная пропитка', 'После очистки и высыхания наносим состав, который снижает впитывание влаги и облегчает дальнейший уход.'),
            ('Обновление швов', 'Восстанавливаем заполнение швов кварцевым или модифицированным песком, чтобы стабилизировать покрытие.'),
            ('Удаление травы', 'Очищаем швы от растительности и подготавливаем их к повторному заполнению песком.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Все услуги', '../services.html')],
    },
    {
        'slug': 'blagoustroystvo-uchastka',
        'title': 'Благоустройство участка',
        'lead': 'Инженерные и ландшафтные работы для комфортного участка: отвод воды, освещение, автоматический полив и укладка газона.',
        'section_title': 'Направления благоустройства',
        'section_lead': 'Каждую систему проектируем с учётом рельефа, планировки, существующих коммуникаций и будущего использования территории.',
        'items': [
            ('Дренаж и ливневая канализация', 'Отводим воду от дома, отмостки и дорожек. Устанавливаем дождеприёмники, линейные лотки, дренажные трубы в геотекстиле и ревизионные колодцы — состав системы зависит от участка.'),
            ('Ландшафтное освещение', 'Планируем освещение дорожек, зон отдыха и растений. Прокладываем защищённые кабельные линии, устанавливаем светильники и настраиваем удобное управление.'),
            ('Автоматический и капельный полив', 'Организуем полив по расписанию: выдвижные спринклеры для газона, капельные линии для клумб и хвойных растений, датчики дождя и контроллер.'),
            ('Подготовка и укладка газона', 'Очищаем и выравниваем участок, готовим плодородный слой, укладываем рулонный газон, прикатываем и выполняем первый полив.'),
        ],
        'related': [('Укладка плитки', 'ukladka-plitki.html'), ('Бетонирование дворов', 'betonirovanie-dvorov.html')],
    },
]

DETAILS = {
    'ukladka-plitki': {
        'about': 'Долговечность мощения зависит не только от плитки. До укладки оцениваем грунт, перепады, предполагаемую нагрузку и отвод воды. Для пешеходной дорожки и парковки нужны разные конструкции основания, поэтому решение принимаем после осмотра участка.',
        'photos': ['Готовое покрытие на объекте', 'Процесс укладки'],
        'cost_factors': [
            ('Состояние участка', 'Учитываем демонтаж старого покрытия, выемку грунта и необходимую глубину основания.'),
            ('Будущая нагрузка', 'Для дорожек, двора и парковки под автомобиль требуется разная конструкция основания.'),
            ('Формат покрытия', 'На трудоёмкость влияют размер плитки, рисунок укладки, количество подрезки и сложных примыканий.'),
            ('Водоотведение', 'В смету могут входить бордюры, формирование уклонов, лотки и дождеприёмники.'),
        ],
    },
    'betonirovanie-dvorov': {
        'about': 'Бетонное покрытие устраиваем для дворов, парковок, проездов и хозяйственных площадок. Перед работами определяем отметки, будущую нагрузку и способ отвода воды — от этого зависят основание, армирование и толщина покрытия.',
        'photos': ['Готовый бетонный двор', 'Этап бетонных работ'],
        'cost_factors': [
            ('Состояние участка', 'На объём работ влияют демонтаж, выемка грунта, перепады и доступ техники.'),
            ('Назначение площадки', 'Пешеходная зона, двор и парковка требуют разной толщины основания и бетона.'),
            ('Армирование и геометрия', 'Учитываем выбранное армирование, форму площадки, опалубку и сложные примыкания.'),
            ('Водоотведение', 'Предусматриваем уклоны, лотки и точки сбора воды, если они необходимы на участке.'),
        ],
    },
    'uhod-za-plitkoy': {
        'about': 'Регулярный уход помогает сохранить внешний вид мощения и состояние швов. Осматриваем покрытие, определяем подходящий способ очистки и предлагаем только необходимые работы: мойку, удаление травы, обновление швов или защитную пропитку.',
        'photos': ['Покрытие до ухода', 'Покрытие после ухода'],
        'cost_factors': [
            ('Площадь покрытия', 'Учитываем общий объём работ, доступ к воде и возможность размещения оборудования.'),
            ('Состояние плитки', 'Тип и глубина загрязнений определяют способ очистки и количество проходов.'),
            ('Состояние швов', 'Проверяем наличие травы, вымывание песка и необходимость повторного заполнения.'),
            ('Состав работ', 'Стоимость зависит от сочетания мойки, пропитки, очистки и обновления швов.'),
        ],
    },
    'blagoustroystvo-uchastka': {
        'about': 'Дренаж, освещение, полив и газон лучше планировать вместе с дорожками и мощением. Так коммуникации прокладываются заранее, вода отводится в нужную сторону, а готовое покрытие не приходится вскрывать после завершения работ.',
        'photos': ['Дренаж и отвод воды', 'Ландшафтное освещение', 'Автоматический полив', 'Уложенный газон'],
        'cost_factors': [
            ('Выбранные системы', 'Рассчитываем отдельно дренаж, освещение, полив и газон или объединяем их в комплекс работ.'),
            ('Площадь и рельеф', 'Учитываем перепады высот, тип грунта, расположение дома, дорожек и посадок.'),
            ('Протяжённость сети', 'На расчёт влияют длина труб и кабелей, количество зон, светильников и точек водосбора.'),
            ('Оборудование и материалы', 'Итог зависит от выбранных труб, автоматики, светильников, газона и других материалов.'),
        ],
    },
}

PHOTO_DATA = {
    'ukladka-plitki': [
        ('../assets/projects/pavers-120/photo_04.webp', 'Брусчатка у бассейна'),
        ('../assets/projects/large-format/photo_07.webp', 'Широкоформатная плитка'),
        ('../assets/projects/kultura/photo_01.webp', 'Мощение парковой территории'),
        ('../assets/projects/pavers-80/photo_09.webp', 'Мощение двора'),
    ],
    'betonirovanie-dvorov': [
        (f'../assets/service-demos/concrete-{n}.webp', label)
        for n, label in [(4, 'Готовый бетонный двор'), (3, 'Выравнивание поверхности'), (2, 'Заливка бетона'), (1, 'Подготовка и армирование')]
    ],
    'uhod-za-plitkoy': [
        (f'../assets/service-demos/care-{n}.webp', label)
        for n, label in [(2, 'Нанесение защитного состава'), (3, 'Обновление швов'), (1, 'Мойка плитки'), (4, 'Удаление травы из швов')]
    ],
    'blagoustroystvo-uchastka': [
        ('../assets/service-demos/landscape-2.webp', 'Ландшафтное освещение'),
        ('../assets/service-demos/landscape-3.webp', 'Автоматический полив'),
        ('../assets/service-demos/lawn-installation.webp', 'Укладка рулонного газона'),
        ('../assets/service-demos/landscape-1.webp', 'Устройство дренажа'),
    ],
}

PAVER_TYPES = [
    ('Брусчатка 100 × 200', '../assets/projects/pavers-120/photo_04.webp', 'Прямоугольный формат для двора, дорожек и зоны у бассейна. Рисунок укладки подбираем под планировку участка.'),
    ('Широкоформатная плитка', '../assets/projects/large-format/photo_07.webp', 'Крупные плиты создают спокойный рисунок покрытия. На одном из наших объектов использован формат 600 × 300 мм.'),
    ('«Старый город»', '../assets/projects/old-town/photo_06.webp', 'Набор элементов разного размера даёт выразительный рисунок мощения. Это покрытие использовано на объекте площадью 200 м².'),
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
    return f'''<section class="detail-section" id="coverings"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Варианты покрытия</div><h2>Виды плитки и брусчатки</h2><p>Выберите покрытие, чтобы увидеть фотографию и описание. На снимках — материалы из выполненных проектов.</p></div><div class="paver-browser"><div class="paver-choices" role="tablist" aria-label="Виды плитки">{buttons}</div><div class="paver-panels">{panels}</div></div><p class="detail-note">Также можно обсудить уличный керамогранит и клинкерную брусчатку. Покрытие подберём под нагрузку и особенности участка.</p></div></section>
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
    cost_factors = ''.join(
        f'<article class="cost-factor"><span>{i:02d}</span><h3>{e(label)}</h3><p>{e(body)}</p></article>'
        for i, (label, body) in enumerate(detail['cost_factors'], 1)
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
  <link rel="stylesheet" href="../pages.css?v=service-content1">
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
    <section class="detail-section cost-section"><div class="container"><div class="detail-section-head"><div class="eyebrow"><span class="eyebrow-line"></span> Расчёт</div><h2>Из чего складывается стоимость</h2><p>Одинаковых участков не бывает, поэтому рассчитываем работу после осмотра и замеров.</p></div><div class="cost-grid">{cost_factors}</div><div class="cost-summary"><p><strong>Подготовим понятную смету.</strong> После осмотра согласуем состав работ и материалы, затем зафиксируем стоимость в смете и договоре.</p><a class="button button-lime" href="../index.html#request">Получить расчёт <span aria-hidden="true">↗</span></a></div></div></section>
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
