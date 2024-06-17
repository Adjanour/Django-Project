from django.urls import path
from .views import notifications_view, notifications_settings_view

urlpatterns = [
    path("", notifications_view, name="notifications"),
    path("settings/", notifications_settings_view, name="notifications_settings"),
]
