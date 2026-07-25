from django.urls import path
from .views import RegistrationForm

urlpatterns = [
    path("register/", RegistrationForm, "register"),
]
