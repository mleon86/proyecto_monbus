from rest_framework import serializers
from .models import Bus_Datos
from carga.models import RaspberryBus

class Bus_DatosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus_Datos
		fields = '__all__'

class RaspberryBusSerializer(serializers.ModelSerializer):
	class Meta:
		model = RaspberryBus
		fields = '__all__'