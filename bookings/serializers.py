from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        check_in = data.get('check_in', getattr(self.instance, 'check_in', None))
        check_out = data.get('check_out', getattr(self.instance, 'check_out', None))

        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError("Check-out must be after check-in.")
        return data

    def validate_number_of_guests(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of guests must be greater than zero.")
        return value

    def validate_guest_email(self, value):
        return value.lower()
