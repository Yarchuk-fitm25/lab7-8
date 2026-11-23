from datetime import date
import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from planner.models import Course, Label, Task, TaskPlan

pytestmark = pytest.mark.django_db


def test_course_creation(course):
    assert Course.objects.get(code="PRG").name == "Програмування"


def test_string_representation(course, label, task, plan):
    assert str(course) == "Програмування"
    assert str(label) == "Практична"
    assert str(task) == "Практична робота"
    assert str(plan).startswith("План:")


def test_default_status(task):
    assert task.status == "todo"
    assert task.is_important is False


def test_max_length(course):
    course.name = "А" * 81
    with pytest.raises(ValidationError):
        course.full_clean()


def test_unique_course_code(course):
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Course.objects.create(name="Інший предмет", code="PRG", semester=2)


def test_many_to_many(task, label):
    assert list(task.labels.all()) == [label]
    assert list(label.tasks.all()) == [task]


def test_one_to_one_and_cascade(task, plan):
    assert task.plan == plan
    task.delete()
    assert TaskPlan.objects.count() == 0


def test_protect_course(task, course):
    with pytest.raises(ProtectedError):
        course.delete()


@pytest.mark.parametrize("priority", ["low", "medium", "high"])
def test_priority_variants(course, priority):
    task = Task.objects.create(
        code=f"P-{priority}", title="Навчальне завдання", summary="Перевірка",
        due_date=date(2026, 12, 20), course=course, priority=priority
    )
    assert task.priority == priority
