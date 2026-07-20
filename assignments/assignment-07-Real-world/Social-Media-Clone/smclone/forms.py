from django import forms
from .models import Profile, User, Post, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator


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


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            "required": "Username is required.",
            "unique": "This username is already taken. Please choose another one.",
        },
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Username can only contain letters, numbers, and underscores.",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "form-input",
            }
        ),
    )

    email = forms.EmailField(
        error_messages={
            "required": "Email address is required.",
            "invalid": "Please enter a valid email address.",
        },
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@gmail.com",
                "class": "form-input",
            }
        ),
    )

    password1 = forms.CharField(
        label="Password",
        error_messages={
            "required": "Password is required.",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter you password",
                "class": "form-input",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm password",
        error_messages={
            "required": "Please confirm your password.",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Re-enter your password",
                "class": "form-input",
            }
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
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
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
            }
        ),
    )

    password = forms.CharField(
        error_messages={
            "required": "Please enter your password.",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "form-input",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.error_messages["invalid_login"] = "Username or password is incorrect."


class UsernameRecoveryForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        required=True,
        error_messages={
            "required": "Please enter your email address.",
            "invalid": "Please enter a valid email address",
        },
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your registered email", "class": "form-input"}
        ),
    )


class UsernameRecoveryCodeForm(forms.Form):
    code = forms.CharField(
        label="Recovery code",
        required=True,
        error_messages={
            "required": "Please enter a recovery code",
            "invalid": "Please enter a valid code",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your 6-digit recovery code",
                "class": "form-input",
                "max-length": "6",
            }
        ),
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "What's on your mind?",
                    "rows": 5,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        content = cleaned_data.get("content")
        image = cleaned_data.get("image")

        if not content and not image:
            raise forms.ValidationError(
                "Your post must contain text, an image, or both."
            )

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ["content"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Write a comment...",
                    "rows": 3,
                }
            ),
        }
