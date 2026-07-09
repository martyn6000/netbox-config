"""
Tables for NetBox Config Plugin.

For more information on NetBox tables, see:
https://docs.netbox.dev/en/stable/plugins/development/tables/

For django-tables2 documentation, see:
https://django-tables2.readthedocs.io/
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .models import Config


class ConfigTable(NetBoxTable):
    device = tables.Column(linkify=True)
    config = tables.Column()
    config_format = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Config
        fields = ("pk", "id","config","config_format","device", "actions")
        default_columns = ("config_format", "config", "device")
