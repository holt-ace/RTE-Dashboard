from django.db import models

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    order_date = models.DateField()
    delivery_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='OPEN')
