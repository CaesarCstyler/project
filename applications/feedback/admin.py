from django.contrib import admin
from applications.feedback.models import Comment, Rating, Favorite

admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)
