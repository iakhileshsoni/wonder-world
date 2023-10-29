
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('categories/', views.categories, name='categories'),
    
    # path('', views.blog_posts, name='blog_posts'),
    # path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    # path('post/<int:post_id>/', views.blog_post, name='blog_post'),
    
]




"""

<div class="container">
    <div class="row">
      {% for category in categories %}
        <div class="col-md-4">
          <div class="card mb-4">
            <!-- Use the category's blog_category_pic field to display the image -->
            <img class="card-img-top" src="{{ category.blog_category_pic.url }}" alt="Category Image">
            <div class="card-body">
              <h5 class="card-title">{{ category.name }}</h5>
              <p class="card-text">{{ category.description }}</p>
            </div>
          </div>
        </div>
        {% if forloop.counter|divisibleby:3 %}
          </div><div class="row">
        {% endif %}
      {% endfor %}
    </div>
  </div>

"""