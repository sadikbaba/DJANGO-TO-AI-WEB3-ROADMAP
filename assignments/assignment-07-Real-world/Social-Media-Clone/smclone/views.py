from django.shortcuts import render, get_object_or_404
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

    context = {
        "profile" : profile,
    }

    return render(request, "smclone/profile_edit.html", context)

