from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from app.forms import FormularioProducto, FormularioCategoria
from django.contrib import messages


def index(request):
    return render(request, "eCommerce.html")


# @login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    products = Product.objects.all()
    return render(request, "listado.html", {"products": products})


def crear_producto(request):
    if request.method == "POST":
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            prod = form.cleaned_data.get("name")
            messages.success(request, f'El producto {prod} se ha creado correctamente')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error.messages[msg])
    form = FormularioProducto()
    return render(request, "agregar_producto.html", {"form": form})


def crear_categoria(request):
    if request.method == "POST":
        form = FormularioCategoria(request.POST)
        if form.is_valid():
            form.save()
            categor = form.cleaned_data.get("name")
            messages.success(request, f'La categoría {categor} se ha creado correctamente')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error.messages[msg])
    form = FormularioCategoria()
    return render(request, "agregar_categoria.html", {"form": form})
