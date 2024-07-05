from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import os
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    precio = models.IntegerField("Precio")
    descripcion = models.ImageField("Descripción", upload_to="productos/descripciones", null=True, blank=True)
    imagen = models.ImageField("Imagen", upload_to="productos", null=True, blank=True)
    fecha_agregado = models.DateTimeField("Fecha de agregado", auto_now_add=True)
    stock = models.PositiveIntegerField("Stock")

    def __str__(self):
        return self.nombre
    
    @property
    def tipo(self):
        '''
        Devuelve el nombre del tipo de producto.
        '''
        return self.__class__._meta.verbose_name
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        abstract = True

    def delete(self, *args, **kwargs):
        if self.imagen and os.path.exists(self.imagen.path):
            os.remove(self.imagen.path)
        if self.descripcion and os.path.exists(self.descripcion.path):
            os.remove(self.descripcion.path)
        return super().delete(*args, **kwargs)

class Fabricante(models.Model):
    nombre = models.CharField("Nombre", max_length=100, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"

class Marca(models.Model):
    nombre = models.CharField("Nombre", max_length=70, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Tarjeta_Grafica(Producto):
    memoria = models.PositiveIntegerField("Memoria", help_text="En GB")
    fabricante = models.ForeignKey("pagina.Fabricante", verbose_name="Fabricante", on_delete=models.PROTECT)
    gpu = models.ForeignKey("pagina.GPU", verbose_name="GPU", on_delete=models.PROTECT)
    bus = models.CharField("Bus", max_length=50)
    perfil = models.CharField("Perfil", max_length=50)
    slots = models.CharField("Slots", max_length=50)
    largo = models.PositiveIntegerField("Largo", help_text="En mm")
    puertos = models.CharField("Puertos de video", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tarjeta Gráfica"
        verbose_name_plural = "Tarjetas Gráficas"

class GPU(models.Model):
    nombre = models.CharField("Nombre", max_length=100, blank=False)
    marca = models.ForeignKey("pagina.Marca", verbose_name="Marca", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "GPU"
        verbose_name_plural = "GPUs"

class Procesador(Producto):
    marca = models.ForeignKey("pagina.Marca", verbose_name="Marca", on_delete=models.PROTECT, null=True)
    nucleos = models.PositiveIntegerField("Núcleos")
    hilos = models.PositiveIntegerField("Hilos")
    frecuencia = models.FloatField("Frecuencia", help_text="En GHz")
    turbo = models.FloatField("Turbo", help_text="En GHz")
    cache = models.FloatField("Cache", help_text="En MB")
    socket = models.ForeignKey("pagina.Socket", verbose_name="Socket", on_delete=models.PROTECT)
    tdp = models.PositiveIntegerField("TDP", help_text="En W")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Procesador"
        verbose_name_plural = "Procesadores"

class PlacaBase(Producto):
    formato = models.CharField("Formato", max_length=50)
    socket = models.ForeignKey("pagina.Socket", verbose_name="Socket", on_delete=models.PROTECT)
    slots_ram = models.PositiveIntegerField("Slots de RAM")
    slots_m2 = models.PositiveIntegerField("Slots M.2")
    slots_sata = models.PositiveIntegerField("Slots SATA")
    puertos_usb = models.PositiveIntegerField("Puertos USB")
    puertos_video = models.PositiveIntegerField("Puertos de video")
    puertos_red = models.PositiveIntegerField("Puertos de red")
    puertos_audio = models.PositiveIntegerField("Puertos de audio")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Placa Base"
        verbose_name_plural = "Placas Base"

class SSD(Producto):
    capacidad = models.PositiveIntegerField("Capacidad", help_text="En GB")
    lectura = models.PositiveIntegerField("Lectura", help_text="En MB/s")
    escritura = models.PositiveIntegerField("Escritura", help_text="En MB/s")
    formato = models.CharField("Formato", max_length=50)
    interfaz = models.CharField("Interfaz", max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "SSD"
        verbose_name_plural = "SSDs"

class HDD(Producto):
    capacidad = models.PositiveIntegerField("Capacidad", help_text="En GB")
    lectura = models.PositiveIntegerField("Lectura", help_text="En MB/s")
    escritura = models.PositiveIntegerField("Escritura", help_text="En MB/s")
    formato = models.CharField("Formato", max_length=50)
    rpm = models.PositiveIntegerField("RPM")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Disco Duro"
        verbose_name_plural = "Discos Duros"

class MemoriaRam(Producto):
    capacidad = models.PositiveIntegerField("Capacidad", help_text="En GB")
    frecuencia = models.PositiveIntegerField("Frecuencia", help_text="En MHz")
    latencia = models.CharField("Latencia", max_length=50)
    formato = models.CharField("Formato", max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Memoria"
        verbose_name_plural = "Memorias"

class FuenteAlimentacion(Producto):
    potencia = models.PositiveIntegerField("Potencia", help_text="En W")
    eficiencia = models.CharField("Eficiencia", max_length=50)
    certificacion = models.CharField("Certificación", max_length=50)
    modular = models.BooleanField("Modular")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Fuente de Alimentación"
        verbose_name_plural = "Fuentes de Alimentación"

class Gabinete(Producto):
    tam_placa = models.CharField("Tamaño máximo de la placa", max_length=50)
    fuente = models.CharField("Ubicación fuente", max_length=50, default="Inferior")
    vent_inc = models.CharField("Ventiladores incluidos", max_length=100, default="No posee")
    esp_vent_front = models.CharField("Espacios para ventiladores frontales", max_length=100)
    esp_vent_top = models.CharField("Espacios para ventiladores superiores", max_length=100)
    esp_vent_back = models.CharField("Espacios para ventiladores traseros", max_length=100)
    esp_vent_bottom = models.CharField("Espacios para ventiladores inferiores", max_length=100, default="No posee")
    puertos = models.CharField("Puertos", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Gabinete"
        verbose_name_plural = "Gabinetes"

class Cooler(Producto):
    socket = models.ForeignKey("pagina.Socket", verbose_name="Socket", on_delete=models.PROTECT)
    rpm = models.PositiveIntegerField("RPM")
    flujo = models.FloatField("Flujo de aire", help_text="En CFM")
    ruido = models.FloatField("Ruido", help_text="En dBA")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cooler"
        verbose_name_plural = "Coolers"

class Socket(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Socket"
        verbose_name_plural = "Sockets"

class Carrito(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name="Usuario", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Carrito {self.pk}"
    
    @property
    def productos_carrito(self):
        productos_c = ProductoCarrito.objects.filter(carrito=self)
        productos = {pc.producto.nombre: {'producto':pc.producto, 'cantidad':pc.cantidad} for pc in productos_c}
        return productos
    
    @property
    def cantidad(self):
        cantidad = 0
        for producto in self.productos_carrito:
            cantidad += self.productos_carrito[producto]['cantidad']
        return cantidad
    
    @property
    def total(self):
        total = 0
        for producto in self.productos_carrito:
            total += self.productos_carrito[producto]['producto'].precio * self.productos_carrito[producto]['cantidad']
        return total

    def valido(self):
        for producto in self.productos_carrito:
            if self.productos_carrito[producto]['producto'].stock < self.productos_carrito[producto]['cantidad']:
                return False
        return True

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

class ProductoCarrito(models.Model):
    cantidad = models.PositiveIntegerField("Cantidad", default=1)
    carrito = models.ForeignKey("Carrito", verbose_name="Carrito", on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.producto} en {self.carrito}"

    class Meta:
        verbose_name = "Producto en carrito"
        verbose_name_plural = "Productos en carrito"

class Pedido(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name="Usuario", on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField("Fecha de pedido", auto_now_add=True)
    tarjeta = models.ForeignKey("usuarios.Tarjeta", verbose_name="Tarjeta", on_delete=models.DO_NOTHING)
    total = models.PositiveIntegerField("Total")
    direccion = models.ForeignKey("usuarios.Direccion", verbose_name="Dirección", on_delete=models.DO_NOTHING)
    estado = models.CharField("Estado", max_length=50, default="En preparación", choices=[("En preparación", "En preparación"), ("Enviado", "Enviado"), ("Entregado", "Entregado"), ("Cancelado", "Cancelado")])

    def __str__(self):
        return f"Pedido {self.pk}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    @property
    def listado_productos(self):
        listado = ProductoPedido.objects.filter(pedido=self)
        productos = [{'nombre': pp.producto, 'cantidad': pp.cantidad} for pp in listado]
        return productos
    
    @property
    def productos_formateados(self):
        productos = self.listado_productos
        productos_formateados = [f"{producto['nombre']} x{producto['cantidad']}" for producto in productos]
        return productos_formateados

class ProductoPedido(models.Model):
    cantidad = models.PositiveIntegerField("Cantidad", default=1)
    pedido = models.ForeignKey("pagina.Pedido", verbose_name="Pedido", on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.producto} en {self.pedido}"

    class Meta:
        verbose_name = "Producto en pedido"
        verbose_name_plural = "Productos en pedido"

    def save(self, *args, **kwargs):
        if self.cantidad > 10:
            self.cantidad = 10
        super().save(*args, **kwargs)
        self.producto.stock -= self.cantidad
        self.producto.save()