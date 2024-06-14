from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import LoginForm

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
    return render(request, "registro.html",{})