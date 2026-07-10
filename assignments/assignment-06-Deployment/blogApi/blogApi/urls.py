from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]