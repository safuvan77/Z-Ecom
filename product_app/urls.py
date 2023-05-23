from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index_page, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('product details/<int:id>', product_details, name='product_details'),
    path('add to cart/<int:id>/', add_to_cart, name='add_cart'),
    path('cart/', cart_view, name='cart'),
    path('item delete/<int:id>/', item_delete, name='item_delete'),
    path('cart/item/inc/<int:id>/', cart_quantity_inc, name='cart_quantity_inc'),
    path('cart/item/dec/<int:id>/', cart_quantity_dec, name='cart_quantity_dec'),

]