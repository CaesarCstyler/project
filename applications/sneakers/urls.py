from django.urls import path, include
# from applications.sneakers.views import SneakersModelViewSet, CreateImageAPIView
from applications.sneakers import views
from applications.feedback.views import CommentModelViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('comment', CommentModelViewSet)
# router.register('', SneakersModelViewSet)

urlpatterns = [
    path('latest-sneakers/', views.LatestSneakersList.as_view()),
    path('sneakers/<slug:category_slug>/<slug:sneakers_slug>/', views.SneakersDetail.as_view()),
    # path('', include(router.urls)),
    # path('add/image/', CreateImageAPIView.as_view()),
]
