from django.test import TestCase
from .models import Sale
from customers.models import Customer
from inventory.models import Inventory

class SaleModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            address="123 Main St"
        )
        self.product = Inventory.objects.create(
            product_name="Test Product",
            category="Test Category",
            price=10.00,
            stock_quantity=100
        )
        self.sale = Sale.objects.create(
            customer=self.customer,
            product=self.product,
            quantity=2,
            total_price=20.00
        )

    def test_sale_creation(self):
        self.assertEqual(self.sale.customer.name, "John Doe")
        self.assertEqual(self.sale.product.product_name, "Test Product")
        self.assertEqual(self.sale.quantity, 2)
        self.assertEqual(self.sale.total_price, 20.00)

    def test_sale_str(self):
        self.assertEqual(str(self.sale), f'Sale {self.sale.sale_id} - {self.sale.customer.name}')

    def test_sale_total_price_calculation(self):
        self.sale.quantity = 3
        self.sale.total_price = self.sale.quantity * self.sale.product.price
        self.sale.save()
        self.assertEqual(self.sale.total_price, 30.00)