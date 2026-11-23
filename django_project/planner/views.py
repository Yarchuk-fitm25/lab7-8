from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Course, Task
from .utils import current_year


def home(request):
    tasks = Task.objects.select_related("course").order_by("due_date")[:5]
    return render(request, "planner/home.html", {
        "courses_count": Course.objects.count(),
        "tasks": tasks,
        "year": current_year(),
    })


def task_list(request):
    tasks = Task.objects.select_related("course").prefetch_related("labels")
    status = request.GET.get("status", "")
    if status in {"todo", "doing", "done"}:
        tasks = tasks.filter(status=status)
    return render(request, "planner/task_list.html", {
        "tasks": tasks,
        "status": status,
        "year": current_year(),
    })


def task_detail(request, task_id):
    task = get_object_or_404(Task.objects.select_related("course").prefetch_related("labels"), pk=task_id)
    return render(request, "planner/task_detail.html", {"task": task, "year": current_year()})


def add_task(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Завдання успішно додано.")
        return redirect("planner:task_list")
    return render(request, "planner/add_task.html", {"form": form, "year": current_year()})
