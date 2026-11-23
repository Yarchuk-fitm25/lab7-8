from datetime import date
import pytest
from django.urls import reverse
from planner.models import Task

pytestmark = pytest.mark.django_db


def test_home_page(web_client, task):
    response = web_client.get(reverse("planner:home"))
    assert response.status_code == 200
    assert "planner/home.html" in [template.name for template in response.templates]
    assert "Практична робота" in response.content.decode("utf-8")


def test_task_list_filter(web_client, task):
    response = web_client.get(reverse("planner:task_list"), {"status": "todo"})
    assert response.status_code == 200
    assert "Практична робота" in response.content.decode("utf-8")


def test_task_detail_missing(web_client):
    response = web_client.get(reverse("planner:task_detail", args=[9999]))
    assert response.status_code == 404


def test_create_task_success(web_client, course):
    response = web_client.post(reverse("planner:add_task"), {
        "code": "WEB-1", "title": "Робота з формою", "summary": "Додати нове завдання",
        "due_date": "2026-12-25", "course": str(course.id), "priority": "medium"
    })
    assert response.status_code == 302
    assert Task.objects.filter(code="WEB-1").exists()


def test_create_task_invalid(web_client, course):
    response = web_client.post(reverse("planner:add_task"), {
        "code": "", "title": "", "summary": "", "due_date": "", "course": str(course.id)
    })
    assert response.status_code == 200
    assert not Task.objects.exists()
    assert response.context["form"].errors
