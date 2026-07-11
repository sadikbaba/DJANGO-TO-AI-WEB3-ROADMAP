from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, UserRegistrationView
from django.urls import path, include

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegistrationView.as_view(), name="register")
]
