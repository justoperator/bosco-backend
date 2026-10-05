from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва гри")
    min_players = models.PositiveIntegerField(verbose_name="Мін. гравців")
    max_players = models.PositiveIntegerField(verbose_name="Макс. гравців")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return f"{self.name} ({self.min_players}-{self.max_players} гравців)"
