from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("busqueda_vehiculos/", views.buscarv, name="buscarv"),
    #path("carrobuscado/", views.carrobuscado, name="carrobuscado")
    path("consulta/", views.consulta, name="consulta"),
    path("agregar/", views.agregar, name="agregar"),
    path("team/", views.team, name="team"),
    path("tienda/", views.tienda, name="tienda"),
]
