from django.contrib import admin
from .models import Dashboard, Tasks


@admin.register(Dashboard, Tasks)
class KanbanAdmin(admin.ModelAdmin):
    pass