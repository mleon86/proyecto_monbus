from django.contrib.gis.db import models
from carga.models import Itinerario, Chofer, RaspberryBus

# Create your models here.

class Viaje_Incio(models.Model):
	id = models.AutoField(primary_key = True)#identificador de viaje proveido por el servidor al raspberry
	itinerario_id = models.ForeignKey(Itinerario, on_delete = models.CASCADE)
	chofer_id = models.ForeignKey(Chofer, on_delete = models.CASCADE)
	raspberry_id = models.ForeignKey(RaspberryBus, on_delete = models.CASCADE)
	time_rasp_logueo = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry al momento de crearse en el bus
	time_created_logueo = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos

	class Meta:
		verbose_name = 'Viaje_Incio'
		verbose_name_plural = 'Viajes_Inicios'
		ordering = ['time_rasp_logueo']

	def __str__(self):
		return self.id

class Bus_Datos(models.Model):
	id = models.AutoField(primary_key = True)
	viaje_id = models.ForeignKey(Viaje_Incio, on_delete = models.CASCADE)#identificador de viaje proveido por el servidor al raspberry
	time_rasp = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry
	time_created = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	siniestro_bus = models.BooleanField(default = False)#boton de siniestro en el bus
	sensor_asiento = models.BooleanField(default = False)#sensor del asiento para personas con discapacidad
	estado_viaje = models.IntegerField()#identificador de viaje proveido por el servidor al raspberry
	location_bus = models.PointField()#locacion del bus

	class Meta:
		verbose_name = 'Bus_Dato'
		verbose_name_plural = 'Bus_Datos'
		ordering = ['viaje_id']

	def __str__(self):
		return self.id

#agregar asiento especial, siniestro