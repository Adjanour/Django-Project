from django.db import models
from TranscriptManagementSystem import settings
from accounts.models import CustomUser as User
from transcripts.models import TranscriptRequest



# Create your models here.
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    transcript_request = models.ForeignKey(TranscriptRequest, on_delete=models.CASCADE, related_name='audit_logs')


