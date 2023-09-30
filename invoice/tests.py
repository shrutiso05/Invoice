# app_name/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceAPITestCase(TestCase):
    # tests.py
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'date': '2023-09-30',
            'customer_name': 'Test Customer',
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)  # Create an Invoice instance

        self.invoice_detail_data = {
            'invoice': self.invoice,  # Use the Invoice instance, not an integer
            'description': 'Test Description',
            'quantity': 2,
            'unit_price': '10.00',
            'price': '20.00',
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)


    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invoice_detail(self):
        response = self.client.post('/api/invoice-details/', self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more test cases for other CRUD operations and validations

