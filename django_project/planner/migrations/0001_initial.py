from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, verbose_name="Назва предмета")),
                ("code", models.CharField(max_length=15, unique=True, verbose_name="Код предмета")),
                ("semester", models.PositiveSmallIntegerField(default=1, verbose_name="Семестр")),
                ("description", models.TextField(blank=True, verbose_name="Опис")),
            ],
            options={"ordering": ["name"], "verbose_name": "Предмет", "verbose_name_plural": "Предмети"},
        ),
        migrations.CreateModel(
            name="Label",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40, unique=True, verbose_name="Назва позначки")),
                ("color", models.CharField(choices=[("blue", "Синій"), ("green", "Зелений"), ("orange", "Помаранчевий")], default="blue", max_length=10, verbose_name="Колір")),
                ("description", models.CharField(blank=True, max_length=150, verbose_name="Пояснення")),
            ],
            options={"ordering": ["name"], "verbose_name": "Позначка", "verbose_name_plural": "Позначки"},
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=20, unique=True, verbose_name="Код завдання")),
                ("title", models.CharField(max_length=120, verbose_name="Назва")),
                ("summary", models.TextField(verbose_name="Опис завдання")),
                ("due_date", models.DateField(verbose_name="Термін виконання")),
                ("priority", models.CharField(choices=[("low", "Низький"), ("medium", "Середній"), ("high", "Високий")], default="medium", max_length=10, verbose_name="Пріоритет")),
                ("status", models.CharField(choices=[("todo", "Заплановано"), ("doing", "Виконується"), ("done", "Виконано")], default="todo", max_length=10, verbose_name="Стан")),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="tasks", to="planner.course", verbose_name="Предмет")),
                ("labels", models.ManyToManyField(blank=True, related_name="tasks", to="planner.label", verbose_name="Позначки")),
            ],
            options={"ordering": ["due_date", "title"], "verbose_name": "Завдання", "verbose_name_plural": "Завдання"},
        ),
        migrations.CreateModel(
            name="TaskPlan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("steps", models.TextField(verbose_name="План виконання")),
                ("planned_hours", models.PositiveSmallIntegerField(default=1, verbose_name="Планові години")),
                ("resource_url", models.URLField(blank=True, verbose_name="Посилання на матеріали")),
                ("notes", models.TextField(blank=True, verbose_name="Нотатки")),
                ("task", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="plan", to="planner.task", verbose_name="Завдання")),
            ],
            options={"ordering": ["task_id"], "verbose_name": "План завдання", "verbose_name_plural": "Плани завдань"},
        ),
    ]
