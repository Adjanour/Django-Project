# transcripts/urls.py
from django.urls import path
from .views import HomePageView,register

urlpatterns = [
 path("", HomePageView.as_view(), name="home"),
path("accounts/register/",register,name="register")
 ]