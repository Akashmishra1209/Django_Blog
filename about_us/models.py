from django.db import models

class About(models.Model):
    site_name=models.CharField(max_length=50)
    site_tagline=models.TextField(max_length=255)
    about_heading=models.CharField(max_length=60)
    about_text=models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='About'
    def __str__(self) -> str:
        return self.about_heading

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.platform