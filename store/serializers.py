from .models import Product, Category, Country, City
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'amount', 'active']

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'amount', 'active', 'category_id']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']



class CountryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

        
class CitySerializer(serializers.ModelSerializer):
    country = CountryBaseSerializer()

    class Meta:
        model = City
        fields = ['id', 'name', 'country']


class CityBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', ]


class CountrySerializer(serializers.ModelSerializer):
    cities = CityBaseSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'cities']


