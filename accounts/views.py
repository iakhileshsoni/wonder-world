from django.shortcuts import render
from .models import BlogPost, BlogCategory


def home(request):

    return render(request, 'accounts/home.html')


def blogs(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    print(context)

    return render(request, 'accounts/blogs.html', context)

def categories(request):
    blogs = BlogPost.objects.all()
    categories = BlogCategory.objects.all()

    context = {'blogs': blogs, 'categories': categories}

    return render(request, 'accounts/blog_categories.html', context)




# from django.shortcuts import render
# from .models import BlogPost, BlogCategory

# def blogs(request):
#     blog_posts = BlogPost.objects.all()
#     categories = BlogCategory.objects.all()
#     context = {
#         'blog_posts': blog_posts,
#         'categories': categories,
#     }
#     return render(request, 'accounts/home.html', context)


# def categories(request, category_id):
#     category = BlogCategory.objects.get(pk=category_id)
#     blog_posts = BlogPost.objects.filter(category=category)
#     categories = BlogCategory.objects.all()
#     context = {
#         'blog_posts': blog_posts,
#         'categories': categories,
#     }
#     return render(request, 'accounts/blog_categories.html', context)


# def blog(request, post_id):
#     post = BlogPost.objects.get(pk=post_id)
#     categories = BlogCategory.objects.all()
#     context = {
#         'post': post,
#         'categories': categories,
#     }
#     return render(request, 'accounts/home.html', context)
