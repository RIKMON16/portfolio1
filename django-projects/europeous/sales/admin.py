from django.contrib import admin
from sales.models import *
# Register your models here.


@admin.register(Agent)
class Agent(admin.ModelAdmin):
    list_display = [
        'name', 'agency_name', 'address', 'city', 'zip', 'country', 
        'email_address', 'phone'
    ]


@admin.register(Create_File)
class Create_File(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'guest_email', 'guest_phone', 'no_of_adults', 'no_of_children',
                    'start_date', 'end_date', 'agent', 'employee', 'accommodation', 'attraction',
                    'day_tour', 'ticket', 'misc', 'arrival_transfer_airport', 'transfer_return_air', 
                    'return_transfer_train', 'train_transfer', 'meal', 'currency', 'tour_cost']
