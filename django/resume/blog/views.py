from django.shortcuts import render
from .models import Blog

# Create your views here.


def all_blogs(request):
    temp = Blog.objects.order_by('-date')
    context = {
        'blogs': temp
    }
    return render(request, 'blog/all_blogs.html', context)
