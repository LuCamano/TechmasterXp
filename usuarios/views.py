from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, RegistroForm, RegistroAdminForm
from django.contrib import messages
from django.views.generic import CreateView

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
        else:
            messages.warning(request, "Usuario o contraseña incorrectos")
            return redirect("login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente")
            return redirect("login")
        else:
            messages.warning(request, "No se pudo registrar el usuario")
            return redirect("registro")
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})

def perfil(request):
    return render(request, "perfil.html", {})

class AgregarUsuario(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = RegistroAdminForm
    template_name = "admin/formulario agregar admin.html"
    success_url = "listado_usuarios"
    
    def get_context_data(self, **kwargs):
        kwargs["tipo"] = "usuario"
        return super().get_context_data(**kwargs)