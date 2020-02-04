from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Bus_Datos

@admin.register(Bus_Datos)
class Bus_DatosAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13