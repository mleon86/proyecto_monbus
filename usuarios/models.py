from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from carga.models import Chofer, Empresa


class Usuario(models.Model):
	ci_nro = models.ForeignKey(Chofer, on_delete = models.CASCADE)
	usuario = models.OneToOneField(User, unique=True, on_delete = models.CASCADE, primary_key = True)

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		ordering = ['ci_nro']

	def __str__(self):
		return str(self.ci_nro)

# Create your models here.
