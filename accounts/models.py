from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    profile_pic = models.ImageField(default="profile_logo.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # method to display actual image in admin panel instead of file path
    def profile_pic_tag(self):
        return format_html('<img style="border-radius: 50%" height=50px; width=45px; src="/media/{}" />'.format(self.profile_pic))
    
    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # It will create new folder called 'category' inside media folder
    blog_category_pic = models.ImageField(upload_to='category/', null=True, blank=True)

    # method to display actual image in admin panel instead of file path
    def blog_category_pic_tag(self):
        return format_html('<img style="border-radius: 50%" height=50px; width=45px; src="/media/{}" />'.format(self.blog_category_pic))

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # It will create new folder called 'post' inside media folder
    blog_pic = models.ImageField(upload_to='post/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    # method to display actual image in admin panel instead of file path
    def blog_pic_tag(self):
        return format_html('<img style="border-radius: 50%" height=50px; width=45px; src="/media/{}" />'.format(self.blog_pic))

    def __str__(self):
        return self.title
