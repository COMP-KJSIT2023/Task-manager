from django.contrib import admin
from .models import Supervisor, Notes, Tasks, Project

# Register your models here.
admin.site.register(Supervisor)
admin.site.register(Project)
admin.site.register(Notes)
admin.site.register(Tasks)