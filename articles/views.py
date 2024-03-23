from django.shortcuts import render
from .models import Article, Author, Tag
from django.core.paginator import Paginator

def blogs(request):
    author_username = request.GET.get('author')
    articles = Article.objects.all() 
    authors = Author.objects.all()
    tags = Tag.objects.all()
    tag_title = request.GET.get('tag')
    page_number = int(request.GET.get('page', 1))
    if author_username:
        articles = articles.filter(author__user__username=author_username)
    if tag_title:
        articles = articles.filter(tags__title=tag_title)

    paginator = Paginator(articles, 3)
    page = paginator.page(page_number)
    articles = page.object_list

    return render(request, 'blogs.html', context={'articles': articles, 'authors': authors, 'tags': tags, 'paginator': paginator, 'page': page})
    





def blog_detail(request,id):
    article = Article.objects.get(id=id)
    return render(request, "blog-detail.html", context={'article': article})



def my_blogs(request):
    return render(request,'my-blogs.html')
def add_blog(request):
    return render(request,'add-blog.html')
def edit_blog(request,id):
    return render(request,'edit-blog.html')
    
    
