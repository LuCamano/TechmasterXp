from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', views.admin, name="admin"),
    path("agregar-usuario/", views.agregar_usuario, name="agregar-usuario"),
    path("checkout/", views.checkout, name="checkout"),
    path("nuevo-producto/", views.nuevo_producto, name="nuevo-producto"),
    path("perfil/", views.perfil, name="perfil"),
    path("producto/", views.producto, name="producto"),
]