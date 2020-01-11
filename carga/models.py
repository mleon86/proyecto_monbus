from django.db import models

PAISES=(('PY','Paraguaya'),('AR',"Argentina"),('BR','Brasilera'),('BO','Boliviana'),('PE',"Peruana"),('CH','Chilena'))

# Create your models here.

#Datos de las Paradas
class Parada(models.Model):
	id = models.AutoField(primary_key = True)
	nro = models.CharField(max_length = 10, blank = False, null = False)
	direccion = models.CharField(max_length = 100, blank = False, null = False)

	class Meta:
		verbose_name = 'Parada'
		verbose_name_plural = 'Paradas'
		ordering = ['nro']

	def __str__(self):
		return self.linea



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
	id = models.AutoField(primary_key = True)
	nro = models.CharField(max_length = 200, blank = False, null = False)
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
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 40, blank = False, null = False)
	descripcion = models.TextField()
	linea_id = models.ForeignKey(Linea, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'Itinerario'
		verbose_name_plural = 'Itinerarios'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class Bus(models.Model):
	id = models.AutoField(primary_key = True)
	marca = models.CharField(max_length = 50, blank = False, null = False)
	modelo = models.CharField(max_length = 50, blank = False, null = False)
	chapa = models.CharField(max_length = 8, blank = False, null = False)
	empresa_id = models.ForeignKey(Empresa, on_delete = models.CASCADE)


	class Meta:
		verbose_name = 'Bus'
		verbose_name_plural = 'Buses'
		ordering = ['chapa', 'empresa_id']

	def __str__(self):
		return self.nombre

#Datos de los choferes
class Chofer(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 50, blank = False, null = False)
	apellido = models.CharField(max_length = 50, blank = False, null = False)
	ci_nro = models.CharField(max_length = 8, blank = False, null = False)
	nacionalidad = models.CharField(max_length=10, choices=PAISES, default='PY')
	observacion = models.TextField(blank = False, null = False)
	empresa_id = models.ForeignKey(Empresa, on_delete = models.CASCADE)


	class Meta:
		verbose_name = 'Chofer'
		verbose_name_plural = 'Choferes'
		ordering = ['ci_nro']

	def __str__(self):
		return self.nombre