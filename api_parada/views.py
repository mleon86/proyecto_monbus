#from django.shortcuts import render
from rest_framework import generics
from rest_framework import status


from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

from rest_framework.permissions import IsAuthenticated

from django.db.models import F

from .models import Datos_Parada, SolicAsiento
from carga.models import Parada, RaspberryParada
from api_bus.models import Bus_Datos_Update, Viaje_Incio
from .serializers import Datos_ParadaSerializer, Bus_Datos_UpdateListSerializer, ParadaSerializer, RaspberryParadaSerializer, SolicAsientoSerializer


from datetime import datetime
# Create your views here.

#Consultando datos de la parada
class RaspParada(generics.RetrieveAPIView):
    permission_classes = () #permisos quitados temporalmente para prueba de la vista IsAuthenticated,
    serializer_class = RaspberryParadaSerializer
    queryset = RaspberryParada.objects.all()
    lookup_field = 'serial_rasp_parada'

#guardado de datos en el servidor
class Info_Parada(generics.RetrieveAPIView):
    permission_classes = () #permisos quitados temporalmente para prueba de la vista IsAuthenticated,
    serializer_class = ParadaSerializer
    queryset = Parada.objects.all()
    lookup_field = 'nombre'

class Datos_ParadaSave(generics.CreateAPIView): #Guarda los datos enviados por la Parada
	permission_classes = (IsAuthenticated,)
	serializer_class = Datos_ParadaSerializer


class Solic_Asiento(APIView):
	permissions_classes = ()
	def get(self, request, nombre):
		parada = get_object_or_404(Parada, nombre = nombre)
		#tomamos los datos de la parada que nos van a ayudar a filtrar los buses
		itinerarios_parada = parada.itinerarios_parada.all() #itinerarios que pasan por esa parada
		tipo_parada = parada.tipo_parada#direccion que siguen los buses que pasan por esa parada, si es ida o vuelta
		#La ida y vuelta, equivaldria a tramo1 o tramo 2...
		location_parada = parada.location_parada#la locacion de la parada para hacer el calculo de distancia
		lista_buses_a_notificar = Bus_Datos_Update.objects.filter(sensor_asiento = False).filter(estado_viaje = tipo_parada).filter(viaje_inicio__itinerario_id__in = (itinerarios_parada)).filter(location_bus__distance_lt = (location_parada, D(km=2)))

		data = Bus_Datos_UpdateListSerializer(lista_buses_a_notificar, many = True).data
		return Response(data)

	def post(self, request, nombre, ):
		estado_solicitud = request.data["estado_solicitud"]

		parada = get_object_or_404(Parada, nombre = nombre)
		#tomamos los datos de la parada que nos van a ayudar a filtrar los buses
		itinerarios_parada = parada.itinerarios_parada.all() #itinerarios que pasan por esa parada
		tipo_parada = parada.tipo_parada#direccion que siguen los buses que pasan por esa parada, si es ida o vuelta
		#La ida y vuelta, equivaldria a tramo1 o tramo 2...
		location_parada = parada.location_parada#la locacion de la parada para hacer el calculo de distancia

		solic_asiento = SolicAsiento.objects.create(parada = Parada.objects.get(nombre = parada.nombre), time_solic = datetime.now(), estado_solicitud = estado_solicitud)
	
		buses_a_notificar = Bus_Datos_Update.objects.filter(sensor_asiento = False).filter(estado_viaje = tipo_parada).filter(viaje_inicio__itinerario_id__in = (itinerarios_parada)).filter(location_bus__distance_lt = (location_parada, D(km=2)))
		for bus in buses_a_notificar:
			solic_asiento.viajes_inicios.add(Viaje_Incio.objects.get(id = str(bus.viaje_inicio)))
		#print(buses_a_notificar.values_list('viaje_inicio', flat = True))
		
		solic_asiento.save()

		data = SolicAsientoSerializer(solic_asiento).data

		return Response(data)


class BorrarSolicAsiento(APIView):
	permissions_classes = ()

	def get(self, request, parada):
		solics_asiento_a_borrar = SolicAsiento.objects.filter(parada = parada)
		data = SolicAsientoSerializer(solics_asiento_a_borrar, many = True).data
		return Response(data)

	def delete(self, request, parada):
		solics_asiento_a_borrar = SolicAsiento.objects.filter(parada = parada)
		print(solics_asiento_a_borrar)

		for e in solics_asiento_a_borrar:
			e.delete()

		return Response(status = status.HTTP_204_NO_CONTENT)

"""    def delete(self, request, parada, format=None):
        snippet = self.get_object(parada)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""


	

#buses a mostrar en el mapa
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
		lista_buses = Bus_Datos_Update.objects.filter(estado_viaje = tipo_parada).filter(viaje_inicio__itinerario_id__in = (itinerarios_parada)).filter(location_bus__distance_lt = (location_parada, D(km=7)))
		#si es true 
		data = Bus_Datos_UpdateListSerializer(lista_buses, many = True).data
		return Response(data)
#solicitud_asiento_especial