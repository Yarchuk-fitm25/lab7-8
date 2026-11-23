from models import Task


def test_home_page(client, task):
    response = client.get("/")
    assert response.status_code == 200
    assert "Практична робота" in response.get_data(as_text=True)


def test_task_list(client, task):
    response = client.get("/tasks/?status=todo")
    assert response.status_code == 200
    assert "Практична робота" in response.get_data(as_text=True)


def test_detail_missing(client):
    assert client.get("/tasks/9999/").status_code == 404


def test_add_task_success(client, course):
    response = client.post("/tasks/add/", data={
        "code": "WEB-1", "title": "Робота з формою", "summary": "Додати нове завдання",
        "due_date": "2026-12-25", "course_id": str(course.id), "priority": "medium"
    })
    assert response.status_code == 302
    assert Task.query.filter_by(code="WEB-1").first() is not None


def test_add_task_invalid(client, course):
    response = client.post("/tasks/add/", data={
        "code": "", "title": "", "summary": "", "due_date": "", "course_id": str(course.id), "priority": "medium"
    })
    assert response.status_code == 200
    assert "Вкажіть назву" in response.get_data(as_text=True)
    assert Task.query.count() == 0
