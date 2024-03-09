from django.shortcuts import render

def blogs(request):
    return render(request, 'blogs.html')
def blog_detail(request,id):
    return render(request, 'blog-detail.html')
def my_blogs(request):
    return render(request,'my-blogs.html')
def add_article(request):
    return render(request,"add-article.html")
def edit_article(request,id):
    return render(request,"edit-article.html")
    
    
