from django.urls import path
from .views import *

urlpatterns = [
    path('eCommerce/', index, name="app"),
    path('', listado_productos, name='listado_productos'),
    path('agregar/producto', crear_producto, name='crear_producto'),
    path('agregar/categoria', crear_categoria, name='crear_categoria'),
    path('eliminar/producto/<int:product_id>', eliminar_producto, name='eliminar_producto'),
    path('editar/producto/<int:product_id>', editar_producto, name='editar_producto'),
    path('acercade/', acercade, name='acercade'),
    path('contacto/', contacto, name='contacto'),
    path('contacto/', contacto, name='contacto'),

]
