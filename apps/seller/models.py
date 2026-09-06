from django.db import models
from django.contrib.auth.models import User
from apps.admin_module.models import Grocery


class Product(models.Model):

    UNIT_CHOICE = [
        ('1KG', '1kg'),
        ('500G', '500g'),
        ('250G', '250g'),
        ('COUNT', 'count'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    grocery = models.ForeignKey(Grocery, on_delete=models.SET_NULL, null=True)
    local_name = models.CharField(max_length=100, blank=True)
    stock = models.PositiveBigIntegerField()
    quantity = models.CharField(max_length=10, choices= UNIT_CHOICE, default='250G')
    count = models.PositiveBigIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grocery.name if self.grocery else "Unknown Product"



class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    shop_name = models.CharField(max_length=100)