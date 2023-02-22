from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.brand.views import BrandsModelViewSet

router = DefaultRouter()
router.register('', BrandsModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
