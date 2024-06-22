# transcripts/urls.py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transcripts/request', views.transcript_request_view, name='request_transcript'),
    path('transcripts/request/edit/<int:request_id>',views.edit_transcript_request_view,name="edit_transcript"),
    path('transcripts/request/edit',views.edit_transcript_request_view,name="edit_transcript_post"),
    path('transcripts/history', views.transcript_request_history_view, name='transcript_request_history'),
    path('transcripts/status', views.transcript_status_view, name='transcript_status'),
]

