from django.shortcuts import render, redirect
from .forms import ProjectFrom
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def project_view(request):

    if request.method == "POST":
        form = ProjectFrom(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("core:dashboard")
    else:
        form = ProjectFrom()

    return render(request, "projects/project.html", {"form": form, "project": project})
