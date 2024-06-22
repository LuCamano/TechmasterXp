from django.contrib import admin
from .models import Fabricante, GPU, Tarjeta_Grafica
# Register your models here.

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(Tarjeta_Grafica)
class Tarjeta_GraficaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fabricante", "precio", "memoria", "gpu", "bus", "perfil", "slots", "largo", "puertos"]
    list_filter = ["fabricante", "gpu"]