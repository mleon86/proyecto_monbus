from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Datos_Parada, SolicAsiento, SolicAsientoConsulta, Siniestro
from carga.models import Parada, RaspberryParada
from api_bus.models import Bus_Datos, Viaje_Incio

class RaspberryParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = RaspberryParada
		fields = '__all__'

class Datos_ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datos_Parada
		fields = '__all__'

class ParadaSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Parada
		geo_field = 'location_parada'
		fields = '__all__'

class  SolicAsientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicAsiento
		fields = '__all__'

class  SolicAsientoConsultaSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicAsientoConsulta
		fields = '__all__'

class Viaje_InicioListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viaje_Incio
		fields = ['id','itinerario_id']

class Bus_Datos_UpdateListSerializer(GeoFeatureModelSerializer):
	viaje_inicio = Viaje_InicioListSerializer(read_only = True)
	class Meta:
		model = Bus_Datos
		geo_field = 'location_bus'
		fields = ['estado_viaje', 'sensor_asiento', 'siniestro_bus', 'viaje_inicio']

class  SiniestroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Siniestro
		fields = '__all__'