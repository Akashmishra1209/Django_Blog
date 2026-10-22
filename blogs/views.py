from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Blog, Category, Comment


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'post_by_category.html', {'posts': posts, 'category': category})


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    related_blogs = Blog.objects.filter(status='Published', category=single_blog.category).order_by('-updated_at')[:3]

    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"]
        comment.save()
        return redirect('blogs', single_blog.slug)

    comments = Comment.objects.filter(blog=single_blog)
    return render(request, 'blogs.html', {'single_blog': single_blog, 'comments': comments, "related_blogs": related_blogs})


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),
        status='Published')
    return render(request, 'search.html', {'blogs': blogs, 'keyword': keyword})
