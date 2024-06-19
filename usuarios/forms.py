from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import RegionalPhoneNumberWidget

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
        fields = ['correo', 'rut', 'nombre', 'apellido', 'direccion1', 'direccion2', 'telefono']
        widgets = {
            'correo': forms.EmailInput(
                attrs={"id": "correo"}
            ),
            'rut': forms.TextInput(
                attrs={"id": "rut"}
            ),
            'nombre': forms.TextInput(
                attrs={"id": "nombre"}
            ),
            'apellido': forms.TextInput(
                attrs={"id": "apellido"}
            ),
            'direccion1': forms.TextInput(
                attrs={"id": "direccion1"}
            ),
            'direccion2': forms.TextInput(
                attrs={"id": "direccion2"}
            ),
            'telefono': RegionalPhoneNumberWidget(
                attrs={"id": "telefono"}
            )
        }

    def save(self):
        return self.model.objects.create_user(self.fields)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'card-body needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {"novalidate":""}
        self.helper.layout = Layout(
            FloatingField("correo", css_id="correo"),
            Div(
                FloatingField('nombre', wrapper_class="col-12 col-md-6"),
                FloatingField('apellido', wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            FloatingField("rut"),
            Div(
                FloatingField('direccion1', wrapper_class="col-12 col-md-6"),
                FloatingField('direccion2', wrapper_class="col-12 col-md-6"),
                css_class="row"
            ),
            FloatingField('telefono'),
            FloatingField("password1"),
            FloatingField("password2"),
            Submit("submit", "Crear cuenta")
        )