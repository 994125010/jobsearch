from django.contrib import admin
from .models import Work, Project, Hobby, Course

for item in (Work, Project, Hobby, Course):
    admin.site.register(item)
# Register your models here.
