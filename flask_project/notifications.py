import smtplib


def send_task_notice(email, title):
    message = f"Subject: Task reminder\n\nRemember: {title}"
    with smtplib.SMTP("localhost", 1025, timeout=3) as server:
        server.sendmail("noreply@localhost", [email], message)
    return True
