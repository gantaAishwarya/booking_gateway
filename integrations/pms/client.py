import requests
import logging
from integrations.pms.exceptions import PMSAPIError,PMSConnectionError,PMSUnexpectedError

logger = logging.getLogger(__name__)

# TODO: Update BASE_URL
BASE_URL = 'xxxxx'

def fetch_pms_bookings():
    try:
        response = requests.get(f"{BASE_URL}/bookings.json")
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError as e:
        logger.error(f"PMS API connection failed: {e}")
        raise PMSConnectionError("Failed to connect to PMS API.")
    except requests.RequestException as e:
        logger.error(f"PMS API request failed: {e}")
        raise PMSAPIError("Failed to fetch PMS bookings.")
    except Exception as e:
        logger.error(f"Unexpected error while fetching PMS bookings: {e}")
        raise PMSUnexpectedError(str(e))