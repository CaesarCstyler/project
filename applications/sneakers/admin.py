from django.contrib import admin
from applications.sneakers.models import Sneakers, SneakersImage, Order
admin.site.register(Sneakers)
admin.site.register(SneakersImage)
admin.site.register(Order)