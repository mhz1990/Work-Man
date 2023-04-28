from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm
from tasks.models import Task

# from projects.models import Project

# from tasks.models import Task


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm

    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    show_my_tasks = Task.objects.filter(assignee=request.user)
    # show_my_tasks = Task.objects.filter(project_id=1)

    context = {
        "show_my_tasks": show_my_tasks,
        # "show_my_tasks_2": Task.objects.filter(assignee=request.user),
    }
    return render(request, "tasks/show_my_tasks.html", context)
