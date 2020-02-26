from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Datos_Parada
from carga.models import Parada
from api_bus.models import Bus_Datos, Viaje_Incio

class Datos_ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datos_Parada
		fields = '__all__'

class ParadaSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Parada
		geo_field = 'location_parada'
		fields = '__all__'

class Viaje_InicioListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viaje_Incio
		fields = ['itinerario_id']

class Bus_Datos_UpdateListSerializer(GeoFeatureModelSerializer):
	viaje_inicio = Viaje_InicioListSerializer(read_only = True)
	class Meta:
		model = Bus_Datos
		geo_field = 'location_bus'
		fields = ['estado_viaje', 'sensor_asiento', 'siniestro_bus', 'viaje_inicio']
