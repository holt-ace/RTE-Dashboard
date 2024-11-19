
# po_dashboard/views.py

from rest_framework.viewsets import ModelViewSet
from .models import PO, Invoice
from .serializers import POSerializer, InvoiceSerializer

class POViewSet(ModelViewSet):
    queryset = PO.objects.all()
    serializer_class = POSerializer


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
