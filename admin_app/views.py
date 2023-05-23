from django.shortcuts import render, redirect
from product_app.models import *
from .forms import ProductUpdate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def add_product(request):
    if request.method == 'POST':
        p_name = request.POST['name']
        p_image = request.FILES['image']
        p_description = request.POST['description']
        p_price = request.POST['price']
        p_stock = request.POST['stock']
        Product.objects.create(
            name = p_name,
            image = p_image,
            description = p_description,
            price = p_price,
            stock = p_stock,
            status = False,
        )
        return redirect('add_product')
    return render(request,'add_product.html')


def admin_home(request):
    if not request.user.is_staff:
        return redirect('home')
    products = Product.objects.all()
    context = {'product':products}
    return render(request,'admin_home.html',context)


def update_product(request,id):
    update = Product.objects.get(id=id)
    form = ProductUpdate(instance=update)
    if request.method == 'POST':
        product = ProductUpdate(request.POST, request.FILES, instance=update)
        if product.is_valid():
            product.save()
            return redirect('admin_home')
        messages.error(request,product.errors)
    return render(request,'update_product.html', context={'form':form})


def delete_product(request,id):
    single_pro = Product.object.get(id=id)
    single_pro.delete()
    return redirect('admin_home') 
