from django.urls import path
from . import views  # Ensure views is properly imported

urlpatterns = [
    path('api/pos/', views.po_list, name='po-list'),
    path('api/invoices/', views.invoice_list, name='invoice-list'),
    path('api/upload-po/', views.upload_po, name='upload-po'),  # Assuming you have this view
]
