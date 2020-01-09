from django.db import models

# Create your models here.

class Datos_Parada(models.Model):
	id_parada = models.CharField(max_length = 15, blank = False, null = False)#identificador de la parada, el cual sera un  proveido por el servidor al raspberry
	time_rasp_parada = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry de la parada
	time_created_parada = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	siniestro_parada = models.BooleanField(default = False)#boton de siniestro en la parada
	prep_asiento = models.BooleanField(default = False)#boton para solicitar asiento para personas con discapacidad
	
	class Meta:
		verbose_name = 'Datos_Parada'
		verbose_name_plural = 'Datos_Paradas'
		ordering = ['id_parada']

	def __str__(self):
		return self.id_parada
#Los datos que se recibiran de la parada