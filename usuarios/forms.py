from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div, Field, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth import get_user_model

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
    def save(self):
        return self.Meta.model.objects.create_user(
            correo=self.cleaned_data["correo"],
            rut=self.cleaned_data["rut"],
            nombre=self.cleaned_data["nombre"],
            apellido=self.cleaned_data["apellido"],
            password=self.cleaned_data["password1"]
        )
    
class RegistroAdminForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))

    class Meta:
        model = user
        fields = ['correo', 'rut', 'nombre', 'apellido', 'direccion1', 'direccion2', 'telefono', 'is_staff']

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
            Row(
                Field("direccion1", placeholder="Dirección...", id="direccion1", wrapper_class="col-12 col-md-6", required=True),
                Field("direccion2", placeholder="Comuna...", id="direccion2", wrapper_class="col-12 col-md-6"),
                ),
            Div(
                Field("telefono", placeholder="Teléfono...", wrapper_class="col-12 col-md-6"),
                Field("is_staff", wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            Div(
                Field("password1", placeholder="Contraseña...", wrapper_class="col-12 col-md-6"),
                Field("password2", placeholder="Repite la contraseña...", wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            Submit("submit", "Agregar")
        )
    def save(self, commit: bool):
        self.cleaned_data["rut"] = self.Meta.model.objects.clean_rut(self.cleaned_data["rut"])
        return super().save(commit)