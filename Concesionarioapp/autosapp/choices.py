from email.policy import default
from tabnanny import verbose
from django.db import models

generos=(
    ('F','Femenino'),
    ('M','Masculino'),
    ('X','Indefinido'),
    ('-','--')
)


categoriaVehiculos=(
    ('p','Pesado'),
    ('M','Ligero'),
    ('E','Especiales'),
    ('A','Agricolas'),
    ('-','--')
)


estadoVehiculos=(
    ('N','Nuevo'),
    ('U','Usado'),
    ('-','--')
)

class Persona(models.Model):
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    cedula = models.IntegerField()
    genero = models.CharField(max_length=1, choices=generos, default='-')
    tfno = models.IntegerField(verbose_name="Telefono")
    correo = models.EmailField()
    direccion = models.CharField(max_length=150)