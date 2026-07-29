from django.urls import path

from .views import (
    ticket_list_view,
    ticket_create_view,
    ticket_detail_view,
    ticket_edit_view,
    ticket_delete_view,
)

app_name = "tickets"

urlpatterns = [
    path(
        "",
        ticket_list_view,
        name="list",
    ),

    path(
        "create/",
        ticket_create_view,
        name="create",
    ),

    path(
        "<int:ticket_id>/",
        ticket_detail_view,
        name="detail",
    ),

    path(
        "<int:ticket_id>/edit/",
        ticket_edit_view,
        name="edit",
    ),

    path(
    "<int:ticket_id>/delete/",
    ticket_delete_view,
    name="delete",
),
]