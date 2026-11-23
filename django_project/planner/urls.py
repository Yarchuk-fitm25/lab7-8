from django.urls import path
from . import views

app_name = "planner"
urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
]
