from notifications.models import Notification
from .models import StudentProfile

def user_profile_picture(request):
    if request.user.is_authenticated:
        profile = StudentProfile.objects.filter(user=request.user).first()
        return {'profile_picture_url': profile.profile_image.url if profile and profile.profile_image else None}
    return {}

def user_notifications_count(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
        return {'notifications_count': notifications.filter(is_read=False).count()}
    return {}