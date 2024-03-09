from django.shortcuts import render

# Create your views here.
def basket(request):
    return render(request, 'basket.html')
def wishlist(request):
    return render(request,'wishlist.html')