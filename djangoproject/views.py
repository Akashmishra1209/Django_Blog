from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from about_us.models import About
from blogs.models import Category, Blog
from djangoproject.forms import RegisterationForm


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    recent_posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    print(featured_posts)
    return render(request, "home.html", {
        'featured_posts': featured_posts,
        'recent_posts':recent_posts,
    })


def register(request):
    if request.method=='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterationForm()
    return render(request,'register.html' ,{'form':form})


def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout(request):
    auth.logout(request)
    return redirect('home')