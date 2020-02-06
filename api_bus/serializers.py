from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Bus_Datos, Viaje_Incio
from carga.models import RaspberryBus, Itinerario

class Viaje_IncioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viaje_Incio
		fields = '__all__'

class Bus_DatosSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Bus_Datos
		geo_field = 'location_bus'
		fields = ('__all__')

class RaspberryBusSerializer(serializers.ModelSerializer):
	class Meta:
		model = RaspberryBus
		fields = '__all__'