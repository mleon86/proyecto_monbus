from django.db import models

# Create your models here.

class Bus_Datos(models.Model):
	id_viaje = models.IntegerField()#identificador de viaje proveido por el servidor al raspberry
	lat = models.FloatField()#latitud del gps conectado al raspberry
	lon = models.FloatField()#longitud del gps del raspberry
	time_rasp = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry
	time_created = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	siniestro_bus = models.BooleanField(default = False)#boton de siniestro en el bus
	sensor_asiento = models.BooleanField(default = False)#sensor del asiento para personas con discapacidad
	estado_viaje = models.IntegerField()#identificador de viaje proveido por el servidor al raspberry
	
	class Meta:
		verbose_name = 'Bus_Dato'
		verbose_name_plural = 'Bus_Datos'
		ordering = ['id_viaje']

	def __str__(self):
		return self.id_viaje


#agregar asiento especial, siniestro