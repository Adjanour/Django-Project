from django.urls import path
from .views import notifications_view,notifications_settings_view,mark_as_read

urlpatterns = [
    path('', notifications_view, name='notifications'),
    path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('settings/', notifications_settings_view, name='notifications_settings'),
]