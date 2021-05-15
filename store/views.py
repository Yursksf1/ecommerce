from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView

from store.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'

