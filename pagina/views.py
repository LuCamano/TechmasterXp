from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, "index.html",{})

@login_required
def admin(request):
    return render(request, "admin.html",{})

def agregar_usuario(request):
    return render(request, "agregar usuario.html",{})

def checkout(request):
    return render(request, "checkout.html",{})

def nuevo_producto(request):
    return render(request, "nuevo producto.html",{})

@login_required
def perfil(request):
    return render(request, "perfil.html",{})

def producto(request):
    return render(request, "producto.html",{})

