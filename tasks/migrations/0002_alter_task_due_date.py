# Generated by Django 4.2 on 2023-04-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(),
        ),
    ]