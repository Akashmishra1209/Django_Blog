from about_us.models import About, SocialLink
from blogs.models import Category

def get_categories(request):
    categories = Category.objects.all()
    try:
        about = About.objects.get()
    except:
        about = None
    return dict(categories=categories, about=about)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)