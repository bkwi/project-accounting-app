import datetime

from django.db import models

from projects.models.project import Project


class Worker(models.Model):
    class Meta:
        ordering = ("surname",)

    name = models.CharField(max_length=50, unique=False)
    surname = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.surname} {self.name}"


class WorkerWorkingTime(models.Model):  # -> Worker
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    hours_amount = models.PositiveIntegerField(default=0)
    price_per_hour = models.FloatField(default=0, max_length=10)

    def __str__(self):
        return f"{self.worker}"
