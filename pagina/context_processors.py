from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from .models import Carrito, ProductoCarrito
from django.contrib.contenttypes.models import ContentType

def carrito(request: HttpRequest):
    if request.user.is_authenticated:
        # Intenta obtener el carrito del usuario autenticado
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        request.session["carrito_id"] = carrito.pk
    else:
        # Para usuarios no autenticados, usa la sesión para obtener el carrito
        carrito_id = request.session.get("carrito_id")
        if carrito_id:
            # Intenta obtener el carrito por ID
            carrito = Carrito.objects.get(pk=carrito_id)
        else:
            # Si no hay carrito en la sesión, crea uno nuevo y guárdalo en la sesión
            carrito = Carrito.objects.create()
            request.session["carrito_id"] = carrito.pk

    # Devuelve el carrito en el contexto
    return {'carrito': carrito}

def obtener_carrito(request: HttpRequest):
    carrito_id = request.session.get("carrito_id")
    if carrito_id:
        # Intenta obtener el carrito existente
        try:
            carrito = Carrito.objects.get(pk=carrito_id)
        except Carrito.DoesNotExist:
            # Si el carrito no existe, crea uno nuevo
            carrito = Carrito.objects.create()
            request.session["carrito_id"] = carrito.pk
    else:
        # Si no hay carrito_id en la sesión, crea uno nuevo
        carrito = Carrito.objects.create()
        request.session["carrito_id"] = carrito.pk

    return carrito

def agregar_producto_al_carrito(request, producto_id, producto_model, cantidad=1):
    # Obtener el carrito
    carrito = obtener_carrito(request)
    # Encontrar o crear ProductoCarrito
    producto_tipo = ContentType.objects.get_for_model(producto_model)
    producto_carrito, creado = ProductoCarrito.objects.get_or_create(
        carrito=carrito,
        content_type=producto_tipo,
        object_id=producto_id,
        defaults={'cantidad': cantidad}  # Si se crea, inicia con cantidad 1
    )

    if not creado:
        # Si el producto ya estaba en el carrito, incrementa la cantidad
        producto_carrito.cantidad += cantidad
        if not producto_carrito.cantidad <= 10:
            producto_carrito.cantidad = 10
        producto_carrito.save()

    # Devuelve el producto_carrito para confirmación o seguimiento adicional
    return producto_carrito

def quitar_producto_del_carrito(request, producto_id, producto_model):
    # Obtener el carrito
    carrito = obtener_carrito(request)

    # Encontrar el ProductoCarrito
    producto_tipo = ContentType.objects.get_for_model(producto_model)
    producto_carrito = ProductoCarrito.objects.get(
        carrito=carrito,
        content_type=producto_tipo,
        object_id=producto_id,
    )

    if producto_carrito.cantidad > 1:
        # Si hay más de un producto, decrementa la cantidad
        producto_carrito.cantidad -= 1
        producto_carrito.save()
    else:
        # Si hay solo un producto, elimina el ProductoCarrito
        producto_carrito.delete()

    # Devuelve el producto_carrito para confirmación o seguimiento adicional
    return producto_carrito

def limpiar_carrito(request):
    # Obtener el carrito
    carrito = obtener_carrito(request)
    # Obtener elementos del carrito
    productos_carrito = ProductoCarrito.objects.filter(carrito=carrito)
    # Eliminar todos los productos del carrito
    productos_carrito.delete()

    # Devuelve el carrito para confirmación o seguimiento adicional
    return carrito