from django.contrib import admin
from applications.sneakers.models import Sneakers, SneakersImage

admin.site.register(Sneakers)
admin.site.register(SneakersImage)