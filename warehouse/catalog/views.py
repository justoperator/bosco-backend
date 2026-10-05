from django.shortcuts import render, redirect
from django.contrib import messages
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
