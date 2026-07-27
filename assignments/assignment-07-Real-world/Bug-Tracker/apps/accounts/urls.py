from django.urls import path
from .views import (
    registration_view,
    login_view,
    logout_view,
    home_view,
    profile_view,
    password_reset_view,
)

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"
urlpatterns = [
    path("register/", registration_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home", home_view, name="home"),
    path("profile/", profile_view, name="profile"),
    path("reset_password/", password_reset_view, name="reset_password"),
    path(
        "reset-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy("accounts:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
