from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            "project",
            "title",
            "description",
            "priority",
            "status",
            "assignee",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Ticket title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Describe the issue...",
                }
            ),
        }