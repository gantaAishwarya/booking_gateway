from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integrations.pms.client import fetch_pms_bookings
from integrations.pms.mapper import map_pms_booking
from bookings.serializers import BookingSerializer
from bookings.models import Booking
from integrations.pms.exceptions import PMSDuplicateReservationError, PMSBaseException
from django.db import IntegrityError


class PMSBookingIntegrationView(APIView):
    """
    GET: Fetch and map PMS bookings, return existing DB entries if present.
    POST: Fetch, map, and save new bookings to the database.
    """
        
    def get(self, request, *args, **kwargs):
        try:
            raw_data = fetch_pms_bookings()
            bookings_to_return = []

            for entry in raw_data:
                reservation_id = entry.get("res_id")

                # Try to fetch existing booking
                existing = Booking.objects.filter(reservation_id=reservation_id).first()

                if existing:
                    bookings_to_return.append(existing)
                else:
                    mapped = map_pms_booking(entry)
                    bookings_to_return.append(mapped)

            serializer = BookingSerializer(bookings_to_return, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except PMSBaseException as e:
            return e.to_response()

    def post(self, request, *args, **kwargs):
        try:
            raw_data = fetch_pms_bookings()
            created_bookings = []
            existing_res_ids = []

            for entry in raw_data:
                reservation_id = entry.get("res_id")
                # Check if booking already exists
                existing = Booking.objects.filter(reservation_id=reservation_id).first()
                if existing:
                    existing_res_ids.append(reservation_id)
                    continue
                
                booking = map_pms_booking(entry)
                booking.save()
                created_bookings.append(booking)

            serializer = BookingSerializer(created_bookings, many=True)
            response_data = {
            "created": serializer.data,
            "skipped_existing_reservations": existing_res_ids
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        except PMSBaseException as e:
            return e.to_response()
        except IntegrityError as e:
            duplicate_error = PMSDuplicateReservationError()
            return duplicate_error.to_response()
