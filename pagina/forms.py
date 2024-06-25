from django import forms
from .models import Producto, Cooler, Fabricante, Marca, Tarjeta_Grafica, FuenteAlimentacion, Gabinete, GPU, HDD, MemoriaRam, PlacaBase, Procesador, SSD, Socket

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen', 'fecha_agregado']

class CoolerForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = Cooler
        fields = ProductoForm.Meta.fields + ['socket', 'rpm', 'flujo', 'ruido']
    
class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nombre']
    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class GPUForm(forms.ModelForm):
    class Meta:
        model = GPU
        fields = ['nombre', 'marca']

class SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['nombre']

class Tarjeta_GraficaForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = Tarjeta_Grafica
        fields = ProductoForm.Meta.fields + ['memoria', 'fabricante', 'gpu', 'bus', 'perfil', 'slots', 'largo', 'puertos']

class FuenteAlimentacionForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = FuenteAlimentacion
        fields = ProductoForm.Meta.fields + ['potencia', 'eficiencia', 'certificacion', 'modular']

class GabineteForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = Gabinete
        fields = ProductoForm.Meta.fields + ['tam_placa', 'fuente', 'vent_inc', 'esp_vent_front', 'esp_vent_top', 'esp_vent_back', 'esp_vent_bottom', 'puertos']

class HDDForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = HDD
        fields = ProductoForm.Meta.fields + ['capacidad', 'lectura', 'escritura', 'formato', 'rpm']

class MemoriaRamForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = MemoriaRam
        fields = ProductoForm.Meta.fields + ['capacidad', 'frecuencia', 'latencia', 'formato']

class PlacaBaseForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = PlacaBase
        fields = ProductoForm.Meta.fields + ['formato', 'socket', 'slots_ram', 'slots_m2', 'slots_sata', 'puertos_usb', 'puertos_video', 'puertos_red', 'puertos_audio']

class ProcesadorForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = Procesador
        fields = ProductoForm.Meta.fields + ['marca', 'nucleos', 'hilos', 'frecuencia', 'turbo', 'cache', 'socket', 'tdp']

class SSDForm(ProductoForm):
    class Meta(ProductoForm.Meta):
        model = SSD
        fields = ProductoForm.Meta.fields + ['capacidad', 'lectura', 'escritura', 'formato', 'interfaz']