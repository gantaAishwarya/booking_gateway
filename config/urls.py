"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# ------------------------------------------------------------------------------
# Swagger/OpenAPI Schema Setup
# ------------------------------------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Straiv API",
        default_version='v1',
        description="Straiv Demo API Documentation",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@straiv.net"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your apps’ API URLs, so they are modular and maintainable
    path("api/", include('bookings.urls')),
    path("api/", include('integrations.pms.urls')),

    # Swagger/OpenAPI docs endpoints
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),

]

# ------------------------------------------------------------------------------
# Admin Site Customization
# ------------------------------------------------------------------------------
admin.site.site_header = "Straiv Super Admin"
admin.site.site_title = "Straiv"
admin.site.index_title = "Straiv Super Admin"
