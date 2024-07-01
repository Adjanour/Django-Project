from django.urls import path

from system import admin_views
from . import views

urlpatterns = [
    path('setup/', views.setup_view, name='setup_view'),
    path('setup/gender/', views.add_gender, name='add_gender'),
    path('setup/program/', views.add_program, name='add_program'),
    path('setup/transcript_type/', views.add_transcript_type, name='add_transcript_type'),
    path('setup/delivery_option/', views.add_delivery_option, name='add_delivery_option'),
    path('setup/identification_type/', views.add_identification_type, name='add_identification_type'),
    path('setup/graduate_type/', views.add_graduate_type, name='add_graduate_type'),
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage-transcript-types/', admin_views.manage_transcript_types, name='manage_transcript_types'),
    path('admin/manage-genders/', admin_views.manage_genders, name='manage_genders'),
    path('admin/manage-programs/', admin_views.manage_programs, name='manage_programs'),
    path('admin/manage-delivery-options/', admin_views.manage_delivery_options, name='manage_delivery_options'),
    path('admin/process-transcript-request/<int:request_id>/', admin_views.process_transcript_request, name='process_transcript_request'),
]
