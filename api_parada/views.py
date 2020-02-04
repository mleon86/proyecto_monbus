#from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

from rest_framework.permissions import IsAuthenticated

from .models import Datos_Parada
from carga.models import Parada
from api_bus.serializers import Bus_DatosSerializer
from .serializers import Datos_ParadaSerializer

# Create your views here.
class Datos_ParadaSave(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Datos_ParadaSerializer

class Datos_MapaList(APIView):
	permissions_classes = ()
	def get(self, request, nombre):
		parada = get_object_or_404(Parada, nombre = nombre)
		geom = parada.location_parada
		lista_buses = Datos_Mapa.objects.filter(location_bus__distance_lt = (geom, D(km=2))) #filtra los buses que estan a 2km de distancia
		data = Datos_MapaSerializer(lista_buses, many = True).data
		return Response(data)