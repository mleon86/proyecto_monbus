from django.contrib.gis.db import models

PAISES=(('PY','Paraguaya'),('AR',"Argentina"),('BR','Brasilera'),('BO','Boliviana'),('PE',"Peruana"),('CH','Chilena'))
TIPO_PARADA=(('T1','Tramo1'),('T2',"Tramo2"))

# Create your models here.


#Datos de las empresas
class Empresa(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	contacto = models.CharField(max_length = 13, blank = False, null = False)
	observacion = models.TextField(blank = False, null = False)

	class Meta:
		verbose_name = 'Empresa'
		verbose_name_plural = 'Empresas'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


#Son la lineas de colectivo, pertenecientes a empresas
class Linea(models.Model):
	nro = models.CharField(max_length = 200, blank = False, null = False, primary_key = True)
	descripcion = models.CharField(max_length = 200, blank = False, null = False)
	empresa_id = models.ForeignKey(Empresa, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'Linea'
		verbose_name_plural = 'Lineas'
		ordering = ['nro']

	def __str__(self):
		return self.nro

#Itinerarios: determinaran la ruta que recorre un determinada empresa
class Itinerario(models.Model):
	nombre = models.CharField(max_length = 40, blank = False, null = False, primary_key = True)
	descripcion = models.TextField()
	linea_id = models.ForeignKey(Linea, on_delete = models.CASCADE)
	mpoly = models.LineStringField()

	class Meta:
		verbose_name = 'Itinerario'
		verbose_name_plural = 'Itinerarios'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

#Datos de las Paradas
class Parada(models.Model):
	nombre = models.CharField(max_length = 10, blank = False, null = False, primary_key = True)
	direccion = models.CharField(max_length = 100, blank = False, null = False)
	location_parada = models.PointField()
	itinerarios_parada = models.ManyToManyField(Itinerario)
	tipo_parada = models.CharField(max_length=10, choices=TIPO_PARADA, default='T1')

	class Meta:
		verbose_name = 'Parada'
		verbose_name_plural = 'Paradas'
		ordering = ['nombre']

	def __str__(self):
		return str(self.nombre)


class Bus(models.Model):
	marca = models.CharField(max_length = 50, blank = False, null = False)
	modelo = models.CharField(max_length = 50, blank = False, null = False)
	chapa = models.CharField(max_length = 8, blank = False, null = False, primary_key = True)
	empresa_id = models.ForeignKey(Empresa, on_delete = models.CASCADE)
	
	class Meta:
		verbose_name = 'Bus'
		verbose_name_plural = 'Buses'
		ordering = ['chapa', 'empresa_id']

	def __str__(self):
		return self.chapa

class RaspberryBus(models.Model):
	serial_rasp_bus = models.CharField(max_length = 50, blank = False, null = False, primary_key = True)
	bus_id = models.OneToOneField(Bus, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'RaspberryBus'
		verbose_name_plural = 'RaspberrysBuses'
		ordering = ['serial_rasp_bus']

	def __str__(self):
		return self.serial_rasp_bus

class RaspberryParada(models.Model):
	serial = models.CharField(max_length = 50, blank = False, null = False, primary_key = True)
	parada_id = models.OneToOneField(Parada, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'RaspberryParada'
		verbose_name_plural = 'RaspberrysParadas'
		ordering = ['serial']

	def __str__(self):
		return self.serial


#Datos de los choferes
class Chofer(models.Model):

	nombre = models.CharField(max_length = 50, blank = False, null = False)
	apellido = models.CharField(max_length = 50, blank = False, null = False)
	ci_nro = models.CharField(max_length = 8, blank = False, null = False, primary_key = True)
	nacionalidad = models.CharField(max_length=10, choices=PAISES, default='PY')
	observacion = models.TextField(blank = False, null = False)
	empresa_id = models.ForeignKey(Empresa, on_delete = models.CASCADE)


	class Meta:
		verbose_name = 'Chofer'
		verbose_name_plural = 'Choferes'
		ordering = ['ci_nro']

	def __str__(self):
		return '%s %s %s' % (self.ci_nro, self.nombre, self.apellido)