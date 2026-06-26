"""
GraphQL schema for NetBox Config Plugin.

For more information on NetBox GraphQL, see:
https://docs.netbox.dev/en/stable/plugins/development/graphql/

For Strawberry GraphQL documentation, see:
https://strawberry.rocks/
"""

from typing import List

import strawberry
import strawberry_django

from .models import Config


@strawberry_django.type(
    Config,
    fields='__all__',
)
class ConfigType:
    """GraphQL type for Config model."""
    pass


@strawberry.type(name="Query")
class ConfigQuery:
    """GraphQL queries for NetBox Config Plugin."""

    config: ConfigType = strawberry_django.field()
    config_list: List[ConfigType] = strawberry_django.field()


schema = [
    ConfigQuery,
]

