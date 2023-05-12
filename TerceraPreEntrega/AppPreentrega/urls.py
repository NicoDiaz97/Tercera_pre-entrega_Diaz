from django.contrib import admin
from django.urls import path

from AppPreentrega.views import BarberoListView, BarberoDetailView, BarberoCreateView, BarberoUpdateView, BarberoDeleteView, ClienteListView, ClienteBuscarPorApellido, ClienteCreateView, ClienteUpdateView, ClienteDetailView, ClienteDeleteView, ServicioListView, ServicioCreateView, ServicioUpdateView, ServicioDetailView, ServicioDeleteView, TurnoListView, TurnoCreateView, TurnoUpdateView, TurnoDetailView, TurnoDeleteView

urlpatterns = [
    path('barberos/', BarberoListView.as_view() , name='lista_barberos'),
    path('crear_barbero/', BarberoCreateView.as_view(), name='crear_barbero'),
    path('modificar_barbero/<int:pk>', BarberoUpdateView.as_view(), name='modificar_barbero' ),
    path('ver_barbero/<int:pk>', BarberoDetailView.as_view(), name='ver_barbero' ),
    path('eliminar_barbero/<int:pk>', BarberoDeleteView.as_view(), name='eliminar_barbero'),

    path('clientes/', ClienteListView.as_view(), name='clientes'),
    path('crear_cliente/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('modificar_cliente/<int:pk>', ClienteUpdateView.as_view(), name='modificar_cliente' ),
    path('ver_cliente/<int:pk>', ClienteDetailView.as_view(), name='ver_cliente'),
    path('eliminar_cliente/<int:pk>', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('buscar_cliente_por_apellido/', ClienteBuscarPorApellido, name='buscar_cliente_por_apellido'),

    path('servicios/', ServicioListView.as_view(), name='servicios'),
    path('crear_servicio/', ServicioCreateView.as_view(), name='crear_servicio'),
    path('modificar_servicio/<int:pk>', ServicioUpdateView.as_view(), name='modificar_servicio' ),
    path('ver_servicio/<int:pk>', ServicioDetailView.as_view(), name='ver_servicio'),
    path('eliminar_servicio/<int:pk>', ServicioDeleteView.as_view(), name='eliminar_servicio'),

    path('turnos/', TurnoListView.as_view(), name='turnos'),
    path('crear_turno/', TurnoCreateView.as_view(), name='crear_turno'),
    path('modificar_turno/<int:pk>', TurnoUpdateView.as_view(), name='modificar_turno' ),
    path('ver_turno/<int:pk>', TurnoDetailView.as_view(), name='ver_turno'),
    path('eliminar_turno/<int:pk>', TurnoDeleteView.as_view(), name='eliminar_turno'),

]