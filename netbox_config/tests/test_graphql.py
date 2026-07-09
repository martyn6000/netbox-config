"""
Test cases for NetBox Config Plugin GraphQL API.
"""
from ..models import Config
from ..testing import PluginGraphQLTestCase


class ConfigGraphQLTestCase(PluginGraphQLTestCase):
    """Test Config GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Config.objects.create(name='GraphQL Test 1')
        Config.objects.create(name='GraphQL Test 2')
        Config.objects.create(name='GraphQL Test 3')

    def test_query_config(self):
        """Test GraphQL query for a single Config."""
        self.add_permissions('netbox_config.view_config')

        instance = Config.objects.first()

        query = (
            "query { "
            "config(id: " + str(instance.pk) + ") { "
            "id name "
            "} "
            "}"
        )

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['config']
        self.assertEqual(data['id'], str(instance.pk))
        self.assertEqual(data['name'], instance.name)

    def test_query_config_list(self):
        """Test GraphQL query for list of Configs."""
        self.add_permissions('netbox_config.view_config')

        query = """
        query {
            config_list {
                id
                name
            }
        }
        """

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['config_list']
        self.assertEqual(len(data), 3)
        self.assertIn('id', data[0])
        self.assertIn('name', data[0])

    def test_query_config_with_all_fields(self):
        """Test GraphQL query with all available fields."""
        self.add_permissions('netbox_config.view_config')

        instance = Config.objects.first()

        query = (
            "query { "
            "config(id: " + str(instance.pk) + ") { "
            "id name created last_updated "
            "} "
            "}"
        )

        response = self.execute_query(query)
        self.assertIsNone(response.get('errors'))

        data = response['data']['config']
        self.assertEqual(data['id'], str(instance.pk))
        self.assertEqual(data['name'], instance.name)
        self.assertIsNotNone(data['created'])
        self.assertIsNotNone(data['last_updated'])

