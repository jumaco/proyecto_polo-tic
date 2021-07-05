from django.urls import path
from .views import index, listado_productos, crear_producto, crear_categoria, eliminar_producto

urlpatterns = [
    path('', index, name="app"),
    path('tienda/', listado_productos, name='listado_productos'),
    path('agregar/producto', crear_producto, name='crear_producto'),
    path('agregar/categoria', crear_categoria, name='crear_categoria'),
    path('eliminar/producto/<int:product_id>', eliminar_producto, name='eliminar_producto')
]
