from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    ProfileForm,
    LoginForm,
    RegisterForm,
    UsernameRecoveryForm,
    UsernameRecoveryCodeForm,
    PostForm,
    CommentForm,
)
from .models import Profile, Post, User, UsernameRecoveryCode
from django.contrib.auth import login, logout
from django.contrib import messages
import secrets
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.http import JsonResponse

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


def logout_view(request):
    logout(request)

    return redirect("login")


def username_reset_view(request):

    if request.method == "POST":
        form = UsernameRecoveryForm(request.POST)
    else:
        form = UsernameRecoveryForm()

    if form.is_valid():
        email = form.cleaned_data["email"]
        user = User.objects.filter(email=email).first()
        # if true should redirect here to page where will paste the otp, then if otp is valid username appear am i on the way?

        if user:
            otp = str(secrets.randbelow(1_000_000)).zfill(6)
            expires_at = timezone.now() + timedelta(minutes=5)
            recovery_code = UsernameRecoveryCode.objects.create(
                user=user, code=otp, expires_at=expires_at
            )

            request.session["username_recovery_code_id"] = recovery_code.id
            send_mail(
                subject="Your user name recovery code",
                message=f"Your username recovery code is: {otp}",
                from_email=None,
                recipient_list=[user.email],
            )

            return redirect("Verify_username")

        else:
            print("user doest not exit")

    context = {"form": form}

    return render(request, "smclone/username_reset.html", context)


def verify_username_view(request):

    if request.method == "POST":
        form = UsernameRecoveryCodeForm(request.POST)
    else:
        form = UsernameRecoveryCodeForm()

    if form.is_valid():
        recovery_code_id = request.session.get("username_recovery_code_id")
        if recovery_code_id:
            recovery_code = UsernameRecoveryCode.objects.filter(
                id=recovery_code_id
            ).first()
            if recovery_code:
                submitted_code = form.cleaned_data["code"]
                if submitted_code == recovery_code.code:
                    if timezone.now() < recovery_code.expires_at:
                        username = recovery_code.user.get_username()
                        recovery_code.delete()
                        request.session.pop("username_recovery_code_id", None)
                        context = {
                            "form": form,
                            "username": username,
                        }
                        return render(
                            request, "smclone/username_otp_verify.html", context
                        )
                    else:
                        recovery_code.delete()

                        request.session.pop("username_recovery_code_id", None)
                        form.add_error("code", "This recovery code has expired")
                else:
                    form.add_error("code", "Invalid recovery code.")
            else:
                form.add_error("code", "The recovery code is no longer valid.")
        else:
            form.add_error("code", "No active recovery request was found")

    context = {"form": form}

    return render(request, "smclone/username_otp_verify.html", context)


@login_required
def home(request):
    posts = Post.objects.prefetch_related("comments").order_by("-created_at")
    comment_form = CommentForm()

    return render(
        request,
        "smclone/home.html",
        {
            "posts": posts,
            "comment_form": comment_form,
        },
    )


def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "smclone/create_post.html", {"form": form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)

        return JsonResponse(
            {
                "liked": False,
                "like_count": post.likes.count(),
            }
        )

    post.likes.add(request.user)

    return JsonResponse(
        {
            "liked": True,
            "like_count": post.likes.count(),
        }
    )


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.user = request.user

            comment.post = post

            comment.save()

    return redirect("home")
