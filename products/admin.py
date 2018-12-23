from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'price']
    list_display = ['__str__', 'description',
                    'price', 'slug', 'created', 'updated']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
