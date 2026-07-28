from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

from .forms import ProjectForm


@login_required
def project_view(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("projects:list")
    else:
        form = ProjectForm()
    return render(request, "projects/project.html", {"form": form})


@login_required
def project_list_view(request):

    projects = Project.objects.filter(owner=request.user).order_by("-created_at")

    return render(
        request,
        "projects/project_list.html",
        {
            "projects": projects,
        },
    )


@login_required
def project_detail_view(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user,
    )

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
        },
    )


@login_required
def project_edit_view(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":

        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects:detail", pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(
        request, "projects/project_edit.html", {"form": form, "project": project}
    )


@login_required
def project_delete_view(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        project.delete()
        return redirect("projects:list")

    return render(
        request,
        "projects/project_delete.html",
        {
            "project": project,
        },
    )
