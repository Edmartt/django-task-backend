from django.contrib import admin
from .tasks.models import Tasks

# Register your models here.
admin.site.register(Tasks)