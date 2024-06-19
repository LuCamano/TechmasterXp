from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegistroForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
        return redirect("login")
    form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return redirect('registro')
    form = RegistroForm()
    return render(request, "registro.html",{'form': form})