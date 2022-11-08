from rest_framework.viewsets import ModelViewSet
from autosapp.models import Vehiculo
from autosapp.api.serializers import VehiculoSerializer

class VehiculoApiViewSet(ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()