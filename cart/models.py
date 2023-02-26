from django.db import models
from store.models import Product

class Order(models.Model):
    username = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=500)
    total = models.DecimalField(max_digits=10, decimal_places=2) #models.DecimalField dung so le lam tron 1
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order number {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id
    