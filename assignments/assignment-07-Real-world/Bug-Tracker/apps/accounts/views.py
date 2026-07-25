from django.shortcuts import render, redirect
from .forms import RegistrationForm

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
