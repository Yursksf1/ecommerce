from django.contrib import admin

# Register your models here.
from .models import Country, City, Address, Category, Product, Imagen, Buy, UserProfile

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Imagen)

admin.site.register(Buy)
admin.site.register(UserProfile)
