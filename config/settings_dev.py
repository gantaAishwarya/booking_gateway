from .settings_base import *

# ------------------------------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
# NEVER use this key in production
# ------------------------------------------------------------------------------
SECRET_KEY = env.str(
    "SECRET_KEY",
    default="django-insecure-36_4n+f^f$#goaw7j1la^13i32n&7l+=1gc3ak851%tqv1@jzd"
)

# ------------------------------------------------------------------------------
# Debug mode (turn OFF in production!)
# ------------------------------------------------------------------------------
DEBUG = True

# ------------------------------------------------------------------------------
# Caching - local memory cache, suitable for development only
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "dev-cache",
    }
}

# TTL for cache: 2 hours
CACHE_TTL = 60 * 60 * 2

# ------------------------------------------------------------------------------
# Admin URL - easier to change if needed
# ------------------------------------------------------------------------------
ADMIN_URL = "admin/"
