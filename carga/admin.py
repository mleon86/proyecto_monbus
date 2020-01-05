from django.contrib import admin

# Register your models here.
from .models import Chofer, Empresa, Linea_Ramal, Parada

admin.site.register(Chofer)
admin.site.register(Empresa)
admin.site.register(Linea_Ramal)
admin.site.register(Parada)