from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProjectForm


# Create your views here.
@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)


@login_required
def show_project(request, id):
    show_project = get_object_or_404(Project, id=id)
    context = {
        "show_project": show_project,
    }
    return render(request, "projects/show_project.html", context)
