from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
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
class Campaign(models.Model):
    title=models.CharField( max_length=50,unique=True)
    description=models.TextField(null=True, blank=True)
    is_slide=models.BooleanField(default=False)
    is_deal_of_day=models.BooleanField(default=False)
    image=models.ImageField( upload_to='campaigns')
    discount_percent=models.FloatField(null=True, blank=True)
    general_category=models.ForeignKey(GeneralCategory,on_delete=models.SET_NULL,null=True,blank=True,related_name='campaign_sub_categories')
    def __str__(self) :
        return self.title
class Product(models.Model):
    company = models.ForeignKey(Collaborate_Company, on_delete=models.CASCADE)
    title=models.CharField( max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price=models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    operating_system=models.CharField(max_length=50)
    weight=models.DecimalField(max_digits=5, decimal_places=2)
    processor=models.CharField(max_length=30)
    ram=models.IntegerField()
    storage=models.CharField(max_length=8)
    screen_size=models.CharField( max_length=50)
    colors=models.ManyToManyField(Color, related_name='products')
    categories=models.ManyToManyField(Category, related_name='products')
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

