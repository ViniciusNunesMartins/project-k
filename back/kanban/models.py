from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django.conf import settings


class Dashboard(TitleDescriptionModel, TimeStampedModel):
    """
    Dashboard model
    """
    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboards"

    def __str__(self):
        return self.title


class Board(TitleDescriptionModel, TimeStampedModel):
    """
    Board model
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.title


class Column(TitleDescriptionModel, TimeStampedModel):
    """
    Column model
    """
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Column"
        verbose_name_plural = "Columns"

    def __str__(self):
        return self.title


class Card(TitleDescriptionModel, TimeStampedModel):
    """
    Card model
    """
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
    
    def __str__(self):
        return self.title


class Comment(TitleDescriptionModel, TimeStampedModel):
    """
    Comment model
    """
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.title
