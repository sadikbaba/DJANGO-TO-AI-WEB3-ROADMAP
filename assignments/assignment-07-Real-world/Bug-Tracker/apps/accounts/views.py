from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    RegistrationForm,
    LoginForm,
    ProfileForm,
    UserForm,
    PasswordResetRequestForm,
)
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile

# Create your views here.


def registration_view(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")  # we will create later
    else:
        form = RegistrationForm()

    return render(request, "accounts/registration.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("core:dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


def home_view(request):

    return render(
        request,
        "core/landing.html",
    )


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        user_form = UserForm(
            request.POST,
            instance=request.user,
        )

        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form
            return redirect("accounts:profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "profile": profile,
        },
    )


def password_reset_view(request):

    if request.method == "POST":

        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                from_email=None,
                email_template_name="accounts/password_reset_email.html",
            )
            return redirect("accounts:password_reset_done")
    else:
        form = PasswordResetRequestForm()

    return render(request, "accounts/reset_password.html", {"form": form})
