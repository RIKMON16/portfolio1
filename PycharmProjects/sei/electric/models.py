from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)


class Customer(models.Model):
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)
    contact_no = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()