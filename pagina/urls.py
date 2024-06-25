from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('admin/listado_productos', views.listado_productos, name="listado_productos"),
    path('admin/listado_usuarios', views.Listado_usuarios.as_view(), name="listado_usuarios"),
    path('admin/listado_pedidos', views.listado_pedidos, name="listado_pedidos"),
    path("agregar-usuario/", views.agregar_usuario, name="agregar-usuario"),
    path("checkout/", views.checkout, name="checkout"),
    path("perfil/", views.perfil, name="perfil"),
    path("producto/<id>", views.producto, name="producto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)