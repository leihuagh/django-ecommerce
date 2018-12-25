from django.contrib import admin
from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ['title', 'description', 'price']
    list_display = ['__str__', 'description',
                    'price', 'slug', 'active', 'created', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
