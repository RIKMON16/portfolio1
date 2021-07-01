from django.contrib import admin
from .models import Product, Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_no', 'email', 'message')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
