from rest_framework import viewsets, filters, permissions, generics
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, UserRegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["category"]

    search_fields = [
        "title",
        "content",
    ]

    ordering_fields = ["title", "created_at", "updated_at"]

    ordering = ["-created_at"]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
