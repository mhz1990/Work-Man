from django.db import models
from django.conf import settings

# from tasks.models import Task

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )
    # project_tasks2 = models.ForeignKey(
    #     "tasks.Task",
    #     related_name="project_tasks2",
    #     on_delete=models.CASCADE,
    #     null=True,
    # )

    def __str__(self):
        return self.name
