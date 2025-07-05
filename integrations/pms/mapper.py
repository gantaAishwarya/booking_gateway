from datetime import datetime
from bookings.models import Booking
from integrations.pms.exceptions import PMSDataMappingError


def parse_date(date_str, field_name, data):
    try:
        return datetime.fromisoformat(date_str)
    except Exception as e:
        raise PMSDataMappingError(data=data, message=f"Invalid date in '{field_name}': {e}")

def map_pms_booking(pms_data):
    try:
        required_fields = ["res_id", "guest", "room", "check_in", "check_out"]
        for field in required_fields:
            if field not in pms_data:
                raise PMSDataMappingError(data=pms_data, message=f"Missing required field: {field}")

        guest = pms_data.get("guest", {})
        room = pms_data.get("room", {})

        return Booking(
            reservation_id=pms_data["res_id"],
            guest_first_name=guest.get("first_name"),
            guest_last_name=guest.get("last_name"),
            guest_email=guest.get("email"),
            room_number=room.get("number"),
            room_type=room.get("type"),
            check_in=datetime.fromisoformat(pms_data["check_in"]),
            check_out=datetime.fromisoformat(pms_data["check_out"]),
            status=pms_data.get("status", Booking.STATUS_CONFIRMED),
            number_of_guests=pms_data.get("guest_count", 1),
            payment_status=pms_data.get("payment_status", Booking.PAYMENT_PENDING),
            special_requests=pms_data.get("notes", ""),
        )
    except (KeyError, TypeError) as e:
        raise PMSDataMappingError(data=pms_data, message=f"Mapping error: {e}")