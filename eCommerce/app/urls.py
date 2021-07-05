from django.urls import path
from .views import index, listado_productos, crear_producto, crear_categoria

urlpatterns = [
    path('', index, name="app"),
    path('tienda/', listado_productos, name='listado_productos'),
    path('agregar/producto', crear_producto, name='crear_producto'),
    path('agregar/categoria', crear_categoria, name='crear_categoria')
]
