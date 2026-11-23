from django.core.mail import send_mail


def send_task_notice(email, title):
    return send_mail(
        "Нагадування про завдання",
        f"Не забудьте виконати: {title}",
        "noreply@localhost",
        [email],
        fail_silently=False,
    )
