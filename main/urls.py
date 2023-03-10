from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='ArnalImanShoes',
        default_version='v1',
        description='blog'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('applications.sneakers.urls')),
    path('api/v1/', include('applications.category.urls')),
    path('api/v1/', include('applications.order.urls')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/feedback/', include('applications.feedback.urls')),
    path('api/v1/category/', include('applications.category.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
