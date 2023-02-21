from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title