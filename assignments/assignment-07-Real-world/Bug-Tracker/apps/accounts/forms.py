from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            "required": "Username is required",
            "unique": "This username is already taken. Please choose another one",
        },
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username", "class": "form-input"}
        ),
    )

    email = forms.EmailField(
        error_messages={
            "required": "Email address is required",
            "invalid": "Please enter a valid email address",
        },
        widget=forms.EmailInput(
            attrs={"placeholder": "example@gmail.com", "class": "form-input"}
        ),
    )

    password1 = forms.CharField(
        label="password",
        error_messages={
            "required": "Password is required",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "form-input",
            }
        ),
    )

    password2 = forms.CharField(
        label="password",
        error_messages={
            "required": "Place confirm your password.",
        },
        widget=forms.PasswordInput(
            attrs={"placeholder": "Re-enter your password", "class": "form-input"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"]

        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists")
        return email
