from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup_view, name='setup_view'),
    path('setup/gender/', views.add_gender, name='add_gender'),
    path('setup/program/', views.add_program, name='add_program'),
    path('setup/transcript_type/', views.add_transcript_type, name='add_transcript_type'),
    path('setup/delivery_option/', views.add_delivery_option, name='add_delivery_option'),
    path('setup/identification_type/', views.add_identification_type, name='add_identification_type'),
    path('setup/graduate_type/', views.add_graduate_type, name='add_graduate_type'),
]
