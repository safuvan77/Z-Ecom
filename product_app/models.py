from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Order(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Order, on_delete=models.CASCADE)
    units = models.PositiveIntegerField(default=1)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)





def calculate_cart_total(cart):
    total = 0
    cart_items = Cart.objects.filter(cart=cart)
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
    return total

def calculate_total_quantity(cart):
    total_quantity = 0
    cart_items = Cart.objects.filter(cart=cart)
    for cart_item in cart_items:
        total_quantity += cart_item.quantity
    return total_quantity

def apply_discount_to_cart(cart, rule_name):
    if rule_name == "tiered_50_discount":
        apply_tiered_discount(cart)
    # Add more discount rule handlers here if needed

def apply_tiered_discount(cart):
    cart_items = Cart.objects.filter(cart=cart)
    for cart_item in cart_items:
        if cart_item.quantity > 15:
            discount_quantity = cart_item.quantity - 15
            discount_amount = (cart_item.product.price * discount_quantity * 0.5)
            cart_item.quantity -= discount_quantity
            cart_item.save()
            # Update cart total or order total based on your model structure
            # cart.total -= discount_amount
            # cart.save()