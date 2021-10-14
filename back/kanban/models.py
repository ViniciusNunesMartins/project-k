from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django.conf import settings
from django.utils import timezone


class Dashboard(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Tasks(TitleDescriptionModel, TimeStampedModel, models.Model):
    status_choices =(
        ("TO DO", "TO_DO"),
        ("DOING", "DOING"),
        ("DONE", "DONE")
    )

    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="creator")
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="responsible")
    deadline = models.DateField(default=timezone.now)
    status = models.CharField(max_length=5, status_choices)

    def __str__(self):
        return f"{self.title} - {self.status}: {self.deadline}" 
    