from django.contrib import admin
from applications.feedback.models import Like, Comment, Rating, Favorite

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)
