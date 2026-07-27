from django.urls import path
from .views import registration_view, login_view, logout_view, home_view, profile_view

app_name = "accounts"
urlpatterns = [
    path("register/", registration_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home", home_view, name="home"),
    path("profile/", profile_view, name="profile"),
]
