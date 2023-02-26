"""EStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from store.views import ProductViewSet


admin.site.site_header = 'Trang Admin Estore' # chinh sua ten trang Admin
admin.site.index_title = 'Estore Admin' # chinh sua ten title

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('cart.urls')),
    path('user/', include('users.urls')),
    path('store-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)