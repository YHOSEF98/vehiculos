from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Vehiculo

def index(request):
    return render(request,'autosapp/index.html')


def buscarv(request):
    return render(request, 'autosapp/busqueda_vehiculos.html')


def carrobuscado(request):
    mensaje="Vehiculo buscado: %r" %request.GET["car"]

    return HttpResponse(mensaje)

def consulta(request):

    consulta=Vehiculo.objects.all()
    return render(request,"autosapp/consulta.html", {"consulta" : consulta})

def agregar(request):
    
    return render(request, "autosapp/agregar.html")

def team(request):
    
    return render(request, "autosapp/team.html")

def tienda(request):

    return render(request, "autosapp/tienda.html")