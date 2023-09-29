# app_name/urls.py
from django.urls import path
from .views import (
    InvoiceListCreateView,
    InvoiceDetailView,
    InvoiceDetailListCreateView,
    InvoiceDetailDetailView,
)

urlpatterns = [
    path('invoice/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice-details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('invoice-details/<int:pk>/', InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
