from django.shortcuts import render, redirect, get_object_or_404

from about_us.models import About, SocialLink
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from dashboards.forms import CategoryForm, BlogPostForm, AddUserForm, EditUserForm, AboutUsForm, SocialForm

@permission_required('blogs.view_blog', login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    posts_count = Blog.objects.count()
    users_count = User.objects.count()
    links_count = SocialLink.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'category_count': category_count,
        'posts_count': posts_count,
        'total_users':users_count,
        'total_links':links_count
    })


@permission_required('blogs.view_category', login_url='login')
@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'categories': categories})


@permission_required('blogs.add_category', login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    return render(request, 'dashboard/add_category.html', {'form': form})


@permission_required('blogs.edit_category', login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    return render(request, 'dashboard/edit_category.html', {'form': form, 'category': category})


@permission_required('blogs.delete_category', login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


@permission_required('blogs.view_blog', login_url='login')
def posts(request):
    posts = Blog.objects.all()
    return render(request, 'dashboard/posts.html', {'posts': posts})


@permission_required('blogs.add_blog', login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    return render(request, 'dashboard/add_post.html', {'form': form})


@permission_required('blogs.edit_blog', login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    return render(request, 'dashboard/edit_post.html', {'form': form, 'post': post})


@permission_required('blogs.delete_blog', login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')


@permission_required('auth.view_user', login_url='login')
def users(request):
    users = User.objects.all()
    return render(request, 'dashboard/users.html', {'users': users})


@permission_required('auth.add_user', login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    return render(request, 'dashboard/add_user.html', {'form': form})

@permission_required('auth.change_user', login_url='login')
def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EditUserForm (request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    return render(request,'dashboard/edit_user.html',{'form':form,'user':user})

@permission_required('auth.delete_user', login_url='login')
def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')

@permission_required('about_us.edit_about')
def about(request):
    about_details = About.objects.first()
    if request.method == 'POST':
        form =AboutUsForm(request.POST,instance=about_details)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AboutUsForm(instance=about_details)
    return render(request,'dashboard/about.html', {'form': form})

@permission_required('about_us.view_social')
def socials(request):
    socials_links = SocialLink.objects.all()
    return render(request, 'dashboard/socials.html', {'socials': socials_links})

@permission_required('about_us.add_social')
def add_social(request):
    if request.method == 'POST':
        form = SocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socials')
    form = SocialForm()
    return render(request, 'dashboard/add_social.html', {'form': form})

@permission_required('about_us.edit_social')
def edit_social(request,pk):
    social=get_object_or_404(SocialLink,pk=pk)
    if request.method == 'POST':
        form = SocialForm(request.POST,instance=social)
        if form.is_valid():
            form.save()
            return redirect('socials')
    form = SocialForm(instance=social)
    return render(request, 'dashboard/edit_social.html', {'form': form,'social':social})


def delete_social(request,pk):
    social = get_object_or_404(SocialLink,pk=pk)
    social.delete()
    return redirect('socials')