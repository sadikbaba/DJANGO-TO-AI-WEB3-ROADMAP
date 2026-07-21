from django.shortcuts import render
from .models import Job, Application, Company

# Create your views here.


def company_list_view(request):

    companies = Company.objects.all()

    return render(request, "job_board/company_list.html", {"companies": companies})
