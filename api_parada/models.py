from django.contrib.gis.db import models

from carga.models import Parada
from api_bus.models import Viaje_Incio, Bus_Datos_Update

# Create your models here.

ESTADOS_SOLICITUD_ASIENTO=(('I','INACTIVO'),('A',"ACTIVO"))
ESTADO_SINIESTRO=(('I','INACTIVO'),('A',"ACTIVO"))


class Datos_Parada(models.Model):
	id = models.AutoField(primary_key = True)
	nombre_parada = models.ForeignKey(Parada, related_name = 'nombre_parada', on_delete = models.CASCADE)#identificador de la parada, el cual sera un  proveido por el servidor al raspberry
	time_rasp_parada = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry de la parada
	time_created_parada = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	siniestro_parada = models.BooleanField(default = False)#boton de siniestro en la parada
	prep_asiento = models.BooleanField(default = False)#boton para solicitar asiento para personas con discapacidad
	
	class Meta:
		verbose_name = 'Datos_Parada'
		verbose_name_plural = 'Datos_Paradas'
		ordering = ['nombre_parada']

	def __str__(self):
		return '%s %s %s %s %s' %(self.id, self.nombre_parada, self.time_rasp_parada, self.siniestro_parada, self.prep_asiento)
#Los datos que se recibiran de la parada


class SolicAsiento(models.Model):
	id = models.AutoField(primary_key = True)
	parada = models.ForeignKey(Parada, on_delete = models.CASCADE, )#identificador de la parada, el cual sera un  proveido por el servidor al raspberry
	time_solic = models.DateTimeField(auto_now_add = False)
	viajes_inicios = models.ManyToManyField(Viaje_Incio)
	estado_solicitud = models.CharField(max_length=10, choices=ESTADOS_SOLICITUD_ASIENTO, default='I')# enviado por el raspberry

	class Meta:
		verbose_name = 'SolicAsiento'
		verbose_name_plural = 'Solicitudes de Asiento'
		ordering = ['time_solic']

	def __str__(self):
		return '%s %s %s %s %s' %(self.id, self.parada, self.time_solic, self.viajes_inicios, self.estado_solicitud)


class SolicAsientoConsulta(models.Model):
	parada = models.OneToOneField(Parada, on_delete = models.CASCADE, primary_key = True )#identificador de la parada, el cual sera un  proveido por el servidor al raspberry
	viajes_inicios = models.ManyToManyField(Viaje_Incio)
	time_solic = models.DateTimeField(auto_now_add = False)

	class Meta:
		verbose_name = 'SolicAsientoConsulta'
		verbose_name_plural = 'SolicAsientoConsultas'
		ordering = ['parada']

	def __str__(self):
		return '%s %s %s' %(self.parada, self.time_solic, self.viajes_inicios)


class Siniestro(models.Model):
	id = models.AutoField(primary_key = True)
	parada = models.ForeignKey(Parada, on_delete = models.CASCADE, )#identificador de la parada, el cual sera un  proveido por el servidor al raspberry
	time_solic = models.DateTimeField(auto_now_add = False)
	estado_solicitud = models.CharField(max_length=10, choices=ESTADO_SINIESTRO, default='I')# enviado por el raspberry

	class Meta:
		verbose_name = 'SiniestroParada'
		verbose_name_plural = 'Siniestros'
		ordering = ['time_solic']

	def __str__(self):
		return '%s %s %s %s' %(self.id, self.parada, self.time_solic, self.estado_solicitud)