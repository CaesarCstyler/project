from django.db import models
from django.contrib.auth import get_user_model
from applications.sneakers.models import Sneakers
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments')
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='Comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.sneaker.title}'
    
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.owner} liked - {self.sneaker.title}'
    
class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.sneaker.title}'
    
class Favorite(models.Model):
    sneaker = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='Favorites')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Favorites')
