from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True,max_length=200)