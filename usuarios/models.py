from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
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
    
    def formatear_rut(self, rut: str):
        cuerpo_valido = "1234567890"
        dv_valido = cuerpo_valido + "K"
        rut = rut.upper()
        rut = rut.replace(".", "")
        rut = rut.replace("-", "")
        if not rut:
            raise ValueError("El rut es obligatorio")
        if 8 <= len(rut) <= 9:
            cuerpo = rut[:-2]
            digito_v = rut[-1]
            for i in range(len(cuerpo)):
                charac = cuerpo[i]
                if charac not in cuerpo_valido:
                    raise ValueError("Rut inválido")
                if i%3 == 0 and i != 0:
                    cuerpo = cuerpo[:-(i+1)] + "." + cuerpo[-(i+1):]
            if digito_v not in dv_valido:
                raise ValueError("Dígito verificador inválido")
            return cuerpo + "-" + digito_v
        else:
            raise ValueError("El rut debe tener entre 8 y 12 caracteres")


class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField("Correo", max_length=254, unique=True)
    rut = models.CharField("Rut", max_length=12, primary_key=True)
    nombre = models.CharField("Nombre", max_length=100, blank=False, null=False)
    apellido = models.CharField("Apellido", max_length=100, blank=False, null=False)
    direccion1 = models.CharField("Dirección", help_text="(Calle, nro, comuna)", max_length=200, blank=True, null=False, default="")
    direccion2 = models.CharField("Dirección 2", help_text="(Departamento, casa, etc.)", max_length=200, blank=True, null=True, default="")
    telefono = PhoneNumberField(verbose_name='Teléfono', blank=True, null=True)
    imagen = models.ImageField("Imagen", upload_to="usuarios", blank=True, null=True)
    is_staff = models.BooleanField("Empleado", default=False)
    is_superuser = models.BooleanField("Superusuario", default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "correo"

    REQUIRED_FIELDS = ["rut", "nombre", "apellido"]

    def __str__(self):
        return self.correo