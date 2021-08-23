from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clientes'),
    path('nuevoCliente/', views.crearClientes, name='crear_cliente'),
    path('nuevaMascota/', views.crearMascota, name='crear_mascota'),
    path('eliminarClientes/<int:id>/',views.eliminarCliente,name='eliminar_cliente'),
    path('eliminarMascota/<int:id>/',views.eliminarMascota, name='eliminar_mascota'),
    path('crearCita/',views.transaccionCita,name='transaccion_cita')
]
