"""
Views for NetBox Config Plugin.

For more information on NetBox views, see:
https://docs.netbox.dev/en/stable/plugins/development/views/

For generic view classes, see:
https://docs.netbox.dev/en/stable/development/views/
"""

from netbox.views import generic
from dcim.models import Device
from utilities.views import ViewTab, register_model_view
from . import filtersets, forms, models, tables
from .models import (
    Config,
)

class ConfigView(generic.ObjectView):
    queryset = models.Config.objects.all()


class ConfigListView(generic.ObjectListView):
    queryset = models.Config.objects.all()
    table = tables.ConfigTable
    filterset = filtersets.ConfigFilterSet


class ConfigEditView(generic.ObjectEditView):
    queryset = models.Config.objects.all()
    form = forms.ConfigForm


class ConfigDeleteView(generic.ObjectDeleteView):
    queryset = models.Config.objects.all()

@register_model_view(Device, name='Configs', path='config')
class DeviceConfigTabView(generic.ObjectChildrenView):
    queryset = Device.objects.all()
    child_model = Config
    table = tables.ConfigTable
    filterset = filtersets.ConfigFilterSet
    template_name = 'netbox_config/config_tab.html'

    tab = ViewTab(
        label='Configs',
        badge=lambda obj: Config.objects.filter(device=obj).count(), 
        weight=500,         
        hide_if_empty=False 
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(device=parent)
    
    def get_extra_context(self, request, instance):
        # 1. Capture the format directly from the URL query string (?format=yaml)
        requested_format = request.GET.get('format')
        valid_formats = ['json', 'yaml', 'raw']

        # 2. Determine the active format to use
        if requested_format in valid_formats:
            active_format = requested_format
            # Optional: persist choice to user profile configuration if logged in
            if request.user.is_authenticated:
                request.user.config.set('data_format', active_format, commit=True)
        elif request.user.is_authenticated:
            # Fallback to user's saved preference
            active_format = request.user.config.get('data_format', 'json')
        else:
            # Hard fallback default
            active_format = 'json'

        # 3. Filter children explicitly by the active format string 
        # (e.g., matching 'yaml', 'json', or 'raw' from your ChoiceSet)
        children = self.get_children(request, parent=instance)
        selected_config = children.filter(config_format=active_format).first()
        
        # 4. Extract the config text body safely
        device_config_text = selected_config.config if selected_config else None

        return {
            'device_config': device_config_text,
            'format': active_format,
        }