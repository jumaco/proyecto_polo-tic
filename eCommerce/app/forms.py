from django import forms
from .models import Product, Category


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'slug', 'price', 'detail', 'image', 'excerpt', 'available')


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
