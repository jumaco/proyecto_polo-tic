from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product


def index(request):
    return render(request, "eCommerce.html")


#@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    products = Product.objects.all()
    return render(request, "listado.html", {"products": products})
