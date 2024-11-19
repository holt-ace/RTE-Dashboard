
# po_dashboard/serializers.py

from rest_framework import serializers
from .models import PO, Invoice

class POSerializer(serializers.ModelSerializer):
    class Meta:
        model = PO
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
