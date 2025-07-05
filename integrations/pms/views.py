from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integrations.pms.client import fetch_pms_bookings
from integrations.pms.mapper import map_pms_booking
from bookings.serializers import BookingSerializer
from integrations.pms.exceptions import PMSBaseException

class PMSBookingIntegrationView(APIView):
    """
    GET /api/integrations/pms/bookings/
    Fetches and maps booking data from a mocked PMS API.
    """

    def get(self, request, *args, **kwargs):
        try:
            raw_data = fetch_pms_bookings()
            mapped_bookings = [map_pms_booking(b) for b in raw_data]
            serializer = BookingSerializer(mapped_bookings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PMSBaseException as e:
            return e.to_response()

