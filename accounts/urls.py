# transcripts/urls.py
from django.urls import path
from .views import HomePageView, register, verify_student, profile, submit_profile

urlpatterns = [
    path("", HomePageView, name="home"),
    path("accounts/register/", register, name="register"),
    path("accounts/verify/<int:student_pk>/", verify_student, name="verify_student"),
    path("accounts/profile/<int:step>", profile, name="profile"),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/profile/submit", submit_profile, name="profile_submit"),
]
