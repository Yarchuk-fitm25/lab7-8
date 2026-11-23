from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["code", "title", "summary", "due_date", "course", "priority", "labels"]
        widgets = {"due_date": forms.DateInput(attrs={"type": "date"})}
