from datetime import date
import pytest
from sqlalchemy.exc import IntegrityError
from models import Course, Label, Task, TaskPlan, db


def test_course_creation(course):
    assert db.session.get(Course, course.id).name == "Програмування"


def test_string_representation(course, label, task, plan):
    assert str(course) == "Програмування"
    assert str(label) == "Практична"
    assert str(task) == "Практична робота"
    assert str(plan).startswith("План:")


def test_default_status(task):
    assert task.status == "todo"
    assert task.is_important is False


def test_unique_code(course):
    db.session.add(Course(name="Інший предмет", code="PRG", semester=1))
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()


def test_many_to_many(task, label):
    assert label in task.labels
    assert task in label.tasks


def test_one_to_one_and_cascade(task, plan):
    plan_id = plan.id
    db.session.delete(task)
    db.session.commit()
    assert db.session.get(TaskPlan, plan_id) is None


@pytest.mark.parametrize("priority", ["low", "medium", "high"])
def test_priority_variants(course, priority):
    task = Task(code=f"P-{priority}", title="Навчальне завдання", summary="Перевірка",
                due_date=date(2026, 12, 20), course_id=course.id, priority=priority)
    db.session.add(task)
    db.session.commit()
    assert task.priority == priority


def test_required_field(course):
    task = Task(code="NO-TITLE", title=None, summary="Немає назви",
                due_date=date(2026, 12, 20), course_id=course.id)
    db.session.add(task)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()
