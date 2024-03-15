from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
from django.utils import timezone
from datetime import datetime, timedelta

class Home_Slider(models.Model):
    description=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    image=models.ImageField( upload_to='slider_images')
class Collaborate_Company(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Color(models.Model):
    title=models.CharField( max_length=20, unique=True)
    def __str__(self) :
        return self.title
class GeneralCategory(models.Model):
    title=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.title

class Category(models.Model):   
    title=models.CharField( max_length=20,unique=True)
    general_category=models.ForeignKey(GeneralCategory,on_delete=models.SET_NULL,null=True,blank=True,related_name='category_sub_categories')
    def __str__(self):
        return self.title
def get_default_end_date():
    # Logic to calculate default end date
    return timezone.now() + timedelta(days=30) 
class Campaign(models.Model):
    title=models.CharField( max_length=50,unique=True)
    description=models.TextField(null=True, blank=True)
    is_slide=models.BooleanField(default=False)
    is_deal_of_day=models.BooleanField(default=False)
    image=models.ImageField( upload_to='campaigns')
    discount_percent=models.IntegerField(null=True, blank=True)
    general_category=models.ForeignKey(GeneralCategory,on_delete=models.SET_NULL,null=True,blank=True,related_name='campaign_sub_categories')
    end_date = models.DateTimeField(default=get_default_end_date)
    def __str__(self) :
        return self.title
class Product(models.Model):
    company = models.ForeignKey(Collaborate_Company, on_delete=models.CASCADE, null=False, blank=False)
    title=models.CharField( max_length=50,null=False, blank=False)
    description=models.TextField(null=False, blank=False)
    price=models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)
    discounted_price=models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    operating_system=models.CharField(max_length=50, null=True, blank=True)
    weight=models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False,help_text="Weight in kilograms")
    processor=models.CharField(max_length=30,null=True, blank=True)
    ram=models.IntegerField(null=True, blank=True,)
    storage=models.CharField(max_length=8,null=True, blank=True)
    view_size=models.CharField( max_length=50, null=True, blank=True, help_text="Size in width × height format")
    colors=models.ManyToManyField(Color, related_name='products',null=False, blank=False)
    categories=models.ManyToManyField(Category, related_name='products',null=False, blank=False)
    campaign=models.ManyToManyField(Campaign, related_name='products', null=True, blank=True)
    featured=models.BooleanField(default=False)
    update=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.title
class ProductImage(models.Model):
    product=models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image=models.ImageField( upload_to='product_images')
    @display(description='Movcud Sekil')
    def image_tag(self):
        return format_html(f'<img width="200" src="{self.image.url}">')

