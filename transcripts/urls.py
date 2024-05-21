# transcripts/urls.py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_transcript, name='request_transcript'),
    path('request/success/', views.transcript_request_success, name='transcript_request_success'),
]
