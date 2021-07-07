from django import forms
from .models import Product, Category


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'price', 'excerpt', 'detail', 'available')


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
