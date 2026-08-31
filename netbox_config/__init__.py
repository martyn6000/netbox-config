"""
NetBox Config Plugin

Plugin configuration for NetBox Config Plugin.

For a complete list of PluginConfig attributes, see:
https://docs.netbox.dev/en/stable/plugins/development/#pluginconfig-attributes
"""

__author__ = """Martyn Stanton"""
__email__ = "martynstanton@hotmail.com"
__version__ = "1.1"


from netbox.plugins import PluginConfig


class ConfigConfig(PluginConfig):
    name = "netbox_config"
    verbose_name = "SCB Netbox configurations'"
    description = "SCB Configuration management plugin for Netbox"
    author= "Martyn Stanton"
    author_email = "martynstanton@hotmail.com"
    version = __version__
    base_url = "configs"
    min_version = "4.3.0"
    max_version = "4.5.99"
    graphql_schema = "graphql.schema"

config = ConfigConfig
