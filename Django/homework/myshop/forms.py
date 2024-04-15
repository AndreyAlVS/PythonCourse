from django import forms
from myshop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name', 'description', 'price', 'quantity', 'photo']
        image = forms.ImageField()
