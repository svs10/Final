from django.contrib import admin

# Register your models here.

from .models import Project, Remarks

# Register your models here.
admin.site.register(Project)
admin.site.register(Remarks)