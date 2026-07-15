from django.shortcuts import render
from .models import Profile

# Create your views here.


def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    context = {
        "profile": profile,
    }

    return render(request, "smclone/profile_detail.html", context)
