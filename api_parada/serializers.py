from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Datos_Parada
from carga.models import Parada
from api_bus.models import Bus_Datos

class Datos_ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datos_Parada
		fields = '__all__'

class ParadaSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Parada
		geo_field = 'location_parada'
		fields = '__all__'