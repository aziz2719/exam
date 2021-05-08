"""Hydra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from users.views import UserView
from products.views import ProductView, ProductCategoryView
from orders.views import OrderView

router = routers.DefaultRouter()

router.register(r'users', UserView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    path('products/', ProductView.as_view({'get': 'list'})),
    path('products/categories/', ProductCategoryView.as_view({'get': 'list'})),
    path('orders/', OrderView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls