from django.db import models
from products.models import Product
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.name

from django.apps import apps
class Techlopian(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    domain = models.CharField(max_length=200)
    spec = models.CharField(max_length=200)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'name:' +self.name + ' domain:'+self.domain

class Order(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Activated','Activated'),
        ('Deactivated','deactivated'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status =models.CharField(max_length=200, null=True, choices=STATUS)