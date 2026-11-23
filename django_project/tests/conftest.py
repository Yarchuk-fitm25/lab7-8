from datetime import date
import pytest
from django.contrib.auth import get_user_model
from planner.models import Course, Label, Task, TaskPlan


@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username="student", password="test-pass-123")


@pytest.fixture
def course(db):
    return Course.objects.create(name="Програмування", code="PRG", semester=3, description="Практика Python")


@pytest.fixture
def label(db):
    return Label.objects.create(name="Практична", color="green", description="Практичне завдання")


@pytest.fixture
def task(course, label):
    value = Task.objects.create(
        code="T-01", title="Практична робота", summary="Робота з моделями",
        due_date=date(2026, 12, 15), course=course, priority="high"
    )
    value.labels.add(label)
    return value


@pytest.fixture
def plan(task):
    return TaskPlan.objects.create(task=task, steps="Зробити моделі і тести", planned_hours=3, notes="Перевірити")


@pytest.fixture
def web_client(client):
    return client
