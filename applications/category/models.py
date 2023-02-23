from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # Для того чтобы было легче получать url
        return f'/{self.slug}/'
