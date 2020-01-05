from django.db import models

# Create your models here.

class Datos_Parada(models.Model):
	parada = models.CharField(max_length = 200, blank = False, null = False)
	siniestro = models.CharField(max_length = 200, blank = False, null = False)
	prep_asiento = models.CharField(max_length = 200, blank = False, null = False)
	
	class Meta:
		verbose_name = 'Datos_Parada'
		verbose_name_plural = 'Datos_Paradas'
		ordering = ['parada']

	def __str__(self):
		return self.parada
#Los datos que se recibiran de la parada