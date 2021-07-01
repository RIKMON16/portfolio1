from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from operations.models import *  # Import all models of operations app
from core.models import *  # Import all models of operations app
# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=100)
    agency_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    country = CountryField()
    email_address = models.EmailField(max_length=200)
    phone = PhoneNumberField()
    
    def __str__(self):
        return self.name


class Create_File(models.Model):
    CURRENCY_CHOICES = (
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('RUP', 'Rs'),
    )
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)
    guest_email = models.EmailField(max_length=300, null=True)
    guest_phone = PhoneNumberField()
    no_of_adults = models.PositiveSmallIntegerField()
    no_of_children = models.PositiveSmallIntegerField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss")
    accommodation = models.ForeignKey(Add_Accommodation, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    attraction = models.ForeignKey(Add_Attraction, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    
    day_tour = models.ForeignKey(Add_Day_Tour, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    ticket = models.ForeignKey(Add_Ticket, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    misc = models.ForeignKey(Add_Misc, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                             related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    arrival_transfer_airport = models.ForeignKey(Transfer_Airport, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                 related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    transfer_return_air = models.ForeignKey(Return_Transfer_Airport, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                         related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    return_transfer_train = models.ForeignKey(Return_Transfer_Train, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                            related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    train_transfer = models.ForeignKey(Transfer_Train, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                                                 related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    meal = models.ForeignKey(Add_Meal, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                              related_query_name="%(app_label)s_%(class)ss", null=True, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    tour_cost = models.DecimalField(max_digits=10, decimal_places=2)
