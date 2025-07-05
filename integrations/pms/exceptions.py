from rest_framework.response import Response
from rest_framework import status


class PMSBaseException(Exception):
    """Base exception for PMS errors."""

    def __init__(self, message=None):
        self.message = message or "An error occurred in PMS integration."
        super().__init__(self.message)

    def to_response(self):
        """Return a DRF Response for this exception."""
        return Response(
            {"error": self.message},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
class PMSUnexpectedError(PMSBaseException):
    """Raised for unexpected errors in PMS integration."""

    def __init__(self, message=None):
        super().__init__(message or "Unexpected error occurred in PMS integration.")

    def to_response(self):
        return Response(
            {"error": "Unexpected error", "details": self.message},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

class PMSConnectionError(PMSBaseException):
    """Raised when there's a connection error with PMS API."""

    def __init__(self, message=None):
        super().__init__(message or "Failed to connect to PMS API.")

    def to_response(self):
        return Response(
            {"error": self.message},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )

class PMSAPIError(PMSBaseException):
    """Raised when the external PMS API request fails."""

    def __init__(self, message=None):
        super().__init__(message or "Failed to fetch data from PMS API.")

    def to_response(self):
        return Response(
            {"error": self.message},
            status=status.HTTP_502_BAD_GATEWAY,
        )

class PMSDataMappingError(PMSBaseException):
    """Raised when PMS response data cannot be mapped to internal data model."""

    def __init__(self, data=None, message=None):
        self.data = data
        message = message or "Failed to map PMS data to Booking model."
        full_message = f"{message} Data: {data}" if data else message
        super().__init__(full_message)

    def to_response(self):
        return Response(
            {"error": self.message, "data": self.data},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
class PMSDuplicateReservationError(PMSBaseException):
    """Raised when a duplicate reservation_id is detected during creation."""

    def __init__(self, message=None):
        super().__init__(message or "Duplicate reservation detected.")

    def to_response(self):
        return Response(
            {"error": self.message},
            status=status.HTTP_409_CONFLICT,
        )