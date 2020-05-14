from django.contrib import admin
from .models import Customer ,Techlopian, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Techlopian)
admin.site.register(Order)