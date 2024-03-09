from django.urls import path
from . import views

app_name='info'

urlpatterns = [
    path('',views.home, name='home'),
    path('products',views.shop, name='shop'),
    path('products/<int:id>',views.product_detail, name='product-detail'),
    path('products/compare',views.product_compare, name='product-compare'),
    path('contact',views.contact, name='contact'),
]