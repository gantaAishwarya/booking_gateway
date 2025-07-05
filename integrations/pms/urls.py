from django.urls import path
from integrations.pms.views import PMSBookingIntegrationView

urlpatterns = [
    path("integrations/pms/bookings/", PMSBookingIntegrationView.as_view(), name="pms-bookings"),
]