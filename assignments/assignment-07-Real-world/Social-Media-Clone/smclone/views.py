from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    context = {
        "profile": profile,
    }

    return render(request, "smclone/profile_detail.html", context)


def profile_edit(request, profile_id):

    profile = get_object_or_404(Profile, pk=profile_id)

    if request.user != profile.user:
        return redirect("profile_detail", profile_id=profile.id)

    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile_detail", profile_id=profile.id)

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, "smclone/profile_edit.html", context)


