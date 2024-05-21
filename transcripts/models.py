from django.db import models
from accounts.models import CustomUser
from accounts.models import StudentProfile

class TranscriptRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile = models.OneToOneField(StudentProfile,on_delete=models.PROTECT)
    delivery_email = models.EmailField()
    delivery_address = models.TextField()
    number_of_transcripts = models.IntegerField(default=1)
    transcript_type = models.CharField(max_length=20, choices=[
        ('OFFICIAL', 'Official'),
        ('UNOFFICIAL', 'Unofficial')
    ], default='OFFICIAL')
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected')
    ], default='PENDING')

    def __str__(self):
        return f"Transcript Request by {self.profile.first_name} {self.profile.last_name}"
