"""
Filtersets for NetBox Config Plugin.

For more information on NetBox filtersets, see:
https://docs.netbox.dev/en/stable/plugins/development/filtersets/

For django-filters documentation, see:
https://django-filter.readthedocs.io/
"""

from netbox.filtersets import NetBoxModelFilterSet

from .models import Config


class ConfigFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Config
        fields = ("id", "device", "config")

    def search(self, queryset, device, value):
        return queryset.filter(device__icontains=value)
