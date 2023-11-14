from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()






