from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html",{})

def admin(request):
    return render(request, "admin.html",{})

def agregar_usuario(request):
    return render(request, "agregar usuario.html",{})

def checkout(request):
    return render(request, "checkout.html",{})

def nuevo_producto(request):
    return render(request, "nuevo producto.html",{})

def perfil(request):
    return render(request, "perfil.html",{})

def producto(request):
    return render(request, "producto.html",{})

