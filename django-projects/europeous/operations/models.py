from django.db import models
from products.models import *  # Import all models from products
# Create your models here.


class Add_Accommodation(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    ROOM_CHOICES = (
        ('SIN', 'Standard Single Room'),
        ('SDL', 'Standard Double Room'),
        ('TWN', 'Standard Twin Room'),
        ('TRP', 'Standard Triple Room'),
        ('DSL', 'Deluxe Single Room'),
        ('DDL', 'Deluxe Double Room'),
        ('DTW', 'Deluxe Twin Room'),
        ('DTR', 'Deluxe Triple Room'),
        ('SSL', 'Superior Single Room'),
        ('SDL', 'Superior Double Room'),
        ('STW', 'Superior Twin Room'),
        ('STR', 'Superior Triple Room'),
        ('JNR', 'Junior Suite Room'),
        ('SUT', 'Suite Room'),
        ('ONE', 'One Bedroom'),
        ('TWO', 'Two Bedroom'),
        ('THR', 'Three Bedroom'),
        ('STD', 'Studio Apartment'),
    )
    BOARD_CHOICES = (
        ('RM', 'Room Only'),
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Half Board Basis'),
        ('FB', 'Full Board Basis'),
        ('AI', 'All Inclusive'),
    )
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                              related_query_name="%(app_label)s_%(class)ss")
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=30, choices=ROOM_CHOICES)
    no_of_rooms = models.PositiveSmallIntegerField()
    board_basis = models.CharField(max_length=30, choices=BOARD_CHOICES)
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.accommodation}'


class Add_Attraction(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")
    date_of_visit = models.DateTimeField()
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.attraction}'


class Add_Day_Tour(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    day_tour = models.ForeignKey(Daytour, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                             related_query_name="%(app_label)s_%(class)ss")
    date_of_tour = models.DateTimeField()
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.day_tour}'


class Add_Ticket(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss")
    date_of_journey = models.DateTimeField()
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.ticket}'
    

class Add_Misc(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    misc = models.ForeignKey(Misc, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")
    date_of_service = models.DateTimeField()
    confirmation_number = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=3000)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.misc}'


class Add_Meal(models.Model):
    MEAL_CHOICES = (
        ('BF', 'Breakfast'),
        ('LU', 'Lunch'),
        ('DN', 'Dinner'),
        ('GD', 'Gala Dinner'),
        ('SN', 'Dinner with Snacks'),
    )
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss")
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    date_of_service = models.DateTimeField()
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.customer} - {self.restaurant}'


class Transfer_Airport(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    PICKUP_CHOICES = (
        ('PVT', 'Private Transfer'),
        ('SIC', 'Shared Transfer'),
    )
    VEHICLE_CHOICES = (
        ('MER E', 'Mercedes E Class or similar'),
        ('LUX', 'Mercedes S / BMW 5 or similar'),
        ('STD', 'Toyota Corola or similar'),
        ('MPV', 'VW Sharon or similar'),
        ('7SEAT', 'Ford Transporter or similar'),
        ('LUX7SEAT', 'Mercedes V Class or similar'),
        ('15SEAT', 'Mercedes Sprinter or similar'),
        ('49SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
        ('54SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
    )
    transfer_type = models.CharField(max_length=40, choices=PICKUP_CHOICES)
    vehicle = models.CharField(max_length=40, choices=VEHICLE_CHOICES)
    pickup_point = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                     related_query_name="%(app_label)s_%(class)ss")
    flight_detail = models.CharField(max_length=100, blank=True)
    pickup_date = models.DateTimeField()
    drop_off_point = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                       related_query_name="%(app_label)s_%(class)ss")
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.transfer_type} - {self.pickup_point}'


class Return_Transfer_Airport(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    PICKUP_CHOICES = (
        ('PVT', 'Private Transfer'),
        ('SIC', 'Shared Transfer'),
    )
    VEHICLE_CHOICES = (
        ('MER E', 'Mercedes E Class or similar'),
        ('LUX', 'Mercedes S / BMW 5 or similar'),
        ('STD', 'Toyota Corola or similar'),
        ('MPV', 'VW Sharon or similar'),
        ('7SEAT', 'Ford Transporter or similar'),
        ('LUX7SEAT', 'Mercedes V Class or similar'),
        ('15SEAT', 'Mercedes Sprinter or similar'),
        ('49SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
        ('54SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
    )
    transfer_type = models.CharField(max_length=40, choices=PICKUP_CHOICES)
    vehicle = models.CharField(max_length=40, choices=VEHICLE_CHOICES)
    pickup_point = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                     related_query_name="%(app_label)s_%(class)ss")
    pickup_date = models.DateTimeField()
    drop_off_point = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                       related_query_name="%(app_label)s_%(class)ss")
    flight_detail = models.CharField(max_length=100, blank=True)
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.transfer_type} - {self.pickup_point}'


class Return_Transfer_Train(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    PICKUP_CHOICES = (
        ('PVT', 'Private Transfer'),
        ('SIC', 'Shared Transfer'),
    )
    VEHICLE_CHOICES = (
        ('MER E', 'Mercedes E Class or similar'),
        ('LUX', 'Mercedes S / BMW 5 or similar'),
        ('STD', 'Toyota Corola or similar'),
        ('MPV', 'VW Sharon or similar'),
        ('7SEAT', 'Ford Transporter or similar'),
        ('LUX7SEAT', 'Mercedes V Class or similar'),
        ('15SEAT', 'Mercedes Sprinter or similar'),
        ('49SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
        ('54SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
    )
    transfer_type = models.CharField(max_length=40, choices=PICKUP_CHOICES)
    vehicle = models.CharField(max_length=40, choices=VEHICLE_CHOICES)
    pickup_point = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                     related_query_name="%(app_label)s_%(class)ss")
    pickup_date = models.DateTimeField()
    train_detail = models.CharField(max_length=100, blank=True)
    drop_off_point = models.ForeignKey(Trainstation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                       related_query_name="%(app_label)s_%(class)ss")
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.transfer_type} - {self.pickup_point} - {self.drop_off_point}'


class Transfer_Train(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    PICKUP_CHOICES = (
        ('PVT', 'Private Transfer'),
        ('SIC', 'Shared Transfer'),
    )
    VEHICLE_CHOICES = (
        ('MER E', 'Mercedes E Class or similar'),
        ('LUX', 'Mercedes S / BMW 5 or similar'),
        ('STD', 'Toyota Corola or similar'),
        ('MPV', 'VW Sharon or similar'),
        ('7SEAT', 'Ford Transporter or similar'),
        ('LUX7SEAT', 'Mercedes V Class or similar'),
        ('15SEAT', 'Mercedes Sprinter or similar'),
        ('49SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
        ('54SEAT', 'SCANIA/Vanhool/Volvo Coach or similar'),
    )
    transfer_type = models.CharField(max_length=40, choices=PICKUP_CHOICES)
    vehicle = models.CharField(max_length=40, choices=VEHICLE_CHOICES)
    pickup_point = models.ForeignKey(Trainstation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                     related_query_name="%(app_label)s_%(class)ss")
    train_detail = models.CharField(max_length=100, blank=True)
    pickup_date = models.DateTimeField()
    drop_off_point = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                       related_query_name="%(app_label)s_%(class)ss")
    confirmation_number = models.CharField(max_length=40, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")

    def __str__(self):
        return f'{self.transfer_type} - {self.pickup_point}'
