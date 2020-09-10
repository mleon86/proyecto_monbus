from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Bus_Datos, Bus_Datos_Update, Viaje_Incio, SiniestroBus

@admin.register(Viaje_Incio)
@admin.register(SiniestroBus)

@admin.register(Bus_Datos)
class Bus_DatosAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13


@admin.register(Bus_Datos_Update)
class Bus_DatosAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13