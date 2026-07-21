from django.urls import path
from .views import company_list_view

urlpatterns = [
    path("companies/", company_list_view, name="companies" ),
]