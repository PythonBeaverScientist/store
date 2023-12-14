from django.shortcuts import render, HttpResponse


def index(request):
    context: dict = {
        'title': 'main store page',
        'username': 'ksenia',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store Каталог',
        'products': [
            {
                'image_path': '/static/vendor/img/products/Adidas-hoodie.png',
                'card_name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'card_text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image_path': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'card_name': 'Синяя куртка The North Face',
                'price': 23725,
                'card_text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image_path': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'card_name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'card_text': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'image_path': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                'card_name': 'Черный рюкзак Nike Heritage',
                'price': 2340,
                'card_text': 'Плотная ткань. Легкий материал.'
            },
            {
                'image_path': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                'card_name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': 13590,
                'card_text': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'image_path': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'card_name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': 2890,
                'card_text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            },
        ],
    }
    return render(request, 'products/products.html', context)
