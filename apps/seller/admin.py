from django.contrib import admin
from .models import Product, ShopDetails, SellerProfile



class ProductAdmin(admin.ModelAdmin):

    list_display = ('grocery', 'seller', 'stock', 'display_size', 'price')

    @admin.display(description='Size')
    def display_size(self, obj):

        if obj.quantity == 'COUNT':
            return f"{obj.count} Nos"

        return obj.get_quantity_display()

admin.site.register(Product, ProductAdmin)


admin.site.register(ShopDetails)

admin.site.register(SellerProfile)