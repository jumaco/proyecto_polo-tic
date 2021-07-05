from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product
from app.forms import FormularioProducto, FormularioCategoria
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    list_products = Product.objects.all()
    paginador = Paginator(list_products, 6)
    pagina = request.GET.get("page") or 1
    products = paginador.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, products.paginator.num_pages + 1)
    return render(request, "eCommerce.html", {"products": products, "paginas": paginas, "pagina_actual": pagina_actual})


def listado_productos(request):
    products = Product.objects.all()
    return render(request, "listado.html", {"products": products})


@staff_member_required(login_url='/accounts/acceder')
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


@staff_member_required(login_url='/accounts/acceder')
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


@staff_member_required(login_url='/accounts/acceder')
def eliminar_producto(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, "El producto que quiere eliminar no existe")
        return redirect("app")

    product.delete()
    messages.success(request, f"El producto {product.name} ha sido removido")
    return redirect("app")


'''#linea 60
    if request.user != request.is_superuser:
        messages.error(request, "No tienes privilegios para esto")
        return redirect("app")
'''
