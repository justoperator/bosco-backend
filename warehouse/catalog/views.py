import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        min_players = request.POST.get('min_players')
        max_players = request.POST.get('max_players')
        genre = request.POST.get('genre')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            min_players=min_players,
            max_players=max_players,
            genre=genre,
            price=price
        )
        messages.success(request, f"Гру «{name}» успішно додано до каталогу!")
        return redirect('products_list')

    return render(request, 'catalog/add_product.html')


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
