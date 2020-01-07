from rest_framework import serializers
from .models import Bus_Datos

class Bus_DatosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus_Datos
		fields = '__all__'