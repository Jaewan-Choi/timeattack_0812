from django.db import models
from user.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=256)
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'


class ProductStatus(models.Model):
    buy_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ProductStatues'