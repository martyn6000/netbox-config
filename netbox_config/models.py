"""
Models for NetBox Config Plugin.

For more information on NetBox models, see:
https://docs.netbox.dev/en/stable/plugins/development/models/

For NetBox model features (tags, custom fields, change logging, etc.), see:
https://docs.netbox.dev/en/stable/development/models/#netbox-model-features
"""

from django.db import models
from django.db.models import UniqueConstraint # Import this
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class ConfigFormat(ChoiceSet):
    CHOICES = (
        ('yaml', 'YAML', 'green'),
        ('json', 'JSON', 'cyan'),
        ('raw', 'RAW', 'blue'),
    )

class Config(NetBoxModel):
    config_format = models.CharField(
        max_length=30,
        choices=ConfigFormat,
        default='raw'
    )
    config = models.TextField()
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='plugin_configs' # Changed to plural for clarity
    )
    
    class Meta:
        app_label = "netbox_config"
        ordering = ("device", "config_format") # Updated ordering
        verbose_name_plural = "Configs"
        
        # Enforce uniqueness per device + format combination
        constraints = [
            UniqueConstraint(
                fields=['device', 'config_format'], 
                name='%(app_label)s_%(class)s_unique_device_format'
            )
        ]

    def __str__(self):
        return f"{self.device.name or f'Device #{self.device.pk}'} ({self.get_config_format_display()})"

    def get_absolute_url(self):
        return reverse("plugins:netbox_config:config", args=[self.pk])

