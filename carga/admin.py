from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
from .models import Chofer, Empresa, Itinerario, Parada, Linea, RaspberryBus, RaspberryParada, Bus

admin.site.register(Chofer)
admin.site.register(Empresa)

@admin.register(Itinerario)
class ItinerarioAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13


@admin.register(Parada)
class ParadaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13

admin.site.register(Bus)
admin.site.register(Linea)
admin.site.register(RaspberryBus)
admin.site.register(RaspberryParada)