from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application, Company
from .forms import CompanyForm, JobForm, RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

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


def job_detail_view(request, job_id):

    job = get_object_or_404(Job, pk=job_id)

    return render(request, "job_board/job_detail.html", {"job": job})


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "job_board/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("")  # i dont where to redirect
    else:
        form = LoginForm()
    return render(request, "job_board/login.html", {"form": form})


def logout_view(request):
    logout(request)

    return redirect("login")
