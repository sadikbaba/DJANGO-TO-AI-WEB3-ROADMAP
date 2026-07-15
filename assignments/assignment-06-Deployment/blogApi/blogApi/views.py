from rest_framework import viewsets, filters, permissions, generics
from .models import Post, Category, Comment, Like, Bookmark
from .serializers import (
    PostSerializer,
    CategorySerializer,
    UserRegistrationSerializer,
    CurrentUserSerializer,
    CommentSerializer,
    LikeSerializer,
    BookmarkSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Allow filtering by post
    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get("post")
        if post_id:
            queryset = queryset.filter(post=post_id)
        return queryset


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views += 1
        post.save(update_fields=["views"])
        return super().get(request, *args, **kwargs)
