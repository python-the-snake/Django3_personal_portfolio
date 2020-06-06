from django.shortcuts import render
from .models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    # limiting seems blogs to 5
    return render(request, 'blog/blogs.html', {'blogs':blogs})


