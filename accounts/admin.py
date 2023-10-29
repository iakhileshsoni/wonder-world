from django.contrib import admin
from .models import Blogger, BlogCategory, BlogPost


class BloggerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'profile_pic_tag', 'date_created']
admin.site.register(Blogger, BloggerAdmin)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'blog_category_pic_tag', 'description']
admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blog_pic_tag', 'category', 'content', 'created_at', 'updated_at']
admin.site.register(BlogPost, BlogPostAdmin)
