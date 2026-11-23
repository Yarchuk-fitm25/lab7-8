from django.db import models


class Course(models.Model):
    name = models.CharField("Назва предмета", max_length=80)
    code = models.CharField("Код предмета", max_length=15, unique=True)
    semester = models.PositiveSmallIntegerField("Семестр", default=1)
    description = models.TextField("Опис", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

    def __str__(self):
        return self.name


class Label(models.Model):
    COLOR_CHOICES = [
        ("blue", "Синій"), ("green", "Зелений"), ("orange", "Помаранчевий")
    ]
    name = models.CharField("Назва позначки", max_length=40, unique=True)
    color = models.CharField("Колір", max_length=10, choices=COLOR_CHOICES, default="blue")
    description = models.CharField("Пояснення", max_length=150, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Позначка"
        verbose_name_plural = "Позначки"

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [("low", "Низький"), ("medium", "Середній"), ("high", "Високий")]
    STATUS_CHOICES = [("todo", "Заплановано"), ("doing", "Виконується"), ("done", "Виконано")]
    code = models.CharField("Код завдання", max_length=20, unique=True)
    title = models.CharField("Назва", max_length=120)
    summary = models.TextField("Опис завдання")
    due_date = models.DateField("Термін виконання")
    priority = models.CharField("Пріоритет", max_length=10, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField("Стан", max_length=10, choices=STATUS_CHOICES, default="todo")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="tasks", verbose_name="Предмет")
    labels = models.ManyToManyField(Label, blank=True, related_name="tasks", verbose_name="Позначки")
    is_important = models.BooleanField("Важливе", default=False)

    class Meta:
        ordering = ["due_date", "title"]
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"

    def __str__(self):
        return self.title


class TaskPlan(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="plan", verbose_name="Завдання")
    steps = models.TextField("План виконання")
    planned_hours = models.PositiveSmallIntegerField("Планові години", default=1)
    resource_url = models.URLField("Посилання на матеріали", blank=True)
    notes = models.TextField("Нотатки", blank=True)

    class Meta:
        ordering = ["task_id"]
        verbose_name = "План завдання"
        verbose_name_plural = "Плани завдань"

    def __str__(self):
        return f"План: {self.task.title}"
