from django.shortcuts import render
from .models import Home_Slider,GeneralCategory
# Create your views here.
def home(request):
    home_slider=Home_Slider.objects.all()
    general_categories = GeneralCategory.objects.all()
    context={
        'home_slider':home_slider,
        'general_categories': general_categories
    }
    return render(request, 'home.html', context)
def shop(request):
    return render(request, 'shop.html')
def product_detail(request,id):
    return render(request, 'product-detail.html')
def product_compare(request):
    return render(request, 'product-compare.html')
def contact(request):
    return render(request, 'contact.html')