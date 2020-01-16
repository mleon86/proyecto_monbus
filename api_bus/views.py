#from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import Bus_Datos
from carga.models import RaspberryBus
from .serializers import Bus_DatosSerializer, RaspberryBusSerializer

# Create your views here.
class Bus_DatosSave(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Bus_DatosSerializer

class RaspberryBusConsulta(generics.RetrieveAPIView):
	permission_classes = () #permisos quitados temporalmente para prueba de la vista
	serializer_class = RaspberryBusSerializer
	queryset = RaspberryBus.objects.all()
	lookup_field = 'serial'