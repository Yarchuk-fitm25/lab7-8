from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("planner", "0001_initial")]
    operations = [
        migrations.AddField(
            model_name="task",
            name="is_important",
            field=models.BooleanField(default=False, verbose_name="Важливе"),
        ),
    ]
