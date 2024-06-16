from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div
from crispy_bootstrap5.bootstrap5 import FloatingField

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
