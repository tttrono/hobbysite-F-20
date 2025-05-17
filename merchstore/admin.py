from django.contrib import admin
from .models import Product, ProductType

class ProductAdmin(admin.ModelAdmin):
    model = Product
    
    search_fields = ('name', 'description', 'productType')
    list_display = ('name',)
    
class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType

    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
