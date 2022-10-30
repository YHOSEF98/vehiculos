from dataclasses import field, fields
from email.policy import default
from tabnanny import verbose
from django.db import models

#from django import forms


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


""" class vehiculosForm(forms.ModelForm):

    class Meta:
        models = Vehiculo

        fields = [
            "idConsecionario",
            "modelo",
            "marca",
            "year",
            "estado",
            "categoria",
            "tipoV",
            "precioCompra",
        ]
        labels = {
            "idConsecionario": "Consecionario",
            "modelo": "Modelo",
            "marca": "Marca",
            "year": "Año",
            "estado": "Estado",
            "categoria": "Categoria",
            "tipoV": "Tipo de vehiculo",
            "precioCompra": "Precio de compra",
        }
        widgets = {
            "idConsecionario": forms.CheckboxSelectMultiple(),
            "modelo": forms.TextInput(attrs={'class':'form-control'}),
            "marca": forms.TextInput(attrs={'class':'form-control'}),
            "year": forms.TextInput(attrs={'class':'form-control'}),
            "estado": forms.CheckboxSelectMultiple(),
            "categoria": forms.CheckboxSelectMultiple(),
            "tipoV": forms.TextInput(attrs={'class':'form-control'}),
            "precioCompra": forms.TextInput(attrs={'class':'form-control'})
        }"""