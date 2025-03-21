from django.db import models

# Create your models here.
# Every class defined here
# inheriting the class models.model fron module django.db

class Product(models.Model):
    name= models.CharField(max_length=225)
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img=models.ImageField(upload_to='products/')
    stock = models.PositiveBigIntegerField()