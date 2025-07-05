from datetime import datetime
from bookings.models import Booking
from integrations.pms.exceptions import PMSDataMappingError

def map_pms_booking(pms_data):
    try:
        return Booking(
            reservation_id=pms_data["res_id"],
            guest_first_name=pms_data["guest"]["first_name"],
            guest_last_name=pms_data["guest"]["last_name"],
            guest_email=pms_data["guest"]["email"],
            room_number=pms_data["room"]["number"],
            room_type=pms_data["room"]["type"],
            check_in=datetime.fromisoformat(pms_data["check_in"]),
            check_out=datetime.fromisoformat(pms_data["check_out"]),
            status=pms_data.get("status", Booking.STATUS_CONFIRMED),
            number_of_guests=pms_data.get("guest_count", 1),
            payment_status=pms_data.get("payment_status", Booking.PAYMENT_PENDING),
            special_requests=pms_data.get("notes", ""),
        )
    except (KeyError, ValueError, TypeError) as e:
        raise PMSDataMappingError(data=pms_data, message=str(e))
