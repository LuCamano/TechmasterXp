from django.shortcuts import render
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import get_user_model

usuario = get_user_model()
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
def listado_productos(request):
    producto_subclasses = get_subclasses(Producto)
    productos = []

    for subclass in producto_subclasses:
        productos.extend(subclass.objects.all())

    return render(request, "admin/listado productos.html", {'productos':productos})

class Listado_usuarios(LoginRequiredMixin, ListView):
    model = usuario
    template_name = "admin/listado usuarios.html"

@login_required
def listado_pedidos(request):
    return render(request, "admin/listado pedidos.html", {})

@login_required
def agregar_usuario(request):
    return render(request, "admin/agregar usuario.html",{})

def checkout(request):
    return render(request, "checkout.html",{})

@login_required
def perfil(request):
    return render(request, "perfil.html",{})

def producto(request, id):
    return render(request, "producto.html",{})

