from django import forms
from .models import Profile


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
