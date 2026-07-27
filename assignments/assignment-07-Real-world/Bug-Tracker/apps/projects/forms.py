from django import forms
from .models import Project


class ProjectFrom(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Project name",
                    "class": "form-input",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe this project...",
                    "class": "form-input",
                    "rows": 5,
                }
            ),
        }

    def clean_name(self):
        """
        Validate the project name.
        """

        name = self.cleaned_data["name"].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                "Project name must be at least 3 characters long."
            )
        return name
