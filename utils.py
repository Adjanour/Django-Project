from notifications.models import Notification
from accounts.models import CustomUser

def send_notification(user, message,type='INFO'):
    notification = Notification.objects.create(user=user, message=message,type=type)
    notification.save()
