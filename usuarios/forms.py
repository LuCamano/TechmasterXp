from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div, Field, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth import get_user_model
import os

user = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(), required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            FloatingField("username", placeholder="Correo"),
            Div(
                FloatingField("password", placeholder="Contraseña"),
                HTML("<a href='#'>¿Olvidaste tu contraseña?</a>"),
                css_class="mb-3",
            ),
            Submit("submit", "Iniciar sesión", css_class="btn btn-primary")
        )

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))

    class Meta:
        model = user
        fields = ["correo", "rut", "nombre", "apellido"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("correo", placeholder="Correo...", id="correo"),
            Div(
                Field("nombre", placeholder="Nombre...", wrapper_class="col-12 col-md-6", id="nombre"),
                Field("apellido", placeholder="Apellido...", wrapper_class="col-12 col-md-6", id="apellido"),
                css_class="row"
            ),
            Field("rut", placeholder="Rut...", id="rut", maxlength="9"),
            Div(
                Field("password1", placeholder="Contraseña...", wrapper_class="col-12 col-md-6"),
                Field("password2", placeholder="Repite la contraseña...", wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            Submit("submit", "Registrarse")
        )

class RegistroAdminForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))

    class Meta:
        model = user
        fields = ['imagen','correo', 'rut', 'nombre', 'apellido', 'direccion1', 'direccion2', 'telefono', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("imagen", placeholder="Imagen...", id="imagen"),
            Field("correo", placeholder="Correo...", id="correo"),
            Div(
                Field("nombre", placeholder="Nombre...", wrapper_class="col-12 col-md-6", id="nombre"),
                Field("apellido", placeholder="Apellido...", wrapper_class="col-12 col-md-6", id="apellido"),
                css_class="row"
            ),
            Field("rut", placeholder="Rut...", id="rut", maxlength="9"),
            Row(
                Field("direccion1", placeholder="Dirección...", id="direccion1", wrapper_class="col-12 col-md-6", required=True),
                Field("direccion2", placeholder="Comuna...", id="direccion2", wrapper_class="col-12 col-md-6"),
                ),
            Field("telefono", placeholder="Teléfono..."),
            Row(
                Field("is_staff", wrapper_class="col-12 col-md-6"),
                Field("is_superuser", wrapper_class="col-12 col-md-6")
            ),
            Div(
                Field("password1", placeholder="Contraseña...", wrapper_class="col-12 col-md-6"),
                Field("password2", placeholder="Repite la contraseña...", wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            Submit("submit", "Agregar")
        )

class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = user
        fields = ['correo', 'nombre', 'apellido', 'direccion1', 'direccion2', 'telefono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("correo", placeholder="Correo...", id="correo"),
            Row(
                Column(Field("nombre", placeholder="Nombre...", id="nombre")),
                Column(Field("apellido", placeholder="Apellido...", id="apellido"))
            ),
            Field("telefono", placeholder="Teléfono..."),
            Row(
                Column(Field("direccion1", placeholder="Dirección...", id="direccion1", required=True)),
                Column(Field("direccion2", placeholder="Departamento, casa, etc.", id="direccion2"))
                ),
            Submit("submit", "Guardar cambios")
        )

class CambiarFotoForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("imagen", id="imagen"),
            Submit("submit", "Cambiar foto")
        )
    
    def save(self):
        oldUsr = user.objects.get(rut=self.instance.rut)
        imagen_antigua = oldUsr.imagen.path if oldUsr.imagen else None
        imagen_nueva = self.cleaned_data.get("imagen") if len(self.cleaned_data.get("imagen").name.split("/")) == 1 else None
        if imagen_nueva and imagen_antigua:
            print("Imagen nueva y antigua")
            print(imagen_nueva.name, os.path.basename(imagen_antigua))
            if imagen_nueva.name != os.path.basename(imagen_antigua):
                print("Nueva imagen")
                if os.path.exists(imagen_antigua):
                    print("Eliminando imagen antigua")
                    os.remove(imagen_antigua)
        usuario = super().save()
        return usuario
    
class EditarUsuarioAdminForm(EditarUsuarioForm):
    class Meta(EditarUsuarioForm.Meta):
        fields = EditarUsuarioForm.Meta.fields + ['rut','is_staff', 'is_superuser', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("correo", placeholder="Correo...", id="correo"),
            Row(
                Column(Field("nombre", placeholder="Nombre...", id="nombre")),
                Column(Field("apellido", placeholder="Apellido...", id="apellido"))
            ),
            Field("rut", placeholder="Rut...", id="rut", maxlength="9", readonly=True),
            Row(
                Column(Field("direccion1", placeholder="Dirección...", id="direccion1", required=True)),
                Column(Field("direccion2", placeholder="Departamento, casa, etc.", id="direccion2"))
                ),
            Field("telefono", placeholder="Teléfono..."),
            Row(
                Column(Field("is_staff")),
                Column(Field("is_superuser"))
            ),
            Field("imagen", id="imagen"),
            Submit("submit", "Guardar cambios")
        )
    def save(self):
        oldUsr = user.objects.get(rut=self.instance.rut)
        imagen_antigua = oldUsr.imagen.path if oldUsr.imagen else None
        imagen_nueva = self.cleaned_data.get("imagen") if len(self.cleaned_data.get("imagen").name.split("/")) == 1 else None
        if imagen_nueva and imagen_antigua:
            print("Imagen nueva: ", imagen_nueva.name, "imagen antigua:", os.path.basename(imagen_antigua))
            if imagen_nueva.name != os.path.basename(imagen_antigua):
                print("Nueva imagen")
                if os.path.exists(imagen_antigua):
                    print("Eliminando imagen antigua")
                    os.remove(imagen_antigua)
        usuario = super().save()
        return usuario
    
class CambiarClaveForm(PasswordChangeForm):
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "cambiar-contrasena"
        self.helper.form_class = "needs-validation card-body"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field("old_password", placeholder="Contraseña actual...", id="old_password"),
            Field("new_password1", placeholder="Nueva contraseña...", id="password1"),
            Field("new_password2", placeholder="Repite la nueva contraseña...", id="password2"),
            Submit("submit", "Cambiar contraseña")
        )