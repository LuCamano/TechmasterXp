from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def get_subclasses(cls):
    subclasses = set()
    work = [cls]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

def index(request):
    producto_subclasses = get_subclasses(Producto)
    all_products = []

    for subclass in producto_subclasses:
        all_products.extend(subclass.objects.all())

    productos = sorted(
        all_products,
        key=lambda producto: producto.fecha_agregado,
        reverse=True
    )
    productos_recientes = productos[:10]
    return render(request, "index.html",{'productos':productos_recientes})

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

def producto(request, id):
    return render(request, "producto.html",{})

