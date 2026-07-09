"""
Test cases for NetBox Config Plugin views.
"""

from django.urls import reverse

from ..models import Config
from ..testing import PluginViewTestCase
from ..testing.utils import disable_warnings, get_random_string


class ConfigViewTestCase(PluginViewTestCase):
    """Test Config views."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Config.objects.create(name='View Test 1')
        Config.objects.create(name='View Test 2')
        Config.objects.create(name='View Test 3')

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.base_url = 'plugins:netbox_config:config'

    def test_list_configs(self):
        """Test Config list view."""
        self.add_permissions('netbox_config.view_config')

        url = reverse('plugins:netbox_config:config_list')
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)

    def test_list_configs_without_permission(self):
        """Test Config list view without permission."""
        url = reverse('plugins:netbox_config:config_list')

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_view_config(self):
        """Test Config detail view."""
        self.add_permissions('netbox_config.view_config')

        instance = Config.objects.first()
        url = reverse('plugins:netbox_config:config', kwargs={'pk': instance.pk})
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)
        self.assertEqual(response.context['object'], instance)

    def test_create_config(self):
        """Test creating a Config via form."""
        self.add_permissions(
            'netbox_config.add_config',
            'netbox_config.view_config'
        )

        url = reverse('plugins:netbox_config:config_add')
        name = f'Created {get_random_string(10)}'

        form_data = self.post_data({
            'name': name,
        })

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was created
        instance = Config.objects.get(name=name)
        self.assertEqual(instance.name, name)

    def test_create_config_without_permission(self):
        """Test creating a Config without permission."""
        url = reverse('plugins:netbox_config:config_add')

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_edit_config(self):
        """Test editing a Config via form."""
        self.add_permissions(
            'netbox_config.change_config',
            'netbox_config.view_config'
        )

        instance = Config.objects.first()
        url = reverse('plugins:netbox_config:config_edit', kwargs={'pk': instance.pk})

        new_name = f'Edited {get_random_string(10)}'
        form_data = self.post_data({
            'name': new_name,
        })

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was updated
        instance.refresh_from_db()
        self.assertEqual(instance.name, new_name)

    def test_delete_config(self):
        """Test deleting a Config."""
        self.add_permissions(
            'netbox_config.delete_config',
            'netbox_config.view_config'
        )

        instance = Config.objects.first()
        url = reverse('plugins:netbox_config:config_delete', kwargs={'pk': instance.pk})

        # Confirm deletion
        response = self.client.post(url, {'confirm': True}, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was deleted
        self.assertFalse(
            Config.objects.filter(pk=instance.pk).exists()
        )

    def test_delete_config_without_permission(self):
        """Test deleting a Config without permission."""
        instance = Config.objects.first()
        url = reverse('plugins:netbox_config:config_delete', kwargs={'pk': instance.pk})

        with disable_warnings('django.request'):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)


class ConfigFormTestCase(PluginViewTestCase):
    """Test Config form validation."""

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.add_permissions(
            'netbox_config.add_config',
            'netbox_config.view_config'
        )

    def test_form_validation_empty_name(self):
        """Test form validation with empty name."""
        url = reverse('plugins:netbox_config:config_add')
        form_data = self.post_data({'name': ''})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should not create object
        self.assertEqual(Config.objects.filter(name='').count(), 0)

    def test_form_validation_duplicate_name(self):
        """Test form validation with duplicate name."""
        Config.objects.create(name='Duplicate')

        url = reverse('plugins:netbox_config:config_add')
        form_data = self.post_data({'name': 'Duplicate'})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should only have one instance with this name
        self.assertEqual(Config.objects.filter(name='Duplicate').count(), 1)
