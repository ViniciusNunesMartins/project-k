from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django.conf import settings 


class Dashboard(models.Model, TimeStampedModel):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class Tasks(models.Model, TitleDescriptionModel, TimeStampedModel):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=(
        ("TO DO", "TO_DO"),
        ("DOING", "DOING"),
        ("DONE", "DONE")
    ))
    