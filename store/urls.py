"""ecommerce URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers

from store.views import ProductDetailView, ProductListView, CategoryViewSet, ProductDetail, ProductList


router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/', ProductList.as_view()),
    path('api/products/<pk>/', ProductDetail.as_view()),

    path('login', TemplateView.as_view(template_name="login.html"), name='login'),
    path('list', ProductListView.as_view(), name='list'),
    path('detail/<pk>', ProductDetailView.as_view(), name='detail'),
    path('', TemplateView.as_view(template_name="base.html"), name='home'),
]
