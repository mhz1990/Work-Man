# Generated by Django 4.2 on 2023-04-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(),
        ),
    ]
