from django.shortcuts import render
from django.template import loader

from .models import Work
from .models import Project
from .models import Hobby
from .models import Course

def index(request):
    work_exp = Work.objects.order_by('-end_date')[:5]
    proj_lst = Project.objects.order_by('-end_date')
    hobbies = Hobby.objects.all()
    courses = Course.objects.all()
    template = loader.get_template('resume/index.html')
    context = {
            'work_exp': work_exp,
            'proj_lst': proj_lst,
            'hobbies': hobbies,
            'courses': courses,
    }
    return render(request, 'resume/index.html', context)

