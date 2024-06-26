from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
import os
from PIL import Image
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        extra_fields["rut"] = self.formatear_rut(extra_fields.get("rut"))
        usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo=correo, password=password, **extra_fields)
    
    def formatear_rut(self, rut: str) -> str:
        cuerpo_valido = "1234567890"
        dv_valido = cuerpo_valido + "K"
        
        # Convertir a mayúsculas y eliminar puntos y guiones
        rut = rut.upper().replace(".", "").replace("-", "")
        
        if not rut:
            raise ValueError("El rut es obligatorio")
        
        if not 8 <= len(rut) <= 9:
            raise ValueError("El rut debe tener entre 8 y 9 caracteres")
        
        cuerpo = rut[:-1]
        digito_v = rut[-1]
        
        # Validar el cuerpo del RUT
        if not all(char in cuerpo_valido for char in cuerpo):
            raise ValueError("Rut inválido")
        
        # Validar el dígito verificador
        if digito_v not in dv_valido:
            raise ValueError("Dígito verificador inválido")
        
        # Formatear el cuerpo con puntos
        cuerpo_formateado = ""
        for i, char in enumerate(reversed(cuerpo)):
            if i != 0 and i % 3 == 0:
                cuerpo_formateado = "." + cuerpo_formateado
            cuerpo_formateado = char + cuerpo_formateado
        
        return f"{cuerpo_formateado}-{digito_v}"


class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField("Correo", max_length=254, unique=True)
    rut = models.CharField("Rut", max_length=12, primary_key=True)
    nombre = models.CharField("Nombre", max_length=100, blank=False, null=False)
    apellido = models.CharField("Apellido", max_length=100, blank=False, null=False)
    direccion1 = models.CharField("Dirección", help_text="(Calle, nro, comuna)", max_length=200, blank=True, null=False, default="")
    direccion2 = models.CharField("Dirección 2", help_text="(Departamento, casa, etc.)", max_length=200, blank=True, null=True, default="")
    telefono = PhoneNumberField(verbose_name='Teléfono', blank=True, null=True, default="", region="CL")
    imagen = models.ImageField("Imagen", upload_to="usuarios/", blank=True, null=True)
    is_staff = models.BooleanField("Empleado", default=False)
    is_superuser = models.BooleanField("Superusuario", default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "correo"

    REQUIRED_FIELDS = ["rut", "nombre", "apellido"]

    def __str__(self):
        return self.correo
    
    @property
    def get_full_name(self):
        return f"{self.nombre} {self.apellido}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen and os.path.exists(self.imagen.path):
            with Image.open(self.imagen.path) as img:
                ancho, alto = img.size

                if ancho > alto:
                    # La imagen es mas ancha que alta
                    nuevo_alto = 1280
                    nuevo_ancho = int((ancho/alto) * nuevo_alto)
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.imagen.path)
                elif alto > ancho:
                    # La imagen es mas alta que ancha
                    nuevo_ancho = 1280
                    nuevo_alto = int((alto/ancho) * nuevo_ancho)
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.imagen.path)
                else:
                    # La imagen es cuadrada
                    img.thumbnail((300, 300))
                    img.save(self.imagen.path)

            # El recorte de la imagen final
            with Image.open(self.imagen.path) as img:
                ancho, alto = img.size

                if ancho > alto:
                    left = (ancho - alto) / 2
                    top = 0
                    right = (ancho + alto) / 2
                    bottom = alto

                else:
                    left = 0
                    top = (alto - ancho) / 2
                    right = ancho
                    bottom = (alto + ancho) / 2

                img = img.crop((left, top, right, bottom))
                img.save(self.imagen.path)