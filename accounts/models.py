# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    # add additional fields in here
    profile = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, null=True, blank=True)


class StudentProfile(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  other_names = models.CharField(max_length=30, blank=True)
  profile_image = models.ImageField(upload_to='profile_images/', blank=True)  
  student_id = models.CharField(max_length=20)
  step = models.IntegerField(default=1)
  graduation_year = models.DateField(blank=True, null=True)
  verification_document = models.FileField(upload_to='verification_documents/', blank=True)
  verification_status = models.CharField(max_length=20, choices=(
      ('PENDING', 'Pending'),
      ('VERIFIED', 'Verified'),
      ('REJECTED', 'Rejected'),
  ), default='PENDING')