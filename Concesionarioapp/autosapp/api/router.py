from rest_framework.routers import DefaultRouter
from autosapp.api.views import VehiculoApiViewSet

router_vehiculos = DefaultRouter()

router_vehiculos.register(prefix='vehiculos', basename='vehiculos', viewset=VehiculoApiViewSet)