from django.test import TestCase
from .models import Inventory

class InventoryModelTest(TestCase):

    def setUp(self):
        Inventory.objects.create(product_name="Test Product", category="Test Category", price=10.00, stock_quantity=100)

    def test_inventory_creation(self):
        product = Inventory.objects.get(product_name="Test Product")
        self.assertEqual(product.category, "Test Category")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.stock_quantity, 100)

    def test_inventory_stock_update(self):
        product = Inventory.objects.get(product_name="Test Product")
        product.stock_quantity = 80
        product.save()
        self.assertEqual(product.stock_quantity, 80)

    def test_inventory_price_update(self):
        product = Inventory.objects.get(product_name="Test Product")
        product.price = 12.00
        product.save()
        self.assertEqual(product.price, 12.00)