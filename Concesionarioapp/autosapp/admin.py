from django.contrib import admin

from  .models import Concesionario, Pais, Administrador,Empleado, Cliente
from .models import Vehiculo, Venta, Provehedor

# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display=("nombre", "continente")
    search_fields=("nombre", "continente")

class ConcesionarioAdmin(admin.ModelAdmin):
    list_display=("razon_social", "pais", "ciudad", "tfno")
    search_fields=("razon_social", "pais", "ciudad", "tfno")

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=("nombres", "apellidos", "idConcesionario", "paisOrigen")
    search_fields=("nombres", "apellidos", "idConcesionario", "paisOrigen")

#@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display=("modelo", "marca", "year", "estado", "precioCompra")
    search_fields=("modelo", "marca", "year", "estado", "precioCompra")

admin.site.register(Pais, PaisAdmin)
admin.site.register(Concesionario, ConcesionarioAdmin)
admin.site.register(Administrador)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Venta)
admin.site.register(Provehedor)