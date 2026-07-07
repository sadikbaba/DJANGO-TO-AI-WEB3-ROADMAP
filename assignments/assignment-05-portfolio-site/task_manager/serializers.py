from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Task

        fields = [
            "id",
            "author",
            "title",
            "description",
            "completed",
            "due_date",
            "priority",
            "created_at",
        ]
