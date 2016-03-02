from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Work
from .models import Project
from .models import Hobby
from .models import Course
from .models import Education

def index(request):
    template_name = 'resume/index.html'
    context_object_name = 'hobbies'
    work_exp = Work.objects.order_by('-end_date')[:5]
    proj_lst = Project.objects.order_by('-end_date')
    hobbies = Hobby.objects.all()
    courses = Course.objects.all()
    education = Education.objects.all()
    template = loader.get_template('resume/index.html')
    context = {
            'education': education,
            'work_exp': work_exp,
            'proj_lst': proj_lst,
            'hobbies': hobbies,
            'courses': courses,
            'false': False,
            'true': True,
    }
    return render(request, 'resume/index.html', context)

