from django import forms
from .models import Company, Job, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "description", "logo", "website", "location", "industry"]

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Enter your name.", "class": "form-input"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter your Company Description.",
                    "class": "form-input",
                }
            ),
            "website": forms.URLInput(
                attrs={"placeholder": "https://example.com", "class": "form-input"}
            ),
            "location": forms.TextInput(
                attrs={"placeholder": "Enter your location", "class": "form-input"}
            ),
            "industry": forms.TextInput(
                attrs={"placeholder": "Enter Industry", "class": "form-input"}
            ),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "requirements",
            "skills",
            "location",
            "deadline",
            "salary_negotiable",
            "salary",
            "experience_level",
            "work_type",
            "employment_type",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter job title (e.g. Senior Python Developer)",
                    "class": "form-input",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe the job role and responsibilities...",
                    "class": "form-input",
                    "rows": 5,
                }
            ),
            "requirements": forms.Textarea(
                attrs={
                    "placeholder": "List the requirements (e.g. 3+ years experience, etc.)",
                    "class": "form-input",
                    "rows": 4,
                }
            ),
            "skills": forms.Textarea(
                attrs={
                    "placeholder": "Required skills (e.g. Python, Django, PostgreSQL)",
                    "class": "form-input",
                    "rows": 3,
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Remote, Lagos, Abuja",
                    "class": "form-input",
                }
            ),
            "deadline": forms.DateInput(attrs={"type": "date", "class": "form-input"}),
            "salary": forms.NumberInput(
                attrs={"placeholder": "Enter salary amount", "class": "form-input"}
            ),
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            "required": "Username is required",
            "unique": "his username is already taken. Please choose another one.",
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
