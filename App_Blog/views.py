from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    # Retrieve all blog posts from the database
    blogs = Blog.objects.all()

    # Pass the list of blog posts to the template
    return render(request, 'App_Blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # Pass the blog post to the template
    return render(request, 'App_Blog/blog_details.html', {'blog': blog})
