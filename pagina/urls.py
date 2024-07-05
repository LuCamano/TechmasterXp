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
    path('productos/<tipo>/', views.vistaProductos, name="productos"),
    path('modificar-producto/<tipo>/<pk>/', views.editarProducto, name="modificar-producto"),
    path('delete-product/<pk>/<tipo>/', views.eliminarProducto, name="delete-product"),
    path('agregar-al-carrito/', views.agregarAlCarrito, name="agregar-al-carrito"),
    path('quitar-del-carrito/', views.quitarDelCarrito, name="quitar-del-carrito"),
    path('obtener-carrito/', views.obtenerCarrito, name="obtener-carrito"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)