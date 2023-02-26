from django.contrib import admin

from applications.order.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
