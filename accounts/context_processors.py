from .models import StudentProfile

def user_profile_picture(request):
    if request.user.is_authenticated:
        profile = StudentProfile.objects.filter(user=request.user).first()
        return {'profile_picture_url': profile.profile_image.url if profile and profile.profile_image else None}
    return {}
