from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.


def many_projects_func(request):
    items = Project.objects.all()
    context = {
        'projects': items
    }
    return render(request, 'the_projects.html', context)


def project_detail_func(request, project_id):
    item = get_object_or_404(Project, id=project_id)
    context = {
        'project': item
    }
    return render(request, 'project_detail.html', context)
