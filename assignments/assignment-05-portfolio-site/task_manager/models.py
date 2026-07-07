from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # time stamp for when the task is due
    due_date = models.DateTimeField(null=True, blank=True)

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium",
    )

    def __str__(self):
        return self.title
