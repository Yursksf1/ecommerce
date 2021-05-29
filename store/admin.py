from django.contrib import admin

# Register your models here.
from .models import Country, City, Address, Category, Product, Imagen, Buy, UserProfile

admin.site.register(Country)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    fields = ('name', 'country')

    list_filter = ['country__name', ]

admin.site.register(City, CityAdmin)



admin.site.register(Address)

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'category', 'stock', 'active', 'name_image')
    fields = ('name', 'amount', 'category',  'active', 'description','stock')
    list_filter = ('active', 'category')
    search_fields = ('name',)

    @admin.display(ordering='name_image')
    def name_image(self, obj):
        name = ''
        if obj.imagen_set.all():
            name = obj.imagen_set.first().name

        return name


admin.site.register(Product, ProductAdmin)


admin.site.register(Imagen)

admin.site.register(Buy)
admin.site.register(UserProfile)
