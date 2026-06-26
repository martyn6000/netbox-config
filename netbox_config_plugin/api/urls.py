"""
API URL patterns for NetBox Config Plugin.

For more information on NetBox REST API routing, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#routers

For Django REST Framework routers, see:
https://www.django-rest-framework.org/api-guide/routers/
"""

from netbox.api.routers import NetBoxRouter

from .views import ConfigViewSet

app_name = "netbox_config_plugin"

router = NetBoxRouter()
router.register("configs", ConfigViewSet)

urlpatterns = router.urls

