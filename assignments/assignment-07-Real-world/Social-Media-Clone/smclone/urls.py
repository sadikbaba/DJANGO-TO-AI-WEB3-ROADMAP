from django.urls import path
from .views import (
    registration_view,
    profile_detail,
    profile_edit,
    login_view,
    logout_view,
    home,
    username_reset_view,
    verify_username_view,
    create_post_view,
    like_post,
    add_comment,
)

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("profile/<int:profile_id>/", profile_detail, name="profile_detail"),
    path("profile/<int:profile_id>/edit/", profile_edit, name="profile_edit"),
    path("login/", login_view, name="login"),
    path("register/", registration_view, name="register"),
    path("", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="smclone/password_reset.html",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="smclone/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="smclone/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/completed/",
        PasswordResetCompleteView.as_view(
            template_name="smclone/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path("username_reset/", username_reset_view, name="username_reset"),
    path(
        "username_reset/Verify_username/",
        verify_username_view,
        name="Verify_username",
    ),
    path("create_post/", create_post_view, name="create_post"),
    path(
        "post/<int:post_id>/like/",
        like_post,
        name="like_post",
    ),
    path(
        "comment/<int:post_id>/",
        add_comment,
        name="add_comment",
    ),
]
