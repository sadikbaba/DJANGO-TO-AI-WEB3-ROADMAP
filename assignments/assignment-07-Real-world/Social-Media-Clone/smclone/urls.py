from .models import Post, Profile
from django.urls import path
from .views import profile_detail, profile_edit

urlpatterns = [
    path("profile/<int:profile_id>/", profile_detail, name="profile_detail"),
    path("profile/<int:profile_id>/edit/", profile_edit, name="profile_edit"),
]
