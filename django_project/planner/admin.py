from django.contrib import admin
from .models import Course, Label, Task, TaskPlan

admin.site.register(Course)
admin.site.register(Label)
admin.site.register(Task)
admin.site.register(TaskPlan)
