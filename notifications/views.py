from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

# Create your views here.

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-date')
    return render(request, 'notifications.html', {'notifications': notifications})

# def notifications_history_view(request):
#     return render(request, 'notifications_history.html')

@login_required
def notifications_settings_view(request):
    return render(request, 'notifications_settings.html')


@login_required
def mark_as_read(request, notification_id):
    notification = Notification.objects.filter(id=notification_id).get()
    notification.is_read = True
    notification.save()
    return redirect('notifications_view_details', notification_id=notification_id)
