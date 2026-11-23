from datetime import date
import pytest
from app import create_app
from models import Course, Label, Task, TaskPlan, db


@pytest.fixture
def app(tmp_path):
    application = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-only-secret-key",
        "WTF_CSRF_ENABLED": False,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(tmp_path / "test.db").replace("\\", "/"),
    })
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture
def course(app):
    course = Course(name="Програмування", code="PRG", semester=3, description="Практика Python")
    db.session.add(course)
    db.session.commit()
    return course


@pytest.fixture
def label(app):
    label = Label(name="Практична", color="green", description="Практичне завдання")
    db.session.add(label)
    db.session.commit()
    return label


@pytest.fixture
def task(course, label):
    task = Task(code="T-01", title="Практична робота", summary="Робота з моделями",
                due_date=date(2026, 12, 15), course_id=course.id, priority="high")
    task.labels.append(label)
    db.session.add(task)
    db.session.commit()
    return task


@pytest.fixture
def plan(task):
    plan = TaskPlan(task_id=task.id, steps="Створити моделі і тести", planned_hours=3, notes="Перевірити")
    db.session.add(plan)
    db.session.commit()
    return plan


@pytest.fixture
def user():
    return {"email": "student@example.com"}
