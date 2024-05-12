# transcripts/urls.py
from django.urls import path
from .views import HomePageView,register,verify_student,edit_profile,profile

urlpatterns = [
 path("", HomePageView.as_view(), name="home"),
 path("accounts/register/",register,name="register"),
 path("accounts/verify/<int:student_pk>/",verify_student,name="verify_student"),
 path("accounts/edit_profile/",edit_profile,name="edit_profile"),
 path("accounts/profile/",profile,name="profile"),
 ]