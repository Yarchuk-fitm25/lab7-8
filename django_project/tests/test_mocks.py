from unittest.mock import patch
import pytest
from django.urls import reverse
from planner.notifications import send_task_notice


def test_external_email_mock():
    with patch("planner.notifications.send_mail", return_value=1) as mocked_mail:
        result = send_task_notice("student@example.com", "Практична робота")
    mocked_mail.assert_called_once_with(
        "Нагадування про завдання",
        "Не забудьте виконати: Практична робота",
        "noreply@localhost",
        ["student@example.com"],
        fail_silently=False,
    )
    assert result == 1


@pytest.mark.django_db
def test_internal_year_mock(web_client):
    with patch("planner.views.current_year", return_value=2033) as mocked_year:
        response = web_client.get(reverse("planner:home"))
    mocked_year.assert_called_once_with()
    assert "2033" in response.content.decode("utf-8")
