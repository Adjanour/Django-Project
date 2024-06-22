from notifications.models import Notification
from accounts.models import CustomUser

def send_notification(user,title, message,type='INFO'):
    notification = Notification.objects.create(user=user,title=title, message=message,type=type)
    notification.save()

def mark_as_read(user,notification_id):
    notification = Notification.objects.filter(id=notification_id).get()
    notification.is_read = True
    notification.save()