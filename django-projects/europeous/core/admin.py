from django.contrib import admin
from core.models import *
# Register your models here.


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = [
        'name', 'emp_code', 'city', 'country', 'phone', 'email'
    ]
