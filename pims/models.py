from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    images = models.JSONField(default=list, blank=True, null=True, max_length=10)

    def __str__(self):
        return self.name

