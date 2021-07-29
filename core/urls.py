"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from django.conf import settings

from account.views import UserViewSet
from app import views
from app.views import CategoryListView, FavoriteViewSet, DescriptionViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('descriptions', DescriptionViewSet)
router.register('favorites', FavoriteViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title='Stack API',
        default_version='v1',
        description='Test description',
    ),
    public=True,
)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui()),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include("account.urls")),
]


urlpatterns += i18n_patterns(
    path('', include(router.urls)),
    path('favorites/category/<int:pk>/', views.description_detail_favorites),
    path('category/', CategoryListView.as_view()),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)