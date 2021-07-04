from django.urls import path
from .views import index, listado_productos

urlpatterns = [
    path('', index, name="app"),
    path('listado/', listado_productos, name='listado_productos')
]
