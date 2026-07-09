"""
Navigation menu items for NetBox Config Plugin.

For more information on navigation menus, see:
https://netbox.dev
"""

from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from django.utils.translation import gettext_lazy as _

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_config:config_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

# 1. Define the separate menu items
config_item = PluginMenuItem(
    link="plugins:netbox_config:config_list",
    link_text="Running Config",
    buttons=plugin_buttons,
    permissions=['netbox_config.view_config'],
    staff_only=True,
)

# 2. Register a top-level standalone sidebar menu
menu = PluginMenu(
    label=_('SCB Configurations'),
    icon_class='mdi mdi-tune-vertical', # Root menu icon
    groups=(
        (_('Configurations'), (config_item,)), # (Group Header, Iterable of items)
    ),
)
