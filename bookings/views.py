from rest_framework import viewsets
from bookings.serializers import BookingSerializer
import logging
from .models import Booking

logger = logging.getLogger(__name__)

class BookingViewSet(viewsets.ModelViewSet):
    """
    General CRUD operations for bookings:
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer