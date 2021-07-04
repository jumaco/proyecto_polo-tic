from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bievenid@ nuevamente a la plataforma {nombre_usuario}")
                return redirect("app")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, 'acceder.html', {"form": form})


class vistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"formulario": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, F"Bievenid@ a la plataforma {nombre}")
            login(request, usuario)
            return redirect("app")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, "registro.html", {"formulario": form})

def salir(request):
    logout(request)
    messages.success(request, F'Tu sesión se ha cerrado correctamente')
    return redirect("acceder")