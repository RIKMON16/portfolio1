from django.contrib import admin
from operations.models import *  # * import everything from the models.py file, so here im importing all models of my files

@admin.register(Add_Accommodation)
class Add_Accommodation(admin.ModelAdmin):
    list_display =['accommodation', 'check_in', 'check_out', 'room_type', 'no_of_rooms', 'board_basis', 'confirmation_number',
                   'currency', 'cost', 'provider']
    

@admin.register(Add_Attraction)
class Add_Attraction(admin.ModelAdmin):
    list_display =['attraction', 'date_of_visit', 'confirmation_number', 'currency', 'cost', 'provider']
    

@admin.register(Add_Day_Tour)
class Add_Day_Tour(admin.ModelAdmin):
    list_display =['day_tour', 'date_of_tour', 'confirmation_number', 'currency', 'cost', 'provider']
    
    
@admin.register(Add_Ticket)
class Add_Ticket(admin.ModelAdmin):
    list_display = ['ticket', 'date_of_journey',
                    'confirmation_number', 'currency', 'cost', 'provider']
    

@admin.register(Add_Misc)
class Add_Misc(admin.ModelAdmin):
    list_display = ['misc', 'date_of_service',
                    'confirmation_number', 'currency', 'cost', 'provider']
    

@admin.register(Add_Meal)
class Add_Meal(admin.ModelAdmin):
    list_display = ['restaurant', 'meal_type', 'date_of_service',
                    'confirmation_number', 'currency', 'cost', 'provider']
    

@admin.register(Transfer_Airport)
class Transfer_Airport(admin.ModelAdmin):
    list_display = ['transfer_type', 'vehicle', 'pickup_point', 'flight_detail', 'pickup_date', 'drop_off_point',
                    'confirmation_number', 'currency', 'cost', 'provider']


@admin.register(Return_Transfer_Airport)
class Return_Transfer_Airport(admin.ModelAdmin):
    list_display = ['transfer_type', 'vehicle', 'pickup_point', 'pickup_date', 'drop_off_point', 'flight_detail',
                    'confirmation_number', 'currency', 'cost', 'provider']


@admin.register(Return_Transfer_Train)
class Return_Transfer_Train(admin.ModelAdmin):
    list_display = ['transfer_type', 'vehicle', 'pickup_point', 'train_detail', 'pickup_date', 'drop_off_point', 'train_detail',
                    'confirmation_number', 'currency', 'cost', 'provider']


@admin.register(Transfer_Train)
class Transfer_Train(admin.ModelAdmin):
    list_display = ['transfer_type', 'vehicle', 'pickup_point', 'pickup_date', 'drop_off_point',
                    'confirmation_number', 'currency', 'cost', 'provider']
