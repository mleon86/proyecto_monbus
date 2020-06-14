#from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

from rest_framework.permissions import IsAuthenticated

from .models import Bus_Datos, Bus_Datos_Update
from carga.models import RaspberryBus, Itinerario
from api_parada.models import SolicAsientoConsulta
from .serializers import Bus_DatosSerializer, RaspberryBusSerializer, Viaje_IncioSerializer, Bus_Datos_UpdateSerializer, ItinerariosSerializer, BusConsultaAsientoSerializer
# Create your views here.

class Viaje_Inicio_Id_Viaje(generics.CreateAPIView): #Crea los viaje_inicio
	permission_classes = (IsAuthenticated,)
	serializer_class = Viaje_IncioSerializer
	lookup_field = ('itinerario_id', 'chofer_id', 'raspberry_id')

class Bus_DatosSave(generics.CreateAPIView): #Guarda los datos en la tabla Bus_Datos.
	permission_classes = (IsAuthenticated,)#(IsAuthenticated,)
	serializer_class = Bus_DatosSerializer

class Bus_DatosUpdateCreate(generics.CreateAPIView): #Crea el primer registro
    permission_classes = (IsAuthenticated,)
    serializer_class = Bus_Datos_UpdateSerializer

class Bus_DatosUpdate(generics.UpdateAPIView): #Actualiza los datos
    permission_classes = (IsAuthenticated,)
    queryset = Bus_Datos_Update.objects.all()
    serializer_class = Bus_Datos_UpdateSerializer
    lookup_field = 'viaje_inicio'

    def get_object(self):
        viaje_inicio = self.kwargs["viaje_inicio"]
        return get_object_or_404(Bus_Datos_Update, viaje_inicio=viaje_inicio)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#class Bus_DatosUpdate(APIView): #Actualiza los datos y a la vez debe cargar en BusDatosSave



class RaspberryBusConsulta(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) #permisos quitados temporalmente para prueba de la vista IsAuthenticated,
    serializer_class = RaspberryBusSerializer
    queryset = RaspberryBus.objects.all()
    lookup_field = 'serial_rasp_bus'

class PrepararAsiento(APIView):
    permissions_classes = (IsAuthenticated,)
    def get(self, request, viaje_inicio):
        solic_asiento_consulta = SolicAsientoConsulta.objects.filter(viajes_inicios = viaje_inicio)
        serializer = BusConsultaAsientoSerializer(solic_asiento_consulta, many = True)
        return Response(serializer.data)

class ConsultaItinerario(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItinerariosSerializer
    def get_queryset(self):
        linea_id = self.kwargs['linea_id']
        return Itinerario.objects.filter(linea_id = linea_id)