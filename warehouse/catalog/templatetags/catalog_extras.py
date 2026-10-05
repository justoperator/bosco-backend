from django import template
from catalog.models import Product

register = template.Library()

@register.filter(name='uah')
def uah(value):
    try:
        return f"{float(value):,.2f} грн".replace(",", " ")
    except (ValueError, TypeError):
        return f"{value} грн"

@register.simple_tag
def product_count():
    return Product.objects.count()
