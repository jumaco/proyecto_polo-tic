from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product, Category
from app.forms import FormularioProducto, FormularioCategoria
from django.contrib import messages
from django.core.paginator import Paginator


def acercade(request):
    categories = Category.objects.all()
    list_products = Product.objects.all()
    contexto = {"products": list_products, "categories": categories}
    return render(request, "acercade.html", contexto)


def contacto(request):
    categories = Category.objects.all()
    list_products = Product.objects.all()
    contexto = {"products": list_products, "categories": categories}
    return render(request, "contacto.html", contexto)


def index(request):
    print(request.GET)
    categories = Category.objects.all()
    list_products = Product.objects.all()
    queryset = request.GET.get("busqueda")
    if queryset:
        list_products = Product.objects.filter(
            Q(name__icontains=queryset) |
            Q(excerpt__icontains=queryset)
        ).distinct()
    paginador = Paginator(list_products, 6)
    pagina = request.GET.get("page") or 1
    products = paginador.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, products.paginator.num_pages + 1)
    contexto = {"products": products,
                "paginas": paginas,
                "pagina_actual": pagina_actual,
                "categories": categories}
    return render(request, "eCommerce.html", contexto)


def listado_productos(request):
    print(request.GET)
    list_products = Product.objects.all().reverse()
    categories = Category.objects.all()
    queryset = request.GET.get("busqueda")
    if queryset:
        list_products = Product.objects.filter(
            Q(name__icontains=queryset) |
            Q(excerpt__icontains=queryset)
        ).distinct()
    return render(request, "listado.html", {"products": list_products, "categories": categories})


@staff_member_required(login_url='/accounts/acceder')
def crear_producto(request):
    categories = Category.objects.all()
    list_products = Product.objects.all()
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
    return render(request, "agregar_producto.html", {"form": form, "products": list_products, "categories": categories})


@staff_member_required(login_url='/accounts/acceder')
def crear_categoria(request):
    categories = Category.objects.all()
    list_products = Product.objects.all()
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
    return render(request, "agregar_categoria.html", {"form": form, "products": list_products, "categories": categories})


@staff_member_required(login_url='/accounts/acceder')
def eliminar_producto(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, "El producto que quiere eliminar no existe")
        return redirect("listado_productos")

    product.delete()
    messages.success(request, f"El producto {product.name} ha sido removido")
    return redirect("listado_productos")


@staff_member_required(login_url='/accounts/acceder')
def editar_producto(request, product_id):
    categories = Category.objects.all()
    list_products = Product.objects.all()
    producto = Product.objects.get(id=product_id)
    if request.method == 'GET':
        form = FormularioProducto(instance=producto)
        contexto = {'form': form, "products": list_products, "categories": categories}
    else:
        form = FormularioProducto(request.POST, instance=producto)
        contexto = {'form': form}
        if form.is_valid():
            form.save()
            return redirect("listado_productos")

    return render(request, 'agregar_producto.html', contexto)


'''def categories_list(request):
    categories = Category.objects.all()
    return render(request, "base.html", {"categories": categories})'''
