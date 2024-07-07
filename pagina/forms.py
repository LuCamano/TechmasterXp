from django import forms
from .models import Producto, Cooler, Fabricante, Marca, Tarjeta_Grafica, FuenteAlimentacion, Gabinete, GPU, HDD, MemoriaRam, PlacaBase, Procesador, SSD, Socket, Pedido
from usuarios.models import Tarjeta, Direccion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import os

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen', 'stock']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.attrs = {"novalidate": ""}
        self.helper.add_input(Submit("submit", "Guardar"))
        for campo in self.fields:
            self.fields[campo].widget.attrs["placeholder"] = self.fields[campo].label + "..."

    def save(self):
        oldProdct = self.Meta.model.objects.get(pk=self.instance.pk)
        #Obtener las rutas de los archivos antiguos
        imagen_antigua = oldProdct.imagen.path if oldProdct.imagen else None
        descripcion_antigua = oldProdct.descripcion.path if oldProdct.descripcion else None
        #Obtener las rutas de los archivos nuevos y si no existen, asignar None
        imagen_nueva = self.cleaned_data.get("imagen") if len(self.cleaned_data.get("imagen").name.split("/")) == 1 else None
        descripcion_nueva = self.cleaned_data.get("descripcion") if len(self.cleaned_data.get("descripcion").name.split("/")) == 1 else None
        #Si hay imagen nueva y antigua
        if imagen_nueva and imagen_antigua:
            #Si las rutas son diferentes
            if imagen_nueva.name != os.path.basename(imagen_antigua):
                if os.path.exists(imagen_antigua):
                    #Borrar la antigua
                    os.remove(imagen_antigua)
        #Si hay descripcion nueva y antigua
        if descripcion_nueva and descripcion_antigua:
            #Si las rutas son diferentes
            if descripcion_nueva.name != os.path.basename(descripcion_antigua):
                if os.path.exists(descripcion_antigua):
                    #Borrar la antigua
                    os.remove(descripcion_antigua)
        return super().save()

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

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['direccion', 'tarjeta']
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("rut_usuario")
        super().__init__(*args, **kwargs)
        self.fields["tarjeta"].queryset = Tarjeta.objects.filter(usuario=usuario)
        self.fields["direccion"].queryset = Direccion.objects.filter(usuario=usuario)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.form_id = "form-pedido"
        self.helper.attrs = {"novalidate": ""}
        for campo in self.fields:
            self.fields[campo].widget.attrs["placeholder"] = self.fields[campo].label + "..."
    