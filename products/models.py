from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name