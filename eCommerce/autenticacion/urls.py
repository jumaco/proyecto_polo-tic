from django.urls import path
from .views import vistaRegistro, salir, acceder

urlpatterns = [
    path('registro/', vistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir"),
]
