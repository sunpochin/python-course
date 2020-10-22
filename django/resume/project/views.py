from django.shortcuts import render
from .models import Project
# Create your views here.


def index(request):
    myprojects = Project.objects.all()
    context = {
        'projects': myprojects
    }
    return render(request, 'project/index.html', context)
