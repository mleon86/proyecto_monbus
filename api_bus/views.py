#from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

from rest_framework.permissions import IsAuthenticated

from .models import Bus_Datos
from carga.models import RaspberryBus
from .serializers import Bus_DatosSerializer, RaspberryBusSerializer, Viaje_IncioSerializer

# Create your views here.

class Viaje_Inicio_Id_Viaje(generics.CreateAPIView):
	permission_classes = ()
	serializer_class = Viaje_IncioSerializer
	lookup_field = ('itinerario_id', 'chofer_id', 'raspberry_id')
		

class Bus_DatosSave(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Bus_DatosSerializer

class RaspberryBusConsulta(generics.RetrieveAPIView):
	permission_classes = (IsAuthenticated,) #permisos quitados temporalmente para prueba de la vista
	serializer_class = RaspberryBusSerializer
	queryset = RaspberryBus.objects.all()
	lookup_field = 'serial'