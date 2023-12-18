from django.contrib import admin
from products.models import ProductCategory, Product


# @admin.register(Product)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'image', 'quantity', 'category')


# admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Product)
