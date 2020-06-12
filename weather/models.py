from django.db import models
from django.utils import timezone
# Create your models here.

class WH(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=50)
    temperature = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    icon = models.CharField(max_length=10)

class seasons(models.Model):
    season = models.CharField(max_length=50)
    temperatureStart = models.CharField(max_length=10,default=0)
    temperatureEnd = models.CharField(max_length=10,default=0)

class fixedItems(models.Model):
    items=models.CharField(max_length=50)

class seasonalItems(models.Model):
    item=models.CharField(max_length=50)
    season = models.CharField(max_length=50)