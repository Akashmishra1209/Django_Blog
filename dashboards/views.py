from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm, BlogPostForm


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    posts_count = Blog.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'category_count': category_count,
        'posts_count': posts_count
    })

@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'categories': categories})

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    return render(request, 'dashboard/add_category.html', {'form': form})

@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    return render(request, 'dashboard/edit_category.html', {'form': form, 'category': category})

@login_required(login_url='login')
def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    return render(request, 'dashboard/posts.html', {'posts': posts})

@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    return render(request,'dashboard/add_post.html',{'form':form})

@login_required(login_url='login')
def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    return render(request,'dashboard/edit_post.html',{'form':form,'post':post})

@login_required(login_url='login')
def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')