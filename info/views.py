from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def shop(request):
    return render(request, 'shop.html')
def product_detail(request,id):
    return render(request, 'product-detail.html')
def product_compare(request):
    return render(request, 'product-compare.html')
def contact(request):
    return render(request, 'contact.html')