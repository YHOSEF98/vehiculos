from codecs import charmap_build
from distutils.command.upload import upload
from email.policy import default
from ensurepip import version
from pyexpat import model
from random import choices
from tabnanny import verbose
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models
from .choices import Persona
from .choices import generos
from .choices import estadoVehiculos
from .choices import categoriaVehiculos

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=25)
    continente = models.CharField(max_length=25)

    def nombre_pais(self):
        return "{}, {}". format(self.nombre, self.continente)

    def __str__(self):
        return self.nombre_pais()

    class Meta:
        verbose_name='Pais'
        verbose_name_plural='Paises'
        db_table='pais'
    


class Concesionario(models.Model):
    razon_social = models.CharField(max_length=60)
    nit = models.IntegerField(verbose_name="Nit")
    pais = models.ForeignKey(Pais,null=True,blank=True,on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=25)
    direccion = models.CharField(max_length=150)
    tfno = models.IntegerField(verbose_name="Telefono")

    def nombre_concesionario(self):
        return "{}, {}".format(self.razon_social, self.pais)

    def __str__(self):
        return self.nombre_concesionario()

    class Meta:
        verbose_name='Concesionario'
        verbose_name_plural='Concesionarios'
        db_table='concesionario'


class Administrador(Persona):
    idConcesionario = models.ForeignKey(Concesionario,null=True,blank=True,on_delete=models.CASCADE)
    paisOrigen = models.ForeignKey(Pais,null=True,blank=True,on_delete=models.CASCADE)

    def nom_admin(self):
        return "{}, {}, {}, {}".format(self.idConcesionario, self.nombres, self.apellidos, self.paisOrigen)

    def __str__(self):
        return self.nom_admin()

    class Meta:
        verbose_name='Administrador'
        verbose_name_plural='Administradores'
        db_table='administrador'


class Empleado(Persona):
    idConcesionario = models.ForeignKey(
        Concesionario,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Concesionario")
    paisOrigen = models.ForeignKey(
        Pais,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Pais de origen")

    def nom_empleado(self):
        return "{}, {}, {}, {}".format(self.idConcesionario, self.nombres, self.apellidos, self.paisOrigen)

    def __str__(self):
        return self.nom_empleado()

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'


class Cliente(Persona):
    idConcesionario = models.ForeignKey(Concesionario,null=True,blank=True,on_delete=models.CASCADE)
    paisOrigen = models.ForeignKey(Pais,null=True,blank=True,on_delete=models.CASCADE)

    def nom_cliente(self):
        return "{}, {}, {}, {}".format(self.idConcesionario, self.nombres, self.apellidos, self.paisOrigen)

    def __str__(self):
        return self.nom_cliente()

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        db_table='cliente'


class Vehiculo(models.Model):
    idConcesionario = models.ForeignKey(
        Concesionario,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Concesionario")
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    year = models.DateField(verbose_name="Año")
    estado = models.CharField(max_length=6, choices=estadoVehiculos, default="-")
    categoria = models.CharField(max_length=15, choices=categoriaVehiculos, default="-")
    tipoV = models.CharField(max_length=50, verbose_name="Tipo de vehiculo")
    precioCompra = models.IntegerField(verbose_name="Precio de compra")
    img = models.ImageField(upload_to="autosapp",null=True,blank=True)

    def nom_vehiculo(self):
        return "{}, {}, {}, {}".format(
            self.idConcesionario, self.modelo, self.marca, self.year)

    def __str__(self):
        return self.nom_vehiculo()

    class Meta:
        verbose_name='Vehiculo'
        verbose_name_plural='Vehiculos'
        db_table='vehiculo'


class Venta(models.Model):
    idVehiculo = models.ForeignKey(
        Vehiculo,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Vehiculo")
    idVendedor = models.ForeignKey(
        Empleado,on_delete=models.CASCADE,verbose_name="Vendedor")
    comprador = models.ForeignKey(
        Cliente,on_delete=models.CASCADE,verbose_name="Comprador")
    precioVehiculo = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    def nom_venta(self):
        return "{}, {}, {}, {}".format(
            self.idVendedor, self.idVehiculo, self.comprador, self.precioVehiculo)

    def __str__(self):
        return self.nom_venta()

    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        db_table='venta'


class Provehedor(Persona):
    paisOrigen = models.ForeignKey(Pais,null=True,blank=True,on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=25)
    idVehiculo = models.ForeignKey(
        Vehiculo,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Vehiculo")

    def nom_cliente(self):
        return "{}, {}, {}, {}".format(self.paisOrigen, self.nombres, self.apellidos, self.paisOrigen)

    def __str__(self):
        return self.nom_cliente()

    class Meta:
        verbose_name='Provehedor'
        verbose_name_plural='Provehedores'
        db_table='provehedor'