from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.


def index_page(request):

    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('cpassword')

        user = User.objects.filter(username=username)
        if not user:
            if password == c_password:
                User.objects.create_user(
                    username = username,
                    email = email,
                    password = c_password
                )
                messages.success(request,"Account created successfully")
                return redirect('signin')
            else:
                messages.error(request,"Password doesn't match")
        else:
            messages.error(request,"Username already taken")      
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username = username,
            password = password
        )

        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('admin_home')
            else:
                return redirect('home')
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,'signin.html')


def logout(request):
    logout(request)
    return redirect('index')


def home(request):
    if request.user.is_staff:
        return redirect('admin_home')
    products = Product.objects.all()
    context = {'product':products}
    return render(request,'home.html',context)


def product_details(request,id):
    single_pro = Product.objects.get(id=id)
    return render(request,'product_details.html',context={'product':single_pro})


def add_to_cart(request,id):
    user  = User.objects.get(username = request.user.username)
    if user:
        single_pro = Product.objects.get(id=id)
        check = Cart.objects.filter(fk_product = single_pro, fk_user = user).first()
        if check:
            check.quantity += 1
            check.sub_total = (check.quantity * check.fk_product.price)
            check.save()
            return redirect('cart')
        else:
            Cart.objects.create(
                fk_user =user,
                fk_product = single_pro,
                quantity = 1,
                sub_total = single_pro.price
            )
        return redirect('cart')


def cart_view(request):
    cart_item = Cart.objects.filter(fk_user = request.user).order_by('-id')
    total_disc = 0
    items = cart_item.filter(quantity__gte=10)
    for item in items:
        discount = (5/100)*sub_total
        total_disc += discount
    total -= total_disc

    total_disc = 0
    items = cart_item.filter(quantity__gte=10)
    for item in items:
        discount = (10/100)*sub_total
        total_disc += discount
    total -= total_disc
    
    sub_total = 0
    count = 0
    disc_name=None
    for i in cart_item:
        count += i.quantity
        sub_total += i.sub_total

    if sub_total > 200:
        total = sub_total - 10
        disc_name='flat_10_discout'
    
    context = {
        'cartitem':cart_item,
        'total':total,
        'count':count,
        'dicounts':disc_name
    }
    return render(request,'cart.html',context)


def cart_quantity_inc(request, id):
    item = Cart.objects.get(id=id)
    item.quantity += 1
    sub_total = item.quantity * item.fk_product.price
    item.sub_total = sub_total
    item.save()
    return redirect('cart')


def cart_quantity_dec(request, id):
    item = Cart.objects.get(id=id)
    item.quantity -= 1
    sub_total = item.quantity * item.fk_product.price
    item.sub_total = sub_total
    item.save()
    return redirect('cart')


def item_delete(request,id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('cart')


# def total_cart_discount(cart):
#     total = 0
#     cart_items = Cart.objects.filter(cart.cart)
#     for cart in cart_items:
#         total += cart * 


