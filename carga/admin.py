from django.contrib import admin

# Register your models here.
from .models import Chofer, Empresa, Itinerario, Parada, Linea

admin.site.register(Chofer)
admin.site.register(Empresa)
admin.site.register(Itinerario)
admin.site.register(Parada)
admin.site.register(Linea)