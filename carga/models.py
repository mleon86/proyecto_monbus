from django.db import models

# Create your models here.

#Datos de los choferes
class Chofer(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	apellido = models.CharField(max_length = 200, blank = False, null = False)
	nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
	observacion = models.TextField(blank = False, null = False)

	class Meta:
		verbose_name = 'Chofer'
		verbose_name_plural = 'Choferes'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


#Datos de las empresas
class Empresa(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	observacion = models.TextField(blank = False, null = False)

	class Meta:
		verbose_name = 'Empresa'
		verbose_name_plural = 'Empresas'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


#Ramales: determinaran la ruta que recorre un determinada empresa
class Linea_Ramal(models.Model):
	id = models.AutoField(primary_key = True)
	linea = models.CharField(max_length = 200, blank = False, null = False)
	ramal = models.CharField(max_length = 200, blank = False, null = False)
	recorrido = models.TextField(blank = False, null = False)

	class Meta:
		verbose_name = 'Linea_Ramal'
		verbose_name_plural = 'Lineas_Ramales'
		ordering = ['linea']

	def __str__(self):
		return self.linea


class Parada(models.Model):
	id = models.AutoField(primary_key = True)
	nro = models.CharField(max_length = 200, blank = False, null = False)
	direccion = models.CharField(max_length = 200, blank = False, null = False)

	class Meta:
		verbose_name = 'Parada'
		verbose_name_plural = 'Paradas'
		ordering = ['nro']

	def __str__(self):
		return self.linea