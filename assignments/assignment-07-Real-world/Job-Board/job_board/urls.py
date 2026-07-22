from django.urls import path
from .views import company_list_view, company_detail_view, company_create_view

urlpatterns = [
    path("companies/", company_list_view, name="companies"),
    path("companies/<int:company_id>/", company_detail_view, name="company_detail"),
    path("companies/create/", company_create_view, name="company_create")
]
