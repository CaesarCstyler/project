from django.db import models
from django.contrib.auth import get_user_model
from applications.brand.models import Brand
from applications.category.models import Category

User = get_user_model

class Sneakers(models.Model):
    title = models.CharField('Название кроссовки', max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='sneakers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sneakers')
    color = models.CharField('Цвет', max_length=30)
    size = models.BigIntegerField('Размер кросовки')
    price = models.DecimalField(max_digits=30, decimal_places=12)
    in_stock = models.BooleanField(verbose_name='В наличии')

    def __str__(self):
        return f'{self.title}'


class SneakersImage(models.Model):
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='sneakers')
    image = models.ImageField(upload_to='sneakers_images')
    
    def __str__(self):
        return f'{self.sneaker.title}'
