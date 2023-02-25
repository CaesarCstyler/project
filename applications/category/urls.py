from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.category.views import CategoryModelViewSet
from applications.category import views

router = DefaultRouter()
router.register('', CategoryModelViewSet)

urlpatterns = [
    path('sneakers/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('', include(router.urls)),
]
