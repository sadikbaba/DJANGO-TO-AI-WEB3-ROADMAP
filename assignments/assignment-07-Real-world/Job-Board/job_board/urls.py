from django.urls import path
from .views import (
    company_list_view,
    company_detail_view,
    company_create_view,
    job_create_view,
    job_detail_view,
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path("companies/", company_list_view, name="companies"),
    path("companies/<int:company_id>/", company_detail_view, name="company_detail"),
    path("companies/create/", company_create_view, name="company_create"),
    path("companies/<int:company_id>/jobs/create/", job_create_view, name="create_job"),
    path("jobs/<int:job_id>/", job_detail_view, name="jobs_detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
