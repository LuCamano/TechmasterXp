from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegistroForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
        else:
            messages.warning(request, "Usuario o contraseña incorrectos")
            return redirect("login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente")
            return redirect("login")
        else:
            messages.warning(request, "No se pudo registrar el usuario")
            return redirect("registro")
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})