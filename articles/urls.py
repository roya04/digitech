from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.blogs, name='blogs'),
    path('<int:id>',views.blog_detail, name='blog-detail'),
    path('my-blogs',views.my_blogs, name='my-blogs'),
    path('add-article',views.add_article, name='add-article'),
    path('edit-article/<int:id>',views.edit_article, name='edit-article'),
]