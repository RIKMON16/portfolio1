from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=15)
    country = CountryField()
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ['name']

class Supplier(CommonInfo):
    phone = PhoneNumberField()
    
    def __str__(self):
        return self.name


class Accommodation(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Attraction(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Daytour(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Airport(CommonInfo):
    phone = PhoneNumberField()

    def __str__(self):
        return self.name


class Trainstation(CommonInfo):
    phone = PhoneNumberField()

    def __str__(self):
        return self.name


class Restaurant(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Misc(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    

class Ticket(CommonInfo):
    phone = PhoneNumberField()
    remark = models.TextField(max_length=1000)
    important = models.TextField(max_length=2000)
    cancellation = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
