from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm


@login_required
def project_view(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("core:dashboard")
    else:
        form = ProjectForm()
    return render(request, "projects/project.html", {"form": form})
