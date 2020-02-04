from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Datos_Parada

@admin.register(Datos_Parada)
class Datos_ParadaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13