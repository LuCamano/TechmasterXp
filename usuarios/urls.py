from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registro/', views.registro, name="registro"),
    path('perfil/', views.perfil, name="perfil"),
    path('agregar-usuario/', views.AgregarUsuario.as_view(), name='agregar-usuario'),
]