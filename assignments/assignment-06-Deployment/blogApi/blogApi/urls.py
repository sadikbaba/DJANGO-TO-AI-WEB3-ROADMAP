from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, UserRegistrationView, CurrentUserView, CommentViewSet,LikeViewSet, PostDetailView,  BookmarkViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)
router.register("bookmarks", BookmarkViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("me/", CurrentUserView.as_view(), name="current-user"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
