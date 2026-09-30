from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Blog, Category


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category,pk=category_id)
    return render(request, 'post_by_category.html', {'posts': posts, 'category': category})
