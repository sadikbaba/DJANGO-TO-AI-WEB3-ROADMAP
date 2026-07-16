from django import forms
from .models import Profile, User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "display_name",
            "bio",
            "location",
            "website",
            "profile_picture",
        ]

        widgets = {
            "display_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your display name",
                    "class": "form-input",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "tell us about your self",
                    "class": "form-input",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "where do you live",
                    "class": "form-input",
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com",
                    "class": "form-input",
                }
            ),
        }

        error_messages = {
            "website": {
                "invalid": "Please enter a valid website URL.",
            },
        }

    def clean_display_name(self):
        display_name = self.cleaned_data["display_name"]

        if len(display_name) < 3:
            raise forms.ValidationError(
                "Display name must be at least 3 characters long."
            )

        return display_name


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "form-input",
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "form-input",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@gmail.com",
                "class": "form-input",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter you password",
                "class": "form-input",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Re-enter your password",
                "class": "form-input",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
