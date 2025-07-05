from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'reservation_id',
        'guest_first_name',
        'guest_last_name',
        'room_number',
        'check_in',
        'check_out',
        'status',
        'payment_status',
    )
    search_fields = ('reservation_id', 'guest_last_name', 'guest_email')
    list_filter = ('status', 'payment_status', 'check_in', 'room_type')
    ordering = ('-check_in',)
    date_hierarchy = 'check_in'