from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .carrito import Carrito
from app.models import Product


@login_required(login_url='/accounts/acceder')
def agregar_producto(request, producto_id):
    carro = Carrito(request)
    produc = Product.objects.get(id=producto_id)
    carro.agregar(product=produc)
    return redirect("carrito:carrito")


@login_required(login_url='/accounts/acceder')
def eliminar_producto(request, producto_id):
    carro = Carrito(request)
    produc = Product.objects.get(id=producto_id)
    carro.remover(product=produc)
    return redirect("carrito:carrito")


@login_required(login_url='/accounts/acceder')
def restar_producto(request, producto_id):
    carro = Carrito(request)
    produc = Product.objects.get(id=producto_id)
    carro.restar(product=produc)
    return redirect("carrito:carrito")


@login_required(login_url='/accounts/acceder')
def vaciar_carro(request):
    carro = Carrito(request)
    carro.vaciar()
    return redirect("carrito:carrito")


@login_required(login_url='/accounts/acceder')
def listado_carrito(request):
    list_products = Product.objects.all()
    return render(request, "carrito/tienda.html", {"products": list_products})
