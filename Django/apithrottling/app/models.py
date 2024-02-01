from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)