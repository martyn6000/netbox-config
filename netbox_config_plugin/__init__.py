"""
NetBox Config Plugin

Plugin configuration for NetBox Config Plugin.

For a complete list of PluginConfig attributes, see:
https://docs.netbox.dev/en/stable/plugins/development/#pluginconfig-attributes
"""

__author__ = """Martyn Stanton"""
__email__ = "martynstanton@hotmail.com"
__version__ = "1.0"


from netbox.plugins import PluginConfig


class ConfigConfig(PluginConfig):
    name = "netbox_config_plugin"
    verbose_name = "NetBox Config Plugin"
    description = "NetBox plugin for Config."
    author= "Martyn Stanton"
    author_email = "martynstanton@hotmail.com"
    version = __version__
    base_url = "netbox_config_plugin"
    min_version = "4.5.0"
    max_version = "4.5.99"
    graphql_schema = "graphql.schema"


config = ConfigConfig
