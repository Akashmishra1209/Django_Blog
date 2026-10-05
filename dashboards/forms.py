from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from about_us.models import About,SocialLink
from blogs.models import Category, Blog


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'category', 'featured_image', 'short_description', 'blog_body', 'status',
                  'is_featured')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions', 'password1', 'password2'
        )

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions'
        )

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class SocialForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'