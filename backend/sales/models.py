from django.db import models
from customers.models import Customer
from inventory.models import Product

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product1', null=True, blank=True)
    quantity1 = models.PositiveIntegerField(null=True, blank=True)
    selling_price1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product2', null=True, blank=True)
    quantity2 = models.PositiveIntegerField(null=True, blank=True)
    selling_price2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    # Add more products as needed
    grand_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.product1:
            self.selling_price1 = self.selling_price1 or self.product1.selling_price
            if self.selling_price1 < self.product1.buying_price:
                raise ValueError("Selling price cannot be less than buying price")
            self.total_price1 = self.quantity1 * self.selling_price1
        if self.product2:
            self.selling_price2 = self.selling_price2 or self.product2.selling_price
            if self.selling_price2 < self.product2.buying_price:
                raise ValueError("Selling price cannot be less than buying price")
            self.total_price2 = self.quantity2 * self.selling_price2
        self.grand_total_price = (self.total_price1 or 0) + (self.total_price2 or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Sale {self.id} - {self.customer.name}'
