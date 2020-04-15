from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Bus_Datos, Viaje_Incio, Bus_Datos_Update
from carga.models import RaspberryBus, Itinerario, Bus
from api_parada.models import SolicAsientoConsulta

class Viaje_IncioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viaje_Incio
		fields = '__all__'

class Bus_Datos_UpdateSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Bus_Datos_Update
		geo_field = 'location_bus'
		fields = '__all__'

class Bus_DatosSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Bus_Datos
		geo_field = 'location_bus'
		fields = '__all__'

class  Bus_Datos_UpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus_Datos_Update
		geo_field = 'location_bus'
		fields = '__all__'


class ItinerariosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Itinerario
		fields = ['nombre']
	

'''	def update(self, instance, validated_data):
		print('hola1')
		Bus_Datos_Update_prueba.viaje_inicio = validated_data.get('viaje_inicio', instance.viaje_inicio)
		Bus_Datos_Update_prueba.time_rasp = validated_data.get('time_rasp', instance.time_rasp)
		Bus_Datos_Update_prueba.location_bus = validated_data.get('location_bus', instance.location_bus)
		Bus_Datos_Update_prueba.save()
		return instance'''

class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = ['chapa','empresa_id','linea_id']

class RaspberryBusSerializer(serializers.ModelSerializer):
	bus_id = BusSerializer(read_only = True)
	class Meta:
		model = RaspberryBus
		fields = ['serial_rasp_bus','bus_id']

class BusConsultaAsientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicAsientoConsulta
		fields = ['parada', 'time_solic']




'''


class BusDatosSerializer(serializers.ModelSerializer):
	datos_bus_ultimo = Datos_Bus_UltimoSerializer()

	class Meta:
		model: BusDatos
		fields = ['id', 'datos_bus_ultimo']

	def update(self, instance, validated_data):
        datos_bus_ultimo_data = validated_data.pop('datos_bus_ultimo')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        datos_bus_ultimo = instance.datos_bus_ultimo

        instance.viaje_inicio = validated_data.get('viaje_inicio', instance.viaje_inicio)

        datos_bus_ultimo.location_bus = datos_bus_ultimo_data.get(
            'location_bus',
            datos_bus_ultimo.location_bus

        datos_bus_ultimo.save()

        return instance

'''