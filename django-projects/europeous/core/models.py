from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = CountryField()
    phone = PhoneNumberField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
