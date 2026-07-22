from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application, Company
from .forms import CompanyForm, JobForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def company_list_view(request):

    companies = Company.objects.all()

    return render(request, "job_board/company_list.html", {"companies": companies})

def company_detail_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    jobs = Job.objects.filter(company=company)

    return render(
        request,
        "job_board/company_detail.html",
        {
            "company": company,
            "jobs": jobs,
        },
    )

@login_required
def company_create_view(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)

        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()

            return redirect("companies")
    else:
        form = CompanyForm()

    return render(request, "job_board/company_create.html", {"form": form})





@login_required
def job_create_view(request, company_id):

    company = get_object_or_404(
        Company,
        pk=company_id,
        owner=request.user,
    )
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()

            return redirect("company_detail", company_id=company.id)
    else:
        form = JobForm()

    return render(
        request,
        "job_board/job_create.html",
        {
            "form": form,
            "company": company,
        },
    )
