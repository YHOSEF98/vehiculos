from rest_framework.serializers import ModelSerializer
from autosapp.models import Vehiculo

class VehiculoSerializer(ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'idConcesionario', 'modelo', 'marca','year',
                    'estado', 'categoria','tipoV','precioCompra','img']