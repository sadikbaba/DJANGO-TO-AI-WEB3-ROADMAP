from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "deployApp/home.html")

def about(request):
    return render(request, "deployApp/about.html")
    
def projects(request):
    return render(request, "deployApp/projects.html")

def contact(request):
    return render(request, "deployApp/contact.html")
