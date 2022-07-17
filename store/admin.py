from django.contrib import admin
from .models import *

class ProductView(admin.ModelAdmin):
    search_fields = ("name", "product_id")
    list_display = ("name", "product_id", "quantity", "updated_on")

admin.site.register(Customer)
admin.site.register(Product, ProductView)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(DeliveryAddress)


