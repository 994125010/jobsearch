from django.contrib import admin
from .models import *

for item in (Work, Project, Hobby, Course, Education, Skill):
    admin.site.register(item)
# Register your models here.
