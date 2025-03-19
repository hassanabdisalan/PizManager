from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        Customer.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            address="123 Main St"
        )

    def test_customer_creation(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone, "1234567890")
        self.assertEqual(customer.address, "123 Main St")

    def test_customer_str(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(str(customer), "John Doe")