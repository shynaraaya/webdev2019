from django.contrib import admin
from .models import TaskList
from .models import Task

# admin.site.register(TaskList)
admin.site.register(Task)

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', )

# Register your models here.
