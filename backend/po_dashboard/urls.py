from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Enables the admin panel
    path('api/', include('po_dashboard.urls')),  # Your app's API endpoints
]
