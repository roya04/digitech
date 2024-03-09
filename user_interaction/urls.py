from django.urls import path
from . import views
app_name='user_interaction'
urlpatterns = [
    path('basket', views.basket,name= 'basket'),
    path('wishlist', views.wishlist,name= 'wishlist'),
    
]