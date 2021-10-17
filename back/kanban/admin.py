from django.contrib import admin
from .models import Dashboard, Task


@admin.register(Dashboard, Task)
class KanbanAdmin(admin.ModelAdmin):
    pass