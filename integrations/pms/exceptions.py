# Customized exceptions

class PMSAPIError(Exception):
    """
    Raised when the external PMS API request fails.
    """
    def __init__(self, message="Failed to fetch data from PMS API."):
        self.message = message
        super().__init__(self.message)


class PMSDataMappingError(Exception):
    """
    Raised when PMS response data cannot be mapped to internal data model.
    """
    def __init__(self, data=None, message="Failed to map PMS data to Booking model."):
        self.data = data
        self.message = message
        super().__init__(f"{self.message} Data: {data}")