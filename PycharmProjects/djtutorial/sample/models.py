from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)

class Music(models.Model):
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)
    instrument = models.CharField(max_length=108)

class Album(models.Model):
    artist = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="Musician"
    )
    name = models.CharField(max_length=108)
    release_date = models.DateField()
    num_stars = models.IntegerField()
