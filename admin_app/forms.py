from django import forms
from product_app.models import Product


class ProductUpdate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'