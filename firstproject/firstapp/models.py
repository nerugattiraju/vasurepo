from django.db import models

# Create your models here.
class Customer(models.Model):
    NAME=models.CharField(max_length=70)
    MOBILE=models.IntegerField()
    AGE=models.IntegerField()
    CITY=models.CharField(max_length=100)

