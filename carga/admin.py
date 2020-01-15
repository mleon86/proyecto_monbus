from django.contrib import admin

# Register your models here.
from .models import Chofer, Empresa, Itinerario, Parada, Linea, RaspberryBus, RaspberryParada, Bus

admin.site.register(Chofer)
admin.site.register(Empresa)
admin.site.register(Itinerario)
admin.site.register(Parada)
admin.site.register(Bus)
admin.site.register(Linea)
admin.site.register(RaspberryBus)
admin.site.register(RaspberryParada)