"""
Forms for NetBox Config Plugin.

For more information on NetBox forms, see:
https://docs.netbox.dev/en/stable/plugins/development/forms/
"""

from netbox.forms import NetBoxModelForm

from .models import Config


class ConfigForm(NetBoxModelForm):
    class Meta:
        model = Config
        fields = ("name", "tags")
