import os
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from django.db.models import Avg, Count, Q
from planner.models import Course, Label, Task, TaskPlan


def main():
    course, _ = Course.objects.update_or_create(
        code="DEMO-PRG", defaults={"name": "Основи програмування", "semester": 3, "description": "Python"}
    )
    label, _ = Label.objects.get_or_create(name="Домашнє", defaults={"color": "blue", "description": "Робота вдома"})
    first, _ = Task.objects.update_or_create(code="DEMO-1", defaults={
        "title": "Створити таблиці", "summary": "Робота з Django ORM", "due_date": date(2026, 12, 15),
        "course": course, "priority": "high", "status": "todo", "is_important": True,
    })
    second, _ = Task.objects.update_or_create(code="DEMO-2", defaults={
        "title": "Написати тести", "summary": "Перевірка PyTest", "due_date": date(2026, 12, 18),
        "course": course, "priority": "medium", "status": "doing", "is_important": False,
    })
    first.labels.add(label)
    TaskPlan.objects.update_or_create(task=first, defaults={"steps": "Створити моделі; перевірити ORM", "planned_hours": 3})
    print("1 CREATE:", Task.objects.filter(code__startswith="DEMO-").count(), "завдання")
    print("2 READ:", Task.objects.get(code="DEMO-1").title)
    first.status = "doing"
    first.save()
    print("3 UPDATE:", first.get_status_display())
    print("4 FILTER:", list(Task.objects.filter(priority="high").values_list("code", flat=True)))
    print("5 EXCLUDE:", list(Task.objects.exclude(status="done").filter(code__startswith="DEMO-").values_list("code", flat=True)))
    print("6 Q (OR):", list(Task.objects.filter(Q(priority="high") | Q(is_important=True)).filter(code__startswith="DEMO-").values_list("code", flat=True)))
    print("7 AGGREGATE:", TaskPlan.objects.aggregate(average_hours=Avg("planned_hours")))
    print("8 ANNOTATE:", list(Course.objects.filter(code="DEMO-PRG").annotate(total=Count("tasks")).values_list("name", "total")))
    print("9 ЗВОРОТНИЙ ЗВ'ЯЗОК:", list(course.tasks.values_list("title", flat=True)))
    print("10 SELECT_RELATED:", [(task.title, task.course.name) for task in Task.objects.filter(code__startswith="DEMO-").select_related("course")])
    print("11 PREFETCH_RELATED:", [(task.title, [tag.name for tag in task.labels.all()]) for task in Task.objects.filter(code__startswith="DEMO-").prefetch_related("labels")])
    second.delete()
    print("12 DELETE: залишилось", Task.objects.filter(code__startswith="DEMO-").count())


if __name__ == "__main__":
    main()
