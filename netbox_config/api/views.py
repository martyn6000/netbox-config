"""
API viewsets for NetBox Config Plugin.

For more information on NetBox REST API viewsets, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#viewsets

For Django REST Framework viewsets, see:
https://www.django-rest-framework.org/api-guide/viewsets/
"""

from netbox.api.viewsets import NetBoxModelViewSet

from ..models import Config
from .serializers import ConfigSerializer


class ConfigViewSet(NetBoxModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

