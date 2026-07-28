from django.urls import path
from .views import (
    project_view,
    project_list_view,
    project_detail_view,
    project_edit_view,
    project_delete_view,
)

app_name = "projects"

urlpatterns = [
    path("create/", project_view, name="create"),
    path("", project_list_view, name="list"),
    path("<int:pk>/", project_detail_view, name="detail"),
    path("<int:pk>/edit/", project_edit_view, name="edit"),
    path("<int:pk>/delete/", project_delete_view, name="delete"),
]
