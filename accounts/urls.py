# transcripts/urls.py
from django.urls import path
from .views import HomePageView,register,verify_profile,profile,submit_profile

urlpatterns = [
 path("", HomePageView, name="home"),
 path("accounts/register/",register,name="register"),
 path("accounts/verify/<int:profile_id>/",verify_profile,name="verify_profile"),
 path("accounts/profile/<int:step>",profile,name="profile"),
 path("accounts/profile/", profile, name="profile"),
 path("accounts/profile/submit",submit_profile,name="profile_submit")
]