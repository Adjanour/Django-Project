from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    type = models.CharField(max_length=20, choices=[
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error')
    ], default='INFO')
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title