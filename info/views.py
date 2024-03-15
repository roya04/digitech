from django.shortcuts import render
from .models import Home_Slider,GeneralCategory, Category,Product, Campaign
from django.db.models import Count
from django.utils import timezone

# Create your views here.
def home(request):
    home_slider=Home_Slider.objects.all()
    general_categories = GeneralCategory.objects.annotate(campaign_count=Count('campaign_sub_categories')).filter(campaign_count__gt=0)[:4]

    for category in general_categories:
        all_subs = category.campaign_sub_categories.all()
        subs_count = all_subs.count()
        if subs_count >= 2:
            subs = all_subs[subs_count - 2: subs_count]
        else:
            subs = all_subs  # Use all subs if there are fewer than 2
        category.campaign_sub_categories.set(subs)
    categories = Category.objects.filter(products__featured=True).annotate(product_count=Count('products')).filter(product_count__gt=0)[:4]
    recent_products=Product.objects.order_by('-created')
    all_products= Product.objects.all()
    is_slide_campaign=Campaign.objects.filter(is_slide=True).order_by('-id')[:6]
    is_deal_campaign=Campaign.objects.filter(is_deal_of_day=True)
    all_campaigns = Campaign.objects.all()
    for single_campaign in all_campaigns:
        if single_campaign.end_date <= timezone.now():
            single_campaign.delete()
    context={
        'home_slider':home_slider,
        'general_categories': general_categories,
        'categories': categories,
        'recent_products' : recent_products,
        'all_products' : all_products,
        'is_slide_campaign' : is_slide_campaign
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
