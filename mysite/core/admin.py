from django.contrib import admin
from core.models import TaskType
from core.models import Task
from core.models import Profile

admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Profile)
