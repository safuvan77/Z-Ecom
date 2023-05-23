from django.urls import path
from .views import *


urlpatterns = [

    path('add product/', add_product, name='add_product'),
    path('admin home', admin_home, name='admin_home'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product),
    
]