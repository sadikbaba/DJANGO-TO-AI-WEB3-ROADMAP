from django.urls import path
from .views import (
    registration_view,
    profile_detail,
    profile_edit,
    login_view,
    logout_view,
    home,
    password_reset_view,
)

urlpatterns = [
    path("profile/<int:profile_id>/", profile_detail, name="profile_detail"),
    path("profile/<int:profile_id>/edit/", profile_edit, name="profile_edit"),
    path("login/", login_view, name="login"),
    path("register/", registration_view, name="register"),
    path("", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path("password_reset/", password_reset_view, name="password_reset" ),
]
