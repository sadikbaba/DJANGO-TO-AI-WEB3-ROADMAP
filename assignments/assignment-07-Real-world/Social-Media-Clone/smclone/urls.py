from .models import Post, Profile
from django.urls import path
from .views import profile_detail

urlpatterns = [
    path("profile/<int:profile_id>/", profile_detail , name="profile_detail"),
]

