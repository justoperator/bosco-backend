import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def products_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})


def replenish_stock(request, count: int):
    sample_names = ["Еволюція", "Вулик", "Еківоки", "Вибухові кошенята", "Мафія", "Кодові імена", "Детектив", "Древній Жах"]
    sample_genres = ["Стратегія", "Для вечірок", "Кооперативна", "Детектив", "Карткова", "Логічна"]

    new_items = []
    for _ in range(count):
        min_p = random.randint(1, 3)
        max_p = min_p + random.randint(1, 5)
        
        game = Product(
            name=f"{random.choice(sample_names)} {random.randint(1, 99)}",
            min_players=min_p,
            max_players=max_p,
            genre=random.choice(sample_genres),
            price=round(random.uniform(300.0, 3000.0), 2)
        )
        new_items.append(game)

    Product.objects.bulk_create(new_items)

    return HttpResponse(
        f"<h2>Успішно додано {count} нових настільних ігор!</h2>"
        f'<p><a href="/products">Повернутися до каталогу</a></p>'
    )
