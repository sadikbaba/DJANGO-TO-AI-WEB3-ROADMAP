from rest_framework import viewsets, filters
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["category"]

    search_fields = [
        "title" ,"content",
    ]

    ordering_fields = ["title", "created_at", "updated_at"]

    ordering = ["-created_at"]
