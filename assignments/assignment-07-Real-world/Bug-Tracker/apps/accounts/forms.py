from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        label="Password",
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
        label="Password",
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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        error_messages={
            "required": "Please enter your username.",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
                "class": "form-input",
            },
        ),
    )
    password = forms.CharField(
        error_messages={"required": "Please enter your password"},
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "form-input"}
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["invalid_login"] = "Username or password is incorrect."


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar",
            "bio",
            "website",
            "location",
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Enter your bio",
                    "class": "form-input",
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "placeholder": "https://yourwebsite.com",
                    "class": "form-input",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "City, Country",
                    "class": "form-input",
                }
            ),
            "avatar": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                }
            ),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]
