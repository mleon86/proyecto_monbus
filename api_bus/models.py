from django.db import models

# Create your models here.

class Bus_geo(models.Model):
	bus = models.CharField(max_length = 200, blank = False, null = False)
	viaje = models.CharField(max_length = 200, blank = False, null = False)
	lat = models.CharField(max_length = 200, blank = False, null = False)
	lon = models.CharField(max_length = 200, blank = False, null = False)
	time = models.CharField(max_length = 100, blank = False, null = False)

	class Meta:
		verbose_name = 'bus_geo'
		verbose_name_plural = 'bus_geo_ubicaciones'
		ordering = ['viaje']

	def __str__(self):
		return self.viaje


#agregar asiento especial, siniestro