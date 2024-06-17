from django.shortcuts import render
from accounts.models import StudentProfile
from .models import Notification

# Create your views here.


def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by("-date")
    return render(request, "notifications.html", {"notifications": notifications})


# def notifications_history_view(request):
#     return render(request, 'notifications_history.html')


def notifications_settings_view(request):
    return render(request, "notifications_settings.html")
