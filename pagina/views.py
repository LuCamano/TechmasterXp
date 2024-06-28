from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib import messages

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

def get_form(tipo):
    form_dict = {
        "Tarjeta Gráfica": Tarjeta_GraficaForm,
        "Procesador": ProcesadorForm,
        "Memoria": MemoriaRamForm,
        "Disco Duro": HDDForm,
        "SSD": SSDForm,
        "Fuente de Alimentación": FuenteAlimentacionForm,
        "Gabinete": GabineteForm,
        "Placa Base": PlacaBaseForm,
        "Cooler": CoolerForm,
    }
    return form_dict.get(tipo, None)

def get_model(tipo):
    model_dict = {
        "Tarjeta Gráfica": Tarjeta_Grafica,
        "Procesador": Procesador,
        "Memoria": MemoriaRam,
        "Disco Duro": HDD,
        "SSD": SSD,
        "Fuente de Alimentación": FuenteAlimentacion,
        "Gabinete": Gabinete,
        "Placa Base": PlacaBase,
        "Cooler": Cooler
    }
    return model_dict.get(tipo, None)

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
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect("index")
    
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

    def get(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("index")
        
    def post(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return redirect("index")

@login_required
def listado_pedidos(request):
    if not request.user.is_staff:
        return redirect("index")

    return render(request, "admin/listado pedidos.html", {})

def checkout(request):
    return render(request, "checkout.html",{})

def producto(request, tipo, id):
    product_class = get_model(tipo)
    product = product_class.objects.get(pk=id)
    campos = product._meta.get_fields()
    camposExcluidos = ['id', 'fecha_agregado', 'descripcion', 'imagen', 'nombre']
    valores = {field.name.replace("_", " "): getattr(product, field.name) for field in campos if field.name not in camposExcluidos}
    return render(request, "producto.html",{'producto': product, 'valores': valores})

@login_required
def agregarProducto(request, tipo):
    form_class = get_form(tipo)

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect("index")

    if not form_class:
        raise ValueError(f"Formulario no encontrado para el tipo {tipo}")
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado exitosamente")
            return redirect("listado_productos")
        else:
            messages.warning(request, "Error al agregar el producto")
            return redirect("agregar-producto", tipo=tipo)
    else:
        form = form_class()
    return render(request, "admin/formulario agregar admin.html", {'form':form, 'tipo':tipo})

@login_required
def editarProducto(request, tipo, pk):
    model = get_model(tipo)
    prod = model.objects.get(pk=pk)
    form_class = get_form(tipo)

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect("index")

    if not form_class:
        raise ValueError(f"Formulario no encontrado para el tipo {tipo}")
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto modificado exitosamente")
            return redirect("listado_productos")
        else:
            messages.warning(request, "Error al modificar el producto")
            return redirect("modificar-producto", tipo=tipo, pk=pk)
    else:
        form = form_class(instance=prod)
    return render(request, "admin/formulario modificar admin.html", {'form':form, 'tipo':tipo})

@login_required
def eliminarProducto(request, pk, tipo):
    model = get_model(tipo)
    prod = model.objects.get(pk=pk)
    prod.delete()

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect("index")

    messages.success(request, "Producto eliminado exitosamente")
    return redirect("listado_productos")