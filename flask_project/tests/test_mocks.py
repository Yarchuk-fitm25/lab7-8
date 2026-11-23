from unittest.mock import patch
from notifications import send_task_notice


def test_external_email_mock(user):
    with patch("notifications.smtplib.SMTP") as mocked_smtp:
        result = send_task_notice(user["email"], "Практична робота")
    mocked_smtp.assert_called_once_with("localhost", 1025, timeout=3)
    mocked_smtp.return_value.__enter__.return_value.sendmail.assert_called_once_with(
        "noreply@localhost", ["student@example.com"],
        "Subject: Task reminder\n\nRemember: Практична робота"
    )
    assert result is True


def test_internal_year_mock(client):
    with patch("app.current_year", return_value=2033) as mocked_year:
        response = client.get("/")
    mocked_year.assert_called_once_with()
    assert "2033" in response.get_data(as_text=True)
