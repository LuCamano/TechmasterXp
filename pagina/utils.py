from .forms import *
from .models import *

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
