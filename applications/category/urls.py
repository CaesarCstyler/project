from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.category.views import CategoryModelViewSet

router = DefaultRouter()
router.register('', CategoryModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
