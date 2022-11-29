from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=18)
    course_type = models.CharField(max_length=50)
