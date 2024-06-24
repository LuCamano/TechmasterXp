from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ["nombre", "marca"]

@admin.register(Tarjeta_Grafica)
class Tarjeta_GraficaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fabricante", "precio", "memoria", "gpu", "bus", "perfil", "slots", "largo", "puertos"]
    list_filter = ["fabricante", "gpu"]

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(Procesador)
class ProcesadorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Procesador._meta.fields]
    list_display_links = ["nombre"]

@admin.register(PlacaBase)
class PlacaBaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlacaBase._meta.fields]
    list_display_links = ["nombre"]

@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SSD._meta.fields]
    list_display_links = ["nombre"]

@admin.register(HDD)
class HDDAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HDD._meta.fields]
    list_display_links = ["nombre"]

@admin.register(MemoriaRam)
class MemoriaRamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MemoriaRam._meta.fields]
    list_display_links = ["nombre"]

@admin.register(FuenteAlimentacion)
class FuenteAlimentacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FuenteAlimentacion._meta.fields]
    list_display_links = ["nombre"]

@admin.register(Gabinete)
class GabineteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gabinete._meta.fields]
    list_display_links = ["nombre"]

@admin.register(Cooler)
class coolerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cooler._meta.fields]
    list_display_links = ["nombre"]

@admin.register(Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ["nombre"]