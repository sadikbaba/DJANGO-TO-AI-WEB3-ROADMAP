from django import forms
from .models import Company


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
