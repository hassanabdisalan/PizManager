from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.selling_price < self.buying_price:
            raise ValueError("Selling price cannot be less than buying price")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
