from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import FavoriteModelViewSet, CommentModelViewSet, RatingModelViewSet

router = DefaultRouter()
router.register('favorite', FavoriteModelViewSet)
router.register('comment', CommentModelViewSet)
router.register('rating', RatingModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
