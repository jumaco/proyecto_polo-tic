from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .carrito import Carrito
from app.models import Product, Category


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
    categories = Category.objects.all()
    queryset = request.GET.get("busqueda")
    if queryset:
        list_products = Product.objects.filter(
            Q(name__icontains=queryset) |
            Q(excerpt__icontains=queryset)
        ).distinct()
        return render(request, 'eCommerce.html', {"products": list_products, "categories": categories})
    return render(request, "carrito/tienda.html", {"products": list_products, "categories": categories})
