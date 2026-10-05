import random
from django.http import HttpResponse
from .models import Product


def products_list(request):
    products = Product.objects.all()

    rows = ""
    for p in products:
        rows += f"""
        <tr>
            <td>{p.id}</td>
            <td>{p.name}</td>
            <td>{p.min_players} - {p.max_players}</td>
            <td>{p.genre}</td>
            <td>{p.price} грн</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Настільні ігри - Склад</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f4f6f9; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; background: #ffffff; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #dddddd; padding: 12px; text-align: left; }}
            th {{ background-color: #27ae60; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>Список настільних ігор на складі</h1>
        <p>Усього найменувань: <strong>{products.count()}</strong></p>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Назва гри</th>
                    <th>Кількість гравців</th>
                    <th>Жанр</th>
                    <th>Ціна</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)
