from django.db import models
from accounts.models import CustomUser
from accounts.models import StudentProfile

class TranscriptRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile = models.ForeignKey(StudentProfile,on_delete=models.PROTECT,unique=False)
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
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    payment_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed')
    ], default='PENDING')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transcript Request {self.id} by {self.profile.first_name} {self.profile.last_name}"
