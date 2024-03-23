from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.blogs, name='blogs'),
    path('<int:id>',views.blog_detail, name='blog-detail'),
    path('my-blogs',views.my_blogs, name='my-blogs'),
    path('add-blog',views.add_blog, name='add-blog'),
    path('edit-blog/<int:id>',views.edit_blog, name='edit-blog'),
]