from django.urls import path, include
from applications.sneakers.views import SneakersModelViewSet
from applications.feedback.views import CommentModelViewSet
from rest_framework.routers import DefaultRouter
from applications.sneakers.views import OrderCreateView

router = DefaultRouter()
router.register('comment', CommentModelViewSet, basename='comment')
router.register('sneakers', SneakersModelViewSet, basename='sneakers')
# router.register('order', OrderCreateView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    path('create/', OrderCreateView.as_view())
    # path('create_order/', )

]
