from django.shortcuts import render

from about_us.models import About
from blogs.models import Category, Blog


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    recent_posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    print(featured_posts)
    return render(request, "home.html", {
        'featured_posts': featured_posts,
        'recent_posts':recent_posts,
    })