from django.urls import path
from .views import landing_view, dashboard_view

app_name = "core"
urlpatterns = [
    path("", landing_view, name="landing"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
