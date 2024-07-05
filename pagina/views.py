from django.shortcuts import render, redirect
from .utils import get_subclasses, get_model, get_form
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import get_user_model
from django.contrib import messages
from .context_processors import agregar_producto_al_carrito, quitar_producto_del_carrito
from django.http import JsonResponse, HttpRequest
import json
from .context_processors import obtener_carrito

usuario = get_user_model()
# Create your views here.

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

def agregarAlCarrito(request:HttpRequest):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            cantidad = data.get('cantidad')
            tipo = data.get('tipo_producto')

            if producto_id:
                producto_model = get_model(tipo)
                agregar_producto_al_carrito(request, producto_id, producto_model, cantidad)
                return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def quitarDelCarrito(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            tipo = data.get('tipo_producto')
            if producto_id:
                producto_model = get_model(tipo)
                quitar_producto_del_carrito(request, producto_id, producto_model)
                return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})
    return JsonResponse({'success': False})

def obtenerCarrito(request):
    carrito = obtener_carrito(request)
    productos = carrito.productos_carrito
    productos_serializados = []
    for producto in productos:
        productos_serializados.append({
            'tipo': productos[producto]['producto'].tipo,
            'pk': productos[producto]['producto'].pk,
            'nombre': productos[producto]['producto'].nombre,
            'imagen': productos[producto]['producto'].imagen.url,
            'precio': productos[producto]['producto'].precio,
            'cantidad': productos[producto]['cantidad']
        })
    return JsonResponse({'productos': productos_serializados, 'total': carrito.total})