
# po_dashboard/models.py

from django.db import models

class PO(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    customer = models.CharField(max_length=255)
    buyer = models.CharField(max_length=255)
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('OPEN', 'Open'),
        ('DELIVERED', 'Delivered'),
        ('CLOSED', 'Closed'),
    ])
    type = models.CharField(max_length=50, choices=[
        ('IQF', 'IQF'),
        ('FRESH', 'Fresh'),
        ('OTHER', 'Other'),
    ])

    def __str__(self):
        return self.po_number


class Invoice(models.Model):
    po = models.ForeignKey(PO, related_name='invoices', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    payment_terms = models.CharField(max_length=255)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('SHORT_PAID', 'Short Paid'),
    ])
    balance_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.invoice_number
