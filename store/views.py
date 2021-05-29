from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ProductSerializer, CategorySerializer, CategoryListSerializer, ProductListSerializer, CreateProductSerializer
from .models import Product, Category

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductListSerializer(product, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request, format=None):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        data = serializer.data

        data['ingreso proyectado'] = data['stock'] * data['amount']
        data['tax'] = data['amount'] * 0.19

        return Response(data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategoryListSerializer(category, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)