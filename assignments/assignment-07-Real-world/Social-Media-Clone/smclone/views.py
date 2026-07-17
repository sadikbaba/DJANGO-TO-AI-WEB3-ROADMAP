from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, LoginForm, RegisterForm
from .models import Profile, Post
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.


def registration_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Registration successful! You can now log in.",
            )
            return redirect("login")

    context = {"form": form}
    return render(request, "smclone/register.html", context)


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    context = {"form": form}

    return render(request, "smclone/login.html", context)


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    context = {
        "profile": profile,
    }

    return render(request, "smclone/profile_detail.html", context)


@login_required
def profile_edit(request, profile_id):

    profile = get_object_or_404(Profile, pk=profile_id)

    if request.user != profile.user:
        return redirect("profile_detail", profile_id=profile.id)

    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile_detail", profile_id=profile.id)

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, "smclone/profile_edit.html", context)


@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")

    context = {
        "posts": posts,
    }
    return render(request, "smclone/home.html", context)



def logout_view(request):
    logout(request)

    return redirect("login")