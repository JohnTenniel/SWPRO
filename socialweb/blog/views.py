from django.shortcuts import render
from . models import Blog

def blog(request):
    bg = Blog.objects.all()
    context = {'blog': bg}
    return render(request, "blog/mainblog.html", context)
