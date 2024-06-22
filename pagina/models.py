from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    fabricante = models.ForeignKey("pagina.Fabricante", verbose_name="Marca", on_delete=models.PROTECT)
    precio = models.IntegerField("Precio")
    descripcion = models.TextField("Descripción")
    imagen = models.ImageField("Imagen", upload_to="productos", null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Fabricante(models.Model):
    nombre = models.CharField("Nombre", max_length=100, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"

class Tarjeta_Grafica(Producto):
    memoria = models.PositiveIntegerField("Memoria")
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

    def __str__(self):
        return self.nombre