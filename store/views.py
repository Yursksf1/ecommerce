from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from store.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'

