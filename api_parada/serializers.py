from rest_framework import serializers
from .models import Datos_Parada

class Datos_ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datos_Parada
		fields = '__all__'