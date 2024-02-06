from django.contrib import admin
from .models import Supervisor, Notes, User, Tasks

# Register your models here.
admin.site.register(Supervisor)
admin.site.register(Notes)
admin.site.register(User)
admin.site.register(Tasks)