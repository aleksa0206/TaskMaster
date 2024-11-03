from django.contrib import admin
from .models import Task


admin.site.site_header = 'Task Master Admin'
admin.site.register(Task)