from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registro/', views.registro, name="registro"),
    path('perfil/', views.perfil, name="perfil"),
    path('bloquear/<rut>/', views.BloquearUsuario, name='bloquear-usuario'),
    path('desbloquear/<rut>/', views.DesbloquearUsuario, name='desbloquear-usuario'),
    path('agregar-usuario/', views.AgregarUsuario.as_view(), name='agregar-usuario'),
    path('delete-user/<pk>/', views.EliminarUsuario.as_view(), name='delete-user'),
    path('modificar-usuario/<pk>/', views.ModificarUsuario.as_view(), name='modificar-usuario'),
    path('modificar-perfil/<pk>/', views.ModificarPerfil.as_view(), name='modificar-perfil'),
    path('cambiar-contrasena/', views.CambiarClaveView.as_view(), name='cambiar-contrasena'),
    path('direcciones/', views.direcciones, name='direcciones'),
    path('direcciones/agregar/', views.AgregarDireccion.as_view(), name='agregar-direccion'),
    path('direcciones/eliminar/<pk>/', views.EliminarDireccion.as_view(), name='eliminar-direccion'),
    path('tarjetas/', views.ListadoTarjetas.as_view(), name='tarjetas'),
    path('tarjetas/agregar/', views.AgregarTarjeta.as_view(), name='agregar-tarjeta'),
    path('tarjetas/eliminar/<pk>/', views.EliminarTarjeta.as_view(), name='eliminar-tarjeta'),
]