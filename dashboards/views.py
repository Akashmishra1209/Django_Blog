from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    posts_count = Blog.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'category_count': category_count,
        'posts_count': posts_count
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    return render(request, 'dashboard/add_category.html', {'form': form})


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    return render(request, 'dashboard/edit_category.html', {'form': form, 'category': category})


def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')