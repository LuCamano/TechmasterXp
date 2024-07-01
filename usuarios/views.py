from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import LoginForm, RegistroForm, RegistroAdminForm, CambiarFotoForm, EditarUsuarioAdminForm, EditarUsuarioForm, CambiarClaveForm, DireccionForm
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView
from .models import Direccion

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

@login_required
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

@login_required
def perfil(request):
    form = CambiarFotoForm()
    direcciones = Direccion.objects.filter(usuario=request.user)
    ClaveForm = CambiarClaveForm(request.user)
    if request.method == "POST":
        form = CambiarFotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")
        else:
            messages.warning(request, "No se pudo actualizar la foto de perfil")
            return redirect("perfil")
    context = {
        'form': form,
        'ClaveForm': ClaveForm,
        'direcciones': direcciones,
    }
    return render(request, "perfil.html", context)

class AgregarUsuario(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = RegistroAdminForm
    template_name = "admin/formulario agregar admin.html"
    success_url = "/admin/listado-usuarios/"
    
    def get_context_data(self, **kwargs):
        kwargs["tipo"] = "usuario"
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Usuario agregado correctamente")
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("index")
        
    def post(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return redirect("index")
    
class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    success_url = "/admin/listado-usuarios/"

    def post(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            messages.success(request, "Usuario eliminado correctamente")
            return super().post(request, *args, **kwargs)
        else:
            return redirect("index")
    
    def get(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return redirect("listado_usuarios")
        else:
            return redirect("index")
        
class ModificarUsuario(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    form_class = EditarUsuarioAdminForm
    template_name = "admin/formulario modificar admin.html"
    success_url = "/admin/listado-usuarios/"

    def form_valid(self, form):
        messages.success(self.request, "Usuario modificado correctamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs["tipo"] = "usuario"
        return super().get_context_data(**kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("index")
        
    def post(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return redirect("index")
        
class ModificarPerfil(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    form_class = EditarUsuarioForm
    template_name = "editar usuario.html"
    success_url = "/usuarios/perfil/"

    def form_valid(self, form):
        messages.success(self.request, "Datos modificados.")
        return super().form_valid(form)
    

class CambiarClaveView(PasswordChangeView, LoginRequiredMixin):
    form_class = CambiarClaveForm
    success_url = "/usuarios/perfil/"

    def form_valid(self, form):
        messages.success(self.request, "Contraseña cambiada correctamente.")
        return super().form_valid(form)
    

def direcciones(request):
    direcciones = Direccion.objects.filter(usuario=request.user)
    return render(request, "direcciones.html", {"direcciones": direcciones})

class AgregarDireccion(LoginRequiredMixin, CreateView):
    form_class = DireccionForm
    template_name = "agregar direccion.html"
    success_url = "/usuarios/perfil/"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Dirección agregada correctamente.")
        return super().form_valid(form)

class EliminarDireccion(LoginRequiredMixin, DeleteView):
    model = Direccion
    success_url = "/usuarios/perfil/"

    def post(self, request, *args, **kwargs):
        messages.success(request, "Dirección eliminada correctamente.")
        return super().post(request, *args, **kwargs)
