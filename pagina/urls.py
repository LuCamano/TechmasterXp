from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('admin/listado-productos/', views.listado_productos, name="listado_productos"),
    path('admin/listado-usuarios/', views.Listado_usuarios.as_view(), name="listado_usuarios"),
    path('admin/listado-pedidos/', views.listado_pedidos, name="listado_pedidos"),
    path('agregar-producto/<tipo>/', views.agregarProducto, name="agregar-producto"),
    path('checkout/', views.checkout, name="checkout"),
    path('producto/<tipo>/<id>/', views.producto, name="producto"),
    path('modificar-producto/<tipo>/<pk>/', views.editarProducto, name="modificar-producto"),
    path('delete-product/<pk>/<tipo>/', views.eliminarProducto, name="delete-product"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)