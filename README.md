# Invoice
# Invoice Management System

This is a simple Invoice Management System built using Django and Django Rest Framework.

## Features

- Create and manage invoices.
- Add and edit invoice details.
- List all invoices and their details.
- Delete invoices and invoice details.

## Getting Started

Follow these steps to get started with the project:

1. Clone this repository:

git clone https://github.com/shrutiso05/Invoice

Install project dependencies:
pip install -r requirements.txt

Run the development server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Access the API at http://localhost:8000/api/

##API Endpoints
List Invoices: /api/invoices/ (GET)

Create Invoice: /api/invoices/ (POST)

Retrieve Invoice: /api/invoices/<int:pk>/ (GET)

Update Invoice: /api/invoices/<int:pk>/ (PUT)

Delete Invoice: /api/invoices/<int:pk>/ (DELETE)

List Invoice Details: /api/invoice-details/ (GET)

Create Invoice Detail: /api/invoice-details/ (POST)

Retrieve Invoice Detail: /api/invoice-details/<int:pk>/ (GET)

Update Invoice Detail: /api/invoice-details/<int:pk>/ (PUT)

Delete Invoice Detail: /api/invoice-details/<int:pk>/ (DELETE)


## Testing
To run tests, use the following command:

python manage.py test
