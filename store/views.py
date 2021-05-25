from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ProductSerializer
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
