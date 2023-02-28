from django.db import models
from django.contrib.auth import get_user_model
from applications.sneakers.models import Sneakers
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} liked - {self.sneakers.name}'

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.sneakers.title}'
    
class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.sneakers.title}'
    
class Favorite(models.Model):
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE, related_name='favorites')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
