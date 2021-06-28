from django.urls import path
from .views import *

urlpatterns = [
    path('hola-mundo/', hola, name="hola"),
]
