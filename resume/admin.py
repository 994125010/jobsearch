from django.contrib import admin
from .models import Work, Project, Hobby, Course, Education

for item in (Work, Project, Hobby, Course, Education):
    admin.site.register(item)
# Register your models here.
