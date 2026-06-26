"""
URL patterns for NetBox Config Plugin.

For more information on URL routing, see:
https://docs.netbox.dev/en/stable/plugins/development/views/#url-registration

For Django URL patterns, see:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    path("configs/", views.ConfigListView.as_view(), name="config_list"),
    path("configs/add/", views.ConfigEditView.as_view(), name="config_add"),
    path("configs/<int:pk>/", views.ConfigView.as_view(), name="config"),
    path("configs/<int:pk>/edit/", views.ConfigEditView.as_view(), name="config_edit"),
    path("configs/<int:pk>/delete/", views.ConfigDeleteView.as_view(), name="config_delete"),
    path(
        "configs/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="config_changelog",
        kwargs={"model": models.Config},
    ),
)
