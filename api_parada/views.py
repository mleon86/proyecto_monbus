#from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

from rest_framework.permissions import IsAuthenticated

from django.db.models import F

from .models import Datos_Parada
from carga.models import Parada
from api_bus.models import Bus_Datos_Update, Viaje_Incio
from .serializers import Datos_ParadaSerializer, Bus_DatosListSerializer

# Create your views here.
class Datos_ParadaSave(generics.CreateAPIView): #Guarda los datos enviados por la Parada
	permission_classes = (IsAuthenticated,)
	serializer_class = Datos_ParadaSerializer

class Datos_MapaList(APIView):#Lista los buses que estan en la tabla Bus_Datos_Update, que estan a 2 km de la posicion de la parada
	permissions_classes = ()
	def get(self, request, nombre):
		parada = get_object_or_404(Parada, nombre = nombre)
		#tomamos los datos de la parada que nos van a ayudar a filtrar los buses
		itinerarios_parada = parada.itinerarios_parada.all() #itinerarios que pasan por esa parada
		tipo_parada = parada.tipo_parada#direccion que siguen los buses que pasan por esa parada, si es ida o vuelta
		#La ida y vuelta, equivaldria a tramo1 o tramo 2...
		location_parada = parada.location_parada#la locacion de la parada para hacer el calculo de distancia
		#tres tipos de filtro por separado.
		#lista_buses = Bus_Datos_Update.objects.filter(estado_viaje = tipo_parada) #si el bus va de ida... filtra conforme a si la parada corresponde a la ida
		#lista_buses = Bus_Datos_Update.objects.filter(viaje_inicio__itinerario_id__in = (itinerarios_parada)) #filtra por buses que pasan por esa parada		
		#lista_buses = Bus_Datos_Update.objects.filter(location_bus__distance_lt = (location_parada, D(km=2))) #filtra los buses que estan a 2km de distancia
		#los filtros anteriores... unidos en uno solo...
		lista_buses = Bus_Datos_Update.objects.filter(estado_viaje = tipo_parada).filter(viaje_inicio__itinerario_id__in = (itinerarios_parada)).filter(location_bus__distance_lt = (location_parada, D(km=2)))

		data = Bus_DatosListSerializer(lista_buses, many = True).data
		return Response(data)