from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "completed",
        "priority",
    ]

    ordering = ["-created_at"]

    ordering_fields = [
        "created_at",
        "priority",
        "due_date",
    ]

    search_fields = [
        "title",
        "description",
    ]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
