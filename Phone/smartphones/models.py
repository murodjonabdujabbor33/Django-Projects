from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=50)

    def __str__(self):
        return self.title
