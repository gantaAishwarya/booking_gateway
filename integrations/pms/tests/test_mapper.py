from django.test import TestCase
from integrations.pms.mapper import map_pms_booking
from bookings.models import Booking
from integrations.pms.exceptions import PMSDataMappingError


class TestMapPMSBooking(TestCase):

    def get_base_pms_data(self, overrides=None):
        data = {
            "res_id": "R000",
            "guest": {"first_name": "John", "last_name": "Doe", "email": "john@example.com"},
            "room": {"number": "100", "type": "Standard"},
            "check_in": "2025-07-01T15:00:00",
            "check_out": "2025-07-05T11:00:00",
            "status": "confirmed",
            "guest_count": 2,
            "payment_status": "paid",
            "notes": "Near elevator"
        }
        if overrides:
            data.update(overrides)
        return data

    def test_valid_booking_mapping(self):
        raw_data = self.get_base_pms_data()
        booking = map_pms_booking(raw_data)

        self.assertIsInstance(booking, Booking)
        self.assertEqual(booking.reservation_id, raw_data["res_id"])
        self.assertEqual(booking.guest_first_name, raw_data["guest"]["first_name"])
        self.assertEqual(booking.room_type, raw_data["room"]["type"])
        self.assertEqual(str(booking.check_in), "2025-07-01 15:00:00")

    def test_missing_required_field_res_id(self):
        data = self.get_base_pms_data()
        del data["res_id"]
        with self.assertRaises(PMSDataMappingError) as ctx:
            map_pms_booking(data)
        self.assertIn("res_id", str(ctx.exception))

    def test_null_guest_and_room_fields(self):
        data = self.get_base_pms_data()
        data["guest"] = {"first_name": None, "last_name": None, "email": None}
        data["room"] = {"number": None, "type": None}

        booking = map_pms_booking(data)
        self.assertIsNone(booking.guest_first_name)
        self.assertIsNone(booking.room_number)

    def test_empty_input(self):
        with self.assertRaises(PMSDataMappingError):
            map_pms_booking({})

    def test_missing_check_in(self):
        data = self.get_base_pms_data()
        del data["check_in"]
        with self.assertRaises(PMSDataMappingError):
            map_pms_booking(data)