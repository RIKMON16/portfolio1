from django.contrib import admin

# Register your models here.
from products.models import *


@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'pin_code', 'country', 'email', 'phone']
    

@admin.register(Accommodation)
class Accommodation(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone', 'remark', 'important', 'cancellation']


@admin.register(Attraction)
class Attraction(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone', 'remark', 'important', 'cancellation']


@admin.register(Daytour)
class Daytour(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone', 'remark', 'important', 'cancellation']


@admin.register(Airport)
class Airport(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone']


@admin.register(Trainstation)
class Trainstation(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone']


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone', 'remark', 'important', 'cancellation']


@admin.register(Misc)
class Misc(admin.ModelAdmin):
    list_display = ['name', 'address', 'city',
                    'pin_code', 'country', 'email', 'phone', 'remark', 'important', 'cancellation']
