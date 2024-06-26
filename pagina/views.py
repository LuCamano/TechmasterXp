from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import *

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

    productos = sorted(
        productos,
        key=lambda producto: producto.fecha_agregado,
        reverse=True
    )
    return render(request, "admin/listado productos.html", {'productos':productos})

class Listado_usuarios(LoginRequiredMixin, ListView):
    model = usuario
    template_name = "admin/listado usuarios.html"

@login_required
def listado_pedidos(request):
    return render(request, "admin/listado pedidos.html", {})

@login_required
def agregar_usuario(request):
    return render(request, "admin/agregar usuario.html", {})

def checkout(request):
    return render(request, "checkout.html",{})

@login_required
def perfil(request):
    return render(request, "perfil.html",{})

def producto(request, id):
    return render(request, "producto.html",{})

def agregarProducto(request, tipo):
    if tipo == "Tarjeta Gráfica":
        form = Tarjeta_GraficaForm()
        if request.method == "POST":
            form = Tarjeta_GraficaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Procesador":
        form = ProcesadorForm()
        if request.method == "POST":
            form = ProcesadorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Memoria":
        form = MemoriaRamForm()
        if request.method == "POST":
            form = MemoriaRamForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Disco Duro":
        form = HDDForm()
        if request.method == "POST":
            form = HDDForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "SSD":
        form = SSDForm()
        if request.method == "POST":
            form = SSDForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Fuente de Alimentación":
        form = FuenteAlimentacionForm()
        if request.method == "POST":
            form = FuenteAlimentacionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Gabinete":
        form = GabineteForm()
        if request.method == "POST":
            form = GabineteForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Placa Base":
        form = PlacaBaseForm()
        if request.method == "POST":
            form = PlacaBaseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    elif tipo == "Cooler":
        form = CoolerForm()
        if request.method == "POST":
            form = CoolerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("listado_productos")
            else:
                return redirect("agregar-producto", tipo=tipo)
    else:
        return redirect("listado_productos")
    return render(request, "admin/agregar producto.html", {'form':form, 'tipo':tipo})