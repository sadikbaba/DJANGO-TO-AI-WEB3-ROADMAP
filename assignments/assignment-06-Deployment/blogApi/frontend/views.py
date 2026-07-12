from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "frontend/home.html")


def login_page(request):
    return render(request, "frontend/login.html")


def register_page(request):
    return render(request, "frontend/register.html")
